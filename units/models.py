from django.db import models


class Unit(models.Model):
    slug = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    housenumber = models.CharField(max_length=256)
    postcode = models.CharField(max_length=256)
    place = models.CharField(max_length=256)

    def __str__(self):
        return '{0}'.format(self.slug)

class Workinghour(models.Model):
    WOCHENTAGE = (
        ('Mo','Montag'),
        ('Di','Dienstag'),
        ('Mi','Mittwoch'),
        ('Do','Donnerstag'),
        ('Fr','Freitag'),
        ('Sa','Samstag'),
        ('SO','Sonntag'),
    )
    unit = models.ForeignKey('Unit',on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('profiles.group',on_delete=models.CASCADE, null=True, blank=True)
    day = models.CharField(max_length=15, null=True, blank=True, choices=WOCHENTAGE)
    starttime =  models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    endtime = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.unit, self.group)