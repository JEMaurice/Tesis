from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class ProveedorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.proveedor"

app_name = "proveedor_app"

urlpatterns = [

    path("contacto-proveedores-listar-todo/", views.ListAllContactoProveedores.as_view(), name = "contacto-proveedor"),
    path("contacto-proveedores-add/", views.CreateViewContactoProveedores.as_view(), name = "contacto-proveedor-add"),
    path("contacto-proveedores-update/<pk>/", views.UpdateViewContactoProveedores.as_view(), name = "contacto-proveedor-modificar"),
    path("contacto-proveedores-detalle/<pk>/", views.DetailsViewsContactoProveedores.as_view(), name = "contacto-proveedor-detalle"),
    path("contacto-proveedores-delete/<pk>/", views.DeleteViewContactoProveedores.as_view(), name = "contacto-proveedor-borrar"),


    path("proveedores-listar-todo/", views.ListAllProveedores.as_view(), name = "proveedores"),
    path("proveedores-add/", views.CreateViewProveedores.as_view(), name = "proveedores-add"),
    path("proveedores-update/<pk>/", views.UpdateViewProveedores.as_view(), name = "proveedores-modificar"),
    path("proveedores-detalle/<pk>/", views.DetailsViewsProveedores.as_view(), name = "proveedores-detalle"),
    path("proveedores-delete/<pk>/", views.DeleteViewProveedores.as_view(), name = "proveedores-borrar"),

]