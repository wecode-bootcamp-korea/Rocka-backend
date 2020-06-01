from django.db import models

class Store(models.Model):
    name            = models.CharField(max_length=100)
    branch          = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=50)
    address         = models.CharField(max_length=500)
    store_time      = models.CharField(max_length=100)
    map_url         = models.URLField(max_length=2000)

    class Meta:
        db_table = 'stores'
