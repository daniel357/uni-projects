from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from base.models.PassengerModel import Passenger
from base.serializers import *
from django.db.models import Count, Avg


# ------------------------------------------------------------------------------------------PASSENGER
from base.serializers.PassengerSerializer import PassengerSerializer
from base.serializers.TicketSerializer import TicketSerializer
from base.views.pagination import CustomPagination


@api_view(['GET'])  # to only allow a get response
def passengerHomePageView(request):
    api_url = {
        'List': '/list-passenger/',
        'Create': '/create-passenger/',
        'Read': '/read-passenger/pk/',
        'Update': '/update-passenger/pk/',
        'Delete': '/delete-passenger/pk/'
    }
    return Response(api_url)


# query the database, serialize the data and return it as a response
@api_view(['GET'])
def passengerList(request):
    paginator = CustomPagination()
    list_of_passengers = Passenger.objects.all()
    paginated_list_of_passengers = paginator.paginate_queryset(list_of_passengers, request)
    serializer = PassengerSerializer(paginated_list_of_passengers, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def createPassenger(request):
    serializer = PassengerSerializer(data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def readPassenger(request, pk):
    try:
        passenger = Passenger.objects.prefetch_related('ticket_passenger').get(id=pk)
        ticket_list = passenger.ticket_passenger.all()
        ticket_list_serializer = TicketSerializer(ticket_list, many=True)
        serializer = PassengerSerializer(passenger, many=False)
        passenger_data = serializer.data
        passenger_data['tickets'] = ticket_list_serializer.data
        return Response(passenger_data)
    except Passenger.DoesNotExist:
        return Response({"error": "Aircraft not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def updatePassenger(request, pk):
    passenger = Passenger.objects.get(id=pk)
    serializer = PassengerSerializer(instance=passenger, data=request.data)
    if serializer.is_valid():  # if the item is valid, send it back to the database and save it
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePassenger(request, pk):
    passenger = Passenger.objects.get(id=pk)
    passenger.delete()
    return Response("Passenger successfully deleted!")


@api_view(['GET'])
def passengerOrderedName(request, name_filter):
    paginator = CustomPagination()
    list_of_passengers = Passenger.objects.filter(last_name__icontains=name_filter)
    paginated_list_of_passengers = paginator.paginate_queryset(list_of_passengers, request)
    serializer = PassengerSerializer(paginated_list_of_passengers, many=True)
    return paginator.get_paginated_response(serializer.data)
