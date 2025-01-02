from django.db import models

class CapturedFrame(models.Model):
    media = models.FileField(upload_to='uploads/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
