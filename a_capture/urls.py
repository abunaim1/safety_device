from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_frame, name='upload_frame'),
]
