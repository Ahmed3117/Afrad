from django.shortcuts import render
from .models import Holiday
# Create your views here.

def home(request):
    # home_data = Home.objects.last()
    # context = {
    #     "home_data" : home_data,
    # }
    return render(request,'maindata/home.html')



def createholidaypdf(request):
    holidays = Holiday.objects.all()
    context = {    
        "holidays" : holidays,
    }
    return render(request,'maindata/printholidays.html',context)

