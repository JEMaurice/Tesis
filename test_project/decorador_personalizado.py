from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from functools import wraps

def active_superuser_required(view_func):
    """
    Decorador que permite el acceso solo a los usuarios activos y superusuarios.
    """
    @login_required
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.usuario_activo:
            return redirect('home_app:login')  # Redirige a la página de inicio de sesión u otra página
        if not request.user.is_superuser:
            return HttpResponseForbidden("Acceso denegado")
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def staff_active_required(view_func):
    """
    Decorador que permite el acceso solo a los usuarios del personal (staff) que estén activos.
    """
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Acceso denegado")
        if not request.user.usuario_activo:
            return redirect('home_app:login')  # Redirige a la página de inicio de sesión u otra página
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view