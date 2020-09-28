from django.urls import path
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('', ProfileListView.as_view(), name="profiles"),
    path('<username>/', ProfileDetailView.as_view(), name="detail"),
], 'profiles')
