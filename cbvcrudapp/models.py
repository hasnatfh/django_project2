from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class CbvCrudModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    cbvdate = models.DateField(auto_now_add=False,) 
    cbv_img = models.ImageField()

    def __str__(self):
        return self.title 
    
    class  Meta:
        verbose_name = 'CBV CRUD'
        verbose_name_plural = 'CBV CRUD Models'

    def get_absolute_url(self):
        return reverse('cbvdetails', kwargs={'pk': self.id,'slug': self.slug})

    #Slug will change in update view (if post updated, slug will also update)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    #Slug will not change in update view (if post updated. it(slug) will the same)
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)    

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(CbvCrudModel, self).save(*args, **kwargs)   

### This will work if not use slug
# def get_absolute_url(self):
#         return reverse("article_detail", args=[str(self.id)])
#or,      return reverse('article-detail', kwargs={'pk': self.pk})
#or,      return reverse('article-detail', kwargs={'id': self.id})

 ### This will work if use slug
 # def get_absolute_url(self):
#or,      return reverse('article-detail', kwargs={'slug': self.slug})

















