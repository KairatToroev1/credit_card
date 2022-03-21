from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status


from credit_carts.models import Cart_Credit
from credit_carts.serializer import CartCreditSerilaizer
from payments.serializers import PaymentSerializer
from .card_is_active import start_scheduler

class CartCreditView(ModelViewSet):
    queryset = Cart_Credit.objects.all()
    serializer_class = CartCreditSerilaizer
    permission_classes = [AllowAny, ]
    filter_backends=[SearchFilter]
    search_filters = ['card_series','card_number','card_issue_date',\
                      'last_date_of','card_status']


    def gen_cart(self):
        for i in Cart_Credit.objects.filter(card_series=Cart_Credit.card_series):
            yield f'{Cart_Credit.card_series}:{i}'

    def status_card(self, card_status):
        card = Cart_Credit.objects.all()
        card.card_status = card_status
        if card.card_status == card.card_status.ACTIVATED:
            start_scheduler()
        card.save()


    def activate_card(self):
        self.status_card(Cart_Credit.StatusType.ACTIVATED)
        return Response(status=status.HTTP_200_OK)

    def deactivate_card(self):
        self.status_card(Cart_Credit.StatusType.NOT_ACTIVATED)
        return Response(status=status.HTTP_200_OK)

    def payments_history(self):
        card = Cart_Credit.objects.all()
        payments = card.payments.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)








