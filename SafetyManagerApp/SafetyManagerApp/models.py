from djongo import models
from django import forms
from django.contrib import admin
  
class equipment(models.Model):
    equipmentName = models.CharField(max_length=100) 
    objects = models.DjongoManager()
 
 
class logs(models.Model):
    image = models.CharField(max_length=100) 
    timestamp = models.DateTimeField()
    LOCATOR_YES_NO_CHOICES = ((None,''), (True,'Yes'), (False, 'No'))

    isviolated  = models.NullBooleanField(choices=LOCATOR_YES_NO_CHOICES,max_length=3,blank=True, null=True, default=None,)
    objects = models.DjongoManager()
      
class logequipment(models.Model):

    logId = models.ForeignKey(logs, on_delete=models.CASCADE)
    equipmentId = models.ForeignKey(equipment, on_delete=models.DO_NOTHING)
    objects = models.DjongoManager()


class accesstoken(models.Model):
    tokenStr = models.CharField(max_length=100) 
    objects = models.DjongoManager()

class channels(models.Model):
    channelStr = models.CharField(max_length=100) 
    objects = models.DjongoManager()



class details:
    pass