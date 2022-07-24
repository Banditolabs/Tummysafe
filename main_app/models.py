from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from django.forms import CharField, ImageField


# Create your models here.
HEALTH = (
    ('TS', 'TummySafe'),
    ('TC', 'TummyCautious'),
    ('TSC', 'TummyScared'),
    ('TN', 'TummyNope')
)
SERVICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5','5')
)
TASTE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5','5')
)
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

class Address(models.Model):
    postcode = models.CharField( max_length=50)
    address_line = models.CharField( max_length=255)
    address_line2 = models.CharField( max_length=255)
    state_province = models.CharField(max_length=150)
    town_city = models.CharField( max_length=150)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "Address"

# Place Information_______
class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    health_rating = models.CharField(
        max_length=3,
        choices=HEALTH,
        default=None

    )
    service_rating = models.CharField(
        max_length=1,
        choices=SERVICE,
        default=[0][0]
    )
    taste_rating = models.CharField(
        max_length=1,
        choices=TASTE,
        default=[0][0]
    )

    def __str__(self):
        return self.name

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Photo (models.Model):
  url = models.CharField(max_length=200)
  place = models.ForeignKey(Place, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for place_id: {self.place_id} @{self.url}"


class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE, )
  medals = models.ManyToManyField(Medal)


