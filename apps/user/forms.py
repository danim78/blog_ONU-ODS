from django import forms
from django.db.models import fields
from django.contrib.auth.models import User
from apps.user.models import Usuario

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = '__all__'