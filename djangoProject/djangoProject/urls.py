
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoProject.web.urls')),
    path('album/', include('djangoProject.albums.urls')),
    path('profile/', include('djangoProject.profiles.urls')),
]
