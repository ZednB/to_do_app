from django.urls import path

from users.apps import UsersConfig
from users.views import home

app_name = UsersConfig.name

urlpatterns = [
    path('', home, name='base'),
]