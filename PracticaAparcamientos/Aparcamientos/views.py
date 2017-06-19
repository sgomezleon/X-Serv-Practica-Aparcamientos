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

	if not aparcamientos:
		aparcamientos = ParsearAparcamientos()	#Utilizamos el parse para crear la lista
		for parking in aparcamientos:	
		# En cada campo del models metemos lo que hemos parseado
			parking_new = Aparcamiento(Nombre			=	parking["NOMBRE"], 
										Descripcion		=	parking["DESCRIPCION"],
										Enlace			=	parking["CONTENT-URL"],
										Accesibilidad	=	parking["ACCESIBILIDAD"],
										Nombre_Via		=	parking["NOMBRE-VIA"],
										Tipo_Via		=	parking["TIPO-VIA"],
										Num				=	parking["NUM"],
										Localidad		=	parking["LOCALIDAD"],
										Codigo_Postal	=	parking["CODIGO-POSTAL"],
										Barrio			=	parking["BARRIO"],
										Distrito		=	parking["DISTRITO"],
										Latitud			=	parking["LATITUD"],
										Longitud		=	parking["LONGITUD"])

			parking_new.save()
	
	#Creamos la lista con los usuarios registrados
	users_list = []
	users = User.objects.all()

	for user in users:
		users_list += [user]
	
	template = get_template('inicio.html')	
	context = RequestContext(request,{"users" : users_list})
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
def mypage (request,username):
	pagina_usuario = User.object.get(username=username)	
#	try:
#		Parking_Selected = 	
	return HttpResponseRedirect('/' + username)

def desconexion(request):
	logout(request)
	return HttpResponseRedirect('/')
