from django.forms import ModelForm
from apps.posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'descripcion', 'imagen')

