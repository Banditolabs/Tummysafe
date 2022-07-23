from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from django.forms import ImageField


# Create your models here.
class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

class Medal(models.Model):
    grades = ["Gold", "Silver", "Bronze"]
    
class GoldMedal(Medal):
    name = 'Gold medal'
    image = open('main_app/static/assets/Goldmedal.png')

    def __str__(self):
        return self.name

class SilverMedal(Medal):
    name = 'Silver medal'
    image = open('main_app/static/assets/Silvermedal.png')
    def __str__(self):
        return self.name

class BronzeMedal(Medal):
    name = 'Bronze medal'
    image = open('main_app/static/assets/Bronzemedal.png')
    def __str__(self):
        return self.name

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE, )
  medals = models.ManyToManyField(Medal)