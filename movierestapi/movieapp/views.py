from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from movierestapi.movieapp.serializers import UserSerializer, GroupSerializer

#import task model
#from movierestapi.movieapp.task.models import Task
#import movie_metadata model
#from movierestapi.movieapp.movie_metadata.models import movie_metadata
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from movieapp.serializers import movie_metadataSerializer

"""
class UserViewSet(viewsets.ModelViewSet):
#API endpoint that allows users to be viewed or edited.
    queryset = User.objects.all()
    serializer_class = UserSerializer

#GroupViewSet not required ------------ Testing----------
class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint that allows groups to be viewed or edited.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""

#Movie Data Operations on view Level
@api_view(['GET','POST'])
def view_movie(request):
    """
    List all tasks, or create a new data
    """
    if request.method == 'GET':
        movie_metadatas = movie_metadata.objects.all()
        serializer = movie_metadataSerializer(movie_metadatas)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = movie_metadataSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def crud_on_movie(request,pk):
    """
    get, update or delete a specific data
    """
    try:
        movie_metadata = movie_metadata.objects.get(pk=pk)
    except movie_metadata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = movie_metadataSerializer(movie_metadata)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = movie_metadataSerializer(movie_metadata, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie_metadata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





