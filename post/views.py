from django.shortcuts import HttpResponse ,render, redirect, Http404
from post.models import Post
from post.forms import PostForm

# Create your views here.

def agregar_post(request):
    template = 'agregar_post.html'
    
    formulario = PostForm(request.POST or None)
    if request.method == "POST":
        if formulario.is_valid():
            post = formulario.save()
            return redirect("listar_posts")

    contexto = {
        "formulario": formulario
    }

    return render(request, template, contexto)

def listar_posts(request):
    lista_posts = Post.objects.all()
    template = "listar_posts.html"
    contexto = {
        "lista_posts": lista_posts,
        #"formulario":formulario,
    }
    return render(request, template, contexto)

def ver_post(request, id):
    try:
        post = Post.objects.get(pk=id)
    except:
        raise Http404("no existe el post")

    contexto = {
        "post": post
    }
    template = "ver_post.html"
    return render(request, template, contexto)

def editar_post(request, id):
    post = Post.objects.get(pk=id)
    formulario = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if formulario.is_valid():
            post = formulario.save()
            return redirect("ver_post", post.id)

    template = "agregar_post.html"
    contexto = {
        "formulario":formulario
    }
    return render(request, template, contexto)

def borrar_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        post.delete()
        return redirect("listar_posts")
    
    template = "borrar_post.html"
    contexto = {"post" : post}

    return render(request, template, contexto)