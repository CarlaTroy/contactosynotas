from django.contrib import admin
#Importamos del framework django la libreria de contibuciones vamos a importar el administador
from .models import Contacto, Apunte
#Del archivo models importamos Contacto 



#Creamos la clase AdminContacto para generar la administracion del contacto, va a listar la informacion 
#en un arreglo y va a tener que heredar del objeto contacto, es una clase anidada
class AdminContacto(admin.ModelAdmin):
    list_display = ["__str__","nombres","apellidos", "cedula", "celular","email"]

    class Meta(object):
        model = Contacto
#Registra en el entprno del administrador el modelo contacto
admin.site.register(Contacto,AdminContacto)

#Gestión que cree un crud basico de una administracion de apuntes 

class AdminApunte(admin.ModelAdmin):
    list_display = ["__str__","titulo","contenido"]

    class Meta(object):
        model = Apunte

#Registra en el entprno del administrador el modelo contacto
admin.site.register( Apunte, AdminApunte)


