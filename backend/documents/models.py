from django.conf import settings
from django.db import models
from crm.models import Client


class Document(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="documents")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="kyc/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name