from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class SectorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.sector"

app_name = "sector_app"

urlpatterns = [

    path("nombre-sector-listar-todo/", views.ListAllNombreSector.as_view(), name = "nombre-sector"),
    path("nombre-sector-add/", views.CreateViewNombreSector.as_view(), name = "nombre-sector-add"),
    path("nombre-sector-update/<pk>/", views.UpdateViewNombreSector.as_view(), name = "nombre-sector-modificar"),
    path("nombre-sector-detalle/<pk>/", views.DetailsViewsNombreSector.as_view(), name = "nombre-sector-detalle"),
    path("nombre-sector-delete/<pk>/", views.DeleteViewNombreSector.as_view(), name = "nombre-sector-borrar"), 

]