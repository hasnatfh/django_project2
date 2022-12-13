from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, ContactInfo
from proj2app2.models import Person


# Create your views here.

class ArticleListView(ListView):
     model = Article
     template_name = 'cindex.html'
     context_object_name = "article_list"
     paginate_by = 1

class ArticleDetailView(DetailView):
     model = Article
     template_name = 'article_details.html'
     context_object_name = "article_detail"
     


def home(request):
     item = Article.objects.all()
     name = Person.objects.all()
     context =  {
          'data': item, 
          'auth': name
          }

     return render(request, 'index.html', context) 

'''
def article_detail(request, id):
     context ={}
     context["ardetails"] = Article.objects.get(id=id)
     return render(request, 'article-details2.html', context)
'''
def article_detail(request, id):
  data = get_object_or_404(Article, pk=id)
  template_name = "article-details2.html"
  context = {
      "ardetails":data
  }
  return render(request, template_name, context)



def about (request):
     return render(request, 'about.html')

def contact (request):
     if request.method == 'POST':
          name = request.POST.get('fname')
          email = request.POST.get('femail')
          message = request.POST.get('fmessage')
          mydata = ContactInfo(cname=name, cemail=email, cmessage=message)
          mydata.save()
     return render(request, 'contact.html')

 