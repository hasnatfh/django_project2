from django import forms
from .models import CKEditorModel

class CKEditorForm(forms.ModelForm):
    class Meta:
        model = CKEditorModel
        fields = ['title', 'content', 'date', 'ck_img', ]
        labels = {'ck_img': 'Upload image'}
