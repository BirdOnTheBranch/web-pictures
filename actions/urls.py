from django.urls import path 
from .views import ArtionListView


actions_patterns = ([
    path('actions/', ArtionListView.as_view(), name='actions'),
    ],'actions') 
