from django.shortcuts import render

# Create your views here.
from site_settings.models import ContactDetails


def contact_details(request):
    contact_info = ContactDetails.objects.all()
    context = {
        'contact_info': contact_info[0],
    }
    return render(request, 'contact_details.html', context)
