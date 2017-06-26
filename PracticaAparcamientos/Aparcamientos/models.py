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

class Comentario(models.Model):
	Usuario			=		models.ForeignKey(User)		
	Comentario		= 		models.TextField(default="")
	Fecha			=		models.DateField(auto_now_add="True")
	Aparcamiento	=		models.ForeignKey('Aparcamiento')

	
