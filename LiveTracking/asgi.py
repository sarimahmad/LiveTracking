"""
ASGI config for LiveTracking project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import path
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from Consumer import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LiveTracking.settings')


websocket_urlpatterns = [
    path('ws/Mobile/<str:room_id>/', MyConsumer.as_asgi())
]
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
})