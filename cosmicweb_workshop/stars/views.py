from django.shortcuts import render, redirect, get_object_or_404
from .models import Star, Telescope
from .forms import StarForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def update_star(request, pk):
    star = get_object_or_404(Star, pk=pk)
    if request.method == "POST":
        form = StarForm(request.POST, instance=star)
        if form.is_valid():
            form.save()
            return redirect('star_list')
    else:
        form = StarForm(instance=star)
    return render(request, 'stars/update_star.html', {'form': form, 'star': star})

def delete_star(request, pk):
    star = get_object_or_404(Star, pk=pk)
    if request.method == "POST":
        star.delete()
        return redirect('star_list')
    return render(request, 'stars/delete_star.html', {'star': star})