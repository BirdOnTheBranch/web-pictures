from django.urls import path 
from .views import PageListView, PageDetailView

urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:page_id>/<slug:page_slug>/', PageDetailView.as_view(), name='page')
]