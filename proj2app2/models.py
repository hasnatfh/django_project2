from django.db import models

# Create your models here.
class CbvArticle(models.Model):
    img = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        verbose_name_plural = 'Cbv Articles'
    
    def __str__(self):
      return self.title

    def excerptf(self):
        return self.description[0:250] 


class Person(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        #return self.fname +' '+ self.lname
        return f"{self.fname} {self.lname}"

    class Meta:
        verbose_name_plural = 'Persons'


class CbvContactinfo(models.Model):  
    cbvname= models.CharField(max_length=200)
    cbvemail = models.EmailField()
    cbvmessage = models.TextField()

    def __str__(self):
        return f"Contact message from: {self.cbvname}"
    
    class Meta:
        verbose_name_plural = 'Cbv Contact'