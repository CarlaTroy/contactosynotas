from django import forms
from .models import Contacto, Apunte

class Formulario(forms.ModelForm):
    class Meta: 
        model = Contacto
        fields =["nombres","apellidos", "cedula", "celular","email"]


class formularioApunte(forms.ModelForm):
    class Meta: 
        model = Apunte
        fields = [ "titulo", "contenido"]