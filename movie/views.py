from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    return render(request, 'home.html', {'name': 'Felipe Gomez Daza'})

def about(request):
    return HttpResponse("<h1> Welcome to About page</h1>")

def Contact(request):
    return  HttpResponse("<h1> Contact Information: </h1>")

