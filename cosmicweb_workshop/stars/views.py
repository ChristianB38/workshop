from django.shortcuts import render, redirect, get_object_or_404
from .models import Star, Telescope
from .forms import StarForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def star_list(request):
    stars = Star.objects.all()

    items = [
        {
            "name": star.name,
            "details": f"Constellation: {star.constellation}, Magnitude: {star.magnitude}",
            "edit_url": reverse('update_star', args=[star.id]),
            "delete_url": reverse('delete_star', args=[star.id])
        }
        for star in stars
    ]

    context = {
        "title": "Star List",
        "items": items,
    }

    return render(request, 'stars/list_view.html', context)

def telescope_list(request):
    telescopes = Telescope.objects.all()

    items = [
        {
            "name": telescope.name,
            "details": f"Location: {telescope.location}, Type: {telescope.type}"
        }
        for telescope in telescopes
    ]

    context = {
        "title": "Telescope List",
        "items": items,
    }

    return render(request, 'stars/list_view.html', context)

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