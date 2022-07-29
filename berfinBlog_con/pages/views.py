from django.shortcuts import render
from urllib import request

def index(request):
    return render(request, 'index.html')
