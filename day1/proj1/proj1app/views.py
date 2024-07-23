from django.shortcuts import render


def home(request):
    return render(request, "homepage.html")

def contact(request):
    return render(request, "contactpage.html")

# Create your views here.

def registration(request):
    return render(request, "registration.html")

def regprocess(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    mobile = request.POST.get("mobile")
    return render(request, "regprocess.html", {"name": name, "email": email, "mobile": mobile})
