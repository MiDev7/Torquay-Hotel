from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class BookingTestCase(TestCase):
    
    fixtures =  ["features.json","category.json","room.json"]

    def setUp(self):
        myuser = User(username="Tony",password="lol77")
        myuser.save()
    def test_room_availability(self):
        rooms = Room.search("2022-08-12","2022-09-10",3)
        self.assertEqual(len(rooms),10)  
        name = User.objects.get(username= "Tony")
        r1 = rooms[1].book("2022-08-12","2022-09-10",name,2)

        self.assertEqual(r1.price,9)
        r2= Room.search("2022-08-12","2022-09-10",3)
        self.assertEqual(len(r2),9)


