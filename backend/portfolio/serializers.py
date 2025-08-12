from rest_framework import serializers
from .models import Account, Holding, Transaction, SIP


class HoldingSerializer(serializers.ModelSerializer):
    market_value = serializers.DecimalField(max_digits=18, decimal_places=4, read_only=True)

    class Meta:
        model = Holding
        fields = ["id", "account", "fund_name", "units", "average_cost", "current_nav", "market_value"]
        read_only_fields = ["id"]


class AccountSerializer(serializers.ModelSerializer):
    holdings = HoldingSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ["id", "client", "name", "type", "holdings"]
        read_only_fields = ["id"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "account", "fund_name", "type", "units", "nav", "date", "created_at"]
        read_only_fields = ["id", "created_at"]


class SIPSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = SIP
        fields = ["id", "account", "fund_name", "amount", "day_of_month", "start_date", "end_date", "is_active"]
        read_only_fields = ["id", "is_active"]