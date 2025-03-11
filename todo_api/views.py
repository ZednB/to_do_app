from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from todo.models import Task
from todo_api.permissions import IsOwnerStaff
from todo_api.serializers import TaskSerializer


class TaskCreateAPI(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        user = serializer.save(owner=self.request.user)
        user.save()


class TaskListAPI(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskRetrieveAPI(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]


class TaskUpdateAPI(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]


class TaskDestroyAPI(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]
