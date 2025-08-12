from django.db import models
from crm.models import Client


class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.client.name} - {self.name}"


class Holding(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="holdings")
    fund_name = models.CharField(max_length=200)
    units = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    average_cost = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    current_nav = models.DecimalField(max_digits=14, decimal_places=4, default=0)

    @property
    def market_value(self):
        return self.units * self.current_nav


class Transaction(models.Model):
    BUY = "BUY"
    SELL = "SELL"
    TYPE_CHOICES = [(BUY, "Buy"), (SELL, "Sell")]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    fund_name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    units = models.DecimalField(max_digits=18, decimal_places=4)
    nav = models.DecimalField(max_digits=14, decimal_places=4)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class SIP(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sips")
    fund_name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    day_of_month = models.PositiveSmallIntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    @property
    def is_active(self):
        from django.utils import timezone

        today = timezone.now().date()
        if self.end_date and self.end_date < today:
            return False
        return self.start_date <= today