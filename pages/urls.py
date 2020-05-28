from django.urls import path 
from . import views
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView, like_button, TagIndexView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PageDeleteView.as_view(), name='delete'),
    path('tags/<slug:slug>/', TagIndexView.as_view(), name='tagged'),
    path('like/<int:pk>', like_button, name='like_button'),
    ], 'pages')
