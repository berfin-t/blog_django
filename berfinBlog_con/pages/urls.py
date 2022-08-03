from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('works.html', views.works, name="works"),
]