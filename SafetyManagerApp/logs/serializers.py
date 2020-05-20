from rest_framework import serializers

from SafetyManagerApp.models import logs


class LogsSerializer(serializers.Serializer):

    image = serializers.CharField() 
    timestamp = serializers.CharField()
    LOCATOR_YES_NO_CHOICES = ((None,''), (True,'Yes'), (False, 'No'))
    isviolated  = serializers.NullBooleanField()
    id = serializers.IntegerField()
    equipment =  serializers.CharField() 

    def create(self, validated_data):
        return logs.objects.create(**validated_data)

class LogsCreateSerializer(serializers.Serializer):

    image = serializers.FileField( default='')
    timestamp = serializers.CharField()
    LOCATOR_YES_NO_CHOICES = ((None,''), (True,'Yes'), (False, 'No'))
    isviolated  = serializers.NullBooleanField()
    equipment =   serializers.ListField(   child=serializers.CharField( ))

    def create(self, validated_data):
        return logs.objects.create(**validated_data)
     

 