from django.db.models import query
from django.shortcuts import render
from .serializers import StudentsSerializer
from .models import Students
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response

from src import serializers


def home(request):
    return render(request,"home.html")

def postdata(request):
    return render(request,"postdata.html")

#post api
class StudentPostView(APIView):
    def post(sefl,request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
             #RAJ.SANDIP96@GMAIL.COM
            return Response(request.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class StudentGetView(APIView):
    def get(self,request):
        query_set= Students.objects.all()
        serializer = StudentsSerializer(query_set,many=True)
        # print(serializer.data)
        
        # return render(request,"home.html")
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    
    

    
    
    
