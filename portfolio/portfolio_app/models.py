from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE)
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile")
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')