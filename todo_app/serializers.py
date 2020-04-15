from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'body', 'author',
                  'is_completed', 'created_at')
