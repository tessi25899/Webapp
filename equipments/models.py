from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    radio_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images' ,null=True, blank=True)
    feature = models.TextField(null=True, blank=True)
    water_tank = models.IntegerField(null=True, blank=True)
    crew = models.ForeignKey(to='Crewgroup', on_delete=models.CASCADE)
    unit = models.ForeignKey('units.unit',on_delete=models.CASCADE, null=True, blank=True)

    vehiclegroup = models.ForeignKey(to='Vehiclegroup', on_delete=models.CASCADE, null=True, blank=True)
    #Fahrzeugdaten
    construction_date = models.IntegerField(null=True, blank=True)
    producer = models.CharField(max_length=256, null=True, blank=True)
    power = models.CharField(max_length=256, null=True, blank=True)
    petrol_tank = models.CharField(max_length=256, null=True, blank=True)
    ton = models.CharField(max_length=256, null=True, blank=True)
    length = models.CharField(max_length=256, null=True, blank=True)
    width = models.CharField(max_length=256, null=True, blank=True)
    heigth = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)

class Tool(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images' ,null=True, blank=True)

    toolgroup = models.ForeignKey(to='Toolgroup', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)

class Assignment(models.Model):
    tool = models.ForeignKey(to='Tool', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(to='Vehicle', on_delete=models.CASCADE)
    place = models.CharField(max_length=256)
    nominal_stock= models.IntegerField() 

class Stocktaking(models.Model):
    assignment = models.ForeignKey(to='Assignment', on_delete=models.CASCADE)
    actual_stock = models.IntegerField()
    date = models.DateField() 

#Kategorie Gruppen:
class Crewgroup(models.Model):
    name = models.CharField(max_length=256)
    size = models.CharField(max_length=256)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.size)

class Toolgroup(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)

class Vehiclegroup(models.Model):
    name = models.CharField(max_length=256)
    shortcut = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)