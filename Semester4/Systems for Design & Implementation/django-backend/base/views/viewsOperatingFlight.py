# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from base.models import *
# from base.models.OperatingFlightsModel import OperatingFlights
# from base.serializers import *
# from django.db.models import Count, Avg
#
#
# # ------------------------------------------------------------------------------------OPERATING FLIGHTS
# from base.serializers.OperatingFlightSerializer import OperatingFlightsSerializer
#
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
