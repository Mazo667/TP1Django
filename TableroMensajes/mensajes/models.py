from django.db import models

# Create your models here.
class Mensaje(models.Model):
    texto = models.TextField
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    fecha_hora = models.DateField

    