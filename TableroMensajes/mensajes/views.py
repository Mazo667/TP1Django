from django.shortcuts import render
from .models import Mensaje

# Create your views here.
def ver_mensajes(request):
    mensajes_recibidos = Mensaje.objects

    return render(request, 'mensajes/recibidos.html',{'mensajes' : mensajes_recibidos})