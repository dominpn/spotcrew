from django.db import models


class Sport(models.Model):
    sport_id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'sports'
