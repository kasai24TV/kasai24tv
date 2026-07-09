from django.contrib import admin
from django.urls import path, include
from videos.views import api_videos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/videos/', api_videos),
    path('', include('television.urls')),
]
