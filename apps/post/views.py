from django.shortcuts import HttpResponse ,render, redirect, Http404
from django.contrib.auth.decorators import login_required
from apps.post.models import Post
from apps.post.forms import PostForm, BusquedaPost

# Create your views here.

#def agregar_post(request):

 #   if not request.user.is_authenticated:
 #       return redirect("login")

 #   template = 'post/agregar_post.html'

    
 #   formulario = PostForm(request.POST, request.FILES  or None)
 #   if request.method == "POST":
 #       if formulario.is_valid():
 #           post = formulario.save()
 #           return redirect("listar_posts")

 #   contexto = {
 #       "formulario": formulario
 #   }

 #   return render(request, template, contexto)

@login_required(login_url='login')
def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'post/agregar_post.html', {'form':form})


def listar_posts(request):

    search_form = BusquedaPost(request.GET or None)
    if search_form.is_valid():
        filtro_titulo = request.GET.get("titulo", "")
        orden_post = request.GET.get("orden", None)
        #param_categorias = request.GET.getlist("categoria")

        posts = Post.objects.filter(titulo__icontains = filtro_titulo)

        #if param_categorias:
        #    posts = posts.filter(categoria__id__in = param_categorias)
        if orden_post == "titulo":
            posts= posts.order_by("titulo")
        elif orden_post == "antiguo":
            posts= posts.order_by("fecha_creado")
        elif orden_post == "nuevo":
            posts= posts.order_by("-fecha_creado")
    else:
        posts = Post.objects.all()

    contexto = {"lista_posts":posts,
                "search_form":search_form,
                }

    template = "post/listar_posts.html"

    return render(request, template ,contexto)


#def listar_posts(request):
#    lista_posts = Post.objects.all()
#    template = "listar_posts.html"
#    contexto = {
#        "lista_posts": lista_posts,
#        #"formulario":formulario,
#    }
#    return render(request, template, contexto)

def ver_post(request, id):
    try:
        post = Post.objects.get(pk=id)
    except:
        raise Http404("no existe el post")

    contexto = {
        "post": post
    }

    template = "post/ver_post.html"

    return render(request, template, contexto)

def editar_post(request, id):
    post = Post.objects.get(pk=id)
    formulario = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if formulario.is_valid():
            post = formulario.save()
            return redirect("ver_post", post.id)


    template = "post/agregar_post.html"

    contexto = {
        "formulario":formulario
    }
    return render(request, template, contexto)

def borrar_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        post.delete()
        return redirect("listar_posts")
    

    template = "post/borrar_post.html"

    contexto = {"post" : post}

    return render(request, template, contexto)