from django import forms
from .models import Page

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title','comment','tags']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Títle', 'class':'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder':'Comment', 'class':'form-control'}),
        }
        
