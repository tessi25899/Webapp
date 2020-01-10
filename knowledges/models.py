from django.db import models

class Fwdv(models.Model):
    fwdv = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0}".format(self.name)# (FwdV: {1})".format(self.name, self.slug)

class Knowledge(models.Model):
    fwdv = models.ForeignKey(to='Fwdv', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return "{0}".format(self.name)

class Knowledgecontent(models.Model):
    knowledge = models.ForeignKey(to='Knowledge', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    context = models.TextField()
    #image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.knowledge)    