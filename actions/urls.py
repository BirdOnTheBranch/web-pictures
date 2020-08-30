from django.urls import path 
from .views import dashboard


actions_patterns = ([
    path('actions/', dashboard, name='actions'),
    ],'actions') 
