from todo.apps import TodoConfig
from django.urls import path
from todo.views import TaskCreate, TaskList, TaskDetail, TaskUpdate, TaskDelete, toggle_activity
from users.views import home

app_name = TodoConfig.name

urlpatterns = [
    path('', home, name='base'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('todo_list/', TaskList.as_view(), name='task_list'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
