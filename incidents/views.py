from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Incident
from login.models import User
from .serializers import IncidentsListSerializer, IncidentsCreateSerializer

# Create your views here.
class IncidentList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        if request.user:
            stu=Incident.objects.filter(user=request.user.id)
            serializer = IncidentsListSerializer(stu,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu = Incident.objects.all()
        serializer = IncidentsListSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        print("----------------",request.user.email)
        print("--------types--------",type(request.user))
        a=User.objects.get(id=request.user.id)
        print("-----a---",a)
        serializer = IncidentsListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save(user=a)
            return Response({"success":"created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    