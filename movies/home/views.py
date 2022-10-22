from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import moviesinfo
from django.contrib import messages

def home(request):
    info=moviesinfo.objects.all()
    context={
        'info':info
    }
    return render(request,'home.html',context)

def download(request,id=0):
    print(id)
    rec=moviesinfo.objects.filter(id=id).first()
    mrec={'rec':rec}
    return render(request,'download.html',mrec)