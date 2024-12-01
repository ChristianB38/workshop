from django.urls import path
from . import views

urlpatterns = [
    path('', views.star_list, name='star_list')
]