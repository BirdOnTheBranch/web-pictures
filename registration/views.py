from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from django import forms

from .models import Profile
from .forms import UCFWithEmail, ProfileForm


#create your views here.
class SignUpView(CreateView):
    """Create view for register user whit generic form"""
    form_class = UCFWithEmail
    template_name = "registration/signup.html"

    def get_success_url(self):
        """Add parameter in url"""
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
    success_url = reverse_lazy('profile')

    def get_object(self):
        """Retrieve the object that will be editable."""
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile