from django.shortcuts import render
from .models import Star, Telescope

def star_list(request):
    stars = Star.objects.all()
    return render(request, 'stars/star_list.html', {'stars': stars})

def telescope_list(request):
    telescopes = Telescope.objects.all()
    return render(request, 'stars/telescope_list.html', {'telescopes': telescopes})
