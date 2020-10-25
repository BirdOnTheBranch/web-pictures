from django.views.generic.list import ListView

from actions.models import Action


class ArtionListView(ListView):
    model = Action

    def get_context_data(self, *args, **kwargs):
        """Create dict context."""
        context = super().get_context_data(*args, **kwargs)
        actions = Action.objects.exclude(user=self.request.user)
        following_ids = self.request.user.following.values_list('id', flat=True)
        if following_ids:
            # If user is following others, retrieve only their actions
            actions = actions.filter(user_id__in=following_ids)
        context['actions'] = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
        return context
