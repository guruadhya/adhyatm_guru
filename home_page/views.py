from django.shortcuts import render

# Create your views here.
from prakalp.models import Prakalp, PrakalpImage


def home_page(request):
    prakalp = Prakalp.objects.all()
    context = {
        'prakalp': prakalp
    }
    return render(request, 'home_page.html', context)


def prakalp_details(request, prakalp_id):
    prakalp = Prakalp.objects.get(id=prakalp_id)
    prakalp_images = PrakalpImage.objects.filter(prakalp_id=prakalp_id)
    context = {
        'prakalp': prakalp,
        'images': prakalp_images,
    }
    return render(request, 'prakalp_details.html')
