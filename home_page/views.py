from django.shortcuts import render, redirect

# Create your views here.
from prakalp.models import Prakalp, PrakalpImage

from .models import AboutTrust, AboutMaharaj, Gallery, LookupField
from site_settings.models import SiteSettings, DanDetails

from carousel.models import Carousel, CarouselImages


def home_page(request):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url

    header_middle_banner = LookupField.objects.filter(title='header_middle_banner')
    if header_middle_banner:
        header_middle_banner = header_middle_banner[0].image.url

    carousel_id = Carousel.objects.filter(title='homepage_carousel')
    if carousel_id:
        carousel = CarouselImages.objects.filter(carousel_id=carousel_id[0].id)
    else:
        carousel = ''

    prakalp = Prakalp.objects.all()

    dan = DanDetails.objects.first()
    if dan:
        dan = dan
    else:
        dan = ''


    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'header_middle_banner': header_middle_banner,
        'carousel': carousel,
        'prakalp': prakalp,
        'dan': dan,
    }
    # return render(request, 'home_page.html', context)
    return render(request, 'new_homepage.html', context)


def about_maharaj(request):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url

    maharaj = AboutMaharaj.objects.all()
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'maharaj': maharaj[0]
    }
    return render(request, 'about_maharaj.html', context)


def about_trust(request):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url

    trust = AboutTrust.objects.all()
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
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
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url
    gallery = Gallery.objects.all()
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'gallery': gallery
    }
    return render(request, 'gellery_images.html', context)


def daan(request):
    site_info = SiteSettings.objects.all()
    header_daan_banner = LookupField.objects.filter(title='header_daan_banner')
    if header_daan_banner:
        header_daan_banner = header_daan_banner[0].image.url

    carousel_id = Carousel.objects.filter(title='homepage_carousel')
    if carousel_id:
        carousel = CarouselImages.objects.filter(carousel_id=carousel_id[0].id)
    else:
        carousel = ''

    dan = DanDetails.objects.first()
    if dan:
        dan = dan
    else:
        dan = ''
    context = {
        'site_info': site_info[0],
        'header_daan_banner': header_daan_banner,
        'carousel': carousel,

        'dan': dan,
    }
    return render(request, 'daan.html', context)
