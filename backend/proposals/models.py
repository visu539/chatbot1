from django.conf import settings
from django.db import models
from crm.models import Client


class Proposal(models.Model):
    STATUS_DRAFT = "DRAFT"
    STATUS_FINAL = "FINAL"
    STATUS_CHOICES = [(STATUS_DRAFT, "Draft"), (STATUS_FINAL, "Final")]

    advisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="proposals")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="proposals")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)


class ProposalItem(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="items")
    fund_name = models.CharField(max_length=200)
    allocation_percent = models.DecimalField(max_digits=5, decimal_places=2)