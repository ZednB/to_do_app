from django.urls import path
from django.contrib.auth.views import LoginView

from users.apps import UsersConfig
from users.views import home, UserCreate, UserLogin, UserDetail, UserLogout, UserUpdate, UserDelete

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreate.as_view(), name='create_user'),
    path('login/', UserLogin.as_view(), name='login_user'),
    path('logout/', UserLogout.as_view(), name='logout_user'),
    path('detail/<int:pk>/', UserDetail.as_view(), name='detail_user'),
    path('update/<int:pk>/', UserUpdate.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='delete_user'),
]