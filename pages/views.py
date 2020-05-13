from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy 

from registration.models import Profile
from .models import Page, Category, Like
from .forms import PageForms



# Create your views here.
class PageListView(ListView):
    model = Page

    def get_context_data(self, *args, **kwargs):
        """Create dict context."""
        context = super().get_context_data(*args, **kwargs)
        context['avatar_list'] = Profile.objects.all()
        return context



class PageDetailView(DetailView):
    model = Page



@method_decorator(login_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    fields = ['image','title','comment','categories']
    success_url = reverse_lazy('pages:pages')

    def form_valid(self, form):
        #Asing self.user.request for default to author model instance.
        form.instance.author = self.request.user
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



def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    avatar_list = Profile.objects.all()
    return render(request, 'pages/category.html', {'category':category,
                                                    'avatar_list':avatar_list})



def like_post(request):
    user = request.user
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
                 
        else:
            like.value = 'Like'
            like.save()

    
    return redirect('pages:pages')
    