from django.db import models


# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'carousel'


class CarouselImages(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carousel_images')

    def __str__(self):
        return str(self.carousel.title)

    class Meta:
        db_table = 'carousel_images'
