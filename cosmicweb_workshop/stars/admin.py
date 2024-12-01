from django.contrib import admin
from .models import Star, Telescope

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ('name', 'constellation', 'magnitude')

@admin.register(Telescope)
class TelescopeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location')
