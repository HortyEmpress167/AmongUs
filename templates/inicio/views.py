from django.shortcuts import render, HttpResponse

# Create your views here.
menu="""
    <a href="/">Home</a>
    <a href="/formulario">Registrar</a>
    <a href"/contacto">Contactanos</a>
    """
# Vista Principal
def principal(request):
    return render(request, "inicio/principal.html")

# Vista Contacto (Esta es la que te faltaba y causaba el error)
def contacto(request):
    return render(request, "inicio/contacto.html")

# Vista Formulario (Esta también te faltaba)
def formulario(request):
    return render(request, "inicio/formulario.html")

def seguridad(request):
    return render(request,"inicio/seguridad.html")