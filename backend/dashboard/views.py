from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from crm.models import Client
from portfolio.models import Holding, Transaction, SIP, Account


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def advisor_dashboard(request):
    user = request.user
    clients_qs = Client.objects.all() if user.role == "ADMIN" else Client.objects.filter(advisor=user)
    total_clients = clients_qs.count()

    accounts = Account.objects.filter(client__in=clients_qs)
    total_aum = (
        Holding.objects.filter(account__in=accounts)
        .aggregate(
            total=Sum(ExpressionWrapper(F("units") * F("current_nav"), output_field=DecimalField(max_digits=18, decimal_places=4)))
        )["total"]
        or 0
    )

    today = timezone.now().date()
    in_30 = today + timedelta(days=30)
    active_sip_count = SIP.objects.filter(account__in=accounts, start_date__lte=today).filter(
        models.Q(end_date__isnull=True) | models.Q(end_date__gte=today)
    ).count()
    upcoming_sip_expiry = SIP.objects.filter(account__in=accounts, end_date__range=(today, in_30)).values(
        "id", "fund_name", "end_date", "account_id"
    )

    recent_transactions = list(
        Transaction.objects.filter(account__in=accounts)
        .order_by("-created_at")
        .values("id", "fund_name", "type", "units", "nav", "date")[:10]
    )

    return Response(
        {
            "total_clients": total_clients,
            "total_aum": total_aum,
            "active_sip_count": active_sip_count,
            "recent_transactions": recent_transactions,
            "alerts": {"sip_expiring": list(upcoming_sip_expiry)},
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def aum_by_client(request):
    user = request.user
    clients_qs = Client.objects.all() if user.role == "ADMIN" else Client.objects.filter(advisor=user)
    data = []
    for client in clients_qs:
        accounts = client.accounts.all()
        total = (
            Holding.objects.filter(account__in=accounts)
            .aggregate(
                total=Sum(ExpressionWrapper(F("units") * F("current_nav"), output_field=DecimalField(max_digits=18, decimal_places=4)))
            )["total"]
            or 0
        )
        data.append({"client_id": client.id, "client_name": client.name, "total_aum": total})
    return Response(data)