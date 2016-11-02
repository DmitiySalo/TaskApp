from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.conf.urls import include
from rest_framework.views import APIView 
#class TaskViewSet(viewsets.ModelViewSet):
#	queryset = Task.objects.all().order_by('-date_created')
#	serializer_class = TaskSerializer

class TaskList(APIView):
	def get(self,request):
		task = Task.objects.all()
		serializer = TaskSerializer(task, many=True)
		return Response(serializer.data)
	def post(self):
			pass	
