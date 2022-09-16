from django.contrib import admin
from django.urls import path,include
from .views import * 

urlpatterns = [
    path('api/bookings/',getbookings,name="bookings" ),
    path('calender/',showcalender,name="showcalender" ),
]