from django.contrib import admin
from .models import SiteSettings, ContactDetails, DanDetails

# Register your models here.
admin.site.register(SiteSettings)
admin.site.register(ContactDetails)
admin.site.register(DanDetails)
