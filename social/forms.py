from django import forms
from .models import Like, Follow

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['post']
        widgets = {
            'post': forms.HiddenInput(),
        }

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ['following']
        widgets = {
            'following': forms.HiddenInput(),
        }