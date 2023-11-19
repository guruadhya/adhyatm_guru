from django.shortcuts import render


# Create your views here.
from .models import Prakalp, PrakalpImage


def prakalp_details(request, prakalp_id):
    prakalp = Prakalp.objects.get(id=prakalp_id)
    prakalp_images = PrakalpImage.objects.filter(prakalp_id=prakalp_id)
    # print(prakalp_images, '============prakalp_images')
    context = {
        'prakalp': prakalp,
        'images': prakalp_images,
    }
    return render(request, 'prakalp_details.html', context)
