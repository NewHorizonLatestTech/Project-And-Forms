from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
    return render(request,'app/home.html')
