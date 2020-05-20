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

from SafetyManagerApp.forms  import ImageUploadForm,EquipmentForm
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from SafetyManagerApp.models import logs ,logequipment ,equipment,details
from .serializers import EquipmentSerializer ,EquipmentCreateSerializer


class EquipmentsView(APIView):
    def get(self, request,pk = None):
        if pk:
            ppeequipment = get_object_or_404(equipment.objects.all(), pk=pk)
            serializer = EquipmentSerializer(ppeequipment)
            return Response({"equipment": serializer.data})
        ppeequipment = equipment.objects.all()
        serializer = EquipmentSerializer(ppeequipment, many=True)
        return Response({"equipment": serializer.data})
  
  
    #def delete(self, request,pk)  :
    #    try :
    #        ppeexists = equipment.objects.filter(id=pk)
    #        if ppeexists.exists():
    #            deletePPE = get_object_or_404(equipment.objects.all(), pk=pk) 
    #            deletePPE.delete() 
    #            content = {'delete': 'success' }
    #            return Response(content)
                 
    #        else :
    #            content = {"delete": "object has already been deleted" }
    #    except :
    #        content = {"Error": "error occured" }


    #    return Response(content)



    def post(self, request):        

         form = EquipmentForm(request.POST ) 
         if form.is_valid():
             try :
                 ppename =form.cleaned_data['equipmentName']   

                 duplicates = equipment.objects.filter(equipmentName=ppename)

                 if duplicates.exists(): 
                     content = {"Error": "This object already exists" }
                     return Response(content)
                 
                 else :
                     ppeequipment = equipment () 
                     ppeequipment.equipmentName = ppename
                     ppeequipment.save()
                     content = {"success": "object has been added" }

             except :
                  content = {"Error": "error occured" }
             
         else : 
              content = {"Error": "form invalid. Add an PPE Name "}

         return Response(content)