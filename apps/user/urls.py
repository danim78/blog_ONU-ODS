from django.urls import path
from apps.user import views    

urlpatterns = [    
    # inicio
    path('', views.inicio, name = 'inicio'),
    # agregar usuario
    path('usuario/nuevo', views.nuevo_usuario, name = 'agregar_usuario'),
]