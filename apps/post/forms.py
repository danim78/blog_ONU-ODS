from django import forms
from django.core.validators import EMPTY_VALUES
from django.db.models import fields
from apps.post.models import Comentario, Post, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido', 'permitir_comentarios', 'categoria', 'imagen')
    
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select, empty_label="Seleccionar categoria")

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Escriba el titulo de su nuevo post aqui.', 'type' : 'text' , 'id' : 'titulo_msj'})
        self.fields["contenido"].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Escriba su nuevo post aqui.', 'type' : 'text' , 'id' : 'contenido_msj'})
        self.fields["permitir_comentarios"].widget.attrs.update({'class' : 'form-check form-switch form-check-input', 'type' : 'checkbox' , 'type' : 'checkbox' , 'id' : 'permitir_comentarios_msj'})
        self.fields["categoria"].widget.attrs.update({'select class':'form-select form-select'})
        self.fields["imagen"].widget.attrs.update({'class':'btn-sm'})

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
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select, required = False, empty_label="Seleccionar categoria")

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
        self.fields["mensaje"].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Escriba un nuevo comentario aqui.', 'type' : 'text'})