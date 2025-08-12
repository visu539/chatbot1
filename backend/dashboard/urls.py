from django.urls import path
from .views import advisor_dashboard, aum_by_client

urlpatterns = [
    path("dashboard/summary/", advisor_dashboard, name="dashboard-summary"),
    path("reports/aum-by-client/", aum_by_client, name="aum-by-client"),
]