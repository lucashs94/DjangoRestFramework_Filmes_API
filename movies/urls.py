from django.urls import path

from movies.views import *



urlpatterns = [
    
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    
]
