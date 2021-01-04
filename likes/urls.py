from django.urls import path

from .views import like_button

likes_patterns = ([
    path('like/<int:pk>', like_button, name='like_button'),
], 'likes')
