from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Profile
import folium
# import geocoder

""" List view class displaying list of user Profiles on home page """
class HomeView(ListView):
    model = Profile
    template_name = 'home.html'

""" functional view for displaying inteactive World Map """
def mapView(request):

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    addresses = Profile.objects.all()

    #loop through user profiles dictionary extracting key-value pairs
    for address in addresses:

        """ usefull future boilerplate  """
        # location = geocoder.osm(address.home_address)
        # lat = location.lat
        # lng = location.lng
        # country = location.country

        # set Gps coordinates
        lat = address.gps_lat
        lng = address.gps_lng

        if lat == None or lng == None:
            return HttpResponse('Your gps coordinates are invalid')
        
        #function to render the dynamic popup html
        def popup_html(address, lat, lng):
            popHome = address.home_address
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
                                        <p class="card-text">My Home: """+ popHome +"""</p>
                                        <p class="card-text">GPS Latitude: """+ str(lat) +"""</p>
                                        <p class="card-text">GPS Longitude: """+ str(lng) +"""</p>
                                        <p class="card-text"><small class="text-muted">Phone number: """+ popPhone +"""</small></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </html>
                """
            return html

        popup = folium.Popup(folium.Html(popup_html(address, lat, lng), script=True), max_width=500)
        folium.Marker([lat, lng], tooltip="check this profile",
                    popup=popup).add_to(m)

    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'map.html', context)