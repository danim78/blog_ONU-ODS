from django.db import models
from django.contrib.auth.models import User
#from usuario.models import Perfil

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="post/", null = True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE,default=1)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null=True)
    permitir_comentarios = models.BooleanField(default = True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User, on_delete= models.CASCADE,default=1)
    post = models.ForeignKey(Post, on_delete= models.CASCADE,default=1)

    def __str__(self):
        return self.mensaje