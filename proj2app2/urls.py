from django.urls import path
from proj2app2 import views


urlpatterns = [
    path('', views.dashboard, name = 'dashboard'), 
    path('add_dboard/', views.add_dboard, name = 'add_dboard'), 
    # path('contact/', views.contact, name = 'contact_us'), 
]

