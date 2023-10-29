from django.urls import path

from genres.views import *



urlpatterns = [
    
    path('genres/', GenreCreateListView.as_view(), name='genre-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    
]