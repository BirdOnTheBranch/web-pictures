from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from registration.models import Profile
from pages.models import Page


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'



class ProfileDetailView(DetailView):
    model = Profile, Page
    template_name = 'profiles/profiles_detail.html'

    def get_object(self):
     return get_object_or_404(Profile, user__username=self.kwargs['username'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['projects_list'] = Page.objects.filter(author=self.request.user)
        return context
