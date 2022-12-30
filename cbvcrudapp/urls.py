from django.urls import path
from .views import CbvCrudListView, CbvCrudDetailView, CbvCrudDeleteView, CbvCrudCreateView, CbvCrudUpdateView

urlpatterns = [

    path('', CbvCrudListView.as_view(), name ='cbvhome'),
    path('cbv-list-add', CbvCrudCreateView.as_view(), name ='cbvadd'),
    path('cbv-list-update/<int:pk>', CbvCrudUpdateView.as_view(), name ='cbvupdate'),
    path('slug/<int:pk>-<str:slug>', CbvCrudDetailView.as_view(), name ='cbvdetails'),
    path('cbv-list-delete/<int:pk>', CbvCrudDeleteView.as_view(), name ='cbvdelete'),
    

]

