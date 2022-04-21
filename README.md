
# Introduction

This application leverages the Python programming language and the Django framework to deliver a modern, responsive, full-stack web application. 

The goal of the application is to provide a "membership"-type website with a User Profile section - storing the GPS coordinates of each members' home address, amongst other user related attributes. A link to a page displaying a dynamic World Map, is provided - with a clickable geo-location icon rendered onto the map at the GPS coordinates for each registered user's Home Address. The python Folium library is imported and leveraged to provide the dynamic mapping functionality.

Upon clicking the individual Users geo-location icon, a popup appears displaying the user's profile data.


### Main features

* Extended django built-in user module to further add relevant user Profile attributes, namely, home address, phone number, GPS longitude and latituude coordinates - as well as an      optional profile picture.

* A User Profile page and a page to edit the user's Profile.

* A Registration page, a Sign-in page and a page to create a user Profile for newly registered users.

* A Change password page.

* A page displaying a fully dynamic and interactive georgaphical map - with each registered user's home address location superimposed onto the map.

* Clickable geo-location icons displaying user Profile popup

* Tech-Stack utilised:
    -   Python
    -   Django
    -   Folium
    -   Git

# Usage

This application is not intended for production - it is, however intended for use as a solution to a coding challenge set forth during the interview process toward a Software Develepoment Role


# wiiHome - django fullstack web application

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/ZeroOneData/django-portfolio.git
    $ cd portfolio
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt

Make migrations:

    $ python manage.py makemigrations
      
Then simply apply the migrations:

    $ python manage.py migrate
    
Then create a super user:

    $ python manage.py createsuperuser  [ Windows OS:   $ winpty python manage.py createsuperuser ]

    -fill in username 
    -fill in password

You can now run the development server:

    $ python manage.py runserver

Launch the application from your Web browser

    From your Web browser navigate to 'http://localhost:8000'

Enjoy!!!!

    author: Tyron Anderson
