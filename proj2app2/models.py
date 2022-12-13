from django.db import models

# Create your models here.
class CbvArticle(models.Model):
    img = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        verbose_name_plural = 'CbvArticles'
    
    def __str__(self):
      return self.title

    def excerptf(self):
        return self.description[0:250] 


class Person(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return self.fname +' '+ self.lname

    class Meta:
        verbose_name_plural = 'Persons'