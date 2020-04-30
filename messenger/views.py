from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Thread, Message


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ThreadTemplateView(TemplateView):
    template_name = "messenger/thread_list.html"


@method_decorator(login_required, name='dispatch')
class ThreadDetailView(DetailView):
    model = Thread

    def get_object(self):
        obj = super().get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj 

def add_message(request, pk):
    json_response = {'created':False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
    else:
        raise Http404('User is not authenticated') 

    return JsonResponse(json_response)
    
    