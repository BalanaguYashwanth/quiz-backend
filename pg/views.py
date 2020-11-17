from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
# Create your views here.

class pgownerView(viewsets.ModelViewSet):
    queryset = pgowner.objects.all() 
    serializer_class = pgownerSerializers

