from rest_framework import serializers
from . import models

class CapturedFrameSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CapturedFrame
        fields = '__all__'

