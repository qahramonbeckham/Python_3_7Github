from django.contrib import admin
from myfolder.models import *
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Type, AdminType)

class AdminType2(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Type2,AdminType2)

class AdminJob(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Job,AdminJob)


class AdminContact(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

admin.site.register(Contact,AdminContact)



class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','type','client','date','url','text']


admin.site.register(Portfolio,AdminPortfolio)


class AdminServices(admin.ModelAdmin):
    list_display = ['id','name','type2','text']


admin.site.register(Services,AdminServices)



class AdminTeam(admin.ModelAdmin):
    list_display = ['id','name','job','text']


admin.site.register(Team,AdminTeam)


class AdminSubcribe(admin.ModelAdmin):
    list_display = ['id','gmail']


admin.site.register(Subcribe,AdminSubcribe)