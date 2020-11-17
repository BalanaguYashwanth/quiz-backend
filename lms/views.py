from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
# Create your views here.


class verifyview(viewsets.ModelViewSet):
    queryset=verify.objects.all()
    serializer_class=verifySerializers


class quizview(viewsets.ModelViewSet):
    queryset=quiz.objects.all()
    serializer_class=quizSerializers


