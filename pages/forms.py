from django import forms
from .models import Page

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title','comment','categories']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Títle', 'class':'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder':'Comment', 'class':'form-control'}),
            'categories': forms.NumberInput(attrs={'placeholder':'Category', 'class':'form-control'}),
        }
        