from django.urls import path

urlpatterns = [

    path('', CbvListView.as_view, name ='cbvhome')

]