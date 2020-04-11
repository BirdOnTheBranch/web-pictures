from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Pages


# Create your views here.
class PageListView(ListView):
    model = Pages


class PageDetailView(DetailView):
    model = Pages
   