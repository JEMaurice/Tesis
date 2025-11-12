from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from test_project.decorador_personalizado import active_superuser_required


from .models import Nombre_Sector
from .forms import FormNombresector



@method_decorator(active_superuser_required, name='dispatch')
class ListAllNombreSector(ListView):
    template_name = "sector/nombre-sector/nombre-sector.html"
    paginate_by = 4
    ordering = "id"
    model = Nombre_Sector
    context_object_name = "nombresector"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")

        queryset = Nombre_Sector.objects
        
        if letter:
            queryset = queryset.filter(nombre__istartswith=letter)
        else:
            queryset = queryset.filter(nombre__icontains=palabra_clave)

        return queryset


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewNombreSector(CreateView):
    model = Nombre_Sector
    template_name = "sector/nombre-sector/nombre-sector-add.html"
    form_class= FormNombresector
    success_url = reverse_lazy("sector_app:nombre-sector")

    def form_valid(self, form):
        messages.success(self.request, 'NOMBRE DEL SECTOR CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewNombreSector(UpdateView):
    model = Nombre_Sector
    template_name = "sector/nombre-sector/nombre-sector-update.html"
    form_class= FormNombresector
    success_url = reverse_lazy("sector_app:nombre-sector")

    def get_object(self, queryset=None):
        nombre_sector = super().get_object(queryset)
        if nombre_sector.id < 7:
            raise PermissionDenied("No se permite modificar este nombre sector.")
        return nombre_sector

    def form_valid(self, form):
        messages.success(self.request, 'NOMBRE DEL SECTOR ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsNombreSector(DetailView): 
    model = Nombre_Sector                  
    template_name = "sector/nombre-sector/nombre-sector-detalle.html"
    context_object_name = "nombresector"

    def get_object(self, queryset=None):
        nombre_sector = super().get_object(queryset)
        if nombre_sector.id < 7:
            raise PermissionDenied("No se permite ver este nombre sector.")
        return nombre_sector


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewNombreSector(DeleteView):
    model = Nombre_Sector
    template_name = "sector/nombre-sector/nombre-sector-delete.html"
    form_class= FormNombresector
    success_url = reverse_lazy("sector_app:nombre-sector")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        nombre_sector = super().get_object(queryset)
        if nombre_sector.id < 7:
            raise PermissionDenied("No se permite eliminar este nombre sector.")
        return nombre_sector

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'NOMBRE DEL SECTOR BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)