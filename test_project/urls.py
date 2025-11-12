from django.contrib import admin #Trae las plantillas de admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('', include('applications.cliente.urls')),
    path('', include('applications.ficha_tecnica.urls')),
    path('', include('applications.insumo.urls')),
    path('', include('applications.prototipo.urls')),
    path('', include('applications.proveedor.urls')),
    path('', include('applications.sector.urls')),
    path('', include('applications.usuario.urls')),
    path('', include('applications.mensajeria.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
