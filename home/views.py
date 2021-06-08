from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import Contact,announcement,Events,JoinIIC,Annou
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime 
from datetime import date

# Create your views here.
def home(request):
    ann = announcement.objects.all().order_by('-createdDate')
    context = {"announcement":ann}
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

def iicStudent(request):
    return render(request,'home/iic-student.html')
def iicFaculty(request):
    return render(request,'home/iic-faculty.html')
def ExternalExperts(request):
    return render(request,'home/external-experts.html')
def incubationCell(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__lt=x,cell="Incubation Cell").order_by('dateEvent')
    context={"events":events}
    return render(request,'home/incubation.html',context)
def iprCell(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__lt=x,cell="IPR Cell").order_by('dateEvent')
    context={"events":events}
    
    return render(request,'home/ipr.html',context)
def download(request):
    return render(request,'home/download.html')

def startupCell(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__lt=x,cell="Startup Cell").order_by('dateEvent')
    context={"events":events}

    return render(request,'home/startup.html',context)

def innovationCell(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__lt=x,cell="Innovation Cell").order_by('dateEvent')
    context={"events":events}
    return render(request,'home/innovation.html',context)
def about(request):
    return render(request,'home/about.html')
def achievements(request):
    annou = Annou.objects.filter()
    context = {"annou":annou}
    return render(request,'home/achievements.html', context)

def upcomingEvents(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__gte=x).order_by('dateEvent')
    context={"events":events}
    return render(request,'home/upcoming-events.html',context)
def previousEvents(request):
    x = datetime.datetime.now()
    events=Events.objects.filter(dateEvent__lt=x).order_by('dateEvent')
    context={"events":events}
    return render(request,'home/previous-events.html',context)

def innovationAmbassador(request):
    return render(request,'home/innovation_ambassador.html')

def Developer(request):
    return render(request,'home/developer.html')

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

def eventDesc(request,slug):
    event = Events.objects.filter(title=slug).first()
    upcoming = False
    if (event.dateEvent >= date.today()):
        upcoming = True
    organize = event.Eventorganizers.all()
    return render(request,'home/eventDescription.html',{"event":event,"organize":organize,"upcoming":upcoming})

