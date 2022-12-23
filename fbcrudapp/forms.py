from django import forms
from .models import FbCrudModel

class FbCrudForm(forms.ModelForm):
    class Meta:
        model = FbCrudModel 
        fields =  ['title', 'description']


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































































































