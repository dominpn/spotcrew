from django.db import models


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    link = models.TextField()

    class Meta:
        managed = True
        db_table = 'images'
