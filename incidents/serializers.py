from rest_framework import serializers
from .models import Incident
from login.models import User


class IncidentsListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Incident
        fields = ['id', 'name', 'body', 'created', 'status','priority']
