from rest_framework.serializers import ModelSerializer
from appUno.models import Contacto

class ContactoSerilizer(ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellidos', 'cedula', 'celular','email']
