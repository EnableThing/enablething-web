# from django.db import models
# 
# class Task( models.Model ):
# 	"""
# 	Model for storing `tasks`
# 	"""
# 
# 	# Whether this task is completed
# 	completed = models.BooleanField( default = False )
# 
# 	# Task title
# 	title = models.CharField( max_length = 100 )
	
from django.db import models


from uuidfield import UUIDField
from jsonfield import JSONField

# ViewSets define the view behavior.
class Task(models.Model):
	BACKLOG = 'Backlog'
	IN_PROGRESS = 'In progress'
	COMPLETE = 'Complete'
	BOARD_OPTIONS = (
                     (BACKLOG, 'Backlog'),
                     (IN_PROGRESS, 'In progress'),
                     (COMPLETE, 'Complete'),
                     )
   	"""
	Model for storing `tasks`
	"""

	# Whether this task is completed
	completed = models.BooleanField( default = False )

	# Task title
	title = models.CharField( max_length = 100,blank = True, null = True )
	
	task_id = UUIDField(auto=True)
	board = models.CharField(max_length=11, choices=BOARD_OPTIONS, default = BACKLOG)
	from_unit = UUIDField()
	to_unit = UUIDField()
	create_time = models.DateTimeField(auto_now_add=True, blank = True, null = True)
	start_time = models.DateTimeField(blank = True, null = True)
	complete_time = models.DateTimeField(blank = True, null = True)
	expires_time = models.DateTimeField(blank = True, null = True)
	command = JSONField(blank = True, null = True)
	response = JSONField(blank = True, null = True)
