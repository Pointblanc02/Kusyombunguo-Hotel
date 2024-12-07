
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings 

# from hotel.hotel import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rooms.urls')),
    path('about/', include('rooms.urls')),
    path('blog/', include('rooms.urls')),
    path('contact/', include('rooms.urls')),
    path('gallery', include('rooms.urls')),
    path('room/', include('rooms.urls')),
    path('viewdata', include('rooms.urls')),
]+static(settings.DATA_URL,document_root=settings.DATA_ROOT)
