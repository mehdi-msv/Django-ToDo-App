from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
    '''
    Custom login view for the application.
    '''
    template_name = 'accounts/register.html'
    redirect_authenticated_user = True
    fields = 'username', 'password'
    success_url = reverse_lazy('todo:tasks_list')
    
    def get_success_url(self):
        '''
        Redirect to the tasks list after successful login.
        '''
        return self.success_url
    
    
class RegisterView(CreateView):
    '''
    Register a new user for the application.
    '''
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('todo:tasks_list')
    
    def get(self, request, *args, **kwargs):
        '''
        Check if the user is authenticated before allowing registration.
        '''
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super(RegisterView,self).get(request, *args, **kwargs)
    
    def form_valid(self, form):
        '''
        Save the new user and log them in after successful registration.
        '''
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)