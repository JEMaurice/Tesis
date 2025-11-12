from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class FichatecnicaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.ficha_tecnica"

app_name = "ficha_tecnica_app"

urlpatterns = [

    path("fichatecnica-listar-todo/", views.ListAllfichatecnica.as_view(), name = "ficha-tecnica"),
    path("fichatecnica-add/", views.CreateViewfichatecnica.as_view(), name = "ficha-tecnica-add"),
    path("fichatecnica-update/<pk>/", views.UpdateViewfichatecnica.as_view(), name = "ficha-tecnica-modificar"),
    path("fichatecnica-detalle/<pk>/", views.DetailsViewsfichatecnica.as_view(), name = "ficha-tecnica-detalle"),
    path("fichatecnica-delete/<pk>/", views.DeleteViewfichatecnica.as_view(), name = "ficha-tecnica-borrar"),


    path('ficha-tecnica-vista/', views.Viewfichatecnicavista.as_view(), name = 'ficha-tecnica-vista'),
    path("fichatecnica-detalle-pers/<pk>/", views.DetallePersonalizadoViewsfichatecnica.as_view(), name = "ficha-tecnica-detalle-personalizado"),

]