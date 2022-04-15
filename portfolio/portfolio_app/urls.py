
from django.urls import path
#from . import views
from .views import HomeView, ProfileDetailView


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name = "home" ),
    path('profiles/<int:pk>', ProfileDetailView.as_view(), name = "profile_detail")
]
