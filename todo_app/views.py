from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer


class TodoListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)


class CreateTodoAPIView(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdateDestroyTodoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
