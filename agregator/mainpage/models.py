from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Room(models.Model):
	class Meta():
		db_table = 'rooms'

	room_name 			=	models.CharField(max_length=300)
	room_descpription	=	models.TextField()
	square				=	models.IntegerField(validators=[MinValueValidator(0)])
	room_equipment		=	models.TextField(max_length=1000)

	room_accesability	=	models.BooleanField()
	room_light			=	models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
	 
	


