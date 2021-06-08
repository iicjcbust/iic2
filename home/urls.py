from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('Validate_admin/',views.Validate_admin,name="Validate_admin"),
    path('iicStudent',views.iicStudent,name="iicStudent"),
    path('iicFaculty',views.iicFaculty,name="iicFaculty"),
    path('ExternalExperts',views.ExternalExperts,name="ExternalExperts"),
    path('incubationCell',views.incubationCell,name="incubationCell"),
    path('innovationCell',views.innovationCell,name="innovationCell"),
    path('upcomingEvents',views.upcomingEvents,name="upcomingEvents"),
    path('previousEvents',views.previousEvents,name="previousEvents"),
    path('eventDesc/<str:slug>',views.eventDesc,name="eventDes"),
    path('innovation_ambassador',views.innovationAmbassador,name="innovationAmbassador"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('joinIIC',views.joinIIC,name="joinIIC"),
    path('download',views.download,name="download"),
    path('iprCell',views.iprCell,name="iprCell"),
    path('startupCell',views.startupCell,name="startupCell"),
    path('developer',views.Developer,name="Developer"),
    path('achievements',views.achievements,name="achievements"),
    
]