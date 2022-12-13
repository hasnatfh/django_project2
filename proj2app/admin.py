from django.contrib import admin
from .models import Article, ContactInfo
from proj2app2.models import Person

# Register your models here.
admin.site.register(Article) 
admin.site.register(ContactInfo) 
admin.site.register(Person)
  
