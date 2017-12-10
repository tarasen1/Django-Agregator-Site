from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('mainpage.urls')),
   #url(r'^personal/', include('persCabinet.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

