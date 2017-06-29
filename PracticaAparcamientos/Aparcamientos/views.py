from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.utils.html import strip_tags
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from Aparcamientos import models
from Aparcamientos.parse import ParsearAparcamientos
from Aparcamientos.models import Aparcamiento,ComentarioAparcamiento,Seleccionado, CSS

# Create your views here.


#PAGINA PRINCIPAL DE LA WEB
def home(request):

#Creamos la lista con los aparcamientos
	park = []
	aparcamientos = Aparcamiento.objects.all()
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

	Listado = []
	AparcamientosPuntuados = Aparcamiento.objects.order_by('-Puntuacion')



	MasPuntuados ="<h2>APARCAMIENTOS MAS PUNTUADOS: </h2>"

	k = 0
	for Listado in AparcamientosPuntuados:
		if Listado.Puntuacion >0:
			MasPuntuados += "<p><ul><b><strong>" + Listado.Nombre + "</strong></b></ul>"  + "<strong> DIRECCION: </strong>" + Listado.Clase_Via + " " + Listado.Nombre_Via +", N " + Listado.Numero + ". <strong> PUNTUACION: </strong>" + str(Listado.Puntuacion)
			MasPuntuados += "<a href= 'aparcamientos/"+ str(Listado.id) + "'> Visitar aparcamiento</a></p>"	
			k = k +1
			if k == 5:
				break
	MasPuntuados += ""

	#Creamos la lista con los usuarios registrados
	users_list = []
	users = User.objects.all()

	for user in users:
		users_list += [user]
	
	template = get_template('index.html')	

	context = RequestContext(request,{"users" : users_list, 'content': MasPuntuados})
	return HttpResponse(template.render(context))



