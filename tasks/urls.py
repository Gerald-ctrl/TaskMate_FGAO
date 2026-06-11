from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
]
