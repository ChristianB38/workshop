from django.shortcuts import render
from .models import Star

def star_list(request):
    stars = Star.objects.all()
    return render(request, 'stars/star_list.html', {'stars': stars})
