from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import UserForm
from users.models import User


def home(request):
    return render(request, 'users/base.html')


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('todo:base')


class UserLogin(LoginView):
    template_name = 'users/login_user.html'
    success_url = reverse_lazy('todo:task_list')


class UserLogout(LogoutView):
    template_name = 'users/logout_user.html'
    success_url = reverse_lazy('todo:task_list')


class UserDetail(DetailView):
    model = User
    template_name = 'users/detail_user.html'


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('detail_user')


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('todo:base')
