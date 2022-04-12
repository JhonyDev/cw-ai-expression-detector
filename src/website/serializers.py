from rest_framework import serializers

from src.website.models import ScanImage


class ScanImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanImage
        fields = '__all__'
