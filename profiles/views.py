from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'



class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profiles_detail.html'

    def get_object(self):
     return get_object_or_404(Profile, user__username=self.kwargs['username'])