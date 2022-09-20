from tabnanny import check
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)
    features = models.ManyToManyField(Feature)
    max_people = models.IntegerField( default= 1,null=True)
    number_of_beds = models.IntegerField(default= 1,null=True)
    price = models.IntegerField(default= 500,null=True)
    pet_allowed = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.name }   {self.price}"   

    
class Room(models.Model):
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return f"{self.id}  {self.category} "

    @classmethod
    def search(cls,date_in,date_out,category_id):
        available_room = []
        category = Category.objects.get(id=category_id)
        rooms = Room.objects.filter(category=category)

        for room in rooms:
            booking = Booking.objects.filter(
                models.Q(room=room) & (
                models.Q(check_in_date__lte=date_in) & models.Q(check_out_date__gte=date_in) |
                models.Q(check_in_date__lte=date_out) & models.Q(check_out_date__gte=date_out)
                
            ))
            if (len(booking) == 0):
                available_room.append(room)

        return available_room

    def book(self,date_in,date_out,user,number_of_people):
        booked =  Booking(
            user = user,
            room = self,
            check_in_date = date_in,
            check_out_date = date_out,
            number_of_people = number_of_people
        )

        booked.save()
        return booked

    @property
    def total_price(self,date_in,date_out):
        time_stay = date_out - date_in
        total = time_stay * self.category.price
        return total 


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL , null=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    confirmed = models.BooleanField(default=False)
    number_of_people = models.IntegerField(blank=False,null=True)
    price = models.IntegerField(null=True)
    
    def save(self, *args, **kwargs):
        date_format = "%Y-%m-%d"
        print(f"type of chekout date {type(self.check_in_date)}")
        delta = (datetime.strptime(self.check_out_date, date_format) - datetime.strptime(self.check_in_date, date_format)) 

        self.price = delta.days * self.room.category.price
        super(Booking, self).save(*args, **kwargs)


