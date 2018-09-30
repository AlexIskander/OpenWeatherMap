from django.test import TestCase
from .midels import City
# Create your tests here.


class CityTestCase(TestCase):
    def setUp(self):
        City.objects.create(name="lion", city_id="roar", lon=21322, lat=12122)
        City.objects.create(name="cat", city_id="meow", lon=2132, lat=1213)
