from django.forms import ModelForm

from todo.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline',)
