from django.db import models

# Create your models here.


#FC = (
#	(True, 'SI'),
#	(False, 'NO'),
#)
    
class Usuario(models.Model):
	nombre=models.CharField(primary_key=True, max_length=30)
	departamento=models.CharField(max_length=40, blank=True)
	email=models.EmailField(blank=True)
	fuera_convenio=models.CharField(max_length=5)

	def __str__(self):
		return '{}'.format(self.nombre)