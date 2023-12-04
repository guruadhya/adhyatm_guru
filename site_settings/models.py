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


class ContactDetails(models.Model):
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.address


class DanDetails(models.Model):
    scaner = models.ImageField(upload_to='daan_scaner')
    details = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'daan_details'
