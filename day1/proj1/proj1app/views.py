from django.shortcuts import render
from .models import Employee
from .models import Products


def home(request):
    return render(request, "homepage.html")

def contact(request):
    return render(request, "contactpage.html")

# Create your views here.

def registration(request):
    return render(request, "registration.html")

def funprocess(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        obj = Employee.objects.create(name=name,email=email,mobile=mobile)
        obj.save()
        #obj.objects.
        return render(request,'success.html')
    

def itemregistration(request):
    return render(request, "productregister.html")

def itemprocess(request):
    if request.method == "POST":
        pname = request.POST['pname']
        desc = request.POST['desc']
        price = request.POST['price']
        quantity = request.POST['quantity']
        obj = Products.objects.create(pname=pname,desc=desc,price=price,quantity=quantity)
        obj.save()
        return render(request, 'success.html')

def displayData(request):
    objs = Employee.objects.all()
    return render(request,"showEmployee.html",{'emps':objs})