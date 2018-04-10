from django.db import models
from apps.usuarios.models import Usuario
from datetime import date, datetime


# Create your models here.
class Dispositivo(models.Model):
	dispositivo=models.CharField(max_length=25)
	marca=models.CharField(max_length=25, blank=True)
	modelo=models.CharField(max_length=25, blank=True)
	num_serie=models.CharField(primary_key=True, max_length=12)
	fecha_instalacion=models.DateField(verbose_name="Fecha de asignación: ",null=True, blank=True)
	nombre=models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
	def __str__(self):
		return '{} {}'.format(self.dispositivo,self.num_serie)