from django.urls import path
from proj2app2 import views
from .views import CbvArticleListView, CbvArticleDetailView, CbvContactView


urlpatterns = [
    path('cindex/', CbvArticleListView.as_view(), name = 'c_index'), 
    path('cvbcontact/', CbvContactView.as_view(), name = 'c_contact'), 
    path('cindex/<int:pk>/details/', CbvArticleDetailView.as_view(), name = 'article_details'), 
]