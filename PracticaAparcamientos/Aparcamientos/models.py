from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aparcamiento(models.Model):
	Nombre 			=		models.TextField(default="")
	Descripcion 	=		models.TextField(default="")
	Accesibilidad 	=		models.IntegerField(default="0")
	Enlace 			=		models.TextField(default="")
	Nombre_Via		=		models.TextField(default="")
	Clase_Via		=		models.TextField(default="")
	Numero			=		models.TextField(default="") 			
	Localidad		=		models.TextField(default="")
	Codigo_Postal 	=		models.IntegerField(default="0")
	Barrio			=		models.TextField(default="")
	Distrito		=		models.TextField(default="")
	Latitud			=		models.TextField(default="")
	Longitud		=		models.TextField(default="")
	Puntuacion		= 		models.IntegerField(default="0")
	Cantidad 		=		models.IntegerField(default = "0")
	def __str__(self):
		return self.Nombre

class ComentarioAparcamiento(models.Model):
	Usuario			=		models.ForeignKey(User)		
	Comment			= 	models.TextField(default="")
	Fecha			=		models.DateField(auto_now_add="True")
	AparcamientoComentado	=		models.ForeignKey('Aparcamiento')
	def __str__(self):
		return str(self.AparcamientoComentado)

class Seleccionado(models.Model):
	Usuario 	= models.ForeignKey(User)
	Fecha 		= models.DateField(auto_now_add="True")
	Elegido 	= models.ForeignKey("Aparcamiento")
	def __str__(self):
		return str(self.Elegido)

class CSS(models.Model):
	Usuario = models.ForeignKey(User)
	Titulo = models.TextField(default="Mi pagina")
	Color = models.CharField(default="blue", max_length=32)
	Tamano = models.IntegerField(default=15)
