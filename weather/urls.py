from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
import openweathermap.views as weather

router = routers.DefaultRouter()
router.register(r'temperature', weather.HourlyWeatherViewSet)
router.register(r'full_weahter', weather.WeatherViewSet)

urlpatterns = [
    # Examples:
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', weather.home, name='home'),
    url(r'^weather$', weather.weather_site, name='weather'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^abc/(?P<param>\d+)/$',
        view=weather.PressureGraph.as_view(), name='abc'),
    url(r'^hor/(?P<param>\d+)/$',
        view=weather.HourlyWeatherGraph.as_view(), name='hor'),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
