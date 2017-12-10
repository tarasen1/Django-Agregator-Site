from django.shortcuts import render, get_object_or_404
from mainpage.models import Room


def mainPage(request):
	context = {
		'pageTitle'	:	'Agreg',
		'rooms'	:	Room.objects.filter(),
	}
	return render(request, 'mainpage/home.html', context)


def room_detail(request, room_id):
	room = get_object_or_404(Room, pk=room_id)
	context = {
		'pageTitle' 	: room.room_name,
		'room' 	: room,	
	}
	return render(request, 'mainpage/room_detail.html', context)

def content_filter(request):
		fltr_city 	=	request.POST.get('city')
		fltr_light	=	request.POST.get('light') 
		fltr_acces	=	request.POST.get('acces')
		fltr_square = 	request.POST.get('square')
		fltr_price 	= 	request.POST.get('price')
		fltr_rooms  =	Room.objects.all()
		if fltr_city is not None and fltr_city != "None":
				fltr_rooms = fltr_rooms.filter(room_city=fltr_city)
		if fltr_light is not None and fltr_light != "None":
				fltr_rooms = fltr_rooms.filter(room_light=int(fltr_light))
				
		context		=	{
			'pageTitle'	:	'Agreg',
			'rooms'		:	fltr_rooms
		}
		return render(request, 'mainpage/home.html', context)
