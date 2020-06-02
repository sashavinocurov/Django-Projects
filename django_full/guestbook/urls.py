from django.urls import path  
from . import views  

urlpatterns = [
    path('', views.index, name="index"),
    path('sign/', views.sign, name="sign"),
    path('search/', views.search, name="search"),
    path('movie/', views.movies, name="movie"),
]