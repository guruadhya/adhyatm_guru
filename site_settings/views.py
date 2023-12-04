from django.shortcuts import render

# Create your views here.
from site_settings.models import ContactDetails

from home_page.models import LookupField
from site_settings.models import SiteSettings


def contact_details(request):
    site_info = SiteSettings.objects.all()
    header_banner_homepage = LookupField.objects.filter(title='header_banner_homepage')
    if header_banner_homepage:
        header_banner_homepage = header_banner_homepage[0].image.url
    contact_info = ContactDetails.objects.all()
    context = {
        'site_info': site_info[0],
        'header_banner_homepage': header_banner_homepage,
        'contact_info': contact_info[0],
    }
    return render(request, 'contact_details.html', context)
