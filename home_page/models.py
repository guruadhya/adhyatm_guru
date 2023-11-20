from django.db import models


# Create your models here.
class AboutMaharaj(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='about_maharaj')

    def __str__(self):
        return self.title


class AboutTrust(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='about_trust')

    def __str__(self):
        return self.title


class LiveTv(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


class SocialMediaIcons(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images')

    class Meta:
        db_table = 'gallery_images'


class LookupField(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='lookup_images', null=True, blank=True)
    file = models.FileField(upload_to='lookup_files', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'lookup_field'
