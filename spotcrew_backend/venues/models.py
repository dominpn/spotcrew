from django.contrib.gis.db import models as gis_models
from django.db import models

from images.models import Image


class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    location = gis_models.PointField()
    city = models.TextField()
    address = models.TextField()
    images = models.ManyToManyField(Image)
    objects = gis_models.Manager()

    class Meta:
        managed = True
        db_table = 'venues'
