from rest_framework import generics, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import renderers

from django.db.models import Q

from rest_framework import viewsets

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView )


from task.models import Task
from api.serializers import TaskSerializer, BasicTaskSerializer

#import django_filters

# Example using function based views
# -----------------------------------

# @api_view(['GET', 'POST'])
# def task_list(request):
#     """
#     List all task, or create a new one
#     """

#     # GET Request
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks)
#         return Response(serializer.data)

#     # POST Request
#     if request.method == 'POST':
#         serializer = TaskSerializer(data=request.DATA)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )


# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Get, update, or delete a specific task
#     """
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # GET request
#     if request.method == 'GET':
#         serializer = TaskSerializer( task )
#         return Response( serializer.data )

#     # PUT request
#     if request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.DATA)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)

#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )

#     # DELETE request
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Example using class based views
# -----------------------------------
class TaskMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    model = Task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('task_id','to_unit','from_unit','board',)
 
class TaskList(TaskMixin, ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    pass

class UnitList(TaskMixin, ListAPIView):
    serializer_class = TaskSerializer
    #http://stackoverflow.com/questions/21292646/capture-parameters-in-django-rest-framework
    #lookup_field = 'to_unit'
    #queryset = Task.objects.all().filter(to_unit = lookup_to_unit)
    #serializer_class = BasicTaskSerializer
    #lookup_field = 'to_unit'
    lookup_field = "to_unit"
    
    lookup_url_kwarg = "to_unit"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        #comments = Task.objects.filter(to_unit=uid, ~Q(board="Complete" ))
        comments = Task.objects.filter(Q(to_unit=uid) & ~Q(board='Complete') )
        
        #comments = Task.objects.filter(to_unit=uid)
        
        return comments    
#     """
#     Return a list of all the tasks, or
#     create new ones
#     """
#     pass

class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    
    """
    Return a specific task, update it, or delete it.
    """
    lookup_field = 'task_id'
    pass

# class TaskDetail(generics.RetrieveUpdateAPIView):
#  
#      serializer_class = TaskSerializer
#      lookup_field = 'task_id'
#      def get_queryset(self):
#          """
#          Optionally restricts the returned purchases to a given user,
#          by filtering against a `username` query parameter in the URL.
#          """
#            
#          task_id = self.kwargs['task_id']
#          return Task.objects.filter(task_id=task_id)
#  
#     
# class TaskList(generics.ListAPIView):
#     model = Task
#     serializer_class = TaskSerializer
#     #lookup_field = 'board'
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ('task_id','to_unit','from_unit','board',)



    