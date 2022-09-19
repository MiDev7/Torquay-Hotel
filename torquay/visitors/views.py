from audioop import reverse
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from django.shortcuts import *
from django.contrib.auth.views import *
from django.contrib.auth import *
# Create your views here.

# Login section
def login_view(request):
    if (request.method == "POST"):
        username = request.cleaned_data['username']
        password = request.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if (user is not None):
            login(request, user)
            return redirect (reverse('homepage'))

        else:
            return redirect(reverse('signup'))
    elif (request.method == "GET"):
        return render(request, "registration/login.html", context={'form': LoginForm})


def signup_view(request):
    if(request.method == "GET"):
        return render(request,'registration/signup.html',context={'form': SignupForm})

    elif(request.method == "POST"):
        myuser = SignupForm(request.POST)
        myuser.save()
        return redirect(reverse('login'))

def logout_view(request):
    logout(request)
    

def booking(request):
    if(request.method == "GET"):
        return render(request,'booking.html',context={'form': BookingForm})

    elif(request.method == "POST"):
        mybooking = BookingForm(request.POST)
        mybooking.save()
        return redirect(reverse('info'))
    return render(request,'booking.html',context={})
    
def info(request):
    return render(request,'info.html',context={})
    