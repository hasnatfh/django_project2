from django.contrib import admin
from .models import CbvArticle, Person, CbvContactinfo


# Register your models here.
admin.site.register(CbvArticle) 
admin.site.register(Person)
admin.site.register(CbvContactinfo) 