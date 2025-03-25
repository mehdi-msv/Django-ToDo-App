from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'user', 'complete', 'created_date', 'updated_date')
    list_filter = ('complete', 'created_date', 'updated_date')
    search_fields = ['title', 'user__username']
    date_hierarchy = 'created_date'
    ordering = ('-updated_date',)
    

admin.site.register(Task, TaskAdmin)