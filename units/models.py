from django.db import models

class Unit(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    housenumber = models.CharField(max_length=256)
    postcode = models.CharField(max_length=256)
    place = models.CharField(max_length=256)

    def __str__(self):
        return self.slug