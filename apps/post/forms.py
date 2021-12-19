from django import forms
from django.db.models import fields
from apps.post.models import Comentario, Post, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido', 'permitir_comentarios', 'categoria', 'imagen')

class BusquedaPost(forms.Form):
    titulo = forms.CharField(max_length=30, required = False)
    
    
    ORDER_OPCIONES = (
        ("titulo", "Titulo"),
        ("Fecha",(
            ("antiguo", "Antiguo"),
            ("nuevo", "Nuevo"))
        ))
    orden = forms.ChoiceField(choices=ORDER_OPCIONES, required = False, initial="nuevo")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select, required = False)

    def __init__(self, *args, **kwargs):
        super(BusquedaPost, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs["placeholder"] = " Titulo"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("mensaje",)
    
    # def __init__(self, *args, **kwargs):
    #     super(ComentarioForm, self).init(*args, **kwargs)
    #     self.fields["mensaje"].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Escriba su comentario', 'type' : 'text'})