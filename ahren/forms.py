from django import forms 
from django.forms import ModelForm
from ahren.models import Sheet

class AddSheetForm(ModelForm):
    class Meta: 
        model = Sheet 
        fields = ['name', 'author', 'url']
        
class DeleteSheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields =['name']
        