from django.db import models

from spotcrew_backend.venues.models import Venues


class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    link = models.TextField()

    class Meta:
        managed = True
        db_table = 'images'


class VenueImages(models.Model):
    venue_image_id = models.AutoField(primary_key=True)
    image_id = models.OneToOneField(Images, models.DO_NOTHING, db_column="image_id")
    venue_id = models.OneToOneField(Venues, models.DO_NOTHING, db_column="venue_id")
