from django.urls import path 
from . import views
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView, TagIndexView
from likes.views import like_button


pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PageDeleteView.as_view(), name='delete'),
    #Taggit
    path('tags/<slug:slug>/', TagIndexView.as_view(), name='tagged'),
    #Likes 
    path('like/<int:pk>', like_button, name='like_button'),
    ], 'pages')
