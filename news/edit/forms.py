from django import forms
from django.utils.text import slugify
from .models import News

class NewsForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = News
        fields = ['title', 'image', 'content', 'category', 'slug']
        widgets = {
            'image': forms.FileInput(attrs={'required': False}),
            'title': forms.TextInput(attrs={'class': 'title-input'}),
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
