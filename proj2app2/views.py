from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import CbvArticle, Person, CbvContactinfo 
from .forms import CbvContactForm

# Create your views here.

class CbvContactView(CreateView):
     model = CbvContactinfo
     template_name = 'cbvtemplate/cbvcontact.html'
     form_class = CbvContactForm
     success_url = reverse_lazy('c_contact')

class CbvArticleListView(ListView):
     model = CbvArticle
     template_name = 'cbvtemplate/cindex.html'
     context_object_name = "article_list"
     paginate_by = 1

class CbvArticleDetailView(DetailView):
     model = CbvArticle
     template_name = 'cbvtemplate/article_details.html'
     context_object_name = "article_detail"
     
     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the Person
        context['person'] = Person.objects.all()
        return context





