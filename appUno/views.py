#from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Formulario,formularioApunte
from .models import Contacto, Apunte

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def contact_view(request):
    contacto= Contacto.objects.all()
    return render(request, "contacts/contact.html", {"contacto":contacto})

    
def registerContact_view(request):
    #f es un objeto de la peticón POST
    f = Formulario(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = Contacto()
            c.nombres = datos.get("nombres")
            c.apellidos = datos.get("apellidos")
            c.cedula = datos.get("cedula")
            c.celular = datos.get("celular")
            c.email = datos.get("email")
            if c.save() != True:
                print('Imprimo en pantalla y guardo data en BD')
                print(f.cleaned_data)                
                return redirect(registerApuntesFirst_view, c.cedula)
    context ={
        "form":f,
    }
    return render(request, "contacts/registerContact.html", context)
    

def updateContact_view(request, cedula):
   contacto = Contacto.objects.get(cedula=cedula)
   return render(request, "contacts/updateContact.html", {"contacto":contacto})


def updateContactPersonal_view(request):
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    cedula=request.POST["cedula"]
    celular = request.POST["celular"]
    email = request.POST["email"]

    contacto = Contacto.objects.get(cedula=cedula)
    contacto.nombres=nombres
    contacto.apellidos=apellidos
    contacto.cedula=cedula
    contacto.celular = celular
    contacto.email=email
    contacto.save()
    return redirect('/contact/')



def deleteContact_view(request, cedula):
    contacto = Contacto.objects.get(cedula=cedula)
    contacto.delete()
    return redirect('/contact/')


def apuntes_view(request, cedula):
    cedula = Contacto.objects.get(pk=cedula)
    apunte = Apunte.objects.filter(cedula=cedula)
    # apunte = Apunte.objects.all()
    return render(request, "notes/mostrarApunte.html", {"apunte":apunte})

def registerApuntesFirst_view(request, cedula):
    f = formularioApunte(request.POST or None)    
    cedula = Contacto.objects.get(cedula=cedula)
       
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            
            a = Apunte()
            a.cedula=cedula
            a.titulo = datos.get("titulo")
            a.contenido = datos.get("contenido")
            
            if a.save() != True:
                print('Imprimo en pantalla y guardo data en BD')
                print(f.cleaned_data)
                return redirect(contact_view)
            else:
                print("mal")
    context ={
        "form":f,
    }
    return render(request, "notes/registerApuntes.html", context)


def registerApuntes_view(request, cedula):
    f = formularioApunte(request.POST or None)
    
    ced = Contacto.objects.get(pk=cedula)
       
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            
            a = Apunte()
            a.cedula=ced
            a.titulo = datos.get("titulo")
            a.contenido = datos.get("contenido")
            
            if a.save() != True:
                print('Imprimo en pantalla y guardo data en BD')
                print(f.cleaned_data)
                return redirect(apuntes_view, cedula)
            else:
                print("mal")
    context ={
        "form":f,
    }
    return render(request, "notes/registerApuntes.html", context)

def updateApuntes_view(request, cedula):
    apunte = Apunte.objects.get(pk=cedula)
    return render(request, "notes/updateApuntes.html", {"apunte":apunte})

def updateApuntesPersonal_view(request,id):
    
    
    titulo = request.POST["titulo"]
    contenido = request.POST["contenido"]
    apunte= Apunte.objects.get(id=id)
    apunte.id = id
    apunte.titulo=titulo
    apunte.contenido=contenido
    apunte.save()
    return redirect(apuntes_view, apunte.cedula_id)



def deleteApunte_view(request, id):
    apunte = Apunte.objects.get(id=id)
    apunte.delete()
    return redirect(apuntes_view, apunte.cedula_id)

# def deleteApunte_view(request, cedula):
#     ap = Apunte.objects.get(cedula_id=cedula)
#     a = Apunte()
#     a.cedula=ap
#     ap.delete()
#     return redirect('/seeApuntes/')
    
def about_view(request):
    return render(request, "about.html", {})

