from django.shortcuts import render

# Create your views here.
from prakalp.models import Prakalp, PrakalpImage

from .models import AboutTrust, AboutMaharaj


def home_page(request):
    prakalp = Prakalp.objects.all()
    context = {
        'prakalp': prakalp
    }
    return render(request, 'home_page.html', context)


def about_maharaj(request):
    maharaj = AboutMaharaj.objects.all()
    context = {
        'maharaj': maharaj[0]
    }
    return render(request, 'about_maharaj.html', context)


def about_trust(request):
    trust = AboutTrust.objects.all()
    context = {
        'trust': trust[0]
    }
    return render(request, 'about_trust.html', context)
