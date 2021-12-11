from django.shortcuts import HttpResponse ,render, redirect
from post.models import Post
from post.forms import PostForm

# Create your views here.

def agregar_post(request):
    template = 'agregar_post.html'
    
    formulario = PostForm(request.POST or None)
    if request.method == "POST":
        if formulario.is_valid():
            post = formulario.save()
            #return redirect("ver_dpto", dpto.id)

    contexto = {
        "formulario": formulario
    }

    return render(request, template, contexto)