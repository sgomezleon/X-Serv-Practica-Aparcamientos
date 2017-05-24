from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from Aparcamientos import models

# Create your views here.

def home(request):
	template = get_template('index.html')	
	return HttpResponse(template.render())

def about(request):

	template= get_template('about.html')
	return HttpResponse(template.render())

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
			return HttpResponse("Usuario no encontrado")
		

		
		
