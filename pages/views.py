from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Taggit
from taggit.models import Tag
import json

from registration.models import Profile
from actions.models import Action
from actions.utils import create_action
from .forms import PageForms
from .models import Page


class TagMixin(object):
    """Mixin for add the tags ojects in views."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class PageListView(TagMixin, ListView):
    model = Page


class PageDetailView(TagMixin, DetailView):
    model = Page


class TagIndexView(TagMixin, ListView):
    template_name = 'pages/pages_list.html'
    model = Page

    def get_queryset(self):
        # Pass the slug and show tag(taggit) in template
        return Page.objects.filter(tags__slug=self.kwargs.get('slug'))


@method_decorator(login_required, name='dispatch')
class PageCreateView(CreateView):
    """Create view to upload images with generic post"""
    model = Page
    success_url = reverse_lazy('pages:pages')
    form_class = PageForms

    def form_valid(self, form):
        # Asing self.user.request for default to author model instance.
        form.instance.author = Profile.objects.get(user=self.request.user)
        # create action
        self.object = form.save()
        page = get_object_or_404(Page, pk=self.object.id)
        create_action(self.request.user, f'new post ', page)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForms
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # Redefine method for pass the id argument
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'


@method_decorator(login_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        action = Action.objects.filter(target_id=self.object.id)
        action.delete()
        self.object.delete()
        return HttpResponseRedirect(success_url)
