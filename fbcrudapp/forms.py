from django import forms
from .models import FbCrudModel

class FbCrudForm(forms.ModelForm):
    class Meta:
        model = FbCrudModel 
        fields =  ['title', 'description', 'datetime', 'fbv_img',] 
        labels = {
            'datetime': 'Date & Time',
            'fbv_img': 'Upload Image'
        }

#'''
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Title"
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Description"
    }))

#''' 































































































