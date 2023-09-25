from django.contrib import admin
from django.urls import path

from genres.views import GenreCreateListView, genre_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-list'),
    path('genres/<int:pk>', genre_detail, name='genre-detail'),
]
