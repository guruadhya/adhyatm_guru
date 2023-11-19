from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prakalp_details/<int:prakalp_id>/', views.prakalp_details, name='prakalp_details'),

]
