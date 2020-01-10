from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    kind = models.ForeignKey(to='Kindtable', on_delete=models.CASCADE)
    unit = models.ForeignKey(to='Unit',on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return "({0}) {1}".format(self.date,self.name)

class Kindtable(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return "{0}".format(self.name)

class Unit(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=256, null=True, blank=True)
    slug = models.SlugField(unique=True,null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    housenumber = models.CharField(max_length=256, null=True, blank=True)
    postcode = models.CharField(max_length=256, null=True, blank=True)
    place = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.slug)