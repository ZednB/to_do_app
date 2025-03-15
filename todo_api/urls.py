from django.urls import path

from todo_api.apps import TodoApiConfig
from todo_api.views import TaskCreateAPI, TaskListAPI, TaskRetrieveAPI, TaskUpdateAPI, TaskDestroyAPI

app_name = TodoApiConfig.name

urlpatterns = [
    path('task_create_api/', TaskCreateAPI.as_view(), name='task_create_api'),
    path('task_list_api/', TaskListAPI.as_view(), name='task_list_api'),
    path('task_retrieve_api/<int:pk>/', TaskRetrieveAPI.as_view(), name='task_retrieve_api'),
    path('task_update_api/<int:pk>/', TaskUpdateAPI.as_view(), name='task_update_api'),
    path('task_destroy_api/<int:pk>/', TaskDestroyAPI.as_view(), name='task_destroy_api'),
]
