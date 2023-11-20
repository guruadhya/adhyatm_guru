from django.shortcuts import render, redirect

# Create your views here.
from prakalp.models import Prakalp, PrakalpImage

from .models import AboutTrust, AboutMaharaj, Gallery, LookupField


def home_page(request):
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url
    prakalp = Prakalp.objects.all()
    context = {
        'header_banner_homepage': header_banner_homepage,
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


def add_gallery_images(request):
    if request.method == 'POST':
        image = request.FILES.getlist('image')
        for i in range(len(image)):
            Gallery.objects.create(image=image[i])
        return redirect('/gallery_images/')
    return render(request, 'add_gallery_images.html')


def gallery_images(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery
    }
    return render(request, 'gellery_images.html', context)
