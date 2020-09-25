from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json

from pages.models import Page
from registration.models import Profile
from actions.utils import create_action
from common.decorators import ajax_required
from .models import Like



@method_decorator(login_required, name='dispatch')
class LikeListView(ListView):
    model = Like

    def get_context_data(self, *args, **kwargs):
        """Create dict context."""
        context = super().get_context_data(*args, **kwargs)
        context['profile_list'] = Profile.objects.all()
        return context 


@method_decorator(login_required, name='dispatch')
class LikeDetailView(DetailView):
    model = Like


@ajax_required
@login_required(login_url='/user')  
def like_button(request, pk):
    "Save user whit page's like and send to Ajax"
    user = request.user

    if request.method == 'POST':
        id = request.POST.get('pk', None)
        page = get_object_or_404(Page, pk=id)

        if page.likes.filter(id=user.id).exists():
            page.likes.remove(user)
            #Delete objecct in data base
            Like.objects.filter(user=user).delete()
        else:
            page.likes.add(user)
            #Create object in data base
            Like.objects.create(user=user, page=page, value="like")
            create_action(request.user, 'like', page)

    context = {'likes_count': page.total_likes}

    return HttpResponse(json.dumps(context), content_type='application/json')
