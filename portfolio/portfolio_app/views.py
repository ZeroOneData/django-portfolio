from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from django.views.generic import TemplateView

#temp import
from django.contrib.auth.models import User

# def home(request):
#     return render (request, 'home.html', {})

class HomeView(ListView):

    #temp model decleration
    model = Profile

    template_name = 'home.html'

class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile_details.html'

class MapView(TemplateView):
    template_name = 'map.html'