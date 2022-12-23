from django.db import models

# Create your models here.

class FbCrudModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
     verbose_name_plural = 'FBV CURD'

    def __str__(self):
        return self.title
