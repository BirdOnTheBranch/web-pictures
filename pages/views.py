from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Page, Category
from .forms import PageForms


# Create your views here.
class StaffrequiredMixin(object):
    """This mixin requires user is staff member."""
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    fields = ['image','title','comment','categories']
    success_url = reverse_lazy('pages:pages')

    def form_valid(self, form):
        #Asing self.user.request for default to author model instance.
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForms
    template_name_suffix = '_update_form'

    def get_success_url(self):
        #Redefine method for pass the id argument
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'


@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')


def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'pages/category.html', {'category':category})
