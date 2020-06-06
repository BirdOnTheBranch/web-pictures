from django.urls import path 
from .views import  LikeListView, LikeDetailView, like_button


likes_patterns = ([
    path('', LikeListView.as_view(), name='likes'),
    path('<int:pk>/<slug:slug>/', LikeDetailView.as_view(), name='like'),
    ], 'likes')


