from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Room(models.Model):
	class Meta():
		db_table = 'rooms'

	def __str__(self):
		return self.room_name
	room_user 			=	models.ForeignKey(User)

	room_name 			=	models.CharField(max_length=300)
	room_descpription	=	models.TextField()
	room_photo			=	models.ImageField(upload_to='mainImages')

	room_city 			=	models.CharField(max_length=40)
	room_adress			=	models.CharField(max_length=100)

	square				=	models.IntegerField(validators=[MinValueValidator(0)])
	room_equipment		=	models.TextField(max_length=1000)

	room_accesability	=	models.BooleanField()
	room_light			=	models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
	 
	
class Comment(models.Model):
	class Meta():
		db_table = 'comments'

	comment_text = models.TextField()
	comment_like = models.IntegerField(default = 0)
	comment_article = models.ForeignKey(Room)
	comment_user = models.ForeignKey(User)