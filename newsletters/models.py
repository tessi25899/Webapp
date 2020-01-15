from django.db import models

class News(models.Model):
    name = models.CharField(max_length=256)
    message = models.TextField()
    published = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=256)

    def __str__(self):
        return self.name
