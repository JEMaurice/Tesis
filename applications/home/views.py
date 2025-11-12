from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import logout
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from test_project.decorador_personalizado import active_superuser_required, staff_active_required



from applications.usuario.models import *
from applications.prototipo.models import *
from applications.insumo.models import *

from .forms import FormUsuarios




class CustomLoginView(LoginView):
    template_name = 'inicio.html'


def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_app:login'))


@method_decorator(staff_active_required, name='dispatch')
class Viewhome(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'


@method_decorator(active_superuser_required, name='dispatch')
class Viewfunciones(TemplateView):
    template_name = 'home/funciones.html'




@method_decorator(staff_active_required, name='dispatch')
class Viewperfil(TemplateView):
    template_name = 'home/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el perfil del usuario actual y pasarlo al contexto
        context['perfil'] = self.request.user
        return context


@method_decorator(staff_active_required, name='dispatch')
class UpdateViewPerfil(UpdateView):
    model = Usuarios
    form_class = FormUsuarios
    template_name = 'home/perfil_editar.html'
    success_url = reverse_lazy("home_app:perfil")

    def form_valid(self, form):
        # Guardar la instancia del formulario
        self.object = form.save()
        """messages.success(self.request, 'USUARIO ACTUALIZADO EXITOSAMENTE.') """
        return super().form_valid(form)

    def get_object(self, queryset=None):
        # Obtener el usuario actual
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Pasar la instancia de usuario actual al formulario
        kwargs['instance'] = self.request.user
        return kwargs




@active_superuser_required
def calculador(request):
    insumos = Insumo.objects.all()
    prototipos = Prototipo.objects.all()
    return render(request, 'home/calculador.html', {'insumos': insumos, 'prototipos': prototipos})


def obtener_datos(request):
    prototipo_id = request.GET.get('prototipo_id')
    if prototipo_id:
        prototipo = Prototipo.objects.get(pk=prototipo_id)
        html = render_to_string('home/tabla-prototipo.html', {'prototipo': prototipo})
        return JsonResponse({'html': html})
    else:
        return JsonResponse({'error': 'ID de prototipo no proporcionado'}, status=400)