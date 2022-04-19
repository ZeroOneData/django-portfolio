
from django.urls import path
#from . import views
from .views import HomeView, MapView, ProfileDetailView



urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name = "home" ),
    path('map/', MapView.as_view(), name="map"),
    path('profiles/<int:pk>', ProfileDetailView.as_view(), name = "profile_detail"),
]
