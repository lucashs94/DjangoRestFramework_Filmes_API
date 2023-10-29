from django.urls import path

from actors.views import *


urlpatterns = [
    
    path('actors/', ActorCreateListView.as_view(), name='actor-list'),
    path('actors/<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),
    
]
