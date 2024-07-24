from django.shortcuts import render
from .models import Applicants

aplno = 0
img_path = "applicant/static/upload/"

def applyform(request):
    return render(request, "getform.html")

def edit(request,idp):
    return render(request, "edit.html",{'applicant':Applicants.objects.get(id=idp)})


def applypost(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        global aplno
        uimage = str(aplno)+".jpg"
        obj= Applicants.objects.create(name=name, email=email, mobile=mobile, uimage=uimage)
        obj.save()
        handle_uploaded_file(request.FILES["uimage"])
        aplno = aplno + 1
        return render(request, "getform.html")
    
#def editpost(request):
    #if request.method == "POST":



def handle_uploaded_file(f):
    with open(img_path+str(aplno)+".jpg","wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
def display(request):
    applicants = Applicants.objects.all()
    return render(request, "display.html", {"applicants": applicants})
# Create your views here.

    