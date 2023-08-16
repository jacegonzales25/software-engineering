from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Philippines Trips<h1>")

# Create your views here.
