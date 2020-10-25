from django.urls import path

from .views import (PageCreateView, PageDeleteView, PageDetailView,
                    PageListView, PageUpdateView, TagIndexView)

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<slug:slug>/<int:pk>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PageDeleteView.as_view(), name='delete'),
    # Taggit
    path('tags/<slug:slug>/', TagIndexView.as_view(), name='tagged'),
], 'pages')
