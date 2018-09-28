#  -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import timedelta
from datetime import datetime as D
from django.utils import timezone
from django.shortcuts import get_object_or_404 as get_obj
from django.shortcuts import render, redirect

from weather.settings import STATIC_URL

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import HourlyWeatherSerializer, WeatherSerializer
from highcharts.views import HighChartsMultiAxesView
from .models import WeatherTwoWeeks, City, HourlyWeather


# Create your views here.

def date_diapason(namber=2):
    """Get date diapason."""
    today = timezone.now()
    delta = timedelta(namber)
    return today, today + delta


class HourlyWeatherViewSet(viewsets.ModelViewSet):
    """API for hourly weather temperature."""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = HourlyWeather.objects.filter(date__range=date_diapason())[:8]

    serializer_class = HourlyWeatherSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    """API  weather for two weeks."""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = WeatherTwoWeeks.objects.filter(id_city=703448)

    serializer_class = WeatherSerializer


def home(request, template='base.html'):
    """Home page."""
    return redirect('/weather')


def weather_site(request, template='weather/weather.html'):
    """Weather page."""
    nowTemp = get_obj(City, name='Kiev')
    return render(request, template, {'nowTemp': nowTemp})


class PressureGraph(HighChartsMultiAxesView):
    """show pressure graph ajax."""
    title = 'Atmosphere pressure'
    chart_type = 'spline'
    xlabels = {'rotation': 0}
    # subtitle = 'params and query'
    chart = {'zoomType': 'xy'}
    tooltip = {'valueSuffix': u'hpa'}
    legend = {
        'layout': 'vertical',
        'align': 'right',
        'verticalAlign': 'top',
        'y': 30
    }
    plot_options = {
        'spline': {
            'dataLabels': {
                'enabled': 'true'
            },
            'enableMouseTracking': 'false',
            'marker': {
                'radius': 4,
                'lineColor': '#666666',
                'lineWidth': 2
            }

        }
    }

    def get_data(self):
        param = self.kwargs['param']
        weather = WeatherTwoWeeks.objects.filter(id_city=param)

        # SERIES
        self.serie = [{'name': weather[0].id_city.name,
                       'data': [int(val.pressure) for val in weather]}]

        # X LABELS
        self.categories = [D.strftime(val.date, '%a %d/%m/%y')
                           for val in weather]

        # Y AXIS DEFINITIONS
        self.yaxis = {
            'title': {
                'text': u'Pressure (hpa)'
            },
            'plotLines': [
                {
                    'value': 0,
                    'width': 1,
                    'color': '#808080'
                }
            ]
        }

        # SERIES WITH VALUES
        self.series = self.serie
        data = super(PressureGraph, self).get_data()
        return data


class HourlyWeatherGraph(HighChartsMultiAxesView):
    """show temperature graph  ajax."""
    title = 'Temperature'
    chart_type = 'spline'
    xlabels = {'rotation': 0}
    # subtitle = 'params and query'
    tooltip = {'valueSuffix': u'°C',
               'shared': 'true',
               }
    legend = {
        'layout': 'vertical',
        'align': 'right',
        'verticalAlign': 'top',
        'y': 30
    }
    plot_options = {
        'spline': {
            'dataLabels': {
                'enabled': 'true'
            }}}

    def data_weather(self, weather):
        return [{'y': int(val.temp),
                 'marker': {'symbol': 'url(%simages/%s.png)' %
                            (STATIC_URL, val.icon)}} for val in weather]

    def get_data(self):
        param = self.kwargs['param']
        weather = HourlyWeather.objects.filter(
            id_city=param).filter(date__range=date_diapason())[:8]

        # SERIES
        self.serie = [{'name': weather[0].id_city.name,
                       'data': self.data_weather(weather),
                       }]

        # X LABELS
        self.categories = [D.strftime(val.date, '%a %H:%M') for val in weather]

        # Y AXIS DEFINITIONS
        self.yaxis = {
            'title': {
                'text': u'Temperature °C'
            },
            'plotLines': [
                {
                    'value': 0,
                    'width': 2,
                    'color': '#808080'
                }
            ]
        }

        # SERIES WITH VALUES
        self.series = self.serie
        data = super(HourlyWeatherGraph, self).get_data()
        return data
