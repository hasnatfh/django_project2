from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class CKEditorModel(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextUploadingField()
    date = models.DateField(auto_now_add=False, null=True)
    ck_img = models.ImageField()
    

    def __str__(self):
        return self.title 