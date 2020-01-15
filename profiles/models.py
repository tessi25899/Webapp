from django.db import models
from django.conf import settings

class Profile(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    biographie = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=256,null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images' ,null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=256, null=True, blank=True)
    unit = models.ForeignKey('units.unit',on_delete=models.CASCADE, null=True, blank=True)
    entrydate = models.DateField(null=True, blank=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey('Role',default= 4 ,on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.username.username

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25)

class ProfileBadges(models.Model):
    user = models.ForeignKey('Profile',on_delete=models.CASCADE, null=True, blank=True)
    badge = models.ForeignKey('Badge',on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{0}: {1}'.format(self.user, self.badge)

class Group(models.Model):
    name = models.CharField(max_length=256) 
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '{0}'.format(self.name)

class Role(models.Model):
    name = models.CharField(max_length=256) 
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '({0}){1}'.format(self.id,self.name)

class Badge(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    require_age = models.IntegerField( null=True, blank=True)
    require_badge = models.ForeignKey('Badge',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Hobby(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True,blank=True)