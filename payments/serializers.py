from rest_framework import serializers


from .models import Payment

class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ['date_of_use','amount']
