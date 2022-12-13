from django.urls import path
from proj2app import views
from .views import ArticleListView, ArticleDetailView 


urlpatterns = [
    path('', views.home, name = 'home'), 
    path('<int:id>/details/', views.article_detail, name = 'article_details2'), 
    path('about/', views.about, name = 'about_us'), 
    path('contact/', views.contact, name = 'contact_us'), 
    path('cindex/', ArticleListView.as_view(), name = 'c_index'), 
    path('cindex/<int:pk>/details/', ArticleDetailView.as_view(), name = 'article_details'), 
]
