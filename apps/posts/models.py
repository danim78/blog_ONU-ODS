from django.db import models
from django.contrib.auth.models import User
#from usuario.models import Perfil


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="media/", default='imagen')
    likes = models.ManyToManyField(User, related_name='post_likes')


    def cantidad_likes(self):
        return self.likes.count()