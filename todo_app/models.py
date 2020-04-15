from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True,)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
