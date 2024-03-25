from django.shortcuts import render
from myfolder.models import *
# Create your views here.

def index(malumot):

    if "subscribe_id" in malumot.POST:
        name=malumot.POST.get('name')
        email = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        message = malumot.POST.get('message')
        idd = malumot.POST.get('subcribe_id')
        Contact( id=idd, name=name,email=email,subject=subject,message=message).save()
    elif malumot.method=="POST":
        gmail=malumot.POST.get("email")
        Subcribe(gmail=gmail).save()
    we_works=Portfolio.objects.all()
    we_team=Team.objects.all()
    we_services=Services.objects.all()
    subcribe = Subcribe.objects.all()
    return render(malumot,'index.html',{"portfolios":we_works,'teams':we_team,'services':we_services,"obuna":subcribe})

def portfolio_details(malumot):
    return render(malumot,'portfolio-details.html')


#def Team(malumot):
   # we_team=Team.objects.all()
   # return render(malumot,'index.html',{"teams":we_team})

#def Services(malumot):
   # we_services=Services.objects.all()
    #return render(malumot,'index.html')

