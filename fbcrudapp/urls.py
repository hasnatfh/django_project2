from django.urls import path
from fbcrudapp import views


urlpatterns = [
    path('', views.fbhome_list, name = 'fbhome'), 
    path('fb-add', views.fbcrud_add, name = 'fbadd'), 
    path('fb-update/<int:id>', views.fbcrud_update, name = 'fbupdate'), 
    path('fb-delete/<int:id>', views.fblist_delete, name = 'fbdelete'), 
    path('fb-detail/<int:id>', views.fblist_details, name = 'fbdetails'), 

]





































