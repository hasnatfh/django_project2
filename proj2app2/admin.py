from django.contrib import admin
from .models import CbvArticle, Person


# Register your models here.
admin.site.register(CbvArticle) 
admin.site.register(Person)