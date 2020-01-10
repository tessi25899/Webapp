from django.db import models

class News(models.Model):
    name = models.CharField(max_length=256)
    message = models.TextField()
    published = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return "{0}".format(self.name)