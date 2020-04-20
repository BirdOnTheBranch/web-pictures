from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Page


# Create your views here.
class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
   