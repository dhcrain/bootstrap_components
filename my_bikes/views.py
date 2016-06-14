from django.shortcuts import render
from my_bikes.models import MyBike
# Create your views here.


def index_view(request):
    context = {
        "bike": MyBike.objects.all()
    }
    return render(request, 'index.html', context)


def my_bikes_view(request):
    context = {
        "bikes": MyBike.objects.all().order_by('-year')
    }
    return render(request, 'bikes.html', context)


def about_view(request):
    context = {
        "bikes": MyBike.objects.get(id=1),
    }
    return render(request, 'about_me.html', context)


def single_bike_view(request, bike_id):
    context = {
        "bikes": MyBike.objects.get(id=bike_id)
    }
    return render(request, 'single_bike.html', context)
