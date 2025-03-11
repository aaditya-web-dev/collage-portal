from django.shortcuts import render,redirect
from .models import student
from .models import teacher
# Create your views here.
def bciit(request):
    return render(request,'testapp/home.html')
def professor(request):
    dict1={"xyz":"xyz"}
    return render(request,"testapp/professor.html",dict1)
def stu(request):
    students=student.objects.all
    return render(request,'testapp/student.html',{'students':students})

def form(request):
    return render(request,"testapp/form.html")

def save(request):
    if request.method=="POST":
        prod=student()
        prod.eno=request.POST.get("eno")
        prod.name=request.POST.get("name")
        prod.specialization=request.POST.get("specialization")
        if len(request.FILES)!=0:
            prod.image=request.FILES['file']
        prod.save()
        return redirect('stu')
    return render(request,"testapp/form.html")

def event(request):
    return render(request,"testapp/events.html")

def teachers(request,id):
    if (id==1):
        data=teacher.objects.filter(id1=1)
    elif (id==2):
        data=teacher.objects.filter(id1=2)
    elif (id==3):
        data=teacher.objects.filter(id1=3)
    elif (id==4):
        data=teacher.objects.filter(id1=4)
    elif (id==5):
        data=teacher.objects.filter(id1=5)
    elif (id==6):
        data=teacher.objects.filter(id1=6)
    elif (id==7):
        data=teacher.objects.filter(id1=7)
    elif (id==8):
        data=teacher.objects.filter(id1=8)
    elif (id==9):
        data=teacher.objects.filter(id1=9)
    elif (id==10):
        data=teacher.objects.filter(id1=10)
    elif (id==11):
        data=teacher.objects.filter(id1=11)
    elif (id==12):
        data=teacher.objects.filter(id1=12)
        
    return render(request,'testapp/teacher.html',{'data':data})
    
        
        




    