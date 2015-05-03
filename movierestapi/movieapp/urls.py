from django.conf.urls import url, include, patterns
from rest_framework import routers
from movierestapi.movieapp import views

"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns(
	'movierestapi.movieapp.views',
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'movieapp', include('rest_framework.urls', namespace='rest_framework')),
    #url patterns for task (testing)
    #url(r'^tasks/$', 'task_list',name='task_list'),
    #url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail',name='task_detail'),

    #url patterns for Movie Data API
    url(r'^movies/$', 'view_movie',name='view_movie'),
    url(r'^movies/(?P<pk>[0-9]+)$', 'crud_on_movie',name='crud_on_movie'),
)