
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def getbookings(request):
    bookings=[
    {
      'id': 'a',
      'title': 'my event',
      'start': '2022-09-16'
    }
    ,{
      'id': 'b',
      'title': 'second',
      'start': '2022-09-20'
    }
  ]
    return JsonResponse(bookings,safe=False)

def showcalender(request):
    return render(request,'base2.html',context={})

def booking(request):
    return render(request,'',context={})