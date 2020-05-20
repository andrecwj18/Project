from django.shortcuts import render ,redirect
import codecs
import datetime 
import random
from bson import ObjectId
 

import pymongo
import gridfs
from pymongo import MongoClient
import os
from django.http import HttpResponse, HttpResponseForbidden
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from SafetyManagerApp.forms  import ImageUploadForm
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from SafetyManagerApp.models import logs ,logequipment ,equipment,details
from .serializers import LogsSerializer ,LogsCreateSerializer

articles = logs.objects.all()

client = pymongo.MongoClient('mongodb+srv://admin:admin@safetymanagerapp-tu3mk.mongodb.net/test')
db = client["SafetyManagerApp"]
fs = gridfs.GridFS(db, collection='SafetyManagerApp_logs')

class LogsView(APIView):
    def get(self, request):

        items = [] 
        alllogs = logs.objects.all()

        try :
        
            for log in alllogs:
                viewlog = details()
                ppeequipment = []

                viewlog.id = log.id
                viewlog.timestamp = log.timestamp
                viewlog.isviolated = log.isviolated
                equipmentviolated =   logequipment.objects.filter(logId= log.id)
           
                for equipementsvio in equipmentviolated :
                    actors = equipment.objects.get(id = equipementsvio.equipmentId_id) 
                    ppeequipment.append(actors.equipmentName) 
             
                outputdata =fs.get(ObjectId(log.image)).read() 
                base64_data = codecs.encode(outputdata, 'base64')
                image = base64_data.decode('utf-8')
         
                viewlog.image=image 
                viewlog.equipment = ','.join(map(str, ppeequipment)) 

                items.append(viewlog) 

        except: 
            context = {'message': 'error occured ' }
            return Response({context})

        serializer = LogsSerializer(items, many=True)
        return Response({"logs": serializer.data})

    
    def post(self, request):        

         form = ImageUploadForm(request.POST, request.FILES) 
         if form.is_valid():

             image =form.cleaned_data['image']  
             equipmentviolationid = form.cleaned_data['ppeequipment']   
             isviolatedfield = form.cleaned_data['isviolated']   

             try :
                 stored = fs.put(image,timestamp =datetime.datetime.now() ) 
                 storedlogId = str(stored) 
              
                 log = logs ()
                 log.image= storedlogId
                 log.timestamp= datetime.datetime.now()
                 log.isviolated = isviolatedfield 
                 log.save()
                 logID =log.id

                 for i in equipmentviolationid :
                     equipemtlog = equipment.objects.get(pk=i)
                     LogEquipmentcreate = logequipment ()
                     LogEquipmentcreate.logId= log
                     LogEquipmentcreate.equipmentId= equipemtlog
                     LogEquipmentcreate.save()

                 return Response({"success": "log has been added" })

             except :
                 return Response({"Error": "error occured" })
             
         else : 
             return Response({"Error": "form invalid. Add an image , ppeequipment or isviolated"})

     

class LogDetailView(APIView):
    def get(self, request,pk):
 
        try :
                log = get_object_or_404(logs.objects.all(), id =pk)

                items = [] 

                viewlog = details()
                ppeequipment = []

                viewlog.id = log.id
                viewlog.timestamp = log.timestamp
                viewlog.isviolated = log.isviolated
                equipmentviolated =   logequipment.objects.filter(logId= log.id)
           
                for equipementsvio in equipmentviolated :
                    actors = equipment.objects.get(id = equipementsvio.equipmentId_id) 
                    ppeequipment.append(actors.equipmentName) 
             
                outputdata =fs.get(ObjectId(log.image)).read() 
                base64_data = codecs.encode(outputdata, 'base64')
                image = base64_data.decode('utf-8')
         
                viewlog.image=image 
                viewlog.equipment = ','.join(map(str, ppeequipment)) 

                items.append(viewlog) 
                

                serializer = LogsSerializer(items, many=True)
                context = {"logs": serializer.data }

        except: 
            context = {'message': 'record not found' }

        return Response(context)

    def delete (self, request,pk):
        try :
            deletelog = get_object_or_404(logs.objects.all(), pk=pk)
            logimage = deletelog.image 
            fs.delete(ObjectId(logimage)) 
            deletelog.delete() 
            context = {'delete': 'success' }
        except :
            context = {'delete': 'record not found' }

        return Response(context)




