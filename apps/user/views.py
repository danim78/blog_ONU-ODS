from django.shortcuts import render, redirect
from apps.user.models import Usuario
from apps.user.forms import UsuarioForm

# Create your views here.

def inicio(request):
    return render(request, "index.html", {})


def nuevo_usuario(request):
    template = 'user/agregar_usuario.html'
    
    formulario = UsuarioForm(request.POST or None)
    if request.method == "POST":
        if formulario.is_valid():
            usuario = formulario.save()
            return redirect("listar_posts")

    contexto = {
        "formulario": formulario
    }

    return render(request, template, contexto)
