from django.shortcuts import render, redirect
from .models import Star, Telescope
from .forms import StarForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


def star_list(request):
    stars = Star.objects.all()

    items = [
        {
            "name": star.name,
            "details": f"Constellation: { star.constellation} , Magnitude: { star.magnitude} ",
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
    return render(request, 'stars/telescope_list.html', {'telescopes': telescopes})


def add_star(request):
    if request.method == "POST":
        form = StarForm(request.POST)
        if form.is_valid():
            form.save() # Save the form data to create a new Star
            return redirect('star_list') # Redirect to the star list page
    else:
        form = StarForm()
    return render(request, 'stars/add_star.html', {'form': form})

def update_star(request, pk):
    star = get_object_or_404(Star, pk=pk) # Fetch the star by primary key or return a 404 error
    if request.method == "POST":
        form = StarForm(request.POST, instance=star)
        if form.is_valid():
            form.save() # Save the updated data
            return redirect('star_list')
    else:
        form = StarForm(instance=star) # Pre-fill the form with the star's current data
    return render(request, 'stars/update_star.html', {'form': form, 'star': star})

def delete_star(request, pk):
    star = get_object_or_404(Star, pk=pk) # Fetch the star by primary key or return a 404 error
    if request.method == "POST":
        # form = StarForm(request.POST, instance=star)
        star.delete() # Save the updated data
        return redirect('star_list')
    # else:
        # form = StarForm(instance=star) # Pre-fill the form with the star's current data
    return render(request, 'stars/delete_star.html', { 'star': star}) #, 
