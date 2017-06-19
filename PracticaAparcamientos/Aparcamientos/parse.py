#Fichero donde vamos a parsear el XML para quedarnos con lo que nos interesa

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

class ContentHandler(ContentHandler):
	def __init__(self):

		self.lista_parking = {}
		self.parking = []
		self.flag = 0
		self.theContent = ""
		self.atrib = ""

	def startElement(self,tag,attrs):

		if tag == "atributo" and attrs["nombre"] in ['NOMBRE', 'DESCRIPCION', 'CONTENT-URL', 'ACCESIBILIDAD', 'NOMBRE-VIA', 'CLASE-VIAL', 'NUM','LOCALIDAD','CODIGO-POSTAL','BARRIO', 'DISTRITO','LATITUD','LONGITUD']:
			self.atrib = attrs['nombre']
			self.flag = 1

	def endElement(self, tag):
		if tag == 'atributo':
			self.lista_parking[self.atrib] = self.theContent
			self.atrib = ""
		if tag == "contenido":
			self.parking.append(self.parking)
			self.park = {}
		if self.flag:
			self.flag = 0
			self.theContent = ""

	def characters(self, chars):
		if self.flag:
			self.theContent = self.theContent + chars

	def terminar (self):
		return (self.parking)

def ParsearAparcamientos():

	theParser = make_parser()
	theHandler = ContentHandler()
	theParser.setContentHandler(theHandler)

	theParser.parse("http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full")
	Parking = theHandler.parking
	return Parking
