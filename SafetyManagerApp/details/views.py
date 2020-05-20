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
from rest_framework.decorators import action, api_view 
 
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
import pytz

from collections import Counter





 

@api_view()
def total_violation(request):

    today =  datetime.now().date()
    fromday = datetime.now().date() - timedelta(days=5)   

    login = []  
    alllogs = logs.objects.all()

   
    for log in alllogs :

        timestampdate = log.timestamp
        logdate = datetime( timestampdate.year,timestampdate.month,timestampdate.day ).date()

        if fromday <= logdate <=today  :
            login.append(logdate)
             

    violationonday = dict(Counter(login))
    print (violationonday)
    base = datetime.today()
    date_list = [base.date() - timedelta(days=x) for x in range(5)]
    print (date_list) 
    violationonday_key_list = list(violationonday.keys()) 
    
    violationvalues = []
 
    for date in date_list :
        if date in violationonday_key_list :
            value = violationonday.get(date)
        else : 
            value = 0
        violationvalues.append(value)

# violationvalues : start with the today till 5 days after 
# so the first value is today's violation then yesterday and so on .... 

    return Response({"series 1 ": violationvalues })


#@api_view()
#def total_violation(request):
#    today =  datetime.now() 
#    fromday = datetime.now() - timedelta(days=5)  
#    utc=pytz.UTC

#    todayutcformat = utc.localize(today) 
#    fromdayutcformat = utc.localize(fromday) 
#    alllogs = logs.objects.all()
#    date_list = [today - timedelta(days=x) for x in range(5)]
# #   for log in alllogs :
# #       timestampdate = log.timestamp
#    for log in alllogs :
#        searcgdayutcformat = utc.localize(date)
#        f = logs.objects.filter(timestamp=searcgdayutcformat)
#        g =  logs.objects.filter(timestamp='2020-05-21')

        
#        if fromdayutcformat <= timestampdate <= todayutcformat :
      
#    return Response({"message": "Hello, world!"})