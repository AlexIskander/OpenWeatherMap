from __future__ import absolute_import, unicode_literals

import os
import json
import urllib2

from celery.task import periodic_task
from celery.task.schedules import crontab

from .models import WeatherTwoWeeks, City, HourlyWeather

host_api = 'http://api.openweathermap.org/data/2.5/forecast'
city_ = '703448'
api_pid = '&APPID=%s' % os.environ["TOKEN"] 

api_full = '%s/daily?id=%s&cnt=14&units=metric&lang=ru%s' % (
    host_api, city_, api_pid)
api_days = '%s?id=%s&units=metric&lang=ru%s' % (host_api, city_, api_pid)


def get_json(api):
    """Get data json."""
    response = urllib2.urlopen(api)
    data = response.read()
    return json.loads(data)


def get_city(data):
    city, created = City.objects.update_or_create(
        city_id=data['city']['id'],
        name=data['city']['name'],
        defaults={
            'lon': data['city']['coord']['lon'],
            'lat': data['city']['coord']['lat'], })
    return city


@periodic_task(ignore_result=True, run_every=(crontab(minute=30, hour='*/3')))
def two_week_weather_task():
    """GET weather to 14th days every 210 minets."""

    data = get_json(api_full)
    city = get_city(data)
    for i, val in enumerate(data['list']):
        WeatherTwoWeeks.objects.update_or_create(
            id_city=city,
            position=i,
            defaults={'max_temp': val['temp']['max'],
                      'min_temp': val['temp']['min'],
                      'description': val['weather'][0]['description'],
                      'icon': val['weather'][0]['icon'],
                      'wind': val['speed'],
                      'pressure': val['pressure'],
                      'humidity': val['humidity'],
                      'clouds': val['clouds'],
                      'date': int(val['dt']),
                      'position': i, })


@periodic_task(ignore_result=True, run_every=(crontab(minute=12, hour='*/1')))
def hourly_weather_task():
    """We get the weather for every three hours."""

    data = get_json(api_days)
    city = get_city(data)

    for i, val in enumerate(data['list']):
        w, create = HourlyWeather.objects.update_or_create(
            id_city=city,
            position=i,
            defaults={
                'date': val['dt'],
                'temp': val['main']['temp'],
                'icon': val['weather'][0]['icon']
            })
