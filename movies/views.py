from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pelicula
# Create your views here.

class Movielistview(ListView):
    model = Pelicula 
    template_name="movies/movie_list.html"

class MoviedeatilView(DetailView):
    model = Pelicula
    template_name="movies/movie_detail.html"
