from django.urls import path
from . import views
from django.apps import AppConfig

""" LAS PAGINAS QUE POSEE EL PROYECTO """

class MensajeriaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.mensajeria"

app_name = "mensajeria_app"

urlpatterns = [

    path("sala-listar-todo/", views.ListAllSala.as_view(), name = "sala"),
    path("sala-add/", views.CreateViewSala.as_view(), name = "sala-add"),
    path("sala-update/<pk>/", views.UpdateViewSala.as_view(), name = "sala-modificar"),
    path("sala-detalle/<pk>/", views.DetailsViewsSala.as_view(), name = "sala-detalle"),
    path("sala-delete/<pk>/", views.DeleteViewSala.as_view(), name = "sala-borrar"),


    path('mensajeria/', views.home, name = 'mensajeria'),
    path('room/<int:room_id>/', views.room, name = 'room'),


    path('api/get-messages/<int:room_id>/', views.get_messages, name='get_messages'),
    
    ]