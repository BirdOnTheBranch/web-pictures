from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy 
from django.http import HttpResponse

import json

from registration.models import Profile
from .models import Page
from .forms import PageForms
from taggit.models import Tag



# Create your views here.
class TagMixin(object):
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
        return Page.objects.filter(tags__slug=self.kwargs.get('slug'))
    

@method_decorator(login_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    fields = ['image','title','comment','tags']
    success_url = reverse_lazy('pages:pages')

    def form_valid(self, form):
        #Asing self.user.request for default to author model instance.
        form.instance.author = Profile.objects.get(user=self.request.user)

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForms
    template_name_suffix = '_update_form'

    def get_success_url(self):
        #Redefine method for pass the id argument
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'



@method_decorator(login_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')


@login_required(login_url='/user')
def like_button(request):
    user = request.user
    id = request.POST.get('pk', None)
    page = get_object_or_404(Page, pk=id)
    if request.method == 'POST':
        if page.likes.filter(id=user.id).exists():
            page.likes.remove(user)
        else:
            page.likes.add(user)

    context = {'likes_count': page.total_likes}
    return HttpResponse(json.dumps(context), content_type='application/json')
    