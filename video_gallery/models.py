from django.db import models


# Create your models here.
class VideoGallery(models.Model):
    link = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.created_at)
