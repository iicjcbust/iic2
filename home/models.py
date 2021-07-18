from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
# Create your models here.

class Event(models.Model):
    image = models.ImageField(upload_to="images/Events")
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
    
    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="70" height="60" />'% (self.image))
    image_tag.short_description = 'Event Image'
    


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



class Achivements(models.Model):
    image = models.ImageField(upload_to="images/Achievement",blank=True, null=True)
    title = models.CharField(max_length=200)
    EventLink = models.URLField(max_length=200,blank=True, null=True)
    undertitle = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    createdDate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="70" height="60" />'% (self.image))
    image_tag.short_description = 'Achievement Image'


class Experts(models.Model):
     image = models.ImageField(upload_to="images/Expert",blank=True, null=True)
     name = models.CharField(max_length=50)
     designation = models.CharField(max_length=100)
     email = models.EmailField(max_length=50)
     phone = models.CharField(max_length=10)
     role = models.CharField(max_length=150)
     def __str__(self):
        return self.name

     def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="70" height="60" />'% (self.image))
     image_tag.short_description = 'Experts Image'


class Downloadtable(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=300)
    def __str__(self):
        return self.name


class cordinator(models.Model):
    image = models.ImageField(upload_to="images/Cordinator",blank=True, null=True)
    name = models.CharField(max_length=50)  
    designation = models.CharField(max_length=200,blank=True, null=True)
    role = models.CharField(max_length=50,choices=(
        ("IPR Co-ordinator","IPR Co-ordinator"),
        ("IPR Member","IPR Member"),
        ("Innovation Co-ordinator","Innovation Co-ordinator"),
        ("Innovation Member","Innovation Member"),
        ("Startup Co-ordinator","Startup Co-ordinator"),
        ("Startup Member","Startup Member"),
        ("Incubation Co-ordinator","Incubation Co-ordinator"),
        ("Incubation Member","Incubation Member"),
        ("IIC Faculty","IIC Faculty"),
        ("IPR Students","IPR Students"),
        ("Innovation Students","Innovation Students"),
        ("Startup Students","Startup Students"),
        ("Incubation Students","Incubation Students"),
        ("Secratary","Secratary")
    ))
    createdDate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + " | " + self.role

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="70" height="60" />'% (self.image))
    image_tag.short_description = 'Cordinator Image'


class HomeSlider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/Slider",blank=True, null=True)
    createdDate = models.DateTimeField(auto_now=True)
    isUploadable = models.BooleanField(default=False)
    def __str__(self):
        return self.name + " " + str(self.isUploadable)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="70" height="60" />'% (self.image))
    image_tag.short_description = 'Slider Image'


class CellInfo(models.Model):
    content = models.TextField()
    cell = models.CharField(max_length=50,choices=(
        ("Incubation Cell","Incubation Cell"),
        ("Innovation Cell","Innovation Cell"),
        ("Startup Cell","Startup Cell"),
        ("IPR Cell","IPR Cell"),
    ))
    image = models.ImageField(upload_to="images/Cell",blank=True, null=True)

    def __str__(self):
        return self.cell

class Developer(models.Model):
    name = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    image = models.ImageField(upload_to="images/Developer",blank=True, null=True)
    facebook_ID = models.CharField(max_length=200)
    instagram_ID = models.CharField(max_length=200)
    linkdin_ID = models.CharField(max_length=200)
    github_ID = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="/media/%s" width="70" height="60" />'% (self.image))
    image_tag.short_description = 'Developer Image'