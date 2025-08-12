from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADVISOR = "ADVISOR", "Advisor"
        ADMIN = "ADMIN", "Admin"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADVISOR)

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"