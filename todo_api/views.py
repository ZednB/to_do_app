from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from todo.models import Task
from todo_api.permissions import IsOwnerStaff
from todo_api.serializers import TaskSerializer
from django.http import HttpResponse, JsonResponse
import json


class TaskCreateAPI(CreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class TaskListAPI(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerStaff]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        response = HttpResponse(
            json.dumps(serializer.data),
            content_type="application/json"
        )
        return response

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskRetrieveAPI(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.filter(id=task_id, owner=self.request.user).first()

        if not task:
            return HttpResponse(
                json.dumps({"error": "Task not found or not authorized to view."}),
                content_type="application/json",
                status=404
            )
        serializer = TaskSerializer(task)
        response = HttpResponse(
            json.dumps(serializer.data),
            content_type="application/json"
        )
        return response


class TaskUpdateAPI(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = json.loads(request.body)
        serializer = self.get_serializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


class TaskDestroyAPI(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse({"detail": "Task deleted successfully"}, status=204)
