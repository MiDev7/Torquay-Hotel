from audioop import reverse
from email import message
from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import *
from django.contrib.auth.views import *
from django.contrib.auth import *
from django.http import JsonResponse
# Create your views here.

# Login section
def login_view(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
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
        form = BookingForm(request.POST or None)
        room = request.POST.get('room')
        room_type = Category.objects.get(name=room)
        category_id = room_type.id
        date_in = request.POST.get('check_in_date')
        date_out = request.POST.get('check_out_date')
        total_people = request.POST.get('number_of_people')
        print(room)
        rooms = Room.search(date_in,date_out,category_id)
        user = request.user
        try: 
            rooms[0].book(date_in,date_out,user,total_people)  
        except:

            return JsonResponse({'message' : 'There is no available room'}, safe=False)


        return redirect(reverse('info'))
    return render(request,'booking.html',context={})
    
def info(request):
    return render(request,'info.html',context={})
    