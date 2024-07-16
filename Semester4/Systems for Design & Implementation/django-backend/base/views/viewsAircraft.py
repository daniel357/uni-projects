from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from base.models.AircraftModel import Aircraft
from base.models.AirlineModel import Airline
from base.serializers import *
from django.db.models import Count, Avg

# -----------------------------------------------------------------------------------------------AIRCRAFT
from base.serializers.AircraftSerializer import AircraftSerializer
from base.serializers.AirlineSerializer import AirlineSerializer
from base.serializers.FlightSerializer import FlightSerializer
from base.views.pagination import CustomPagination


@api_view(['GET'])  # to only allow a get response
def aircraftHomePageView(request):
    api_url = {
        'List': '/list-aircraft/',
        'Create': '/create-aircraft/',
        'Read': '/read-aircraft/pk/',
        'Update': '/update-aircraft/pk/',
        'Delete': '/delete-aircraft/pk/'
    }
    return Response(api_url)


# query the database, serialize the data and return it as a response
@api_view(['GET'])  # to only allow a get response
def aircraftList(request):
    paginator = CustomPagination()
    list_of_aircraft = Aircraft.objects.annotate(no_flights=Count('aircraft'))
    paginated_list_of_airports = paginator.paginate_queryset(list_of_aircraft, request)
    serializer = AircraftSerializer(paginated_list_of_airports, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def createAircraft(request):
    serializer = AircraftSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def readAircraft(request, pk):
    try:
        aircraft = Aircraft.objects.prefetch_related('aircraft').get(id=pk)
        airline = Airline.objects.get(id=pk)
        serialized_airline = AirlineSerializer(airline, many=False)
        flight_list = aircraft.aircraft.all()
        flight_list_serializer = FlightSerializer(flight_list, many=True)
        serializer = AircraftSerializer(aircraft, many=False)
        aircraft_data = serializer.data
        aircraft_data['operated_flights'] = flight_list_serializer.data
        aircraft_data['airline_name'] = serialized_airline.data
        return Response(aircraft_data)
    except Aircraft.DoesNotExist:
        return Response({"error": "Aircraft not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def updateAircraft(request, pk):
    aircraft = Aircraft.objects.get(id=pk)
    serializer = AircraftSerializer(instance=aircraft, data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAircraft(request, pk):
    aircraft = Aircraft.objects.get(id=pk)
    aircraft.delete()
    return Response("Aircraft successfully deleted!")


@api_view(['GET'])
def aircraftOrderedName(request, name_filter):
    paginator = CustomPagination()
    list_of_airlines = Aircraft.objects.filter(name__icontains=name_filter)
    paginated_list_of_airlines = paginator.paginate_queryset(list_of_airlines, request)
    serializer = AircraftSerializer(paginated_list_of_airlines, many=True)
    return paginator.get_paginated_response(serializer.data)
