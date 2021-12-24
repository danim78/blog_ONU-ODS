from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from django import forms
from django.core.files.images import get_image_dimensions
from apps.user.models import Perfil

class NuevoUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = "username","first_name","last_name","password1","password2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = "Ayuda para el campo username"
        self.fields["username"].widget.attrs.update({"class":"form-control"})

class EditarUsuarioForm(UserChangeForm):
    class Meta:
        model = User
        fields = "username","first_name","last_name"

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('img_perfil',)

    def clean_img_perfil(self):
            img_perfil = self.cleaned_data["img_perfil"]

            try:
                w, h = get_image_dimensions(img_perfil)

                #validate dimensions
                max_width = max_height = 315
                if w > max_width or h > max_height:
                    raise forms.ValidationError(
                        u'Please use an image that is '
                        '%s x %s pixels or smaller.' % (max_width, max_height))

                #validate content type
                main, sub = img_perfil.content_type.split('/')
                if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                    raise forms.ValidationError(u'Please use a JPEG, '
                        'GIF or PNG image.')

                #validate file size
                if len(img_perfil) > (20 * 1024):
                    raise forms.ValidationError(
                        u'Avatar file size may not exceed 20k.')

            except AttributeError:
                """
                Handles case when we are updating the user profile
                and do not supply a new avatar
                """
                pass

            return img_perfil