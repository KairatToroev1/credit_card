from django.db import models

from credit_carts.models import Cart_Credit

class Payment(models.Model):
    card = models.ForeignKey(Cart_Credit,on_delete=models.CASCADE, related_name='payments')
    date_of_use = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
