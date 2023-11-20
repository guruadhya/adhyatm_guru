from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('about_maharaj/', views.about_maharaj, name='about_maharaj'),
    path('about_trust/', views.about_trust, name='about_trust'),

]
