from rest_framework import serializers
from task.models import Task

class TaskSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse Task data
	"""

	class Meta:
		model = Task
		fields = ('title','task_id', 'board','from_unit','to_unit','command','response', )
		
class BasicTaskSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse Task data
	"""

	class Meta:
		model = Task
		fields = ('task_id',)