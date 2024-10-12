from django import forms
from .models import Post, Like, Follow, Comment

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
        

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["title", "description"]
        

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "pic"]
        

class DeletePostForm(forms.Form):
    confirm = forms.BooleanField(widget=forms.HiddenInput, initial=True)
