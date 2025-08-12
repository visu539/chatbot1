from rest_framework import serializers
from .models import Client, Lead


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "advisor",
            "name",
            "contact",
            "email",
            "stage",
            "probability",
            "expected_investment",
            "notes",
            "created_at",
        ]
        read_only_fields = ["id", "advisor", "created_at"]


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "id",
            "advisor",
            "name",
            "contact",
            "email",
            "stage",
            "probability",
            "expected_investment",
            "notes",
            "created_at",
        ]
        read_only_fields = ["id", "advisor", "created_at"]