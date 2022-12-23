
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Article, ContactInfo
from proj2app2.models import Person
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

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


#function based signup/registration
def user_signup(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               user = form.save()
               login(request, user)
               return redirect('home')
     else:
          form = UserCreationForm()
          context = {'form': form}
          
     return render(request, 'signup.html', context)
     

def user_signup2(request):
     if request.method == 'GET':
          form  = UserCreationForm()
          context = {'form': form}
          return render(request, 'signup2.html', context)
     if request.method == 'POST':
          form  = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account was created for ' + user)
               return redirect('home')
          else:     
               print('Form is not valid')                   
               messages.error(request, 'Error Processing Your Request')
               context = {'form': form}
               return render(request, 'signup2.html', context)

     return render(request, 'signup2.html', {})



def user_signup3(request):
     if request.method == 'POST':
          form = UserRegistrationForm(request.POST)
          if form.is_valid():
               user_obj = form.cleaned_data
               username = user_obj['username']
               email = user_obj['email']
               password = user_obj['password']
               if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)     
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    messages.success(request, 'Thanks!Sign up success.')
                    return redirect('home')
               else:
                    raise forms.ValidationError('Looks like a username with that email already exists')
     
     else: 
          form  = UserRegistrationForm()  
          messages.error(request, 'Wrong info, pleae try again.')     
     return render(request, 'signup3.html', {'form': form})
    


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

     return render(request, 'login.html'  ) 



def user_login2(request):
     if request.method == 'POST':
          form = AuthenticationForm(request, data=request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username= username, password= password)
               if user is not None:
                    login(request, user)
                    return redirect('home')
               else:
                    messages.error(request,"Invalid username or password.")
          else:
               messages.error(request,"Invalid username or password.")
     form = AuthenticationForm()
     return render(request, 'login2.html', {'form':form})



def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')

    