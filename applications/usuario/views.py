from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from test_project.decorador_personalizado import active_superuser_required
from django.core.exceptions import PermissionDenied



from .models import  Usuarios
from .forms import FormUsuarios, ModificarUserForm



@method_decorator(active_superuser_required, name='dispatch')
class ListAllUsuarios(ListView):
    template_name = "usuario/usuarios/usuarios.html"
    
    paginate_by = 4 #cantidad de objetos por pagina
    ordering = "id" #ordenarlo dependiendo que columna usar
    model = Usuarios
    context_object_name = "usuario"
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        queryset = Usuarios.objects.filter(id__gte=3)  # Filtrar usuarios con ID >= 3
        
        if letter:
            queryset = queryset.filter(username__istartswith=letter)
        elif palabra_clave:
            queryset = queryset.filter(username__icontains=palabra_clave)
        
        return queryset


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewUsuarios(CreateView):
    model = Usuarios
    template_name = "usuario/usuarios/usuarios-add.html"
    form_class = FormUsuarios
    success_url = reverse_lazy("usuario_app:usuario")

    def form_valid(self, form):
        # Verificar que las contraseñas coincidan
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            return self.form_invalid(form)
        usuario = form.save(commit=False)

        # Encripta la contraseña
        usuario.set_password(password1)  

        # Establecer is_staff y is_superuser
        usuario.is_staff = form.cleaned_data.get('is_staff')
        usuario.is_superuser = form.cleaned_data.get('is_superuser')
        usuario.usuario_activo = form.cleaned_data.get('usuario_activo')
        if usuario.is_superuser:
            usuario.is_staff = True

        # Guardar el usuario en la base de datos
        usuario.save()

        # Agregar los sectores asignados al usuario
        sectores_asignados = form.cleaned_data.get('sector_asignado')
        for sector in sectores_asignados:
            usuario.sector_asignado.add(sector)
        messages.success(self.request, 'USUARIO CREADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewUsuarios(UpdateView):
    model = Usuarios
    form_class = ModificarUserForm
    template_name = "usuario/usuarios/usuarios-update.html"
    success_url = reverse_lazy("usuario_app:usuario")

    def get_object(self, queryset=None):
        usuario = super().get_object(queryset)
        if usuario.id < 3:
            raise PermissionDenied("No se permite modificar este usuario.")
        return usuario

    def get_initial(self):
        initial = super().get_initial()
        usuario = self.get_object()
        initial['is_staff'] = usuario.is_staff
        initial['is_superuser'] = usuario.is_superuser
        initial['usuario_activo'] = usuario.usuario_activo
        return initial

    def form_valid(self, form):
        usuario = form.save(commit=False)

        # Verificar que las contraseñas coincidan
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            return self.form_invalid(form)
        
        # Encriptar la nueva contraseña antes de guardarla si se proporciona
        if password1:
            usuario.password = make_password(password1)
        
        # Actualizar los campos del usuario con los datos del formulario
        usuario.is_staff = form.cleaned_data.get('is_staff')
        usuario.is_superuser = form.cleaned_data.get('is_superuser')
        usuario.usuario_activo = form.cleaned_data.get('usuario_activo')

        # Verificar si es superusuario, también debe ser staff
        if usuario.is_superuser:
            usuario.is_staff = True

        usuario.save()
        messages.success(self.request, 'USUARIO ACTUALIZADO EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsUsuarios(DetailView): 
    model = Usuarios                  
    template_name = "usuario/usuarios/usuarios-detalle.html"
    context_object_name = "usuario"

    def get_object(self, queryset=None):
        usuario = super().get_object(queryset)
        if usuario.id < 3:
            raise PermissionDenied("No se permite ver este usuario.")
        return usuario


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewUsuarios(DeleteView):
    model = Usuarios
    template_name = "usuario/usuarios/usuarios-delete.html"
    fields = ("__all__")
    success_url = reverse_lazy("usuario_app:usuario")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        usuario = super().get_object(queryset)
        if usuario.id < 3:
            raise PermissionDenied("No se permite eliminar este usuario.")
        return usuario

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'TIPO DE UNIDAD BORRADA EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)