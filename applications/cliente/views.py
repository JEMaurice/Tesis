from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from test_project.decorador_personalizado import active_superuser_required


from .models import Cliente, Contacto_cliente
from .forms import Formcontactocliente, Formcliente, Formupdatecliente



@method_decorator(active_superuser_required, name='dispatch')
class ListAllContactoCliente(ListView):
    template_name = "cliente/contacto-cliente/contacto-cliente.html"
    paginate_by = 4
    ordering = "id"
    model = Contacto_cliente
    context_object_name = "contactocliente"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Contacto_cliente.objects.filter(nombre__istartswith=letter)
        else:
            return Contacto_cliente.objects.filter(nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewContactoCliente(CreateView):
    model = Contacto_cliente
    template_name = "cliente/contacto-cliente/contacto-cliente-add.html"
    form_class= Formcontactocliente
    success_url = reverse_lazy("cliente_app:contacto-cliente")

    def form_valid(self, form):
        messages.success(self.request, 'CONTACTO CLIENTE CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewContactoCliente(UpdateView):
    model = Contacto_cliente
    template_name = "cliente/contacto-cliente/contacto-cliente-update.html"
    form_class= Formcontactocliente
    success_url = reverse_lazy("cliente_app:contacto-cliente")

    def form_valid(self, form):
        messages.success(self.request, 'CONTACTO CLIENTE ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)




@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsContactoCliente(DetailView): 
    model = Contacto_cliente                  
    template_name = "cliente/contacto-cliente/contacto-cliente-detalle.html"
    context_object_name = "contactocliente"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewContactoCliente(DeleteView):
    model = Contacto_cliente
    template_name = "cliente/contacto-cliente/contacto-cliente-delete.html"
    form_class= Formcontactocliente
    success_url = reverse_lazy("cliente_app:contacto-cliente")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'CONTACTO CLIENTE BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)


@method_decorator(active_superuser_required, name='dispatch')
class ListAllCliente(ListView):
    template_name = "cliente/cliente/cliente.html"
    paginate_by = 4
    ordering = "id"
    model = Cliente
    context_object_name = "cliente"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        if letter:
            return Cliente.objects.filter(
                Q(fantasia__istartswith=letter) |
                Q(razon_social__istartswith=letter))
        else:
            return Cliente.objects.filter(
                Q(fantasia__icontains=palabra_clave) |
                Q(razon_social__icontains=palabra_clave))


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewCliente(CreateView):
    model = Cliente
    template_name = "cliente/cliente/cliente-add.html"
    form_class= Formcliente
    success_url = reverse_lazy("cliente_app:cliente")

    def form_valid(self, form):
        messages.success(self.request, 'CLIENTE CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewCliente(UpdateView):
    model = Cliente
    template_name = "cliente/cliente/cliente-update.html"
    form_class= Formupdatecliente
    success_url = reverse_lazy("cliente_app:cliente")

    def form_valid(self, form):
        messages.success(self.request, 'CLIENTE ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsCliente(DetailView): 
    model = Cliente                  
    template_name = "cliente/cliente/cliente-detalle.html"
    context_object_name = "cliente"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewCliente(DeleteView):
    model = Cliente
    template_name = "cliente/cliente/cliente-delete.html"
    form_class= Formupdatecliente
    success_url = reverse_lazy("cliente_app:cliente")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'CLIENTE BORRADO EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)
