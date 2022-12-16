from django.urls import path
from proj2app import views
 


urlpatterns = [
    path('', views.home, name = 'home'), 
    path('<int:id>/details/', views.article_detail, name = 'article_details2'), 
    path('about/', views.about, name = 'about_us'), 
    path('contact/', views.contact, name = 'contact_us'), 
    path('login/', views.user_login, name = 'login'), 
    path('logout/', views.logout_view, name = 'logout'), 
]
