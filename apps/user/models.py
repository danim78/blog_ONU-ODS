from django.db import models
#from django.contrib.auth.models import User

#Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length=50)
    usuario = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    contraseña = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="perfil", null=True, blank=True)
    #seguidos = models.ManyToManyField("Perfil", blank=True, related_name="seguidores")

    def __str__(self):
        return self.usuario