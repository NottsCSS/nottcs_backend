#models
from django.db import models
from django.contrib.auth.models import User

class Names(models.Model):
    primary_key = True
    #Club name and description fields
    club_nameQuestion = models.CharField('Club name: ')
    club_name = models.CharField(max_length = 60)
    club_nameDesc = models.CharField('Club description: ')
    club_desc = models.CharField(max_length = 120)
    
class pictures(models.Model):
    #club pic and logo fields , width and height as arguments
    club_pic = models.ImageField(width_field= 300, height_field= 300)
    club_icon = models.ImageField(width_field = 20, height_field = 20)

class timestamp(models.Model):
    #timestamp below
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self)
        return self.created_at
        return self.updated_at

#This code requires the Pillow library for the ImageField
#URL : https://pillow.readthedocs.io/en/latest/
