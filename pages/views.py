from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy 
from django.http import JsonResponse

from registration.models import Profile
from .models import Page, Like
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


def like_post(request):
    user = request.user
    json_response = {'value':False}
    if request.user.is_authenticated:
        page_id = request.POST.get('page_id',)
        page_page = Page.objects.get(id=page_id)
        if  user in page_page.liked.all():
            page_page.liked.remove(user)
        else:
            page_page.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, page_id=page_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
                json_response['value'] = 'Unlike'
                 
        else:
            like.value = 'Like'
            like.save()
            json_response['value'] = 'like'

    
    return JsonResponse(json_response)
    