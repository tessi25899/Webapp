from django.db import models
from units.models import Unit

class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    kind = models.ForeignKey(to='Kindtable', on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(to= 'units.Unit',on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time =  models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.name)
        #return "({0}) {1}".format(self.date,self.name)

class Kindtable(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.name)
