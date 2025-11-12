from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from test_project.decorador_personalizado import active_superuser_required



from .models import Contacto_proveedores, Proveedores
from .forms import Formcontactoproveedores, Formproveedores, Formupdateproveedores



@method_decorator(active_superuser_required, name='dispatch')
class ListAllContactoProveedores(ListView):
    template_name = "proveedor/contacto-proveedores/contacto-proveedores.html"
    paginate_by = 4
    ordering = "id"
    model = Contacto_proveedores
    context_object_name = "contactoproveedor"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Contacto_proveedores.objects.filter(nombre__istartswith=letter)
        else:
            return Contacto_proveedores.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewContactoProveedores(CreateView):
    model = Contacto_proveedores
    template_name = "proveedor/contacto-proveedores/contacto-proveedores-add.html"
    #fields = ("__all__")
    form_class= Formcontactoproveedores
    success_url = reverse_lazy("proveedor_app:contacto-proveedor")

    def form_valid(self, form):
        messages.success(self.request, 'CONTACTO PROVEEDOR CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewContactoProveedores(UpdateView):
    model = Contacto_proveedores
    template_name = "proveedor/contacto-proveedores/contacto-proveedores-update.html"
    form_class= Formcontactoproveedores
    success_url = reverse_lazy("proveedor_app:contacto-proveedor")

    def form_valid(self, form):
        messages.success(self.request, 'CONTACTO PROVEEDOR ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsContactoProveedores(DetailView): 
    model = Contacto_proveedores                  
    template_name = "proveedor/contacto-proveedores/contacto-proveedores-detalle.html"
    context_object_name = "contactoproveedor"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewContactoProveedores(DeleteView):
    model = Contacto_proveedores
    template_name = "proveedor/contacto-proveedores/contacto-proveedores-delete.html"
    form_class= Formcontactoproveedores
    success_url = reverse_lazy("proveedor_app:contacto-proveedor")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'CONTACTO PROVEEDOR BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@method_decorator(active_superuser_required, name='dispatch')
class ListAllProveedores(ListView):
    template_name = "proveedor/proveedores/proveedores.html"
    paginate_by = 4
    ordering = "id"
    model = Proveedores
    context_object_name = "proveedor"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Proveedores.objects.filter(razon_social__istartswith=letter)
        else:
            return Proveedores.objects.filter(razon_social__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewProveedores(CreateView):
    model = Proveedores
    template_name = "proveedor/proveedores/proveedores-add.html"
    #fields = ("__all__")
    form_class = Formproveedores
    success_url = reverse_lazy("proveedor_app:proveedores")

    def form_valid(self, form):
        messages.success(self.request, 'PROVEEDOR CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewProveedores(UpdateView):
    model = Proveedores
    template_name = "proveedor/proveedores/proveedores-update.html"
    form_class = Formupdateproveedores
    success_url = reverse_lazy("proveedor_app:proveedores")

    def form_valid(self, form):
        messages.success(self.request, 'PROVEEDOR ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsProveedores(DetailView):
    model = Proveedores
    template_name = "proveedor/proveedores/proveedores-detalle.html"
    context_object_name = "proveedor"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewProveedores(DeleteView):
    model = Proveedores
    template_name = "proveedor/proveedores/proveedores-delete.html"
    form_class = Formproveedores
    success_url = reverse_lazy("proveedor_app:proveedores")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'PROVEEDOR BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)