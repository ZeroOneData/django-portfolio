from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from django.views.generic import TemplateView
import folium
import geocoder

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

def mapView(request):

            # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    # address = Profile.objects.all().last()
    addresses = Profile.objects.all()
    for address in addresses:
        print(address.home_address)

        location = geocoder.osm(address.home_address)
        lat = location.lat
        lng = location.lng
        country = location.country
        if lat == None or lng == None:
            return HttpResponse('You address input is invalid')
        
        def popup_html(address, country):
            popCity = address.home_address
            popPhone = address.phone_number
            popFirstName = address.user.first_name
            popLastName = address.user.last_name
            
            html = """<!DOCTYPE html>
                <html>
                    <div class="shadow mb-5 bg-body rounded" style="max-width: 540px;">
                        <div class="card mb-3" style="max-width: 540px;">
                            <div class="row g-0">  
                                <div class="col-md-8">
                                    <div class="card-body">
                                        <h5 class="card-title">"""+ popFirstName  + ' ' + popLastName +"""</h5>
                                        <p class="card-text">My City: """+ popCity +"""</p>
                                        <p class="card-text">Country: """+ country +"""</p>
                                        <p class="card-text"><small class="text-muted">Phone number: """+ popPhone +"""</small></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </html>
                """
            return html

        popup = folium.Popup(folium.Html(popup_html(address, country), script=True), max_width=500)
        folium.Marker([lat, lng], tooltip=location.city,
                    popup=popup).add_to(m)

    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'map.html', context)