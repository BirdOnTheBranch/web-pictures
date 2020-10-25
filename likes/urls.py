from django.urls import path

from .views import LikeDetailView, LikeListView, like_button

likes_patterns = ([
    path('', LikeListView.as_view(), name='likes'),
    path('<int:pk>/<slug:slug>/', LikeDetailView.as_view(), name='like'),
    path('like/<int:pk>', like_button, name='like_button'),
], 'likes')
