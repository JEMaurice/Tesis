from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class ClienteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.cliente"

app_name = "cliente_app"

urlpatterns = [

    path("cliente-listar-todo/", views.ListAllCliente.as_view(), name = "cliente"),
    path("cliente-add/", views.CreateViewCliente.as_view(), name = "cliente-add"),
    path("cliente-update/<pk>/", views.UpdateViewCliente.as_view(), name = "cliente-modificar"),
    path("cliente-detalle/<pk>/", views.DetailsViewsCliente.as_view(), name = "cliente-detalle"),
    path("cliente-delete/<pk>/", views.DeleteViewCliente.as_view(), name = "cliente-borrar"),


    path("contacto-cliente-listar-todo/", views.ListAllContactoCliente.as_view(), name = "contacto-cliente"),
    path("contacto-cliente-add/", views.CreateViewContactoCliente.as_view(), name = "contacto-cliente-add"),
    path("contacto-cliente-update/<pk>/", views.UpdateViewContactoCliente.as_view(), name = "contacto-cliente-modificar"),
    path("contacto-cliente-detalle/<pk>/", views.DetailsViewsContactoCliente.as_view(), name= "contacto-cliente-detalle"),
    path("contacto-cliente-delete/<pk>/", views.DeleteViewContactoCliente.as_view(), name = "contacto-cliente-borrar"),

]