from django.db import models

class Cart_Credit(models.Model):
    class StatusType(models.TextChoices):
        NOT_ACTIVATED = 'not_activated'
        ACTIVATED = 'activated'
        EXPIRED = 'expired'
    card_series = models.IntegerField()
    card_number = models.IntegerField()
    card_issue_date = models.DateTimeField()
    last_date_of = models.DateTimeField()
    date_of_use = models.DateTimeField(auto_now_add=True)
    summa = models.IntegerField()
    card_status = models.CharField(max_length=50, choices=StatusType.choices, default=StatusType.NOT_ACTIVATED)
    is_active_card = models.BooleanField(default=False)

    def __str__(self):
        return self.card_status
    

