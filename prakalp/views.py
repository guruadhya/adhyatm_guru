from django.shortcuts import render

# Create your views here.
from .models import Prakalp, PrakalpImage
from home_page.models import LookupField
from site_settings.models import SiteSettings


def prakalp_details(request, prakalp_id):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url

    prakalp = Prakalp.objects.get(id=prakalp_id)
    prakalp_images = PrakalpImage.objects.filter(prakalp_id=prakalp_id)
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'prakalp': prakalp,
        'images': prakalp_images,
    }
    return render(request, 'prakalp_details.html', context)


def prakal(request):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url

    prakalp = Prakalp.objects.all()
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'prakalp': prakalp,
    }
    return render(request, 'prakalp.html', context)
