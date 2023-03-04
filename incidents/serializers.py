from rest_framework import serializers
from .models import Incident
from login.models import User


class IncidentsListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Incident
        fields = ['id','incident_id', 'name', 'body', 'created', 'status','priority']

class IncidentsCreateSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Incident
        fields = ['id','incident_id', 'name', 'body', 'created', 'status','priority','user']
        
        def create(self, validated_data):
            print("----hi---")
            return Incident.objects.create(**validated_data)
    
        # def create(self,validated_data):
        #     print("----val---",validated_data)
        #     print("-----user",self.context.get("user"))
        #     incident = Incident()
        #     # incident.user.email=self.context.get("user") 
        #     print("-----user",incident.user)
        #     incident.name = validated_data.get("name")
        #     incident.status = validated_data.get("status")
        #     incident.body = validated_data.get("body")
        #     incident.priority = validated_data.get("priority")
        #     incident.save(self.context.get("user") )
        #     return incident