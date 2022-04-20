from django.urls import path
from .views import HomeView,  ProfileDetailView, mapView

urlpatterns = [
    path('', HomeView.as_view(), name = "home" ),
    path('map/', mapView, name="map"),
    path('profiles/<int:pk>', ProfileDetailView.as_view(), name = "profile_detail"),
]
