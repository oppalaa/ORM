from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def insert_Topic(request):
    topics=Topic.objects.all()
    topics=Topic.objects.filter(top_name='cricket')
    
    d={'topics':topics}
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    #webpage=WebPage.objects.get(top_name='Kabaddi')
    webpage=WebPage.objects.all()
    webpage=WebPage.objects.filter(top_name='Kabaddi')
    webpage=WebPage.objects.all()
    webpage=WebPage.objects.exclude(top_name='Kabaddi')
    webpage=WebPage.objects.all()[::1]
    webpage=WebPage.objects.all()[1:2:]
    webpage=WebPage.objects.all().order_by('name')
    webpage=WebPage.objects.all().order_by('-name')
    webpage=WebPage.objects.all().order_by(Length('name'))
    webpage=WebPage.objects.all().order_by(Length('name').desc())
    webpage=WebPage.objects.all()
    
    d={'webpage':webpage}
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    ACO=AcessRecord.objects.all()
    d={'ACO':ACO}
    return render(request,'insert_access.html',d)


def update_webpage(request):
    #webpage=WebPage.objects.filter(name='Naveen').update(url='http//www.Naveen.in')
    #webpage=WebPage.objects.all()
    #WebPage.objects.filter(name='Naveen').update(url='http//www.Naveen.in')
    WebPage.objects.filter(name='Thirumalesh').update(url='http//www.KTM.in')
    WebPage.objects.filter(name='Thirumalesh').update(top_name='cricket')
    topics=Topic.objects.get(top_name='cricket')

    WebPage.objects.update_or_create(name='deva',defaults={'top_name':topics})
    webpage=WebPage.objects.all()
    d={'webpage':webpage}
    return render(request,'insert_webpage.html',d)
