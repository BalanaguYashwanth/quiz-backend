from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'home.html')

def add(request):
    if request.method=='POST':
        number1=request.POST['number1']
        number2=request.POST['number2']
        num=int(number1)+int(number2)
        addition.objects.create(number1=number1,number2=number2,result=num)
        return render(request,'result.html',{'num':num})

