from rest_framework import serializers

from SafetyManagerApp.models import equipment


class EquipmentSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    equipmentName =  serializers.CharField()  

class EquipmentCreateSerializer(serializers.Serializer):
    
    equipmentName =  serializers.CharField()  
     

 