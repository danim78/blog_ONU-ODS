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
from django.urls import path, include
# from apps.users.urls import urlUsers
# from prueba import views
# from post import views
# import post.views
# import usuario.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('', include('apps.post.urls')),
    # path('', views.hola_mundo),
    # path('', usuario.views.inicio, name = 'inicio'),
    # agregar usuario
    # path('usuario/nuevo', usuario.views.nuevo_usuario, name = 'agregar_usuario'),
    # path('user/', include('users.urls')),
]

# urlpatterns = [
#     path('index/', views.index, name='main-view'),
#     path('bio/<username>/', views.bio, name='bio'),
#     path('articles/<slug:title>/', views.article, name='article-detail'),
#     path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
#     path('blog/', include('blog.urls')),
#     ...
# ]