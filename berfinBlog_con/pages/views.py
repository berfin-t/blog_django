from django.shortcuts import render
from urllib import request

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def works(request):
    return render(request, 'works.html')
