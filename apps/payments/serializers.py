from rest_framework.serializers import Serializer, IntegerField  # noqa


class GeneratePayLinkSerializer(Serializer):
    order_id = IntegerField()
    amount = IntegerField()
