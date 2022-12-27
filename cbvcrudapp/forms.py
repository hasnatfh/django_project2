from django import forms
from .models import CbvCrudModel

class CbvCrudForm(forms.ModelForm):
    class Meta:
        model = CbvCrudModel
        fields = ['title', 'content', 'cbvdate', 'cbv_img']
        labels = {
            'cbvdate': 'Date',
            'cbv_img': 'Upload image',
        }