from django.contrib.auth.models import User, Group
from rest_framework import serializers
#import Task
#from movierestapi.movieapp.task.models import Task
#import movie_metadata model
#from movierestapi.movieapp.movie_metadata.models import Movie_Metadata
from ..movieapp.models import movie_metadata

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#GroupSerializer not required ------------ Testing----------
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

"""			
#define serializer for Movie_Metadata
class movie_metadataSerializer(object):
	class Meta:
		model = movie_metadata
		fields = ('name','director','imdb_score','_99popularity','genre')
			

			
	
