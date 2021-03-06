import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from actions.utils import create_action
from common.decorators import ajax_required
from pages.models import Page

from .models import Like


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
            # Delete objecct in data base
            Like.objects.filter(user=user).delete()
        else:
            page.likes.add(user)
            # Create object in data base
            Like.objects.create(user=user, page=page, value="like")
            create_action(request.user, 'like', page)

    context = {'likes_count': page.total_likes}

    return HttpResponse(json.dumps(context), content_type='application/json')
