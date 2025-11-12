from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from django.utils.decorators import method_decorator
from test_project.decorador_personalizado import active_superuser_required, staff_active_required


from .models import Sala, Mensaje
from .forms import FormSala



@method_decorator(active_superuser_required, name='dispatch')
class ListAllSala(ListView):
    template_name = "mensajeria/sala_chat/sala.html"
    paginate_by = 4
    ordering = "id"
    model = Sala
    context_object_name = "room"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        letter = self.request.GET.get("letter")
        
        
        if letter:
            return Sala.objects.filter(name__nombre__istartswith=letter)
        else:
            return Sala.objects.filter(name__nombre__icontains=palabra_clave)


@method_decorator(active_superuser_required, name='dispatch')
class CreateViewSala(CreateView):
    model = Sala
    template_name = "mensajeria/sala_chat/sala-add.html"
    form_class= FormSala
    success_url = reverse_lazy("mensajeria_app:sala")

    def form_valid(self, form):
        messages.success(self.request, 'SALA CREADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class UpdateViewSala(UpdateView):
    model = Sala
    template_name = "mensajeria/sala_chat/sala-update.html"
    form_class= FormSala
    success_url = reverse_lazy("mensajeria_app:sala")

    def form_valid(self, form):
        messages.success(self.request, 'SALA ACTUALIZADA EXITOSAMENTE.')
        return super().form_valid(form)


@method_decorator(active_superuser_required, name='dispatch')
class DetailsViewsSala(DetailView): 
    model = Sala                  
    template_name = "mensajeria/sala_chat/sala-detalle.html"
    context_object_name = "room"


@method_decorator(active_superuser_required, name='dispatch')
class DeleteViewSala(DeleteView):
    model = Sala
    template_name = "mensajeria/sala_chat/sala-delete.html"
    form_class= FormSala
    success_url = reverse_lazy("mensajeria_app:sala")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'GET':
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'SALA BORRADA EXITOSAMENTE.')
        return super().delete(request, *args, **kwargs)



@staff_active_required
def home(request):
    rooms= Sala.objects.all()
    return render(request, 'mensajeria/room/home_mensajeria.html', {'room' : rooms})

@staff_active_required
def room(request, room_id):
    try:
        room = request.user.room_joined.get(id=room_id)
    except Sala.DoesNotExist:
        error_message = 'No tienes permisos para el acceso a este chat'
        return render(request, 'mensajeria/room/home_mensajeria.html', {'error_message':error_message, 'room':Sala.objects.all()})
        
    return render(request, 'mensajeria/room/room.html', {'room' : room})



def get_messages(request, room_id):
    # Obtener los mensajes de la sala filtrados por el ID de la sala
    messages = Mensaje.objects.filter(room_id=room_id).order_by('timestamp')

    # Serializar los mensajes para devolverlos como JSON
    message_list = [{'user': msg.user.username, 'message': msg.message, 'timestamp': msg.timestamp} for msg in messages]

    return JsonResponse({'messages': message_list})