"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from prueba import views
#from post import views
import post.views
import usuario.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.hola_mundo),
    path('', usuario.views.inicio, name = 'inicio'),
    #agregar post
    path('post/nuevo', post.views.agregar_post, name = 'agregar_post'),
    #listar posts
    path('posts/', post.views.listar_posts, name = 'listar_posts'),
    #ver post
    path('post/<int:id>', post.views.ver_post, name = 'ver_post'),
    #editar post
    path('post/<int:id>/editar/', post.views.editar_post, name="editar_post"),
    #borrar post
    path('post/<int:id>/borrar/', post.views.borrar_post, name="borrar_post"),
    #agregar usuario
    path('usuario/nuevo', usuario.views.nuevo_usuario, name = 'agregar_usuario'),
]