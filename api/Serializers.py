from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id','task_name','task_desc')


"""
class TaskSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	task_name = serializers.ReadOnlyField()
	task_desc = serializers.ReadOnlyField()
	

	def to_representation(self, data):
		res = super(TaskSerializer, self).to_representation(data)
		return {res['id']: res}"""

