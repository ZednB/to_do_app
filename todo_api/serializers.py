from rest_framework.serializers import ModelSerializer

from todo.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
            # ('id', 'name', 'description', 'deadline', 'owner',)
