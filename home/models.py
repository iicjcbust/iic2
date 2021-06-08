from django.db import models
from django.utils import timezone
# Create your models here.


class organizer(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.BigIntegerField()
    email = models.CharField(max_length=200,blank=True,null=True)
    department = models.CharField(max_length=50,blank=True,null=True)
    image = models.ImageField(upload_to="organizers/",blank=True,null=True)

    def __str__(self):
        return self.name

class Events(models.Model):
    image = models.ImageField(upload_to="images")
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    dateEvent = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    cell = models.CharField(max_length=50,choices=(
        ("Institution’s Innovation Council (IICs)","Institution’s Innovation Council (IICs)"),
        ("Incubation Cell","Incubation Cell"),
        ("Innovation Cell","Innovation Cell"),
        ("Startup Cell","Startup Cell"),
        ("IPR Cell","IPR Cell"),
    ))
    speakerName = models.CharField(max_length=100)
    googleFormLink = models.URLField(max_length=200,blank=True, null=True)
    venue = models.CharField(max_length=100)
    createdDate = models.DateTimeField(default=timezone.now)
    
    Eventorganizers = models.ManyToManyField(organizer)
    
    def __str__(self):
        return self.title
    

class announcement(models.Model):
    fileUpload = models.FileField(upload_to ='uploads/',blank=True, null=True) 
    title = models.CharField(max_length=200)
    EventLink = models.URLField(max_length=200,blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    createdDate = models.DateTimeField(default=timezone.now)
    isLatest = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject + " from " + self.name

class JoinIIC(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    college = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.course + ") "

class Annou(models.Model):
     image = models.ImageField(upload_to="images",blank=True, null=True)
     title = models.CharField(max_length=200)
     EventLink = models.URLField(max_length=200,blank=True, null=True)
     undertitle = models.CharField(max_length=200)
     body = models.TextField(blank=True, null=True)
     def __str__(self):
        return self.title
    
    