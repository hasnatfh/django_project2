from django.urls import path
from proj2app2 import views
from .views import CbvArticleListView, CbvArticleDetailView, CbvContactView, SignUpView, SignUpView2, SignUpView3, UserLoginView, UserLogoutView, UserLoginView2


urlpatterns = [
    path('cindex/', CbvArticleListView.as_view(), name = 'c_index'), 
    path('cvbcontact/', CbvContactView.as_view(), name = 'c_contact'), 
    path('cindex/<int:pk>/details/', CbvArticleDetailView.as_view(), name = 'article_details'), 
    path('signup/', SignUpView.as_view(), name = 'cbvsign_up'), 
    path('signup2/', SignUpView2.as_view(), name = 'cbvsign_up2'), 
    path('signup3/', SignUpView3.as_view(), name = 'cbvsign_up3'), 
    path('login/', UserLoginView.as_view(), name = 'cbvlogin'), 
    path('login2/', UserLoginView2.as_view(), name = 'cbvlogin2'), 
    path('logout/', UserLogoutView.as_view(), name = 'cbvlogout'), 
]