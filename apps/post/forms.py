from django import forms
from django.core.validators import EMPTY_VALUES
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
        ("comentarios", "Comentarios"),
        ("Fecha",(
            ("antiguo", "Antiguo"),
            ("nuevo", "Nuevo"))
        ))
        
    orden = forms.ChoiceField(choices=ORDER_OPCIONES, widget=forms.Select, required = False, initial="titulo")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select, required = False, empty_label="Categoria")

    def __init__(self, *args, **kwargs):
        super(BusquedaPost, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({'class':'form-control form-control-lg', 'placeholder':' Titulo', 'type':'text'})
        self.fields["orden"].widget.attrs.update({'select class':'form-select form-select-lg'})
        self.fields["categoria"].widget.attrs.update({ 'select class':'form-select form-select-lg'})

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("mensaje",)
    
    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields["mensaje"].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Escriba su comentario', 'type' : 'text'})