#PAGINA "ABOUT" CON INFORMACION DE LA PAGINA
def about(request):

	template= get_template('about.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))




# INGRESAMOS EL USUARIO REGISTRADO PREVIAMENTE
@csrf_exempt
def entrar_usuario(request):
	if request.method == "POST":
		usuario = request.POST.get("usuario")
		contrasena = request.POST.get("contrasena")

		user = authenticate(username = usuario, password = contrasena)

		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
		else:
			template = get_template("error.html")
			return HttpResponse(template.render())



def registrar_usuario(request):

	if request.method == "GET":
		template = get_template("registro.html")
		context = RequestContext(request, {})
		return HttpResponse(template.render(context))
	if request.method == "POST":
		username = request.POST.get('username')
		password = make_password(request.POST.get('password'))

		UsuarioNuevo = User(username=username,password=password)
		UsuarioNuevo.save()
		user = User.objects.get(username=username)
		config = CSS(Usuario=user)
		config.save()
		return HttpResponseRedirect("/")
	else:
		template = get_template("error.hmtl")
		return HttpResponseNotFound(template.render())



def XML(request, userXML):
	ListadoParking = []
	user = User.objects.get(username = userXML)
	AparcamientoFavorito = Seleccionado.objects.filter(Usuario=user)
	for fav in AparcamientoFavorito:
		ListadoParking += [fav.Elegido]
	context = RequestContext(request, {"ListadoParking" : ListadoParking})
	template = get_template("XML.xml")
	return HttpResponse(template.render(context), content_type = "text/xml")



def mypage(request, user):
	if request.method =="POST":
		TituloNuevo = request.POST.get("TituloNuevo")
		FondoNuevo = request.POST.get("Fondo")
		NuevoTamano = request.POST.get("TamanoLetra")
		print(FondoNuevo)
		user = User.objects.get(username=user)
		print(user)
		newConfig = CSS.objects.all()
		print(newConfig)
		#newConfig = CSS.objects.get(Usuario=user) 
		try:
			newConfig = CSS.objects.get(Usuario=user)
			print(newConfig)
		except CSS.DoesNotExist:
			newConfig.Usuario = user
			newConfig.update()
		if TituloNuevo != "Titulo de la pagina." and TituloNuevo != None:
			newConfig.Titulo = TituloNuevo
			newConfig.save()
		if FondoNuevo != None and FondoNuevo != newConfig.Color:
			newConfig.Color = FondoNuevo
			newConfig.save()
		if NuevoTamano != None and NuevoTamano != newConfig.Tamano:
			newConfig.Tamano = NuevoTamano
			newConfig.save()

	userPage = User.objects.get(username=user)
	userConfig = CSS.objects.all()
	try:
		userConfig = CSS.objects.get(Usuario=userPage)
	except CSS.DoesNotExist:
		userConfig.user = userPage
		userConfig.update()

	AparcamientoElegido = Seleccionado.objects.filter(Usuario=userPage)
	ListadoAparcamientos = []
	for fav in AparcamientoElegido:
		ListadoAparcamientos += [fav.Elegido]


	template = get_template("mypage.html")
	context = RequestContext(request, {"ListadoAparcamientos" : ListadoAparcamientos, "userPage" : userPage, "userConfig" : userConfig})
	return HttpResponse(template.render(context))



#PAGINA CON TODOS LOS APARCAMIENTOS 
def aparcamientos(request):
	
	if request.method == "GET":
		Listado_Aparcamientos = Aparcamiento.objects.all()
	elif request.method == "POST":
		district = request.POST.get('district')
		if district != "None":
			Listado_Aparcamientos = Aparcamiento.objects.filter(Distrito=district)
		else:
			Listado_Aparcamientos = Aparcamiento.objects.all()

	template = get_template('aparcamientos.html')
	context = RequestContext(request, {'Listado_Aparcamientos' : Listado_Aparcamientos})
	return HttpResponse(template.render(context))

def accesibles(request):
	if request.method == "GET":
		Parking_Accesible = Aparcamiento.objects.filter(Accesibilidad = '1')

	template = get_template('accesibles.html')
	context = RequestContext(request, {'Parking_Accesible': Parking_Accesible})
	return HttpResponse(template.render(context))


#PAGINA INDIVIDUAL DE CADA APARCAMIENTO
def pag_aparcamiento(request, identif):
	aparcamiento = Aparcamiento.objects.get(id = identif)
	comments = ComentarioAparcamiento.objects.filter(AparcamientoComentado = aparcamiento)
	seleccionado = Seleccionado(Elegido=aparcamiento)
	puntuacion = aparcamiento.Puntuacion
	cantidad = aparcamiento.Cantidad
	if request.method == "POST":
		comment= request.POST.get("comentarios")
		elegido = request.POST.get("aparcamiento")
		Liked = request.POST.get("liked")
		Repetido = False
		if Liked:
			NuevaPuntuacion = puntuacion + 1
			aparcamiento.Puntuacion = NuevaPuntuacion
			aparcamiento.save()
		if comment != "Escribe tu comentario: " and comment != None:
			Usuario = User.objects.get(username=request.user.username)
			UsuariosComentado = ComentarioAparcamiento.objects.filter(AparcamientoComentado=aparcamiento)
			NuevaCantidad = cantidad + 1
			aparcamiento.cantidad = NuevaCantidad
			aparcamiento.save()
			for UsuarioComentado in UsuariosComentado:
				if UsuarioComentado.Usuario == Usuario:
					Repetido = True
			if Repetido:
				ComentarioModificado = ComentarioAparcamiento.objects.get(AparcamientoComentado=aparcamiento, Usuario=Usuario)
				ComentarioModificado.Comment = comment
				ComentarioModificado.save()
			else:
				NuevoComentario = ComentarioAparcamiento(Comment=comment, AparcamientoComentado = aparcamiento, Usuario = Usuario)
				NuevoComentario.save()
		if elegido != None :
			userchosen = User.objects.get(username=request.user.username)
			NuevoElegido = Seleccionado(Elegido=aparcamiento, Usuario = userchosen)
			NuevoElegido.save()
	Puntuacion = aparcamiento.Puntuacion
	template = get_template('pag_aparcamiento.html')
	context = RequestContext(request, {'aparcamiento': aparcamiento, 'seleccionado':seleccionado, 'comments':comments, 'puntuacion':puntuacion})
	return HttpResponse(template.render(context))


def css(request):
	color = '7EA2E1'
	size = 10
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user.username)
		userConfig = CSS.objects.get(Usuario=user)
		color = userConfig.Color
		size = userConfig.Tamano
	template = get_template("picks/1.css")
	print('miau')
	context = RequestContext(request, {"color": color, "size": size})
	return HttpResponse(template.render(context), content_type="text/css")


# DESCONEXION
def desconexion(request):
	logout(request)
	return HttpResponseRedirect('/')
