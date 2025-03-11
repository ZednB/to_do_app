from django.urls import path

from todo_api.apps import TodoApiConfig
from todo_api.views import TaskCreateAPI, TaskListAPI, TaskRetrieveAPI, TaskUpdateAPI, TaskDestroyAPI

app_name = TodoApiConfig.name

urlpatterns = [
    path('task_create/', TaskCreateAPI.as_view(), name='task_create_api'),
    path('task_list/', TaskListAPI.as_view(), name='task_create_api'),
    path('task_retrieve/<int:pk>/', TaskRetrieveAPI.as_view(), name='task_retrieve_api'),
    path('task_update/<int:pk>/', TaskUpdateAPI.as_view(), name='task_update_api'),
    path('task_destroy/<int:pk>/', TaskDestroyAPI.as_view(), name='task_destroy_api'),
]