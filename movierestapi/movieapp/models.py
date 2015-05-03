from django.db import models

#customFloat Field for actual mysql float data type
class customFloatField(models.Field): 
    def db_type(self,connection):
        return 'float'

#create table model for movie_metadata
class movie_metadata(models.Model):
	name = models.CharField(max_length=255)
	director = models.CharField(max_length=255)
	imdb_score = customFloatField(null=True,blank=True)
	_99popularity = customFloatField(null=True,blank=True)
	genre = models.CharField(max_length=535)
	
	

