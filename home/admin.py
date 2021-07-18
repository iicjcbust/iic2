from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class EventAdmin(ImportExportModelAdmin):
    list_display = ('title','cell','venue','speakerName','image_tag')
    list_filter = ('cell','venue')
    search_fields = ('title','cell','venue','speakerName')
    list_per_page = 15

class announcementAdmin(ImportExportModelAdmin):
    list_display = ('title','isLatest','EventLink')
    list_filter = ('isLatest',)
    search_fields = ('title','createdDate','isLatest','EventLink')
    list_editable = ('isLatest',)
    list_per_page = 15

class HomeSliderAdmin(ImportExportModelAdmin):
    list_display = ('name','isUploadable','image_tag')
    list_filter = ('isUploadable',)
    search_fields = ('name','isUploadable')
    list_editable = ('isUploadable',)
    list_per_page = 15

class cordinatorAdmin(ImportExportModelAdmin):
    list_display = ('name','designation','role','image_tag')
    list_filter = ('designation','role')
    search_fields = ('name','designation','role')
    list_per_page = 15

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('name','email','subject')
    search_fields = ('name','email','subject')
    list_per_page = 15

class JoinIICAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','email','phone','course','college','year')
    list_filter = ('course','college','year')
    search_fields = ('first_name','last_name','email','phone','course','college','year')
    list_per_page = 15

class AchivementsAdmin(ImportExportModelAdmin):
    list_display = ('title','EventLink','undertitle','image_tag')
    search_fields = ('title','EventLink','undertitle','body')
    list_per_page = 15

class ExpertsAdmin(ImportExportModelAdmin):
    list_display = ('name','designation','email','phone','role','image_tag')
    list_filter = ('role','designation')
    search_fields = ('name','designation','email','phone','role')
    list_per_page = 15


class DeveloperAdmin(ImportExportModelAdmin):
    list_display = ('name','profession','image_tag')
    list_filter = ('profession',)
    search_fields =('name','profession')
    list_per_page = 15

class DownloadtableAdmin(ImportExportModelAdmin):
    list_display = ('name','link')
    search_fields =('name','link')
    list_per_page = 15


admin.site.register(Event,EventAdmin)
admin.site.register(announcement,announcementAdmin)
admin.site.register(HomeSlider,HomeSliderAdmin)
admin.site.register(cordinator,cordinatorAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(JoinIIC,JoinIICAdmin)
admin.site.register(Achivements,AchivementsAdmin)
admin.site.register(Experts,ExpertsAdmin)
admin.site.register(Developer,DeveloperAdmin)

