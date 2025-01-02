from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

class CapturedFrameViewset(viewsets.ModelViewSet):
    queryset = models.CapturedFrame.objects.all()
    serializer_class = serializers.CapturedFrameSerializers

    