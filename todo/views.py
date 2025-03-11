from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from todo.forms import TaskForm
from todo.models import Task
from django.urls import reverse_lazy, reverse

from users.models import User


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    # context = {'name': Task.name, 'description': Task.description, 'owner_id': owner.pk}


    # def task_create(self, request):
    #     if request.method.POST == 'POST':
    #         Task.objects.create(name=Task.name, description=Task.description, owner_id=User.id)
    #         Task.save(Task)


class TaskList(ListView):
    model = Task
    template_name = 'todo/todo_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/todo_detail.html'


class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:task_list')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:task_list')


def toggle_activity(request, pk):
    status_item = get_object_or_404(Task, pk=pk)
    if status_item.status:
        status_item.status = False
    else:
        status_item.status = True

    status_item.save()
    return redirect(reverse_lazy('todo:task_list'))
