from django.contrib import admin
from django.urls import path

from genres.views import *
from actors.views import *
from movies.views import *
from reviews.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    
    path('actors/', ActorCreateListView.as_view(), name='actor-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),
    
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    
    path('reviews/', ReviewCreateListView().as_view(), name='review-list'),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView().as_view(), name='review-detail'),
]
