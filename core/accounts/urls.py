from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterView

app_name = "accounts"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
