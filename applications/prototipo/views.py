from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from test_project.decorador_personalizado import active_superuser_required

from .models import NombrePrototipo, Prototipo, Piezas, PiezaPrototipo
from .forms import FormPiezaPrototipo, FormPiezas, FormNombrePrototipo, FormPrototipo, FormupdatePrototipo



@method_decorator(active_superuser_required, name='dispatch')
class ListAllpiezas(ListView):
    template_name = "prototipo/piezas/piezas.html"
    paginate_by = 4
    ordering = "id"
    model = Piezas
    context_object_name = "piezas"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Piezas.objects.filter(nombre__istartswith=letter)
        else:
            return Piezas.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewpiezas(CreateView):
    model = Piezas
    template_name = "prototipo/piezas/piezas-add.html"
    #fields = ("__all__")
    form_class = FormPiezas
    success_url = reverse_lazy("prototipo_app:piezas")

    def form_valid(self, form):
        messages.success(self.request, 'PIEZA CREADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewpiezas(UpdateView):
    model = Piezas
    template_name = "prototipo/piezas/piezas-update.html"
    form_class = FormPiezas
    success_url = reverse_lazy("prototipo_app:piezas")

    def form_valid(self, form):
        messages.success(self.request, 'PIEZA ACTUALIZADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewspiezas(DetailView): 
    model = Piezas                  
    template_name = "prototipo/piezas/piezas-detalle.html"
    context_object_name = "piezas"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewpiezas(DeleteView):
    model = Piezas
    template_name = "prototipo/piezas/piezas-delete.html"
    form_class = FormPiezas
    success_url = reverse_lazy("prototipo_app:piezas")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'PIEZA BORRADA EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAllpiezaprototipo(ListView):
    template_name = "prototipo/piezaprototipo/piezaprototipo.html"
    paginate_by = 4
    ordering = "id"
    model = PiezaPrototipo
    context_object_name = "piezaprototipo"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return PiezaPrototipo.objects.filter(piezas__nombre__istartswith=letter)
        else:
            return PiezaPrototipo.objects.filter(piezas__nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewpiezaprototipo(CreateView):
    model = PiezaPrototipo
    template_name = "prototipo/piezaprototipo/piezaprototipo-add.html"
    #fields = ("__all__")
    form_class = FormPiezaPrototipo
    success_url = reverse_lazy("prototipo_app:pieza-prototipo")

    def form_valid(self, form):
        messages.success(self.request, 'PIEZA DE PROTOTIPO CREADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch') 
class UpdateViewpiezaprototipo(UpdateView):
    model = PiezaPrototipo
    template_name = "prototipo/piezaprototipo/piezaprototipo-update.html"
    form_class = FormPiezaPrototipo
    success_url = reverse_lazy("prototipo_app:pieza-prototipo")

    def form_valid(self, form):
        messages.success(self.request, 'PIEZA DE PROTOTIPO ACTUALIZADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewspiezaprototipo(DetailView): 
    model = PiezaPrototipo                  
    template_name = "prototipo/piezaprototipo/piezaprototipo-detalle.html"
    context_object_name = "piezaprototipo"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewpiezaprototipo(DeleteView):
    model = PiezaPrototipo
    template_name = "prototipo/piezaprototipo/piezaprototipo-delete.html"
    form_class = FormPiezaPrototipo
    success_url = reverse_lazy("prototipo_app:pieza-prototipo")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'PIEZA DE PROTOTIPO BORRADA EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAllnombreprototipo(ListView):
    template_name = "prototipo/nombreprototipo/nombreprototipo.html"
    paginate_by = 4
    ordering = "id"
    model = NombrePrototipo
    context_object_name = "nombreprototipo"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return NombrePrototipo.objects.filter(nombre__istartswith=letter)
        else:
            return NombrePrototipo.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewnombreprototipo(CreateView):
    model = NombrePrototipo
    template_name = "prototipo/nombreprototipo/nombreprototipo-add.html"
    #fields = ("__all__")
    form_class = FormNombrePrototipo
    success_url = reverse_lazy("prototipo_app:nombre-prototipo")

    def form_valid(self, form):
        messages.success(self.request, 'NOMBRE DE PROTOTIPO CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewnombreprototipo(UpdateView):
    model = NombrePrototipo
    template_name = "prototipo/nombreprototipo/nombreprototipo-update.html"
    form_class = FormNombrePrototipo
    success_url = reverse_lazy("prototipo_app:nombre-prototipo")

    def form_valid(self, form):
        messages.success(self.request, 'NOMBRE DE PROTOTIPO ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsnombreprototipo(DetailView): 
    model = NombrePrototipo                  
    template_name = "prototipo/nombreprototipo/nombreprototipo-detalle.html"
    context_object_name = "nombreprototipo"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewnombreprototipo(DeleteView):
    model = NombrePrototipo
    template_name = "prototipo/nombreprototipo/nombreprototipo-delete.html"
    form_class = FormNombrePrototipo
    success_url = reverse_lazy("prototipo_app:nombre-prototipo")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'NOMBRE DE PROTOTIPO BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAllPrototipo(ListView):
    template_name = "prototipo/prototipo/prototipo.html"
    paginate_by = 4
    ordering = "id"
    context_object_name = "prototipo"
    queryset = Prototipo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prototipo'] = Prototipo.objects.all()
        context['prototipo_ids'] = [prototipo.id for prototipo in context['prototipo']]
        return context

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Prototipo.objects.filter(nombre__istartswith=letter)
        else:
            return Prototipo.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewprototipo(CreateView):
        model = Prototipo
        template_name = "prototipo/prototipo/prototipo-add.html"
        #fields = ("__all__")
        form_class = FormPrototipo
        success_url = reverse_lazy("prototipo_app:prototipo")

        def form_valid(self, form):
            messages.success(self.request, 'PROTOTIPO CREADO EXITOSAMENTE.')
            return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewprototipo(UpdateView):
    model = Prototipo
    template_name = "prototipo/prototipo/prototipo-update.html"
    form_class = FormupdatePrototipo
    success_url = reverse_lazy("prototipo_app:prototipo")

    def form_valid(self, form):
        messages.success(self.request, 'PROTOTIPO ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsprototipo(DetailView): 
    model = Prototipo                  
    template_name = "prototipo/prototipo/prototipo-detalle.html"
    context_object_name = "prototipo"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewprototipo(DeleteView):
    model = Prototipo
    template_name = "prototipo/prototipo/prototipo-delete.html"
    form_class = FormPrototipo
    success_url = reverse_lazy("prototipo_app:prototipo")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'PROTOTIPO BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)