from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from Aparcamientos import models
from Aparcamientos.parse import ParsearAparcamientos
from Aparcamientos.models import Aparcamiento

# Create your views here.

def home(request):

#Creamos la lista con los aparcamientos
	aparcamientos = Aparcamiento.objects.all()
	park = []
	if not aparcamientos:
		park = ParsearAparcamientos()	#Utilizamos el parse para crear la lista
		for parking in park:
		# En cada campo del models metemos lo que hemos parseado
			try:
				parking_new = Aparcamiento(Nombre=parking["NOMBRE"], 
										Descripcion=parking["DESCRIPCION"],
										Accesibilidad=parking["ACCESIBILIDAD"],
										Enlace=parking["CONTENT-URL"],
										Nombre_Via=parking["NOMBRE-VIA"],
										Clase_Via=parking["CLASE-VIAL"],
										Numero=parking["NUM"],
										Localidad=parking["LOCALIDAD"],
										Codigo_Postal=parking["CODIGO-POSTAL"],
										Barrio=parking["BARRIO"],
										Distrito=parking["DISTRITO"],
										Latitud=parking["LATITUD"],
										Longitud=parking["LONGITUD"])
				
			except KeyError:
				continue
			except ValueError:
				continue

			parking_new.save()



	#Creamos la lista con los usuarios registrados
	users_list = []
	users = User.objects.all()

	for user in users:
		users_list += [user]
	
	template = get_template('inicio.html')	
	context = RequestContext(request,{"users" : users_list, 'aparcamientos':aparcamientos})
	return HttpResponse(template.render(context))

def about(request):

	template= get_template('about.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

@csrf_exempt
def entrar_usuario(request):
	if request.method == "POST":
		usuario = request.POST.get("usuario")
		contraseña = request.POST.get("contraseña")

		user = authenticate(username = usuario, password = contraseña)

		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
		else:
			template = get_template("error.html")
			return HttpResponse(template.render())
@csrf_exempt
def mypage (request):
	if request.user.is_authenticated():
		username = request.user.username
		return HttpResponseRedirect('/' + username)

def aparcamientos(request):

	Listado_Aparcamientos = Aparcamiento.objects.all()

	template = get_template('aparcamientos.html')
	context = RequestContext(request, {'Listado_Aparcamientos' : Listado_Aparcamientos})
	return HttpResponse(template.render(context))

def desconexion(request):
	logout(request)
	return HttpResponseRedirect('/')
