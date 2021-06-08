from django.contrib import admin

from .models import Events,announcement,organizer,Contact,JoinIIC,Annou
# Register your models here.
admin.site.register(Events)
admin.site.register(announcement)
admin.site.register(organizer)
admin.site.register(Contact)
admin.site.register(JoinIIC)
admin.site.register(Annou)
