from django.shortcuts import render


def home(request):
    return render(request, "homepage.html")

def contact(request):
    return render(request, "contactpage.html")

# Create your views here.

def registration(request):
    return render(request, "registration.html")
