from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class PrototipoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.prototipo"

app_name = "prototipo_app"

urlpatterns = [

    path("piezas-listar-todo/", views.ListAllpiezas.as_view(), name = "piezas"),
    path("piezas-add/", views.CreateViewpiezas.as_view(), name = "piezas-add"),
    path("piezas-update/<pk>/", views.UpdateViewpiezas.as_view(), name = "piezas-modificar"),
    path("piezas-detalle/<pk>/", views.DetailsViewspiezas.as_view(), name = "piezas-detalle"),
    path("piezas-delete/<pk>/", views.DeleteViewpiezas.as_view(), name = "piezas-borrar"),


    path("piezaprototipo-listar-todo/", views.ListAllpiezaprototipo.as_view(), name = "pieza-prototipo"),
    path("piezaprototipo-add/", views.CreateViewpiezaprototipo.as_view(), name = "pieza-prototipo-add"),
    path("piezaprototipo-update/<pk>/", views.UpdateViewpiezaprototipo.as_view(), name = "pieza-prototipo-modificar"),
    path("piezaprototipo-detalle/<pk>/", views.DetailsViewspiezaprototipo.as_view(), name = "pieza-prototipo-detalle"),
    path("piezaprototipo-delete/<pk>/", views.DeleteViewpiezaprototipo.as_view(), name = "pieza-prototipo-borrar"),


    path("nombreprototipo-listar-todo/", views.ListAllnombreprototipo.as_view(), name = "nombre-prototipo"),
    path("nombreprototipo-add/", views.CreateViewnombreprototipo.as_view(), name = "nombre-prototipo-add"),
    path("nombreprototipo-update/<pk>/", views.UpdateViewnombreprototipo.as_view(), name = "nombre-prototipo-modificar"),
    path("nombreprototipo-detalle/<pk>/", views.DetailsViewsnombreprototipo.as_view(), name = "nombre-prototipo-detalle"),
    path("nombreprototipo-delete/<pk>/", views.DeleteViewnombreprototipo.as_view(), name = "nombre-prototipo-borrar"),


    path("prototipo-listar-todo/", views.ListAllPrototipo.as_view(), name = "prototipo"),
    path("prototipo-add/", views.CreateViewprototipo.as_view(), name = "prototipo-add"),
    path("prototipo-update/<pk>/", views.UpdateViewprototipo.as_view(), name = "prototipo-modificar"),
    path("prototipo-detalle/<pk>/", views.DetailsViewsprototipo.as_view(), name = "prototipo-detalle"),
    path("prototipo-delete/<pk>/", views.DeleteViewprototipo.as_view(), name = "prototipo-borrar"),

]