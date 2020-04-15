from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.TodoListAPIView.as_view()),
    path('<int:pk>/', views.UpdateDestroyTodoAPIView.as_view()),
    path('new/', views.CreateTodoAPIView.as_view()),
]
