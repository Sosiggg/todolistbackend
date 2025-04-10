from django.urls import path
from . import views
from .views import SecureHelloView

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('tasks/', views.todo_list, name='todo_list'),
    path('tasks/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('secure-hello/', SecureHelloView.as_view(), name='secure-hello'),
]