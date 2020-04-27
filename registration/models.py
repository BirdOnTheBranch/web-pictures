from django.db import models
from django.contrib.auth.models import User



def custom_upload_to(instance, filename):
    """Delete old file image in media repository."""
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True )
    bio = models.TextField(null=True, blank=True)

