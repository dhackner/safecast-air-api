from __future__ import unicode_literals

from django.contrib.gis.db import models as gis_models
from django.db import models


class Point(gis_models.Model):

    lon = models.FloatField(help_text="Longitude in decimal degrees")
    lat = models.FloatField(help_text="Latitude in decimal degrees")
    altitude = models.FloatField(help_text='Altitude in meters')
    angle = models.FloatField(help_text='Angle in degrees')
