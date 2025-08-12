from rest_framework import viewsets, permissions

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DocumentSerializer
    queryset = Document.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)