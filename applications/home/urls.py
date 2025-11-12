from django.urls import path
from . import views
from .views import CustomLoginView
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.home"

app_name = "home_app"

urlpatterns = [

    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('home/', views.Viewhome.as_view(), name = 'home'),
    path('funciones/', views.Viewfunciones.as_view(), name = 'funciones'),
    path('perfil/', views.Viewperfil.as_view(), name = 'perfil'),
    path('perfil_editar/<int:pk>/', views.UpdateViewPerfil.as_view(), name = 'perfil_editar'),

    path('calculador/', views.calculador, name = 'calculador'),
    path('obtener_datos/', views.obtener_datos, name='obtener_datos'),

]