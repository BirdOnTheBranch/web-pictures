from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django import forms

from .models import Profile
from .forms import UCFWithEmail, ProfileForm, EmailForm


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
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Password enter'})
        form.fields['password2'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Password confirm'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = "registration/profile_form.html"

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'username': self.request.user})

    def get_object(self):
        """Recover the object that will be editable."""
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    template_name = "registration/profile_email_form.html"

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'username': self.request.user})

    def get_object(self):
        """Recover the user."""
        return self.request.user

    def get_form(self, form_class=None):
        """Modified form in real time."""
        form = super().get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        return form
