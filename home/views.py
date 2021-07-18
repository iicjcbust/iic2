from typing import ContextManager
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from . models import *
from django.db.models import Count,Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime 
from datetime import date

# Create your views here.
def home(request):
    ann = announcement.objects.all().order_by('-createdDate')
    slider = HomeSlider.objects.filter(isUploadable=True).order_by('name')
    context = {"announcement":ann,"slider":slider}
    return render(request,'home/index.html',context)

def Validate_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/admin')
        else:
            return redirect('home')

def joinIIC(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        college = request.POST['college']
        course = request.POST['course']
        year = request.POST['year']
        if JoinIIC.objects.filter(email=email).exists() or JoinIIC.objects.filter(phone=phone).exists():
            message = "You are already a IIC member :)"
            tag = "danger"
        else:
            obj = JoinIIC(first_name=fname,last_name=lname,email=email,phone=phone,college=college,course=course,year=year)
            obj.save()
            message = "Thankyou for joining IIC, we will contact you soon"
            tag = "success"
        ann = announcement.objects.all().order_by('-createdDate')
        context = {"announcement":ann,"message":message,"tag":tag}
        return render(request,'home/index.html',context)

def Cell(request,cell):
    if cell == 'Incubation' or cell == 'Innovation' or cell == 'Startup' or cell == 'IPR':
        cord = cell+ " Co-ordinator"
        member = cell + " Member"
        cellName = cell+ " Cell"
        cellCord = cordinator.objects.filter(role=cord)
        cellMember = cordinator.objects.filter(role=member)
        content = CellInfo.objects.filter(cell=cellName).first().content
        x = datetime.datetime.now()
        events=Event.objects.filter(dateEvent__lt=x,cell=cellName).order_by('dateEvent')
        context = {'cellCord':cellCord,'cellMember':cellMember,'events':events,'name':cell,'content':content}
        return render(request,'home/Cell.html',context)
    else:
        return redirect('home')

def Events(request,name):
    if name == 'upcoming' or name == 'previous':
        x = datetime.datetime.now()
        if name == 'upcoming':
            events=Event.objects.filter(dateEvent__gte=x).order_by('dateEvent')
        elif name == 'previous':
            events=Event.objects.filter(dateEvent__lt=x).order_by('dateEvent')
        context={"events":events,"name":name}
        return render(request,'home/Events.html',context)
    else:
        return redirect('home')

def eventDesc(request,slug):
    event = Event.objects.filter(title=slug).first()
    if event is None:
        return redirect("home")
    upcoming = False
    if (event.dateEvent >= date.today()):
        upcoming = True
    context = {"event":event,"upcoming":upcoming}
    return render(request,'home/eventDescription.html',context)

def contact(request):
    context = {}
    if request.method == 'POST':
        person_name = request.POST['person_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj1 = Contact(name=person_name,email=email,subject=subject,message=message)
        obj1.save()
        context = {"message":True}
    return render(request,'home/contact.html',context)

def iicFaculty(request):
    iicFaculty = cordinator.objects.filter(role="IIC Faculty")
    context = {"iicFaculty":iicFaculty}
    return render(request,'home/iic-faculty.html', context)

def ExternalExperts(request):
    experts = Experts.objects.all()
    context = {"experts":experts}
    return render(request,'home/external-experts.html', context)

def iicStudent(request):
    cordinators = []
    cord = cordinator.objects.filter(role__contains="Students").values('role').annotate(dcount=Count('role'))
    for c in cord:
        r = c["role"]
        cd = cordinator.objects.filter(role=r)
        if len(cd)>=1:
            cordinators.append(cd)
    secratary = cordinator.objects.filter(role="Secratary")
    context = {"cordinators":cordinators,"secratary":secratary }
    return render(request,'home/iic-student.html', context)

def download(request):
    down = Downloadtable.objects.all().filter()
    context = {"down":down}
    return render(request,'home/download.html', context)

def achievements(request):
    annou = Achivements.objects.filter()
    context = {"annou":annou}
    return render(request,'home/achievements.html', context)


def innovationAmbassador(request):
    return render(request,'home/innovation_ambassador.html')

def Developers(request):
    developers = Developer.objects.all().order_by('id')
    context = {'developers':developers}
    return render(request,'home/developer.html',context)

def about(request):
    return render(request,'home/about.html')
