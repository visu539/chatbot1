from decimal import Decimal
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from rest_framework import viewsets, permissions, decorators
from rest_framework.response import Response

from .models import Account, Holding, Transaction, SIP
from .serializers import AccountSerializer, HoldingSerializer, TransactionSerializer, SIPSerializer
from crm.models import Client


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(BaseViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class HoldingViewSet(BaseViewSet):
    queryset = Holding.objects.all()
    serializer_class = HoldingSerializer


class TransactionViewSet(BaseViewSet):
    queryset = Transaction.objects.all().order_by("-created_at")
    serializer_class = TransactionSerializer


class SIPViewSet(BaseViewSet):
    queryset = SIP.objects.all()
    serializer_class = SIPSerializer


@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def client_aum(request, client_id: int):
    accounts = Account.objects.filter(client_id=client_id)
    total_value = Holding.objects.filter(account__in=accounts).aggregate(
        total=Sum(ExpressionWrapper(F("units") * F("current_nav"), output_field=DecimalField(max_digits=18, decimal_places=4)))
    )["total"] or Decimal("0")
    return Response({"client_id": client_id, "total_aum": total_value})