from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import WeatherTwoWeeks, HourlyWeather


class HourlyWeatherSerializer(serializers.ModelSerializer):
    """Serializer for HourlyWeather."""
    class Meta:
        model = HourlyWeather
        fields = ('date', 'temp')


class WeatherSerializer(serializers.ModelSerializer):
    """Serializer for WeatherTwoWeeks."""
    class Meta:
        model = WeatherTwoWeeks
        fields = '__all__'
