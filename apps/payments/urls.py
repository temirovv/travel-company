from django.urls import path
from .views import PaymePaymentView

urlpatterns = [
    path('payment/<int:booking_id>/', PaymePaymentView.as_view(), name='payment'),
]
