from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from base.models.AirlineModel import Airline
from base.serializers import *
from django.db.models import Count, Avg

# ----------------------------------------------------------------------------------------AIRLINE
from base.serializers.AircraftSerializer import AircraftSerializer
from base.serializers.AirlineSerializer import AirlineSerializer
from base.views.pagination import CustomPagination


@api_view(['GET'])  # to only allow a get response
def airlineHomePageView(request):
    api_url = {
        'List': '/list-airline/',
        'Create': '/create-airline/',
        'Read': '/read-airline/pk/',
        'Update': '/update-airline/pk/',
        'Delete': '/delete-airline/pk/'
    }
    return Response(api_url)


# query the database, serialize the data and return it as a response
@api_view(['GET'])  # to only allow a get response
def airlineList(request):
    paginator = CustomPagination()
    list_of_airlines = Airline.objects.annotate(no_aircrafts=Count('airlines'))
    paginated_list_of_airlines = paginator.paginate_queryset(list_of_airlines, request)
    serializer = AirlineSerializer(paginated_list_of_airlines, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def createAirline(request):
    serializer = AirlineSerializer(data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def readAirline(request, pk):
    try:
        airline = Airline.objects.prefetch_related('airlines').get(id=pk)
        aircraft_list = airline.airlines.all()
        aircraft_list_serializer = AircraftSerializer(aircraft_list, many=True)
        serializer = AirlineSerializer(airline, many=False)
        airline_data = serializer.data
        airline_data['aircraft_list'] = aircraft_list_serializer.data
        return Response(airline_data)
    except Airline.DoesNotExist:
        return Response({"error": "Airline not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def updateAirline(request, pk):
    airline = Airline.objects.get(id=pk)
    serializer = AirlineSerializer(instance=airline, data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAirline(request, pk):
    airline = Airline.objects.get(id=pk)
    airline.delete()
    return Response("Airline successfully deleted!")


@api_view(['GET'])
def airlineOrderedName(request, name_filter):
    paginator = CustomPagination()
    list_of_airlines = Airline.objects.filter(name__icontains=name_filter)
    paginated_list_of_airlines = paginator.paginate_queryset(list_of_airlines, request)
    serializer = AirlineSerializer(paginated_list_of_airlines, many=True)
    return paginator.get_paginated_response(serializer.data)
