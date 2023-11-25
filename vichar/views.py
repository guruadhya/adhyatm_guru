from django.shortcuts import render

# Create your views here.
from .models import Vichar


def vichar(request):
    vichar = Vichar.objects.all()
    context = {
        'vichar': vichar,
    }
    return render(request, 'vichar.html', context)
