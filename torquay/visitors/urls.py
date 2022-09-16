
from django.contrib import admin
from django.urls import path,include
from .views import * 

urlpatterns = [
    path('booking/',booking,name="booking" ),
    path('info/',info,name="info" ),
]