from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .Serializers import TaskSerializer
from django.conf.urls import include

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('-date_created')
	serializer_class = TaskSerializer

# Create your views here.
