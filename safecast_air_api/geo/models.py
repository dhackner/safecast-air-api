from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.db import models


class Point(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    altitude = models.FloatField()
    angle = models.FloatField()
