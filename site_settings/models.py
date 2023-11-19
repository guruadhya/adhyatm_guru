from django.db import models


# Create your models here.
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=256)
    site_logo = models.ImageField(upload_to='site_logo')
    site_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.site_name

    class Meta:
        db_table = 'site_settings'
