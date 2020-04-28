from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed 


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField( auto_now_add=True)

    
    class Meta():
        ordering = ['-created']



class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='Threats')
    messages = models.ManyToManyField(Message)


def message_changed(sender, **kwargs):
    """This signal intercept the pk_set, to search in messages content 
    and delete they, if her author not a part of thread. 

    Arguments:
        sender {[<class 'django.db.models.base.ModelBase'>} -- Argument to pass parametters at signal  
    """
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)

    false_pk_set = set()
    if action is 'pre_add':
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print(f"Caution! {msg.user} is not a part of thread")
                false_pk_set.add(msg_pk)
                #Search messages in false_pk_set and if messages be in pk_set, is will delete they.
    pk_set.difference_update(false_pk_set)



m2m_changed.connect(message_changed, sender=Thread.messages.through)