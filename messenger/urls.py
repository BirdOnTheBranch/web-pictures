from django.urls import path
from .views import ThreadTemplateView, ThreadDetailView, add_message


messenger_patterns = ([
    path('', ThreadTemplateView.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='detail'),
    path('thread/add/<int:pk>/', add_message, name='add'),
], 'messenger')
