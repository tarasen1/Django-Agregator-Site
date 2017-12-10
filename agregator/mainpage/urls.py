from django.conf.urls import url, include
from . import views


urlpatterns = [
	#url(r'^', views.mainPage),
	url(r'^$', views.mainPage),
	url(r'^room/get/(?P<room_id>[\d+])/$',views.room_detail),
	url(r'^fltr/',views.content_filter)
]

#urlpatterns += staticfiles_urlpatterns()
