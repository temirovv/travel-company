from django.urls import path
from .views import home, place_detail

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', place_detail, name='place_detail'),
]
