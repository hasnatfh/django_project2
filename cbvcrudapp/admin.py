from django.contrib import admin
from .models import CbvCrudModel
 
# Register your models here.

#@admin.register(CbvCrudModel)
class CbvCrudModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'cbvdate',)
    prepopulated_fields = {"slug": ('title','cbvdate',)}
admin.site.register(CbvCrudModel, CbvCrudModelAdmin)


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ("title", "body",)
#     prepopulated_fields = {"slug": ("title",)}  # new

# admin.site.register(Article, ArticleAdmin)












