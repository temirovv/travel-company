from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.models import AnonymousUser

from .models import TourPackage, Destination
from ..bookings.forms import BookingForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['main_banner_packages'] = TourPackage.objects.main_banner().prefetch_related('gallery')
        context['regular_tour_packages'] = TourPackage.objects.regular().prefetch_related('gallery', 'destinations')
        context['destinations'] = Destination.objects.all().prefetch_related('gallery')

        return context


class TourPackageDetailView(DetailView):
    model = TourPackage
    template_name = 'package-details.html'
    context_object_name = 'package'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset().select_related().prefetch_related(
            'destinations',
            'gallery',
            'travel_plans',
            'travel_plans__activities'
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package: TourPackage = self.object

        context['form'] = BookingForm()
        context['gallery_images'] = package.gallery.all()
        context['travel_plans'] = package.travel_plans.all()
        context['related_packages'] = TourPackage.objects.filter(
            destinations__in=package.destinations.all()
        ).exclude(id=package.id).distinct().prefetch_related('gallery')[:3]

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = BookingForm(request.POST)
        print(f"request.POST = {request.POST}")
        print(f"Form errors: {str(form.errors).encode('utf-8')}")
        if form.is_valid():
            booking = form.save(commit=False)

            if isinstance(request.user, AnonymousUser):
                booking.user = None
            else:
                booking.user = request.user

            booking.tour_package = self.object
            booking.amount = booking.calculate_total_price() * 100
            
            booking.save()

            messages.success(request, 'Joyingiz muvaffaqiyatli band qilindi!\nTez orada sizga aloqaga chiqamiz')

            return redirect(reverse('payment', kwargs={'booking_id': booking.id}))
            # return redirect(reverse('package_detail', kwargs={'slug': self.object.slug}))

        context = self.get_context_data(form=form)
        messages.error(request, 'Ma\'lumotlarni xato kiritindingiz qaytadan urinib ko\'ring')
        return self.render_to_response(context)
