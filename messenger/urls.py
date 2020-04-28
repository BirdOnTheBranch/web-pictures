from django.urls import path
from .views import ThreadTemplateView, ThreadDetailView


messenger_patterns = ([
    path('', ThreadTemplateView.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='detail'),
], 'messenger')