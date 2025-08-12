from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ["id", "client", "uploaded_by", "name", "file", "file_url", "created_at"]
        read_only_fields = ["id", "uploaded_by", "created_at", "file_url"]

    def get_file_url(self, obj):
        request = self.context.get("request")
        if obj.file and hasattr(obj.file, "url"):
            url = obj.file.url
            if request is not None:
                return request.build_absolute_uri(url)
            return url
        return None