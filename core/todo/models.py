from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
    
        return self.title
    
    def get_absolute_api_url(self):
        return reverse("todo:api-v1:task-detail", kwargs={"pk": self.pk})
    
    
    class META:
    
        order_with_respect_to = "user"