from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CbvCrudForm 
from .models import CbvCrudModel
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
 

# Create your views here.

class CbvCrudListView(ListView):
    model = CbvCrudModel
    template_name = 'cbvcrudtemplate/cbvindex.html'
    context_object_name = 'cbvcrud_list'
    ordering = ['-id']

class CbvCrudCreateView(CreateView):
    model = CbvCrudModel
    form_class = CbvCrudForm
    template_name = 'cbvcrudtemplate/cbvadd.html'  
    success_url = reverse_lazy('cbvhome')

class CbvCrudUpdateView(UpdateView):
    model = CbvCrudModel
    form_class = CbvCrudForm
    template_name = 'cbvcrudtemplate/cbvupdate.html'  
    success_url = reverse_lazy('cbvhome')

    
class CbvCrudDetailView(DetailView):
    model = CbvCrudModel
    template_name = 'cbvcrudtemplate/cbvdetail.html'
    context_object_name = 'cbvcrudlist_detail'
    query_pk_and_slug = True


class CbvCrudDeleteView(DeleteView):
    model = CbvCrudModel
    template_name = 'cbvcrudtemplate/cbvdelete.html'
    context_object_name = 'cbvcrudlist_delete'
    success_url = reverse_lazy ('cbvhome')

  