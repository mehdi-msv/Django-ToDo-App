from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from todo.models import Task

# Create your views here.


class TaskListView(LoginRequiredMixin, ListView):
    """
    List all tasks for the current user.
    """

    model = Task
    template_name = "todo/tasks_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).order_by(
            "-updated_date"
        )


class TaskCompleteView(LoginRequiredMixin, UpdateView):
    """
    Mark a task as complete or incomplete.
    """

    model = Task
    success_url = reverse_lazy("todo:tasks_list")

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(
            Task, pk=kwargs.get("pk"), author=request.user
        )
        task.complete = not task.complete
        task.save()

        return redirect(self.success_url)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new task for the current user.
    """

    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:tasks_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return redirect(self.success_url)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing task for the current user.
    """

    model = Task
    template_name = "todo/task_update.html"
    fields = ["title"]
    success_url = reverse_lazy("todo:tasks_list")

    def get_queryset(self):
        """
        Filter tasks to only those belonging to the current user.
        """
        return self.model.objects.filter(author=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete an existing task for the current user.
    """

    model = Task
    success_url = reverse_lazy("todo:tasks_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        """
        Filter tasks to only those belonging to the current user.
        """
        return self.model.objects.filter(author=self.request.user)
