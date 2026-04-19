from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from django.db.models import Q

# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
#all recupera todos los objetos del modelo (registros de la tabla alumnos)

    return render(request,"registros/principal.html",{'alumnos':alumnos})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    form = ComentarioContactoForm()
    return render(request, 'inicio/contacto.html', {'form': form})

def consultarComentarioContacto(request):
    comentarios=ComentarioContacto.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla
    #comentariosContacto)

    return render(request,"registros/consultaContacto.html",
                               {'comentarios':comentarios})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de comentarios recuperados.

def eliminarComentarioContacto(request, id,
      confirmacion='registros/confirmarEliminacion.html'):
      comentario = get_object_or_404(ComentarioContacto, id=id)
      if request.method=='POST':
          comentario.delete()
          comentarios=ComentarioContacto.objects.all()
          return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
      return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario=get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if  form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
#Si el formulario no es valido nos regresa al formulario para verificar
#datos
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})

def consultar1(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.filter(carrera__contains="I")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(carrera__in=['TI', 'Mecatronica'])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(Q(carrera="TI") | Q(carrera="Mecatronica"))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2021, 7, 1)
    fechaFin = datetime.date(2021, 7, 13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",
    {'nombre':nombre})
