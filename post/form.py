from django import forms
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_date', 'published_date', 'update_date', 'image', 'tags']


class PostImageForm(forms.Form):
    image = forms.ImageField(required=True)

