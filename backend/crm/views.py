from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Client, Lead
from .serializers import ClientSerializer, LeadSerializer


class AdvisorOwnedMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.role == "ADMIN":
            return qs
        return qs.filter(advisor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(advisor=self.request.user)


class ClientViewSet(AdvisorOwnedMixin, viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["stage", "probability"]
    search_fields = ["name", "email", "contact", "notes"]
    ordering_fields = ["name", "created_at", "expected_investment", "probability"]


class LeadViewSet(AdvisorOwnedMixin, viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lead.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["stage", "probability"]
    search_fields = ["name", "email", "contact", "notes"]
    ordering_fields = ["name", "created_at", "expected_investment", "probability"]