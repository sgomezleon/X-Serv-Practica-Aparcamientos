from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def home(request):
	template = get_template('index.html')	
	return HttpResponse(template.render())

def about(request):

	respuesta= ('Aqui esta toda la informacion del sitio web')
	return HttpResponse(respuesta)
