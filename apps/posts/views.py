from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.posts.models import Post
from apps.posts.forms import PostForm
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    num_pagina = request.GET.get('page')
    pagina_actual = paginator.get_page(num_pagina)
    return render(request, 'index.html', {'posts': pagina_actual})



@login_required(login_url='login')
def crearPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'creacion.html', {'form':form})



def registrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})



def verPost(request, pk):
    post = get_object_or_404(Post, id=pk)
    tieneLike = request.user in post.likes.all()
    return render(request, 'post.html', {'post': post, 'likes': post.cantidad_likes(), 'tiene_like': tieneLike})



@login_required(login_url='login')
def actualizarPost(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user == post.autor:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post.save()
                return redirect('index')
        else:
            form = PostForm(instance=post)
            return render(request, 'creacion.html', {'form':form})
    else:
        return redirect(f'/post/{post.id}')



@login_required(login_url='login')
def eliminarPost(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.autor == request.user:
        if request.method == 'POST':
            post.delete()
            return redirect('index')
        return render(request, 'eliminar.html', {'post':post})
    else:
        return redirect(f'/post/{post.id}')


    return render(request, 'eliminar.html', {'post':post})



@login_required(login_url='login')
def darLike(request, pk):
    if request.method == 'POST':        
        post = get_object_or_404(Post, id=pk)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect('/post/'+str(post.id))
    else:
        raise Http404()