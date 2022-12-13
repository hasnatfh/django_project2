from django.db import models

# Create your models here.

class Article(models.Model):
    img = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        verbose_name_plural = 'Articles'
    
    def __str__(self):
      return self.title

    def excerptf(self):
        return self.description[0:250] 




class ContactInfo(models.Model):
  cname = models.CharField(max_length=200)
  cemail = models.EmailField(max_length=200)
  cmessage = models.TextField()
  
  def __str__(self):
    return self.cname

  class Meta:
        verbose_name_plural = 'AllContactInfo'




























    