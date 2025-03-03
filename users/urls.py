from django.urls import path
from django.contrib.auth.views import LoginView

from users.apps import UsersConfig
from users.views import home, UserCreate, UserLogin

app_name = UsersConfig.name

urlpatterns = [
    path('', home, name='base'),
    path('create/', UserCreate.as_view(), name='create_user'),
    # path('login/', LoginView.as_view(template_name='users/login_user.html'), name='login_user'),
    path('login/', UserLogin.as_view(), name='login_user'),
]