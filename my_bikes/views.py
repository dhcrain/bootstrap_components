from django.shortcuts import render

# Create your views here.


def index_view(request):
    context = {

    }
    return render(request, 'index.html', context)


def my_bikes_view(request):
    context = {

    }
    return render(request, 'bikes.html', context)


def about_view(request):
    context = {

    }
    return render(request, 'about_me.html', context)
