from django.db import models


class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    city = models.TextField()
    address = models.TextField()

    class Meta:
        managed = True
        db_table = 'venues'
