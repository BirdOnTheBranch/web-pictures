from django import forms

from .models import Page


class PageForms(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'comment', 'tags', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Títle', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Comment', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'placeholder': 'image', 'class': 'form-control'}),
        }
