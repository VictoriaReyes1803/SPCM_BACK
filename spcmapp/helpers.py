from datetime import datetime
from django.contrib.auth.models import User
from .models import Actividad

def registrar_actividad(usuario, metodo, actividad):
    """
    Registra una actividad en la tabla de logs de actividad.

    Args:
        usuario (User): El usuario que realizó la actividad.
        metodo (str): El método HTTP (GET, POST, PUT, DELETE).
        actividad (str): Descripción de la actividad.
    """
    Actividad.objects.create(
        usuario=usuario, 
        metodo=metodo, 
        actividad=actividad)
