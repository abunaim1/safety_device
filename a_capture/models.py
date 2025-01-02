from django.db import models

class CapturedFrame(models.Model):
    media = models.FileField(upload_to='uploads/', blank=True, null=True)  # To store image file
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Frame {self.id} - {self.timestamp}"
