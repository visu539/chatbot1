from django.contrib import admin
from .models import Client, Lead

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "advisor", "stage", "probability", "expected_investment", "created_at")
    list_filter = ("stage", "advisor")
    search_fields = ("name", "email")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "advisor", "stage", "probability", "expected_investment", "created_at")
    list_filter = ("stage", "advisor")
    search_fields = ("name", "email")