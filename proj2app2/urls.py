from django.urls import path
from proj2app2 import views
from .views import CbvArticleListView, CbvArticleDetailView, CbvContactView, SignUpView, SignUpView2, SignUpView3


urlpatterns = [
    path('cindex/', CbvArticleListView.as_view(), name = 'c_index'), 
    path('cvbcontact/', CbvContactView.as_view(), name = 'c_contact'), 
    path('cindex/<int:pk>/details/', CbvArticleDetailView.as_view(), name = 'article_details'), 
    path('signup/', SignUpView.as_view(), name = 'sign_up'), 
    path('signup2/', SignUpView2.as_view(), name = 'sign_up2'), 
    path('signup3/', SignUpView3.as_view(), name = 'sign_up3'), 
]