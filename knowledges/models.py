from django.db import models
from profiles.models import Profile

class Topic(models.Model):
    name = models.SlugField(unique=True)
    ordernumber = models.IntegerField()
    created_by = models.ForeignKey(to='profiles.profile', on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{0}".format(self.name) 

class Knowledge(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256, null=True, blank=True)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images' ,null=True, blank=True)
    content = models.TextField()
    footer = models.CharField(max_length=256, null=True, blank=True)#Quellen etc.
    ordernumber = models.IntegerField(unique=True)
    created_by = models.ForeignKey(to='profiles.profile',on_delete=models.DO_NOTHING)

    def __str__(self):
        return "({0} / {1}) {2} [{3}]".format(self.topic, self.title, self.name, self.ordernumber) 