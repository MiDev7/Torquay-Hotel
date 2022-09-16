from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)
    features = models.ManyToManyField(Feature)

    
class Room(models.Model):
    availability = models.BooleanField(default=True)
    max_people = models.IntegerField(max_length=20)
    number_of_beds = models.IntegerField()
    price = models.IntegerField(max_length=500)
    pet_allowed = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)

class Booking(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , null=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL , null=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    confirmed = models.BooleanField(default=False)
    number_of_people = models.IntegerField(max_length=15, blank=False,null=True)

