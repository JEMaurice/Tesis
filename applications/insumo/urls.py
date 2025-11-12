from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class InsumoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.insumo"

app_name = "insumo_app"

urlpatterns = [

    path("tipounidad-listar-todo/", views.ListAlltipounidad.as_view(), name = "tipo-unidad"),
    path("tipounidad-add/", views.CreateViewtipounidad.as_view(), name = "tipo-unidad-add"),
    path("tipounidad-update/<pk>/", views.UpdateViewtipounidad.as_view(), name = "tipo-unidad-modificar"),
    path("tipounidad-detalle/<pk>/", views.DetailsViewstipounidad.as_view(), name = "tipo-unidad-detalle"),
    path("tipounidad-delete/<pk>/", views.DeleteViewtipounidad.as_view(), name = "tipo-unidad-borrar"),


    path("tipoinsumo-listar-todo/", views.ListAlltipoinsumo.as_view(), name = "tipo-insumo"),
    path("tipoinsumo-add/", views.CreateViewtipoinsumo.as_view(), name = "tipo-insumo-add"),
    path("tipoinsumo-update/<pk>/", views.UpdateViewtipoinsumo.as_view(), name = "tipo-insumo-modificar"),
    path("tipoinsumo-detalle/<pk>/", views.DetailsViewstipoinsumo.as_view(), name = "tipo-insumo-detalle"),
    path("tipoinsumo-delete/<pk>/", views.DeleteViewtipoinsumo.as_view(), name = "tipo-insumo-borrar"),


    path("tipocolor-listar-todo/", views.ListAlltipocolor.as_view(), name = "tipo-color"),
    path("tipocolor-add/", views.CreateViewtipocolor.as_view(), name = "tipo-color-add"),
    path("tipocolor-update/<pk>/", views.UpdateViewtipocolor.as_view(), name = "tipo-color-modificar"),
    path("tipocolor-detalle/<pk>/", views.DetailsViewstipocolor.as_view(), name = "tipo-color-detalle"),
    path("tipocolor-delete/<pk>/", views.DeleteViewtipocolor.as_view(), name = "tipo-color-borrar"),


    path("insumo-listar-todo/", views.ListAllinsumo.as_view(), name = "insumo"),
    path("insumo-add/", views.CreateViewinsumo.as_view(), name = "insumo-add"),
    path("insumo-update/<pk>/", views.UpdateViewinsumo.as_view(), name = "insumo-modificar"),
    path("insumo-detalle/<pk>/", views.DetailsViewsinsumo.as_view(), name = "insumo-detalle"),
    path("insumo-delete/<pk>/", views.DeleteViewinsumo.as_view(), name = "insumo-borrar"),

]