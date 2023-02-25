from django.contrib import admin
from django.urls import include, path
from .views import page_not_found_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', include('room.urls')),
    path('', include('core.urls')),
]

handler404 = page_not_found_view
