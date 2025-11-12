from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.utils.decorators import method_decorator
from test_project.decorador_personalizado import active_superuser_required


from .models import Tipo_Color, Tipo_Insumo, Insumo, TipoUnidad
from .forms import FormTipounidad, FormTipoinsumo, FormTipocolor, FormInsumo




@method_decorator(active_superuser_required, name='dispatch')
class ListAlltipounidad(ListView):
    template_name = "insumo/tipounidad/tipounidad.html"
    paginate_by = 4
    ordering = "id"
    model = TipoUnidad
    context_object_name = "tipounidad"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return TipoUnidad.objects.filter(nombre__istartswith=letter)
        else:
            return TipoUnidad.objects.filter(nombre__icontains=palabra_clave) 


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewtipounidad(CreateView):
    model = TipoUnidad
    template_name = "insumo/tipounidad/tipounidad-add.html"
    form_class = FormTipounidad
    success_url = reverse_lazy("insumo_app:tipo-unidad")

    def form_valid(self, form):
        messages.success(self.request, 'TIPO DE UNIDAD CREADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewtipounidad(UpdateView):
    model = TipoUnidad
    template_name = "insumo/tipounidad/tipounidad-update.html"
    form_class = FormTipounidad
    success_url = reverse_lazy("insumo_app:tipo-unidad")

    def form_valid(self, form):
        messages.success(self.request, 'TIPO DE UNIDAD ACTUALIZADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewstipounidad(DetailView): 
    model = TipoUnidad                  
    template_name = "insumo/tipounidad/tipounidad-detalle.html"
    context_object_name = "tipounidad"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewtipounidad(DeleteView):
    model = TipoUnidad
    template_name = "insumo/tipounidad/tipounidad-delete.html"
    form_class = FormTipounidad
    success_url = reverse_lazy("insumo_app:tipo-unidad")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'TIPO DE UNIDAD BORRADA EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAlltipoinsumo(ListView):
    template_name = "insumo/tipoinsumo/tipoinsumo.html"
    paginate_by = 4
    ordering = "id"
    model = Tipo_Insumo
    context_object_name = "tipoinsumo"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Tipo_Insumo.objects.filter(nombre__istartswith=letter)
        else:
            return Tipo_Insumo.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewtipoinsumo(CreateView):
    model = Tipo_Insumo
    template_name = "insumo/tipoinsumo/tipoinsumo-add.html"
    form_class = FormTipoinsumo
    success_url = reverse_lazy("insumo_app:tipo-insumo")

    def form_valid(self, form):
        messages.success(self.request, 'TIPO DE INSUMO CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewtipoinsumo(UpdateView):
    model = Tipo_Insumo
    template_name = "insumo/tipoinsumo/tipoinsumo-update.html"
    form_class = FormTipoinsumo
    success_url = reverse_lazy("insumo_app:tipo-insumo")

    def form_valid(self, form):
        messages.success(self.request, 'TIPO DE INSUMO ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewstipoinsumo(DetailView): 
    model = Tipo_Insumo                  
    template_name = "insumo/tipoinsumo/tipoinsumo-detalle.html"
    context_object_name = "tipoinsumo"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewtipoinsumo(DeleteView):
    model = Tipo_Insumo
    template_name = "insumo/tipoinsumo/tipoinsumo-delete.html"
    form_class = FormTipoinsumo
    success_url = reverse_lazy("insumo_app:tipo-insumo")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'TIPO DE INSUMO BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAlltipocolor(ListView):
    template_name = "insumo/tipocolor/tipocolor.html"
    paginate_by = 4
    ordering = "id"
    model = Tipo_Color
    context_object_name = "tipocolor"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Tipo_Color.objects.filter(nombre__istartswith=letter)
        else:
            return Tipo_Color.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewtipocolor(CreateView):
    model = Tipo_Color
    template_name = "insumo/tipocolor/tipocolor-add.html"
    form_class = FormTipocolor
    success_url = reverse_lazy("insumo_app:tipo-color")

    def form_valid(self, form):
        messages.success(self.request, 'TIPO DE COLOR CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewtipocolor(UpdateView):
    model = Tipo_Color
    template_name = "insumo/tipocolor/tipocolor-update.html"
    form_class = FormTipocolor
    success_url = reverse_lazy("insumo_app:tipo-color")

    def form_valid(self, form):
        messages.success(self.request, 'TIPO DE COLOR ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewstipocolor(DetailView): 
    model = Tipo_Color                  
    template_name = "insumo/tipocolor/tipocolor-detalle.html"
    context_object_name = "tipocolor"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewtipocolor(DeleteView):
    model = Tipo_Color
    template_name = "insumo/tipocolor/tipocolor-delete.html"
    form_class = FormTipocolor
    success_url = reverse_lazy("insumo_app:tipo-color")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'TIPO DE INSUMO BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAllinsumo(ListView):
    template_name = "insumo/insumo/insumo.html"
    paginate_by = 4
    ordering = "id"
    model = Insumo
    context_object_name = "insumo"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Insumo.objects.filter(
                Q(proveedor__razon_social__istartswith=letter) |
                Q(tipo_insumo__nombre__istartswith=letter)
            )
        else:
            return Insumo.objects.filter(
                Q(proveedor__razon_social__icontains=palabra_clave) |
                Q(tipo_insumo__nombre__icontains=palabra_clave)
            )


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewinsumo(CreateView):
    model = Insumo
    template_name = "insumo/insumo/insumo-add.html"
    form_class = FormInsumo
    success_url = reverse_lazy("insumo_app:insumo")

    def form_valid(self, form):
        messages.success(self.request, 'INSUMO CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewinsumo(UpdateView):
    model = Insumo
    template_name = "insumo/insumo/insumo-update.html"
    form_class = FormInsumo
    success_url = reverse_lazy("insumo_app:insumo")

    def form_valid(self, form):
        messages.success(self.request, 'INSUMO ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsinsumo(DetailView): 
    model = Insumo                  
    template_name = "insumo/insumo/insumo-detalle.html"
    context_object_name = "insumo"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewinsumo(DeleteView):
    model = Insumo
    template_name = "insumo/insumo/insumo-delete.html"
    form_class = FormInsumo
    success_url = reverse_lazy("insumo_app:insumo")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'INSUMO BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)