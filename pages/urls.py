from django.urls import path 
from . import views
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView, category_view, like_post

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('category/<category_id>/', views.category_view, name='category'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PageDeleteView.as_view(), name='delete'),
    path('like/', like_post, name='like-post'),
    ], 'pages')
