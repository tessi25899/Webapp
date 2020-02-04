from django.db import models

class Filedocument(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    document = models.FileField(upload_to="files", max_length=254)
    published = models.DateField(null=True, blank=True, auto_now=True, editable=False)
    updated = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(to= 'profiles.Profile',on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.owner) 

class Commentary(models.Model):
    filedocument = models.ForeignKey(to='Filedocument', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    published = models.DateField(null=True, blank=True, auto_now=True, editable=False)
    owner = models.ForeignKey(to= 'profiles.Profile',on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return "{0} | {1}: {2}".format(self.filedocument, self.owner, self.comment) 