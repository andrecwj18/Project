
from django.forms import ModelForm
from django import forms 
from SafetyManagerApp.models import equipment
from django.forms import ModelForm

class ImageUploadForm(forms.Form):
        ppeequipmentlist = equipment.objects.all().values_list("id", "id")
        image = forms.ImageField()
        isviolated =forms.NullBooleanField()
        ppeequipment = forms.MultipleChoiceField(choices = ppeequipmentlist )


class EquipmentForm(forms.Form): 
        equipmentName = forms.CharField()  
