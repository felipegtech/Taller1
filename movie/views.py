from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

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


def statistics_view(request):
    matplotlib.use('Agg')

    # ------------------ Grafica: Peliculas por año ----------------------

    # ----------------- Gráfica: Películas por año -----------------
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year = "None"
        count = movies_in_year.count()
        movie_counts_by_year[year] = count

    plt.figure(figsize=(10,5))
    plt.bar(range(len(movie_counts_by_year)), movie_counts_by_year.values(), width=0.5, align='center')
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(range(len(movie_counts_by_year)), movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)
    
    buffer_year = io.BytesIO()
    plt.savefig(buffer_year, format='png')
    buffer_year.seek(0)
    plt.close()
    graphic_year = base64.b64encode(buffer_year.getvalue()).decode('utf-8')
    buffer_year.close()

    # ----------------- Gráfica: Películas por género -----------------
    movies = Movie.objects.all()
    genre_counts = {}

    for movie in movies:
        if movie.genre:  # Asegurarse que el género exista
            first_genre = movie.genre.split(',')[0].strip()  # Tomar solo el primer género
            genre_counts[first_genre] = genre_counts.get(first_genre, 0) + 1

    plt.figure(figsize=(10,5))
    plt.bar(range(len(genre_counts)), genre_counts.values(), width=0.5, align='center', color='orange')
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(range(len(genre_counts)), genre_counts.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer_genre = io.BytesIO()
    plt.savefig(buffer_genre, format='png')
    buffer_genre.seek(0)
    plt.close()
    graphic_genre = base64.b64encode(buffer_genre.getvalue()).decode('utf-8')
    buffer_genre.close()

    # ----------------- Renderizar plantilla -----------------
    context = {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    }
    return render(request, 'statistics.html', context)

def about(request):
    return render (request, 'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def contact(request):
    return  HttpResponse("<h1> Contact Information: </h1>")
