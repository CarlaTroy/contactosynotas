from unittest.util import _MAX_LENGTH
from django.db import models

#CLASE CONTACTO QUE TIENE Nombre, Apellido, cedula, email, celular
#Retorna un tipo de dato texto y nos apuntar con el email
class Contacto(models.Model):
    nombres=models.CharField(max_length=30,blank=True)
    apellidos=models.CharField(max_length=30)
    celular=models.CharField(max_length= 10)
    cedula=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.cedula


class Apunte(models.Model):
    cedula = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=30,blank=True)
    contenido=models.CharField(max_length=30)
    #un contcto tiene varias notas, la tabla muchos lleva el campo de forkey
    
    
    def __str__(self):
        return self.titulo