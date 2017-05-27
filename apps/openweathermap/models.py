from datetime import datetime as D

import pytz

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class City(models.Model):
    """City with a unique identifier and its coordinates to show
    temperature."""
    name = models.CharField(max_length=40, verbose_name=_(u"City name"))
    city_id = models.PositiveIntegerField(
        verbose_name=_(u"City ID"), unique=True)
    lon = models.DecimalField(
        max_digits=12, decimal_places=8, verbose_name=_(u"Long"))
    lat = models.DecimalField(
        max_digits=12, decimal_places=8, verbose_name=_(u"Latitude"))

    class Meta:
        verbose_name = _(u'name')
        verbose_name_plural = _(u'name')
        ordering = [u'name']

    def __unicode__(self):
        return self.name


class WeatherTwoWeeks(models.Model):
    """General information about the weather for two weeks, including such
    factors as:

    pressure, humidity, wind speed, cloudiness, temperature, etc.

    """
    id_city = models.ForeignKey(
        City, to_field='city_id',
        related_name='weather', verbose_name=_(u"City id"))
    max_temp = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name=_(u"Max temperature"))
    min_temp = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name=_(u"Min temperature"))
    description = models.CharField(
        max_length=40, verbose_name=_(u"Weather condition"))
    icon = models.CharField(max_length=20, verbose_name=_(u"Weather icon"))
    wind = models.DecimalField(
        max_digits=8, decimal_places=0, verbose_name=_(u"Wind speed"))
    pressure = models.DecimalField(
        max_digits=4, decimal_places=0, verbose_name=_(u"Pressure, hpa"))
    humidity = models.DecimalField(
        max_digits=3, decimal_places=0, verbose_name=_(u'Humidity'))
    clouds = models.DecimalField(
        max_digits=3, decimal_places=0, verbose_name=_(u"Cloudiness, %"))
    date = models.DateTimeField(verbose_name=_(u"Date"))
    position = models.DecimalField(
        max_digits=3, decimal_places=0, verbose_name=_(u"Position for day"))

    def __unicode__(self):
        return '%d: %s' % (self.pressure, self.description,)

    def save(self, *args, **kwargs):
        try:
            zone = pytz.timezone('Europe/Kiev')
            self.date = D.fromtimestamp(self.date).replace(tzinfo=zone)
        except:
            pass
        super(WeatherTwoWeeks, self).save(*args, **kwargs)


class HourlyWeather(models.Model):
    """Weather for the day.

    To plot the daily temperature

    """
    id_city = models.ForeignKey(City, to_field='city_id')
    date = models.DateTimeField(verbose_name=_(u'Date time'))
    temp = models.DecimalField(max_digits=2, decimal_places=0)
    icon = models.CharField(max_length=8, verbose_name=_(u'Icon'))
    position = models.DecimalField(
        max_digits=3, decimal_places=0, verbose_name=_(u"Position for day"))

    def __unicode__(self):
        return '%d' % self.temp

    def save(self, *args, **kwargs):
        try:
            zone = pytz.timezone('Europe/Kiev')
            self.date = D.fromtimestamp(self.date).replace(tzinfo=zone)
        except:
            pass
        super(HourlyWeather, self).save(*args, **kwargs)
