from django.db import models

class Unit(models.Model):
    slug = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    housenumber = models.CharField(max_length=256)
    postcode = models.CharField(max_length=256)
    place = models.CharField(max_length=256)
    day = models.CharField(max_length=15, null=True, blank=True)
    starttime =  models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    endtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.slug
