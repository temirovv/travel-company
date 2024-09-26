from django.urls import path
from .views import HomeView, TourPackageDetailView, temp


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('package-details/<slug:slug>/', TourPackageDetailView.as_view(), name="package_detail"),
    path('package/', temp)
]
