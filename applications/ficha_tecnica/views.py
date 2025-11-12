from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from test_project.decorador_personalizado import active_superuser_required, staff_active_required


from .models import FichaTecnica
from .forms import Formfichatecnica, Formupdatefichatecnica




@method_decorator(active_superuser_required, name='dispatch')
class ListAllfichatecnica(ListView):
    template_name = "ficha_tecnica/fichatecnica/fichatecnica.html"
    paginate_by = 4
    ordering = "id"
    model = FichaTecnica
    context_object_name = "fichatecnica"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
    
        
        if letter:
            return FichaTecnica.objects.filter(
                Q(codigo__istartswith=letter) |
                Q(cliente__razon_social__istartswith=letter))
        else:
            return FichaTecnica.objects.filter(
                Q(codigo__icontains=palabra_clave) |
                Q(cliente__razon_social__icontains=palabra_clave))


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewfichatecnica(CreateView):
    model = FichaTecnica
    template_name = "ficha_tecnica/fichatecnica/fichatecnica-add.html"
    form_class = Formfichatecnica
    success_url = reverse_lazy("ficha_tecnica_app:ficha-tecnica")

    def form_valid(self, form):
        messages.success(self.request, 'FICHA TECNICA CREADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewfichatecnica(UpdateView):
    model = FichaTecnica
    template_name = "ficha_tecnica/fichatecnica/fichatecnica-update.html"
    form_class = Formupdatefichatecnica
    success_url = reverse_lazy("ficha_tecnica_app:ficha-tecnica")

    def form_valid(self, form):
        messages.success(self.request, 'FICHA TECNICA ACTUALIZADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsfichatecnica(DetailView): 
    model = FichaTecnica                  
    template_name = "ficha_tecnica/fichatecnica/fichatecnica-detalle.html"
    context_object_name = "fichatecnica"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewfichatecnica(DeleteView):
    model = FichaTecnica
    template_name = "ficha_tecnica/fichatecnica/fichatecnica-delete.html"
    form_class = Formfichatecnica
    success_url = reverse_lazy("ficha_tecnica_app:ficha-tecnica")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'FICHA TECNICA BORRADA EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)




@method_decorator(staff_active_required, name='dispatch')
class Viewfichatecnicavista(TemplateView):
    template_name = 'ficha_tecnica/fichatecnica/fichatecnica-vista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtrar los objetos FichaTecnica por estado activo
        context['fichatecnica'] = FichaTecnica.objects.filter(estado__id=1)
        return context


@method_decorator(staff_active_required, name='dispatch')
class DetallePersonalizadoViewsfichatecnica(DetailView): 
    model = FichaTecnica                  
    template_name = "ficha_tecnica/fichatecnica/fichatecnica-detalle-personalizado.html"
    context_object_name = "fichatecnica"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_sectors'] = self.request.user.sector_asignado.all()
        return context