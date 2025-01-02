from rest_framework import serializers
from .models import CapturedFrame

class CapturedFrameSerializers(serializers.ModelSerializer):
    class Meta:
        model = CapturedFrame
        fields = ['media', 'timestamp']
