#Fichero donde vamos a parsear el XML para quedarnos con lo que nos interesa

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

class ContentHandler(ContentHandler):
	def __init__(self):

		self.dataType = 'contenido'
		

		self.inContent = True
		self.theContent = ""

		self.inSection = False
		self.atrSection = ''

		self.Lista_Parking = {}
		self.Parking = []
		
	def startElement(self,tag,attrs):

		if tag == "atributo" and attrs["nombre"] in ['NOMBRE', 'DESCRIPCION', 'ACCESIBILIDAD','CONTENT-URL', 'NOMBRE-VIA', 'CLASE-VIAL', 'NUM','LOCALIDAD','CODIGO-POSTAL','BARRIO', 'DISTRITO','LATITUD','LONGITUD']:
			self.atrSection = attrs['nombre']
			self.inSection = 1

	def endElement(self, tag):
		if tag == 'atributo' and self.atrSection in ['NOMBRE', 'DESCRIPCION', 'ACCESIBILIDAD','CONTENT-URL', 'NOMBRE-VIA', 'CLASE-VIAL', 'NUM','LOCALIDAD','CODIGO-POSTAL','BARRIO', 'DISTRITO','LATITUD','LONGITUD']:
			self.Lista_Parking[self.atrSection] = self.theContent
			self.atrSection = ""
		if tag == "atributo" and self.atrSection == 'LOCALIZACION' and self.atrSection in ['NOMBRE', 'DESCRIPCION', 'ACCESIBILIDAD','CONTENT-URL', 'NOMBRE-VIA', 'CLASE-VIAL', 'NUM','LOCALIDAD','CODIGO-POSTAL','BARRIO', 'DISTRITO','LATITUD','LONGITUD']:
			self.Lista_Parking[self.atrSection] = self.theContent
		if tag == self.dataType:
			self.Parking.append(self.Lista_Parking)
			self.Lista_Parking = {}
		if self.inSection:
			self.inSection = 0
			self.AtrSection = ""
			self.theContent = ""

	def characters(self, chars):
		if self.inSection:
			self.theContent = self.theContent + chars

	def terminar (self):
		return (self.parking)

def ParsearAparcamientos():

	theParser = make_parser()
	theHandler = ContentHandler()
	theParser.setContentHandler(theHandler)

	theParser.parse("http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full")
	Parking = theHandler.Parking
	return Parking
