from django.urls import path
from .views import friend_follow


contact_patterns = ([
    path('friends/follow/', friend_follow, name='friends_follow'),
], 'contact')
