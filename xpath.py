#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse('book.xml')
raiz=doc.getroot()
print ("'q' for exit...")

consulta=raw_input("XPATH:")
while consulta!="q":
	try:
		res=raiz.xpath(consulta)
	except:
		print "Error en consulta XPATH."
	print res
	for r in res:
		if isinstance(r,etree._Element):
			print etree.tostring(r,pretty_print=True)
		else:
			print r
	consulta=raw_input("XPATH:")


