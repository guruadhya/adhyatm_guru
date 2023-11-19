from django.db import models


# Create your models here.
class Prakalp(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    main_image = models.ImageField(upload_to='prakalp_images')

    def __str__(self):
        return self.title

    class meta:
        db_table = 'prakalp'


class PrakalpImage(models.Model):
    prakalp = models.ForeignKey(Prakalp, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prakalp_images')

    class Meta:
        db_table = 'prakalp_image'
