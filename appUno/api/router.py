from rest_framework import routers
from appUno.api.views import ContactoApiViewSet

router_Contacto = routers.SimpleRouter()

router_Contacto.register(prefix='post', basename='post', viewset=ContactoApiViewSet)

