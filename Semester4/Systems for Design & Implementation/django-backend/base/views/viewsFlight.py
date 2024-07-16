from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from base.models.AirportModel import Airport
from base.models.FlightModel import Flight
from base.serializers import *
from django.db.models import Count, Avg

# -------------------------------------------------------------------------------------------FLIGHT
from base.serializers.AircraftSerializer import AircraftSerializer
from base.serializers.AirportSerializer import AirportSerializer
from base.serializers.FlightSerializer import FlightSerializer
from base.serializers.TicketSerializer import TicketSerializer
from base.views.pagination import CustomPagination


@api_view(['GET'])  # to only allow a get response
def flightHomePageView(request):
    api_url = {
        'List': '/list-flight/',
        'Create': '/create-flight/',
        'Read': '/read-flight/pk/',
        'Update': '/update-flight/pk/',
        'Delete': '/delete-flight/pk/'
    }
    return Response(api_url)


# query the database, serialize the data and return it as a response
@api_view(['GET'])
def flightList(request):
    paginator = CustomPagination()
    list_of_flights = Flight.objects.all()
    paginated_list_of_flights = paginator.paginate_queryset(list_of_flights, request)
    serializer = FlightSerializer(paginated_list_of_flights, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def createFlight(request):
    serializer = FlightSerializer(data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


# @api_view(['GET'])
# def readFlight(request, pk):
#     try:
#
#         flight = Flight.objects.prefetch_related('ticket_flight').get(id=pk)
#         ticket_list = flight.ticket_flight.all()
#         ticket_list_serializer = TicketSerializer(ticket_list, many=True)
#         serializer = FlightSerializer(flight, many=False)
#         flight_data = serializer.data
#         flight_data['tickets'] = ticket_list_serializer.data
#         return Response(flight_data)
#     except Flight.DoesNotExist:
#         return Response({"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def readFlight(request, pk):
    try:
        flight = Flight.objects.prefetch_related('ticket_flight').get(id=pk)

        # Accessing related objects
        departure_airport = flight.departure_airport
        arrival_airport = flight.arrival_airport
        operating_aircraft = flight.operating_aircraft

        ticket_list = flight.ticket_flight.all()
        ticket_list_serializer = TicketSerializer(ticket_list, many=True)
        serializer = FlightSerializer(flight, many=False)
        flight_data = serializer.data
        flight_data['tickets'] = ticket_list_serializer.data

        # Adding related objects to the response
        flight_data['departure_airport'] = AirportSerializer(departure_airport).data
        flight_data['arrival_airport'] = AirportSerializer(arrival_airport).data
        flight_data['operating_aircraft'] = AircraftSerializer(operating_aircraft).data

        return Response(flight_data)
    except Flight.DoesNotExist:
        return Response({"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def updateFlight(request, pk):
    flight = Flight.objects.get(id=pk)
    serializer = FlightSerializer(instance=flight, data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteFlight(request, pk):
    flight = Flight.objects.get(id=pk)
    flight.delete()
    return Response("Flight successfully deleted!")


@api_view(['GET'])
def flightOrderedName(request, name_filter):
    paginator = CustomPagination()
    list_of_flights = Flight.objects.filter(call_sign__icontains=name_filter)
    paginated_list_of_flights = paginator.paginate_queryset(list_of_flights, request)
    serializer = FlightSerializer(paginated_list_of_flights, many=True)
    return paginator.get_paginated_response(serializer.data)
