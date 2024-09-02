from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Place, Category, Interest
from .forms import InterestModelForm


def home(request):
    if request.method == 'GET':
        places = Place.objects.all()
        context = {
            'places': places
        }
        return render(request, 'places/index.html', context=context)  # noqa


def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)

    if request.method == 'POST':
        form = InterestModelForm(request.POST, place=place)
        if form.is_valid():
            form.save()
            messages.info(request, "So'rovingiz qabul qilindi tez orada sizga bog'lanamiz")

            return redirect('place_detail', slug=place.slug)
    else:
        form = InterestModelForm(place=place)

    context = {
        'place': place,
        'form': form
    }

    return render(request, 'places/place-detail.html', context=context)  # noqa
