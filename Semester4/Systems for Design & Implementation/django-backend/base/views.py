from operator import attrgetter

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Count, Avg


@api_view(['GET'])  # to only allow a get response
def HomePageView(request):
    api_url = {
        'Airport': '/airport/',
        'Airline': '/airline/',
        'Aircraft': '/aircraft'
    }
    return Response(api_url)


# # --------------------------------------------------------------------------------------------AIRPORT
# @api_view(['GET'])  # to only allow a get response
# def airportHomePageView(request):
#     api_url = {
#         'List': '/list-airport/',
#         'Create': '/create-airport/',
#         'Read': '/read-airport/pk/',
#         'Update': '/update-airport/pk/',
#         'Delete': '/delete-airport/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])  # to only allow a get response
# def airportList(request):
#     list_of_airports = Airport.objects.all().values('id')
#     # serializer = AirportSerializer(list_of_airports, many=True)
#     return Response(list_of_airports)
#
#
# @api_view(['POST'])
# def createAirport(request):
#     serializer = AirportSerializer(data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readAirport(request, pk):
#     try:
#         airport = Airport.objects.get(id=pk)
#         serializer = AirportSerializer(airport, many=False)
#         return Response(serializer.data)
#     except Airport.DoesNotExist:
#         return Response({"error": "Airport not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updateAirport(request, pk):
#     airport = Airport.objects.get(id=pk)
#     serializer = AirportSerializer(instance=airport, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteAirport(request, pk):
#     airport = Airport.objects.get(id=pk)
#     airport.delete()
#     return Response("Airport successfully deleted!")
#
#
# @api_view(['GET'])
# def filter_airport(request, pk):
#     list_of_airports = Airport.objects.filter(noTerminals__gt=pk).values()
#     serializer = AirportSerializer(list_of_airports, many=True)
#     return Response(serializer.data)
#
#
# # ----------------------------------------------------------------------------------------AIRLINE
# @api_view(['GET'])  # to only allow a get response
# def airlineHomePageView(request):
#     api_url = {
#         'List': '/list-airline/',
#         'Create': '/create-airline/',
#         'Read': '/read-airline/pk/',
#         'Update': '/update-airline/pk/',
#         'Delete': '/delete-airline/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])  # to only allow a get response
# def airlineList(request):
#     list_of_airlines = Airline.objects.all().values('id')
#     # serializer = AirlineSerializer(list_of_airlines, many=True)
#     return Response(list_of_airlines)
#
#
# @api_view(['POST'])
# def createAirline(request):
#     serializer = AirlineSerializer(data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readAirline(request, pk):
#     try:
#         airline = Airline.objects.get(id=pk)
#         serializer = AirlineSerializer(airline, many=False)
#         return Response(serializer.data)
#     except Airline.DoesNotExist:
#         return Response({"error": "Airline not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updateAirline(request, pk):
#     airline = Airline.objects.get(id=pk)
#     serializer = AirlineSerializer(instance=airline, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteAirline(request, pk):
#     airline = Airline.objects.get(id=pk)
#     airline.delete()
#     return Response("Airline successfully deleted!")
#
#
# # -----------------------------------------------------------------------------------------------AIRCRAFT
# @api_view(['GET'])  # to only allow a get response
# def aircraftHomePageView(request):
#     api_url = {
#         'List': '/list-aircraft/',
#         'Create': '/create-aircraft/',
#         'Read': '/read-aircraft/pk/',
#         'Update': '/update-aircraft/pk/',
#         'Delete': '/delete-aircraft/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])  # to only allow a get response
# def aircraftList(request):
#     list_of_aircraft = Aircraft.objects.all().values('id')
#     # serializer = AircraftSerializer(list_of_aircraft, many=True)
#     return Response(list_of_aircraft)
#
#
# @api_view(['POST'])
# def createAircraft(request):
#     serializer = AircraftSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readAircraft(request, pk):
#     try:
#         aircraft = Aircraft.objects.get(id=pk)
#         serializer = AircraftSerializer(aircraft, many=False)
#         return Response(serializer.data)
#     except Aircraft.DoesNotExist:
#         return Response({"error": "Aircraft not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updateAircraft(request, pk):
#     aircraft = Aircraft.objects.get(id=pk)
#     serializer = AircraftSerializer(instance=aircraft, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteAircraft(request, pk):
#     aircraft = Aircraft.objects.get(id=pk)
#     aircraft.delete()
#     return Response("Aircraft successfully deleted!")
#
#
# # ------------------------------------------------------------------------------------------PASSENGER
# @api_view(['GET'])  # to only allow a get response
# def passengerHomePageView(request):
#     api_url = {
#         'List': '/list-passenger/',
#         'Create': '/create-passenger/',
#         'Read': '/read-passenger/pk/',
#         'Update': '/update-passenger/pk/',
#         'Delete': '/delete-passenger/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])
# def passengerList(request):
#     list_of_passengers = Passenger.objects.all().values('id')
#     return Response(list_of_passengers)
#
#
# @api_view(['POST'])
# def createPassenger(request):
#     serializer = PassengerSerializer(data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readPassenger(request, pk):
#     try:
#         passenger = Passenger.objects.get(id=pk)
#         serializer = PassengerSerializer(passenger, many=False)
#         return Response(serializer.data)
#     except Passenger.DoesNotExist:
#         return Response({"error": "Aircraft not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updatePassenger(request, pk):
#     passenger = Passenger.objects.get(id=pk)
#     serializer = PassengerSerializer(instance=passenger, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deletePassenger(request, pk):
#     passenger = Passenger.objects.get(id=pk)
#     passenger.delete()
#     return Response("Passenger successfully deleted!")
#
#
# # -------------------------------------------------------------------------------------------FLIGHT
#
# @api_view(['GET'])  # to only allow a get response
# def flightHomePageView(request):
#     api_url = {
#         'List': '/list-flight/',
#         'Create': '/create-flight/',
#         'Read': '/read-flight/pk/',
#         'Update': '/update-flight/pk/',
#         'Delete': '/delete-flight/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])
# def flightList(request):
#     list_of_flights = Flight.objects.all().values('id')
#     return Response(list_of_flights)
#
#
# @api_view(['POST'])
# def createFlight(request):
#     serializer = FlightSerializer(data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readFlight(request, pk):
#     try:
#         flight = Flight.objects.get(id=pk)
#         serializer = FlightSerializer(flight, many=False)
#         return Response(serializer.data)
#     except Flight.DoesNotExist:
#         return Response({"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updateFlight(request, pk):
#     flight = Flight.objects.get(id=pk)
#     serializer = FlightSerializer(instance=flight, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteFlight(request, pk):
#     flight = Flight.objects.get(id=pk)
#     flight.delete()
#     return Response("Flight successfully deleted!")
#
#
# # --------------------------------------------------------------------------------------------------------TICKET
#
#
# @api_view(['GET'])  # to only allow a get response
# def ticketHomePageView(request):
#     api_url = {
#         'List': '/list-ticket/',
#         'Create': '/create-ticket/',
#         'Read': '/read-ticket/pk/',
#         'Update': '/update-ticket/pk/',
#         'Delete': '/delete-ticket/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])
# def ticketList(request):
#     list_of_tickets = Ticket.objects.all().values('id')
#     return Response(list_of_tickets)
#
#
# @api_view(['POST'])
# def createTicket(request):
#     serializer = TicketSerializer(data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readTicket(request, pk):
#     try:
#         ticket = Ticket.objects.get(id=pk)
#         serializer = TicketSerializer(ticket, many=False)
#         return Response(serializer.data)
#     except Ticket.DoesNotExist:
#         return Response({"error": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updateTicket(request, pk):
#     ticket = Ticket.objects.get(id=pk)
#     serializer = TicketSerializer(instance=ticket, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteTicket(request, pk):
#     ticket = Ticket.objects.get(id=pk)
#     ticket.delete()
#     return Response("Ticket successfully deleted!")
#
#
# # ------------------------------------------------------------------------------------OPERATING FLIGHTS
#
# @api_view(['GET'])  # to only allow a get response
# def OperatingFlightsHomePageView(request):
#     api_url = {
#         'List': '/list-operatingFlights/',
#         'Create': '/create-operatingFlights/',
#         'Read': '/read-operatingFlights/pk/',
#         'Update': '/update-operatingFlights/pk/',
#         'Delete': '/delete-operatingFlights/pk/'
#     }
#     return Response(api_url)
#
#
# # query the database, serialize the data and return it as a response
# @api_view(['GET'])
# def OperatingFlightsList(request):
#     list_of_operatingFlights = OperatingFlights.objects.all().values('id')
#     return Response(list_of_operatingFlights)
#
#
# @api_view(['POST'])
# def createOperatingFlights(request):
#     serializer = OperatingFlightsSerializer(data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def readOperatingFlights(request, pk):
#     try:
#         operatingFlights = OperatingFlights.objects.get(id=pk)
#         serializer = OperatingFlightsSerializer(operatingFlights, many=False)
#         return Response(serializer.data)
#     except OperatingFlights.DoesNotExist:
#         return Response({"error": "OperatingFlights not found."}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def updateOperatingFlights(request, pk):
#     operatingFlights = OperatingFlights.objects.get(id=pk)
#     serializer = OperatingFlightsSerializer(instance=operatingFlights, data=request.data)
#     if serializer.is_valid():  # if the item is valid, send it back to the database and save it
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteOperatingFlights(request, pk):
#     operatingFlights = OperatingFlights.objects.get(id=pk)
#     operatingFlights.delete()
#     return Response("OperatingFlights successfully deleted!")
#
#
# # ----------------------------------------------------------------------------------------statistical report
# # get the top 3 airlines with the most revenue per aircraft
#
#
# def get_airline_revenue_report():
#     aircrafts = Aircraft.objects.all()
#     airlines_revenue = {}
#     for aircraft in aircrafts:
#         airline_name = aircraft.airline_name.name
#         if airline_name in airlines_revenue:
#             airlines_revenue[airline_name] += aircraft.airline_name.revenue
#         else:
#             airlines_revenue[airline_name] = aircraft.airline_name.revenue
#     sorted_airlines = sorted(airlines_revenue.items(), key=lambda x: x[1], reverse=True)
#     airline_revenue_dto_list = []
#     i = 0
#     for airline_name, revenue in sorted_airlines:
#         airline_revenue_dto_list.append(AirlineRevenueDTO(airline_name=airline_name, revenue=revenue))
#         i = i + 1
#         if i == 3:
#             break
#     return airline_revenue_dto_list
#
#
# def airline_revenue_report_view(request):
#     airline_dtos = get_airline_revenue_report()
#     data = {
#         'airlines': [
#             {'airline_name': dto.airline_name, 'revenue': dto.revenue}
#             for dto in airline_dtos
#         ]
#     }
#     return JsonResponse(data)
#
#
# # ----------------------------------------------
# # statistical report that shows all flights sorted by their duration that have the most passengers
#
# def flights_passengers_report(request):
#     flights = Flight.objects.annotate(num_passengers=Count('ticket')) \
#         .order_by('-num_passengers', 'duration') \
#         .values('id', 'duration', 'num_passengers')
#
#     max_passengers = flights.first()['num_passengers']
#
#     result = [FlightPassengersDTO(item['id'], item['num_passengers']) for item in flights if
#               item['num_passengers'] == max_passengers]
#
#     result.sort(key=lambda x: x.passengers, reverse=True)
#
#     response_data = {
#         'flights': [{'id': item.flight_id, 'passengers': item.passengers} for item in
#                     result]
#     }
#
#     return JsonResponse(response_data)
#
#
# # ---------------------------------------------------------------------------
# # add multiple aircraft to an airline, by specifying the airline id in the url
#
# @api_view(['POST'])
# def add_aircrafts(request, airline_id):
#     airline = get_object_or_404(Airline, pk=airline_id)
#     aircraft_data = request.data
#     for aircraft in aircraft_data:
#         aircraft['airline_name'] = airline_id
#     serializer = AircraftSerializer(data=aircraft_data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
