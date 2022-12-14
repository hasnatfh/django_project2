from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
#from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, TemplateView, CreateView, FormView
from .models import CbvArticle, Person, CbvContactinfo 
from .forms import CbvContactForm, SignUpViewform2, LoginForm2
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

class CbvContactView(SuccessMessageMixin,CreateView):
     model = CbvContactinfo
     template_name = 'cbvtemplate/cbvcontact.html'
     form_class = CbvContactForm
     success_url = reverse_lazy('c_contact')
     success_message = 'Your message sent successfully.'


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


class SignUpView(CreateView):
     form_class = UserCreationForm
     success_url = reverse_lazy('c_index')
     template_name = 'cbvtemplate/csignup.html'
    

class SignUpView2(CreateView):
     form_class = SignUpViewform2
     success_url = reverse_lazy('c_index')
     template_name = 'cbvtemplate/csignup2.html'

class SignUpView3(FormView):
     template_name = 'cbvtemplate/csignup3.html'
     form_class = UserCreationForm
     redirect_authenticated_user = True
     success_url = reverse_lazy('cbvlogin')

#This is a function for keep logged in after registration/signup
     def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView3, self).form_valid(form)

#This is a function that disallows you to register a new account while one is still logged in. 
     def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('c_index')
        return super(SignUpView3, self).get(*args, **kwargs)


class UserLoginView(LoginView):
     template_name = 'cbvtemplate/clogin.html'
     redirect_authenticated_user = True
     fields = '__all__' 

     def get_success_url(self):
          return reverse_lazy('c_index')


class UserLoginView2(LoginView):
     form_class = LoginForm2
     template_name = 'cbvtemplate/clogin2.html'
     
     redirect_authenticated_user = True
     def get_success_url(self):
          return reverse_lazy('c_index')


class UserLogoutView(LogoutView):
     next_page = 'cbvlogin' 