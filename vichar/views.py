from django.shortcuts import render

# Create your views here.
from .models import Vichar
from site_settings.models import SiteSettings

from home_page.models import LookupField


def vichar(request):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url

    vichar = Vichar.objects.all()
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'vichar': vichar,
    }
    return render(request, 'vichar.html', context)
