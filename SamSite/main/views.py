from django.shortcuts import render
from django.http import HttpResponse
from .models import TList, Item
# Create your views here.

def home(response):
    return HttpResponse(f"<h1>This is Homepage</h1>")

def user(response, sname):
    return HttpResponse(f"Hi {sname}, wassup?")

def index(response, id):
    lst = TList.objects.get(id=id)
    return HttpResponse(f"{lst.name}")

