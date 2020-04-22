from django import forms
from .models import Page

class PageForms(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title','comment','categories']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Títle'}),
            'comment': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Category'}),
        }
        labels = {
            'title':'', 'comment':'', 'categories':'',
        }
