from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

"""Profile model class - extends base User model """
class Profile(models.Model):
    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE)
    home_address = models.CharField(max_length=255)
    gps_lat = models.DecimalField(decimal_places=4, max_digits=6, default='0')
    gps_lng = models.DecimalField(decimal_places=4, max_digits=7, default='0')
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile")
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')