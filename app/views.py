from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    ETDO=TopicForm()
    d={'ETDO':ETDO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic data is inserted successfully')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EMWO=WebpageForm()
    d={'EMWO':EMWO}

    if request.method=='POST':
        EMDO=WebpageForm(request.POST)
        if EMDO.is_valid():
            EMDO.save()
            return HttpResponse('webpage data is inserted sucessfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EMAO=AccessRecordForm()
    d={'EMAO':EMAO}

    if request.method=='POST':
        ACRD=AccessRecordForm(request.POST)
        if ACRD.is_valid():
            ACRD.save()
            return HttpResponse('insert_accessrecord data is inseted sucessfully')
    
    return render (request,'insert_accessrecord.html',d)