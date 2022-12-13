from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CbvArticle

# Create your views here.




class CbvArticleListView(ListView):
     model = CbvArticle
     template_name = 'cindex.html'
     context_object_name = "article_list"
     paginate_by = 1

class CbvArticleDetailView(DetailView):
     model = CbvArticle
     template_name = 'article_details.html'
     context_object_name = "article_detail"




