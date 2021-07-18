from django.contrib import admin
from django.urls import path
from home import views
#django admin header custamization
admin.site.site_header = "IIC JCBUST"
admin.site.site_title = "IIC Dashboard"
admin.site.index_title = "Welcome to IIC Admin Portal"

urlpatterns = [
    path('',views.home,name="home"),
    path('Validate_admin/',views.Validate_admin,name="Validate_admin"),
    path('joinIIC',views.joinIIC,name="joinIIC"),
    path('cell/<str:cell>',views.Cell,name="Cell"),
    path('Events/<str:name>',views.Events,name="Events"),
    path('eventDesc/<str:slug>',views.eventDesc,name="eventDes"),
    path('contact',views.contact,name="contact"),
    path('ExternalExperts',views.ExternalExperts,name="ExternalExperts"),
    path('iicFaculty',views.iicFaculty,name="iicFaculty"),

    path('achievements',views.achievements,name="achievements"),
    path('download',views.download,name="download"),
    
    path('iicStudent',views.iicStudent,name="iicStudent"),
    path('innovation_ambassador',views.innovationAmbassador,name="innovationAmbassador"),
    path('developer',views.Developers,name="Developers"),
    
    path('about',views.about,name="about"),
]