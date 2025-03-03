from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from users.forms import UserForm
from users.models import User


def home(request):
    return render(request, 'users/base.html')


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('users:base')


class UserLogin(LoginView):
    template_name = 'users/login_user.html'
    success_url = reverse_lazy('users:base')

