from django.conf import settings
from django.db import models


class Client(models.Model):
    advisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="clients")
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    stage = models.CharField(max_length=100, blank=True)
    probability = models.PositiveIntegerField(default=0)
    expected_investment = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Lead(models.Model):
    advisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="leads")
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    stage = models.CharField(max_length=100, blank=True)
    probability = models.PositiveIntegerField(default=0)
    expected_investment = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Lead: {self.name}"