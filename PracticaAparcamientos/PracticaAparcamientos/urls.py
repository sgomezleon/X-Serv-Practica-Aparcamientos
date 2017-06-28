"""PracticaAparcamientos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Aparcamientos import views

urlpatterns = [
	url(r'^about/$', views.about, name='Pagina con la informacion'),
	url(r'^login$', views.entrar_usuario),
	url(r'^logout$', views.desconexion),
	url(r'^aparcamientos$', views.aparcamientos),
	url(r'^aparcamientos/(\d+)', views.pag_aparcamiento),
	url(r'^accesibles$', views.accesibles),
	url(r'^mypage$',views.mypage),
	url(r'^$', views.home, name='Pagina principal del sitio'),
    url(r'^admin/', include(admin.site.urls)),
]
