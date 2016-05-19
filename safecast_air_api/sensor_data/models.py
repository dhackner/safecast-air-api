from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel

from django.contrib.postgres.fields import JSONField


class RawReading(TimeStampedModel):

    raw_json = JSONField(null=True)

    @property
    def processed(self):
        return self.readings.exists()


class Device(TimeStampedModel):

    class Meta:
        ordering = ('created', )

    user = models.ForeignKey('users.User')
    type = models.CharField(max_length=32)
    id = models.CharField(max_length=32, primary_key=True)


class Sensor(TimeStampedModel):

    class Meta:
        ordering = ('created', )

    device = models.ForeignKey('Device')


class ReadingStamp(TimeStampedModel):  # Way to link readings across sensors

    class Meta:
        ordering = ('reading_time', )

    reading_time = models.DateTimeField()
    location = models.ForeignKey('geo.Point')
    fix = models.BooleanField()
    speed = models.FloatField(help_text='Speed in meters per second')
    satellite_count = models.PositiveSmallIntegerField()


class Reading(TimeStampedModel):

    reading_id = models.PositiveSmallIntegerField()
    sensor = models.ForeignKey('Sensor')
    stamp = models.ForeignKey('ReadingStamp')
    raw_reading = models.ForeignKey('RawReading', related_name='readings')


class GasReading(Reading):

    pass


class PMReading(Reading):

    pass


class TemperatureReading(Reading):

    header = models.PositiveSmallIntegerField()
    temperature = models.FloatField(verbose_name='Temperature in Celsius')
    temperature_lowpass = models.FloatField(verbose_name='Temperature in Celsius lowpass filtered')
