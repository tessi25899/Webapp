from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    birthday = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=256)
    unit = models.ForeignKey('units.unit',on_delete=models.CASCADE, null=True, blank=True)
    entrydate = models.DateTimeField(null=True, blank=True)
    hobby = models.TextField(null=True,blank=True)
    flameone = models.BooleanField(default=False)
    flametwo = models.BooleanField(default=False)
    performanceclasp = models.BooleanField(default=False)
    flamethree = models.BooleanField(default=False)

    def __str__(self):
        return self.username

