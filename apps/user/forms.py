from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets

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
        fields = "username","first_name","last_name",