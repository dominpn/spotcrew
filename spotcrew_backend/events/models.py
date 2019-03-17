from django.db import models

from users.models import User
from venues.models import Venue


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    venue_id = models.OneToOneField(Venue, models.DO_NOTHING, db_column='venue_id')
    host_id = models.OneToOneField(User, models.DO_NOTHING, db_column='user_id')
    name = models.TextField()
    description = models.TextField()
    # TODO trim seconds
    event_start = models.DateTimeField()
    event_stop = models.DateTimeField()
    # TODO validate field value from list (enumerate)
    sport_name = models.TextField()

    class Meta:
        managed = True
        db_table = 'events'
