"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from home.consumers import TestConsumer

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


ws_patterns = [
    path('ws/test/',TestConsumer.as_asgi())
]
application = get_asgi_application()
print("Here")
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(ws_patterns),
})