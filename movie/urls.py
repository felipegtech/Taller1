from django.urls import path
from . import views   # Importa las vistas de la app movie

urlpatterns = [
    path('', views.home, name='movie-home'),  #  /movies/ -> movie list
    path('about/', views.about, name='movie-about'),  # Ejemplo: /movies/about/
    path('contact/', views.contact, name='movie-contact') # /movie/Contact
]
