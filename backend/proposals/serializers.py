from rest_framework import serializers
from .models import Proposal, ProposalItem


class ProposalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalItem
        fields = ["id", "fund_name", "allocation_percent"]
        read_only_fields = ["id"]


class ProposalSerializer(serializers.ModelSerializer):
    items = ProposalItemSerializer(many=True)

    class Meta:
        model = Proposal
        fields = ["id", "advisor", "client", "status", "created_at", "items"]
        read_only_fields = ["id", "advisor", "created_at"]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        proposal = Proposal.objects.create(**validated_data)
        for item in items_data:
            ProposalItem.objects.create(proposal=proposal, **item)
        return proposal

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if items_data is not None:
            instance.items.all().delete()
            for item in items_data:
                ProposalItem.objects.create(proposal=instance, **item)
        return instance