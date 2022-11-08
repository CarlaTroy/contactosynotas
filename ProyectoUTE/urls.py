"""ProyectoUTE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appUno.views import deleteApunte_view, updateApuntesPersonal_view, updateApuntes_view, registerApuntesFirst_view, home_view, apuntes_view, contact_view, about_view , registerContact_view, registerApuntes_view, deleteContact_view, updateContact_view, updateContactPersonal_view

from appUno.api.router import router_Contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('registrarContacto/', registerContact_view),
    path('contact/', contact_view),
    path('deleteContact/<cedula>', deleteContact_view),
    path('updateContact/<cedula>', updateContact_view),
    path('updateContactPersonal/', updateContactPersonal_view),
    path('registerApuntes/<cedula>', registerApuntes_view),
    path('seeApuntes/<cedula>', apuntes_view),
    path('registerApuntesFirst/<cedula>', registerApuntesFirst_view),
     path('updateApunte/<cedula>', updateApuntes_view),
     path('updateApuntesPersonal/<id>', updateApuntesPersonal_view),
     path('deleteApunte/<id>', deleteApunte_view),
    path('api/', include(router_Contacto.urls)),
]
