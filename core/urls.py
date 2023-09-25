from django.contrib import admin
from django.urls import path

from genres.views import genre_detail, genre_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_list, name='genre-list'),
    path('genres/<int:pk>', genre_detail, name='genre-detail'),
]
