from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse 
from django import forms
from django.http import HttpResponseRedirect

from .models import Profile, Friendship
from .forms import UCFWithEmail, ProfileForm, EmailForm
from django.contrib.auth.models import User



class SignUpView(CreateView):
    """Create view for register user whit generic form"""
    form_class = UCFWithEmail
    template_name = "registration/signup.html"

    def get_success_url(self):
        """Add parameter to url"""
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        """Modified form in real time."""
        form = super().get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Password enter'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Password confirm'})  
        return form



@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = "registration/profile_form.html"

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'username': self.request.user } )

    def get_object(self):
        """Retrieve the object that will be editable."""
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    template_name = "registration/profile_email_form.html"

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'username': self.request.user } )

    def get_object(self):
        """Retrieve the user."""
        return self.request.user

    def get_form(self, form_class=None):
        """Modified form in real time."""
        form = super().get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        return form
        
        
def add_friend(request, username):
    if request.user.is_authenticated and request.user != username:
        friendUser = User.objects.get(username=username)
        friendProfile = User.objects.get(username=friendUser)
        myProfile = User.objects.get(username=request.user)
        model = Friendship.objects.filter(creator=myProfile)
        if model:
            print(f'{myProfile}'+"is in your friend's list")
        else:
            model = Friendship.objects.create(creator=myProfile, following=friendProfile)
            print(model)
            model.save()
        
    return HttpResponseRedirect(reverse_lazy('profiles:detail', kwargs={'username': friendUser }))


def delete_friend(request, username):
    if request.user.is_authenticated and request.user != username:
        friendUser = User.objects.get(username=username)
        friendProfile = User.objects.get(username=friendUser)
        myProfile = User.objects.get(username=request.user)
        Friendship.objects.filter(creator=myProfile, following=friendProfile).delete()        
        
    return HttpResponseRedirect(reverse_lazy('profiles:detail', kwargs={'username': friendUser}))


def is_friend(user1, user2):
    user1 = User.objects.get(username=user1)
    user2 = User.objects.get(username=user2)
    friends = Friendship.objects.filter(creator=user1, following=user2)
    if (friends):
        return True
    else:
        return False


def get_friends(request, username):
    if request.user.is_authenticated:
        friendUser = User.objects.get(username=username)
        friends = Friendship.objects.filter(creator=friendUser)
        return friends
    
    return HttpResponseRedirect(reverse_lazy('pages:pages'))
