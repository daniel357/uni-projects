from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import joblib

model = joblib.load(r"C:\Users\User\Downloads\rf_regressor_model.pkl")


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            days_before_flight = data.get('daysBeforeFlight')
            flight_day_of_week = data.get('flightDayOfWeek')
            travel_duration_minutes = data.get('travelDurationMinutes')
            near_holiday = data.get('nearHoliday')
            flight_month = data.get('flightMonth')
            flight_day = data.get('flightDay')
            departure_hour = data.get('departureHour')
            departure_minute = data.get('departureMinute')
            arrival_hour = data.get('arrivalHour')
            arrival_minute = data.get('arrivalMinute')

            if None in [days_before_flight, flight_day_of_week, travel_duration_minutes, near_holiday,
                        flight_month, flight_day, departure_hour, departure_minute, arrival_hour, arrival_minute]:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            features = np.array([[days_before_flight, flight_day_of_week, travel_duration_minutes, near_holiday,
                                  flight_month, flight_day, departure_hour, departure_minute, arrival_hour,
                                  arrival_minute]])
            print(features)
            prediction = model.predict(features)
            return JsonResponse({'prediction': prediction[0]})
        except KeyError as e:
            return JsonResponse({'error': f'Missing key: {e}'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
