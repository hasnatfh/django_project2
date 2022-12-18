from django.urls import path
from proj2app import views
 


urlpatterns = [
    path('', views.home, name = 'home'), 
    path('<int:id>/details/', views.article_detail, name = 'article_details2'), 
    path('about/', views.about, name = 'about_us'), 
    path('contact/', views.contact, name = 'contact_us'), 
    path('signup/', views.user_signup, name = 'signup'), 
    path('signup2/', views.user_signup2, name = 'signup2'), 
    path('signup3/', views.user_signup3, name = 'signup3'), 
    path('login/', views.user_login, name = 'login'), 
    path('login2/', views.user_login2, name = 'login2'), 
    path('logout/', views.user_logout, name = 'logout'), 
]
