import io
from django.http import HttpResponse
from rest_framework import viewsets, permissions, decorators
from rest_framework.response import Response
from xhtml2pdf import pisa
from django.template.loader import render_to_string

from .models import Proposal
from .serializers import ProposalSerializer


class ProposalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Proposal.objects.all().select_related("client", "advisor").prefetch_related("items")
    serializer_class = ProposalSerializer

    def perform_create(self, serializer):
        serializer.save(advisor=self.request.user)


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def proposal_pdf(request, pk: int):
    proposal = Proposal.objects.select_related("client", "advisor").prefetch_related("items").get(pk=pk)
    html = render_to_string("proposal_pdf.html", {"proposal": proposal})
    pdf_file = io.BytesIO()
    pisa.CreatePDF(io.BytesIO(html.encode("utf-8")), dest=pdf_file)
    response = HttpResponse(pdf_file.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename=proposal-{proposal.id}.pdf"
    return response