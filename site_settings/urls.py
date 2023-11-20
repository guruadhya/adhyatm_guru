from django.urls import path
from . import views

urlpatterns = [
    path('contact_details/', views.contact_details, name='contact_details'),
]
