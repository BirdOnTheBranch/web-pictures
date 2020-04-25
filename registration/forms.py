from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


# Extend original form
class UCFWithEmail(UserCreationForm):
    """Add email field to UserCreationForm."""
    email = forms.EmailField(required=True,)

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        """Return help text None"""
        super().__init__(*args, **kwargs)

        for fieldname in ['username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        """Recover email field, and check not exist in database."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        return email


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatar','bio']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control mt-3'}),
            'bio': forms.Textarea(attrs={'placeholder':'Biografia', 'class':'form-control'}),
        }


        