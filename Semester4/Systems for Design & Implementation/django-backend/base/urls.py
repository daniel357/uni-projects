from django.urls import path
from base.views.viewsAircraft import *
from base.views.viewsAirport import *
from base.views.viewsAirline import *
from base.views.viewsPassenger import *
from base.views.viewsStatistics import *
from base.views.viewsFlight import *
from base.views.viewsOperatingFlight import *
from base.views.viewsTicket import *
from base.views.viewsToken import *
from base.views.userViews.viewsConfirmation import *
from base.views.userViews.viewsRegister import *
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('register/confirm', confirm, name='register'),

    path('', HomePageView, name="home-page"),
    path('airport/', airportHomePageView, name="airport-home-page"),
    path('list-airport/', airportList, name="airport-list"),
    path('create-airport/', createAirport, name="airport-create"),
    path('update-airport/<str:pk>/', updateAirport, name="airport-update"),
    path('delete-airport/<str:pk>/', deleteAirport, name="airport-delete"),
    path('read-airport/<str:pk>/', readAirport, name="airport-read"),
    path('filter-airport/<int:pk>/', filter_airport, name="airport-filter"),

    path('aircraft/', aircraftHomePageView, name="aircraft-home-page"),
    path('list-aircraft/', aircraftList, name="aircraft-list"),
    path('create-aircraft/', createAircraft, name="aircraft-create"),
    path('update-aircraft/<str:pk>/', updateAircraft, name="aircraft-update"),
    path('delete-aircraft/<str:pk>/', deleteAircraft, name="aircraft-delete"),
    path('read-aircraft/<str:pk>/', readAircraft, name="aircraft-read"),

    path('airline/', airlineHomePageView, name="airline-home-page"),
    path('list-airline/', airlineList, name="airline-list"),
    path('create-airline/', createAirline, name="aircraft-create"),
    path('update-airline/<str:pk>/', updateAirline, name="airline-update"),
    path('delete-airline/<str:pk>/', deleteAirline, name="airline-delete"),
    path('read-airline/<str:pk>/', readAirline, name="airline-read"),

    path('passenger/', passengerHomePageView, name="passenger-home-page"),
    path('list-passenger/', passengerList, name="passenger-list"),
    path('create-passenger/', createPassenger, name="passenger-create"),
    path('update-passenger/<str:pk>/', updatePassenger, name="passenger-update"),
    path('delete-passenger/<str:pk>/', deletePassenger, name="passenger-delete"),
    path('read-passenger/<str:pk>/', readPassenger, name="passenger-read"),

    path('flight/', flightHomePageView, name="flight-home-page"),
    path('list-flight/', flightList, name="flight-list"),
    path('create-flight/', createFlight, name="flight-create"),
    path('update-flight/<str:pk>/', updateFlight, name="flight-update"),
    path('delete-flight/<str:pk>/', deleteFlight, name="flight-delete"),
    path('read-flight/<str:pk>/', readFlight, name="flight-read"),

    path('ticket/', ticketHomePageView, name="ticket-home-page"),
    path('list-ticket/', ticketList, name="ticket-list"),
    path('create-ticket/', createTicket, name="ticket-create"),
    path('update-ticket/<str:pk>/', updateTicket, name="ticket-update"),
    path('delete-ticket/<str:pk>/', deleteTicket, name="ticket-delete"),
    path('read-ticket/<str:pk>/', readTicket, name="ticket-read"),

    # path('operating-flights/', OperatingFlightsHomePageView, name="operating-flights-home-page"),
    # path('list-operating-flights/', OperatingFlightsList, name="operating-flights-list"),
    # path('create-operating-flights/', createOperatingFlights, name="operating-flights-create"),
    # path('update-operating-flights/<str:pk>/', updateOperatingFlights, name="operating-flights-update"),
    # path('delete-operating-flights/<str:pk>/', deleteOperatingFlights, name="operating-flights-delete"),
    # path('read-operating-flights/<str:pk>/', readOperatingFlights, name="operating-flights-read"),

    path('airline-stats/', airline_revenue_report_view, name="airline-stats"),
    path('flights_passengers_report/', flights_passengers_report, name="flights_passengers_report"),
    path('airline/<int:airline_id>/add_aircrafts', add_aircrafts),
    path('airlineOrderedName/<str:name_filter>/', airlineOrderedName),
    path('airportOrderedName/<str:name_filter>/', airportOrderedName),
    path('aircraftOrderedName/<str:name_filter>/', aircraftOrderedName),
    path('flightOrderedName/<str:name_filter>/', flightOrderedName),
    path('passengerOrderedName/<str:name_filter>/', passengerOrderedName),
]
