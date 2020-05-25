from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from registration.models import Profile, Friendship
from pages.models import Page


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profiles_detail.html'

    def get_object(self):
        """Get username model field for use in path."""
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def _get_friends(self):
        if self.request.user.is_authenticated:
            friends = Friendship.objects.filter(creator=self.request.user)
            return friends
        return []

    def get_context_data(self, *args, **kwargs):
        """Create dict context."""
        context = super().get_context_data(*args, **kwargs)
        context['projects_list'] = Page.objects.all()
        context['friends_list'] = self._get_friends()
        return context
