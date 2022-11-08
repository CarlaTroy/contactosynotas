from rest_framework.viewsets import ModelViewSet
from appUno.models import Contacto
from appUno.api.serializers import ContactoSerilizer

class ContactoApiViewSet(ModelViewSet):

    serializer_class= ContactoSerilizer
    queryset=Contacto.objects.all()