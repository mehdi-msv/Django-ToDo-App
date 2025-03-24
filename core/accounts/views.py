from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    fields = 'username', 'password'
    success_url = reverse_lazy('home')
    # def get_success_url(self):
    #     return reverse_lazy('home')

class RegisterView(CreateView,CustomLoginView):
    model = User
    template_name = 'accounts/register.html'
    success_url = '/admin'
    form_class = UserCreationForm
