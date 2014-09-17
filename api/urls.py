from django.conf.urls import patterns, include, url

# Function based API views
# from api.views import task_list, task_detail

# Class based API views
from api.views import TaskList, TaskDetail, UnitList

from task import views
from rest_framework.routers import DefaultRouter

# urlpatterns = patterns('',
# 
#     # Regular URLs
# 	# url(r'^tasks/$', task_list, name='task_list'),
#     # url(r'^tasks/(?P<pk>[0-9]+)$', task_detail, name='task_detail'),
# 
#     # Class based URLs,
#     url( r'^tasks/$', TaskList.as_view(), name = 'task_list' ),
#     url( r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name = 'task_detail' ),
#     url( r'^tasks/task_id/(?P<task_id>.+)/$', TaskIDList.as_view()),



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
# urlpatterns = [
# url(r'^tasks/$', TaskView.as_view(), name='task-list'),
# ]

#router = DefaultRouter()
#router.register(r'tasks', TaskViewSet)

urlpatterns = patterns('',
    url( r'^tasks/task_id/(?P<task_id>.+)/$', TaskDetail.as_view()),
    url( r'^tasks/to_unit/(?P<to_unit>.+)/$', UnitList.as_view()),
    url( r'^tasks/$', TaskList.as_view()),
    #url( r'^tasks/task_id/(?P<pk>.+)/$', TaskDetail.as_view()),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
