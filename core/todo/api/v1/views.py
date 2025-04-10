from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ...models import Task
from .serializers import TaskSerializer


class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
