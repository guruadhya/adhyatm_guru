from django.contrib import admin
from .models import SiteSettings, ContactDetails

# Register your models here.
admin.site.register(SiteSettings)
admin.site.register(ContactDetails)
