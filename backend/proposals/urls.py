from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ProposalViewSet, proposal_pdf

router = DefaultRouter()
router.register(r"proposals", ProposalViewSet)

urlpatterns = [
    path("proposals/<int:pk>/export-pdf/", proposal_pdf, name="proposal-pdf"),
]
urlpatterns += router.urls