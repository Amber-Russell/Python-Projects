from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    users = ["Adam","Jerry", "Tommy", "Sarah","Tina"]
    context = {
        'users':users,
    }
    return render(request, "home.html", context)