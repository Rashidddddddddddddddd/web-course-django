"""
ASGI config for firstPro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstPro.settings')

application = get_asgi_application()

"""
Asinxrom nma degani?

Asinxron degani biror protsess boshqa protessga buyruq berganda
uning keyingi qadami buyruq berilgan protsessdan kelgan 
natijaga bog'liq emas, yani u zapros berib qo'yib 
keyingi ishlarini bajarishda davom etadi.

"""