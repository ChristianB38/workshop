from django.shortcuts import render, redirect
from .models import Star, Telescope
from .forms import StarForm

def star_list(request):
    stars = Star.objects.all()
    return render(request, 'stars/star_list.html', {'stars': stars})

def telescope_list(request):
    telescopes = Telescope.objects.all()
    return render(request, 'stars/telescope_list.html', {'telescopes': telescopes})

def add_star(request):
    if request.method == "POST":
        form = StarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('star_list')
    else:
        form = StarForm()

    return render(request, 'stars/add_star.html', {'form': form})