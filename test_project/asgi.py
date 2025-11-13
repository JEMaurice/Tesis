import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
import applications.mensajeria.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings.local')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(applications.mensajeria.routing.websocket_urlpatterns)
    )
})