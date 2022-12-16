
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Article, ContactInfo
from proj2app2.models import Person
from django.contrib.auth import authenticate, login, logout

# Create your views here.
     


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
          messages.success(request, f"{name}, Your message sent ")
          
     return render(request, 'contact.html')


#login system
def user_login(request):
          if request.method == "POST":
               username = request.POST['username']
               password = request.POST['password']
               user = authenticate(request, username = username, password = password)
               if user is not None:
                    login(request, user)
                    return redirect('home')
               else:
                    messages.error(request, f"  Incorrect username or password")

              

          return render(request, 'login.html') 

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')

    