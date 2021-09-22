from django.shortcuts import render
from django.http import HttpResponse
from .models import TList, Item
from .forms import CreateForm
# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

# def user(response, sname):
#     return render(response, "main/user.html", {"name": sname, "length": str(len(sname))})

def index(response, id):
    lst = TList.objects.get(id=id)
    return render(response, "main/index.html", {"list": lst})

def create(response):
    form = CreateForm()
    return render(response, 'main/create.html', {"form": form})

