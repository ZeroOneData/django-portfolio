from django.urls import path
from .views import HomeView, mapView

urlpatterns = [
    path('', HomeView.as_view(), name = "home" ),
    path('map/', mapView, name="map"),
]
