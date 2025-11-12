from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class UsuarioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.usuario"

app_name = "usuario_app"

urlpatterns = [

    path("usuarios-listar-todo/", views.ListAllUsuarios.as_view(), name = "usuario"),
    path("usuarios-add/", views.CreateViewUsuarios.as_view(), name = "usuario-add"),
    path("usuarios-update/<pk>/", views.UpdateViewUsuarios.as_view(), name = "usuario-modificar"),
    path("usuarios-detalle/<pk>/", views.DetailsViewsUsuarios.as_view(), name = "usuario-detalle"),
    path("usuarios-delete/<pk>/", views.DeleteViewUsuarios.as_view(), name = "usuario-borrar"),

]