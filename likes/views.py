from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

import json

from pages.models import Page
from .models import Like


# Create your views here.
class LikeListView(ListView):
    model = Like


class LikeDetailView(DetailView):
    model = Like


@login_required(login_url='/user')  
def like_button(request, pk):
    user = request.user
    if request.method == 'POST':
        id = request.POST.get('pk', None)
        page = get_object_or_404(Page, pk=id)
        if page.likes.filter(id=user.id).exists():
            page.likes.remove(user)
            Like.objects.filter(user=user).delete()
        else:
            page.likes.add(user)
            print(pk)
            Like.objects.create(user=user, page=page, value="Like")

        
    context = {'likes_count': page.total_likes}
    return HttpResponse(json.dumps(context), content_type='application/json')
