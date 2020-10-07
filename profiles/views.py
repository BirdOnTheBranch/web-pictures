from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView
from pages.models import Page
from registration.models import Profile


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
        """Filter post only profile user"""
        user = get_object_or_404(Profile, user=self.object.id)
        author_pages = Page.objects.all().filter(author=user)
        context = super().get_context_data(*args, **kwargs)
        context['projects'] = author_pages
        return context
