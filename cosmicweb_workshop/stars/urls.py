from django.urls import path
from . import views

urlpatterns = [
    path('star/', views.star_list, name='star_list'),
    path('telescope/', views.telescope_list, name='telescope_list'),
    path('add_star/', views.add_star, name='add_star'),
    path('update_star/<int:pk>/', views.update_star, name='update_star'),
    path('delete_star/<int:pk>/', views.delete_star, name='delete_star')

]