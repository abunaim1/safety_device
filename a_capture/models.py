from django.db import models

class CapturedFrame(models.Model):
    media = models.FileField(upload_to='frames/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
