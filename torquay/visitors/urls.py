
from django.contrib import admin
from django.urls import path,include
from .views import * 

urlpatterns = [
    path('booking/',booking,name="booking" ),
    path('info/',info,name="info" ),
    path('signup/', signup_view, name='signup'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
]