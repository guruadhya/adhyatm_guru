from django.shortcuts import render

# Create your views here.
from adhyatm_guru.prakalp.models import Prakalp


def home_page(request):
    prakalp = Prakalp.objects.all()
    context = {
        'prakalp': prakalp
    }
    return render(request, 'home_page.html', context)
