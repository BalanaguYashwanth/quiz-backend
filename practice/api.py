from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class add(APIView):

    def get(self,request):
        model=addition.objects.all()
        serializer=addSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=addSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self,request):
        model=addition.objects.all()
        model.delete()
        return Response("successfully deleted")

class addone(APIView):

    def get(self,request,id):
        model = addition.objects.get(id=id)
        serializer=addSerializer(model)
        return Response(serializer.data)

    def put(self,request,id):
        model=addition.objects.get(id=id)
        serializer=addSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        model=addition.objects.get(id=id)
        model.delete()
        return Response("successfully deleted")
