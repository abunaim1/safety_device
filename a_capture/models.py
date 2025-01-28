from django.db import models
from django.contrib.auth.models import User

class CapturedFrame(models.Model):
    media = models.FileField(upload_to='frames/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
