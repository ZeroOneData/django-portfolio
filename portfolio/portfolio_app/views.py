from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

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