#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

with open("xpath.cfg", "r") as archivo: 
    contenido = archivo.read() 
contenido=contenido[:-1]

doc = etree.parse(contenido)
print ("'q' for exit...")

consulta=raw_input("XPATH:")
while consulta!="q":
	try:
		res=doc.xpath(consulta)
	except:
		print "Error en consulta XPATH."
		res=[]
	if isinstance(res,list):	
		for r in res:
			if isinstance(r,etree._Element):
				print etree.tostring(r,pretty_print=True)
			else:
				print r
	else:
		print res
	consulta=raw_input("XPATH:")


