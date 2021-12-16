"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
# View
from apps.users import views

urlpatterns = [
    path(
        route='login',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='new_post/',
        view=TemplateView.as_view(template_name='templates/users/new_post.html'),
        name='new_post'
        ),
    path(
        route='registro',
        view=views.SignupView.as_view(),
        name='register'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='registro_completado/',
        view=TemplateView.as_view(template_name='templates/users/registerok.html'),
        name='registerok'
    ),
    path("logout/", LogoutView.as_view(), name="logout")
]
