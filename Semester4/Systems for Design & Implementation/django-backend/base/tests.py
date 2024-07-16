import unittest

from django.test import TestCase, Client
from django.urls import reverse

from base.views import flights_passengers_report


class TestStatisticalReports(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_flights_no_passenger_duration(self):
        url = reverse(flights_passengers_report)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        expected_data = '{"flights": [{"id": 6, "passengers": 3}]}'
        self.assertEqual(str(response.content, encoding='utf8'), expected_data)
        # print(str(response.content, encoding='utf8'))
        # print(expected_data)

    def test_top_airlines_by_revenue(self):
        url = reverse('airline-stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        expected_data = '{"airlines": [{"airline_name": "Delta Air Lines", "revenue": 179600000000}, {"airline_name": "American Airlines", "revenue": 44100000000}, {"airline_name": "United Airlines", "revenue": 43000000000}]}'
        self.assertEqual(str(response.content, encoding='utf8'), expected_data)
        # print(str(response.content, encoding='utf8'))
        # print(expected_data)
