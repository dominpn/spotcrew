from django.db import models

from spotcrew_backend.venues.models import Venue


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    link = models.TextField()

    class Meta:
        managed = True
        db_table = 'images'


class VenueImage(models.Model):
    venue_image_id = models.AutoField(primary_key=True)
    image_id = models.OneToOneField(Image, models.DO_NOTHING, db_column="image_id")
    venue_id = models.OneToOneField(Venue, models.DO_NOTHING, db_column="venue_id")
