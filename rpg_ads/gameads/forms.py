from django import forms
from .models import Ad, Reply

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'content', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
