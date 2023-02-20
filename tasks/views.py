from rest_framework import permissions, generics, filters
from .models import Task
from .serializers import TaskSerializer
from tudu_api.permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """
    Lists tasks or create a task if logged in
    The perform_create method associates the task with the logged in user.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
            
    ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a task and edit or delete it if you own it.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Task.objects.all()
