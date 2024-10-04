from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


from payme.views import MerchantAPIView  # noqa
from payme.methods.generate_link import GeneratePayLink  # noqa

from .models import Payment
from apps.bookings.models import Booking
from .serializers import GeneratePayLinkSerializer


class PaymeCallBackAPIView(MerchantAPIView):
    def create_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"create_transaction for order_id: {order_id}, response: {action}")

    def perform_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"perform_transaction for order_id: {order_id}, response: {action}")

    def cancel_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"cancel_transaction for order_id: {order_id}, response: {action}")


class GeneratePayLinkAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = GeneratePayLinkSerializer(
            data=request.data
        )
        serializer.is_valid(
            raise_exception=True
        )
        pay_link = GeneratePayLink(**serializer.validated_data).generate_link()

        return Response({"pay_link": pay_link})


class PaymePaymentView(View):
    def get(self, request, booking_id):  # noqa
        booking = get_object_or_404(Booking, id=booking_id)
        amount = int(booking.amount)  # Amount in tiyin (smallest currency unit)
        serializer = GeneratePayLinkSerializer(
            data={
                "order_id": booking.id,
                "amount": amount
            }
        )
        serializer.is_valid(
            raise_exception=True
        )
        pay_link = GeneratePayLink(**serializer.validated_data).generate_link()
        print(pay_link)
        return redirect(pay_link)

