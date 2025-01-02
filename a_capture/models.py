from django.db import models

class CapturedFrame(models.Model):
    image = models.ImageField(upload_to="frames/")
    timestamp = models.DateTimeField(auto_now_add=True)
