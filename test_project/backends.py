from django.contrib.auth.backends import ModelBackend
from applications.usuario.models import Usuarios

class ActiveUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuarios.objects.get(username=username)
            if user.check_password(password) and user.usuario_activo:
                return user
        except Usuarios.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuarios.objects.get(pk=user_id)
        except Usuarios.DoesNotExist:
            return None