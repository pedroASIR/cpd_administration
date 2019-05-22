from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def sensor_list_view(request):
    return HttpResponse("Saludos")


def sensor_detail_view(request):
    return HttpResponse("Saludos")