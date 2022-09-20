
from django.shortcuts import render
from django.http import JsonResponse
from visitors.models import *
# Create your views here.
def getbookings(request):
    booking_array=[]
    bookings=Booking.objects.all()
  
    for i in bookings:
      i={'id':i.id,'title':f"{i.user.username} {i.room.category.name}",'start':i.check_in_date,'end':i.check_out_date}
      booking_array.append(i)
    return JsonResponse(booking_array,safe=False)

def showcalender(request):
    return render(request,'base2.html',context={})

def booking(request):
    return render(request,'',context={})