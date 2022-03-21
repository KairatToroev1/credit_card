from rest_framework import serializers

from credit_carts.models import Cart_Credit

class CartCreditSerilaizer(serializers.Serializer):
    class Meta:
        model = Cart_Credit
        fields = ['card_series','card_number','card_issue_date',
                  'last_date_of','date_of_use','summa','card_status']
