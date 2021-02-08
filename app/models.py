from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Country(models.Model):
    Country_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Country_name

class Customer(AbstractUser):

    travel_country=models.ManyToManyField(Country,related_name="country")
    PhoneNumber=models.PositiveIntegerField(null=True)
    address=models.CharField(max_length=200,null=True)
    zipcode=models.PositiveIntegerField(null=True)

    def __str__(self):
        # return str(self.id)
        return self.first_name



