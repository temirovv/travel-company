from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import TourPackage, Destination, PackageDisplayChoices


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['main_banner_packages'] = TourPackage.objects.main_banner().prefetch_related('gallery')
        context['regular_tour_packages'] = TourPackage.objects.regular().prefetch_related('gallery', 'destinations')
        context['destinations'] = Destination.objects.all().prefetch_related('gallery')

        return context


def temp(request):
    return render(request, 'package-details.html')


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
            'travel_plans'
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package: TourPackage = self.object

        context['gallery_images'] = package.gallery.all()
        context['travel_plans'] = package.travel_plans.all()

        context['related_packages'] = TourPackage.objects.filter(
            description__in=package.destinations.all()
        ).exclude(id=package.id).distinct().prefetch_related('gallery')[:3]

        return context
