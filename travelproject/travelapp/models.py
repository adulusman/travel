from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.


class Place(models.Model):
    head = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    
    def __str__(self):
        return self.head
    
class Team(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250)
    desc = models.TextField()
    def __str__(self):
        return self.name
    