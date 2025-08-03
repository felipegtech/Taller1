from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html', {'name': 'Felipe Gomez Daza'})
    
    # busqueda de peliculas
    searchTerm = request.GET.get('searchMovie')

    # si esta buscando una pelicula
    if searchTerm:
        # solo liste las peliculas que contiene  el nombre que se busca
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})

def about(request):
    return render (request, 'about.html')

def Contact(request):
    return  HttpResponse("<h1> Contact Information: </h1>")
