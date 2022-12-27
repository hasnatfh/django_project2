from django.db import models
from django.urls import reverse

# Create your models here.

class CbvCrudModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    cbvdate = models.DateField(auto_now_add=True)
    cbv_img = models.ImageField()

    def __str__(self):
        return self.title 


    def get_absolute_url(self):
        return reverse('cbvdetail', kwargs={'pk': self.pk})

### This will work if not use slug
# def get_absolute_url(self):
#         return reverse("article_detail", args=[str(self.id)])
#or,      return reverse('article-detail', kwargs={'pk': self.pk})
#or,      return reverse('article-detail', kwargs={'id': self.id})

 ### This will work if use slug
 # def get_absolute_url(self):
#or,      return reverse('article-detail', kwargs={'slug': self.slug})