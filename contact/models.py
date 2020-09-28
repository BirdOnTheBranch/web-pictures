from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendships'
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


# Add following field to User dynamically
User.add_to_class('following', models.ManyToManyField(
    'self', through=Contact, related_name='followers', symmetrical=False))
