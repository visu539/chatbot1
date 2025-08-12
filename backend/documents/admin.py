from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "client", "uploaded_by", "created_at")
    list_filter = ("client",)
    search_fields = ("name",)