from django.contrib import admin
from .models import Proposal, ProposalItem

class ProposalItemInline(admin.TabularInline):
    model = ProposalItem
    extra = 0

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "advisor", "client", "status", "created_at")
    list_filter = ("status", "advisor")
    inlines = [ProposalItemInline]