from django.urls import path
from apps.post import views
from apps.user import views as views_pro

urlpatterns = [
    #inicio
    path('', views.inicio, name = 'inicio'),
    #agregar post
    path('post/nuevo', views.agregar_post, name='agregar_post'),
    #path('post/nuevo', views.agregar_post, name = 'agregar_post'),
    #listar posts
    path('posts/', views.listar_posts, name = 'listar_posts'),
    #ver post
    path('post/<int:id>', views.ver_post, name = 'ver_post'),
    #editar post
    path('post/<int:id>/editar/', views.editar_post, name="editar_post"),
    #borrar post
    path('post/<int:id>/borrar/', views.borrar_post, name="borrar_post"),
    #agregar comentarios
    path('post/<int:id>/', views.comentar, name="comentar"),
    # ver perfil
    path("perfil/<int:id>", views_pro.perfil, name="perfil"),
]