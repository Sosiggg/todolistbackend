from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('tasks/', views.todo_list, name='todo_list'),
    path('tasks/<int:pk>/', views.todo_detail, name='todo_detail'),
]