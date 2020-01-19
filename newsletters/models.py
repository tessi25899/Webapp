from django.db import models
from profiles.models import Profile

class News(models.Model):
    name = models.CharField(max_length=256)
    topic = models.ForeignKey(to='Topic', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    published = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(to= 'profiles.Profile',on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=256,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name