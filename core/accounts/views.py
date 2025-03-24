from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView
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

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    success_url = '/admin'
    form_class = UserCreationForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super(RegisterView,self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # کاربر را لاگین می کند.
        return redirect(self.success_url)