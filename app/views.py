from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFOD=TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('TMFOD is inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFOD=WebpageModelForm(request.POST)
        WMFOD.save()
        return HttpResponse('WMFOD is inserted')

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AMFO=AccessRecordModelForm()
    d={'AMFO':AMFO}
    if request.method=='POST':
        AMFOD=AccessRecordModelForm(request.POST)
        AMFOD.save()
        return HttpResponse('AMFOD is inserted')

    return render(request,'insert_accessrecord.html',d)

