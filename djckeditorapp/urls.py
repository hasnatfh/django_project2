from django.urls import path
from djckeditorapp import views


urlpatterns = [
    path('', views.ckindex, name = 'ckhome'), 
    path('cke-add', views.ck_add, name = 'ckadd'), 
    path('fb-update/<int:id>', views.ck_update, name = 'ckupdate'), 
    path('fb-delete/<int:id>', views.ck_delete, name = 'ckdelete'), 
    path('ck-detail/<int:id>', views.ck_details, name = 'ckdetails'), 

]





































