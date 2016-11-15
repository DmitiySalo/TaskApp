from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .Serializers import TaskSerializer
from django.conf.urls import include
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
	

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    tasks = TaskSerializer(Task.objects.all(), many=True)
    data = tasks.data[:]
    #{task['id']: task for task in data}

"""   def retrieve(self, request, *args, **kwargs):
        return Response({task['id']: task for task in TaskViewSet.data})

    def list(self, request, *args, **kwargs):
        return Response({task['id']: task for task in TaskViewSet.data})"""
   

