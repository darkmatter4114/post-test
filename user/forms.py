from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML

from post.models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text', 'published_date', 'image']

        def __init__(self, *args, **kwargs):
            super(Post, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_tag = False
            self.helper.disable_csrf = True
            self.helper.layout = Layout(
                'title',
                'description',
                'imagefile',
                HTML(
                    """{% if form.imagefile.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.imagefile.value }}">{% endif %}""", ),
                'flag_featured',
            )

    class NoticeImageForm(forms.Form):
        image = forms.ImageField(required=True)