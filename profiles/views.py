from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from registration.models import Profile
from pages.models import Page


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profiles_detail.html'

    def get_object(self):
        """Get username model field for use in URL path."""
        return get_object_or_404(User, username=self.kwargs['username'])

    def get_context_data(self, *args, **kwargs):
        """Create dict context."""
        context = super().get_context_data(*args, **kwargs)
        user = get_object_or_404(Profile, user=self.object.id)
        query_page = Page.objects.all().filter(author=user)
        context['projects'] = query_page
        return context
