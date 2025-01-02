from django.urls import path
from .views import CapturedFrameUploadView

urlpatterns = [
    path('frame/', CapturedFrameUploadView.as_view(), name='frame-upload'),
]