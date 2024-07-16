from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from base.models.AircraftModel import Aircraft
from base.models.AirlineModel import Airline
from base.models.DTOModels import AirlineRevenueDTO, FlightPassengersDTO
from base.models.FlightModel import Flight
from base.serializers import *
from django.db.models import Count, Avg, Sum

# ----------------------------------------------------------------------------------------statistical report
# get the top 3 airlines with the most revenue per aircraft
from base.serializers.AircraftSerializer import AircraftSerializer


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
#     data = [{"airline_name": dto.airline_name, "revenue": dto.revenue} for dto in airline_dtos]
#     return JsonResponse(data, safe=False)


def get_airline_revenue_report():
    aircrafts = Aircraft.objects.select_related('airline_name').values('airline_name__name').annotate(
        revenue=Sum('airline_name__revenue')).order_by('-revenue')[:3]
    airline_revenue_dto_list = [
        AirlineRevenueDTO(airline_name=aircraft['airline_name__name'], revenue=aircraft['revenue']) for aircraft in
        aircrafts]
    return airline_revenue_dto_list


def airline_revenue_report_view(request):
    airline_dtos = get_airline_revenue_report()
    data = [{"airline_name": dto.airline_name, "revenue": dto.revenue} for dto in airline_dtos]
    return JsonResponse(data, safe=False)


# ----------------------------------------------
# statistical report that shows all flights sorted by their duration that have the most passengers

def flights_passengers_report(request):
    flights = Flight.objects.annotate(num_passengers=Count('ticket')) \
        .order_by('-num_passengers', 'duration') \
        .values('id', 'duration', 'num_passengers')

    max_passengers = flights.first()['num_passengers']

    result = [FlightPassengersDTO(item['id'], item['num_passengers']) for item in flights if
              item['num_passengers'] == max_passengers]

    result.sort(key=lambda x: x.passengers, reverse=True)
    response_data = {
        'flights': [{'id': item.flight_id, 'passengers': item.passengers} for item in
                    result]
    }

    return JsonResponse(response_data)


# ---------------------------------------------------------------------------
# add multiple aircraft to an airline, by specifying the airline id in the url

@api_view(['POST'])
def add_aircrafts(request, airline_id):
    airline = get_object_or_404(Airline, pk=airline_id)
    aircraft_data = request.data
    for aircraft in aircraft_data:
        aircraft['airline_name'] = airline_id
    serializer = AircraftSerializer(data=aircraft_data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
