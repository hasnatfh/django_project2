from django.db import models
from django.utils import timezone

# Create your models here.

class FbCrudModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    fbv_img = models.ImageField(blank=True, upload_to='fbv-img/', null=True) 

    class Meta:
     verbose_name_plural = 'FBV CURD'

    def __str__(self):
        return self.title

    def excerpt(self):
        return self.description[0:100]