from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



def custom_upload_to(instance, filename):
    """Delete old file image in media repository."""
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename
    


class Profile(models.Model):
    user    =   models.OneToOneField(User, on_delete=models.CASCADE)
    avatar  =   models.ImageField(upload_to=custom_upload_to, null=True, blank=True )
    bio     =   models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    def __str__(self):
        return self.user.username
        

class Friendship(models.Model):
    creator     =   models.ForeignKey(User, related_name="friendship_creator_set", on_delete=models.CASCADE)
    following   =   models.ForeignKey(User, related_name="friend_set", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendships'
    
    def __str__(self):
        return f'{self.creator.username}'+' is friend '+f'{self.following.username}'


#signal
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """Created a user and their linked profile"""
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        