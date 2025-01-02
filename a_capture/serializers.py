from rest_framework import serializers
from .models import CapturedFrame

class CapturedFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedFrame
        fields = ['media'] 