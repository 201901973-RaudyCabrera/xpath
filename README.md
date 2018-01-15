# xpath

Ejemplos de consultas xpath, con python!!!

## Prerquisitos

Para que el progrma funcione hay que instalar la libreria lxml:

	apt-get install python-lxml

## Usando el programa

En el fichero xpath.cfg indicamos el fichero XML con el que vamos a trabajar. También se puede indicar una URL. A continuación simplemente ejecutamos el programa:

	python xpath.py

## Ejemplos de consultas xpath

Estos ejemplos se hacen sobre el fichero book.xml:

	<?xml version="1.0" encoding="utf-8"?>
	<bookstore>
	<book category="COOKING">
	  <title lang="en">Everyday Italian</title>
	  <author>Giada De Laurentiis</author>
	  <year>2005</year>
	  <price>30.00</price>
	</book>
	<book category="CHILDREN">
	  <title lang="en">Harry Potter</title>
	  <author>J K. Rowling</author>
	  <author>Giada De Laurentiis</author>
	  <year>2006</year>
	  <price>29.99</price>
	</book>
	</bookstore>

Todas las búsquedas se hacen desde el nodo raíz.

1. Ruta de localización:

	* /bookstore/book: Selecciona todos los nodos "book" que están en la ruta.
	* //year: Selecciona todos los nodos "year" a partir del nodo raíz.
	* /bookstore/book/title/text(): Selecciona todos los nodos texto (información) de los elementos seleccionados con la ruta.
	* /bookstore/book/title/@lang: Selecciona todos los atributos llamados "lang" de los elementos seleccionados con la ruta.
	* . : Selecciona el nodo actual.
	* .. : Selecciona al nodo padre.
	* * : Selecciona todos los nodos

2. Filtrado de nodos:

	* /bookstore/book[title="Everyday Italian"]: Predicado que filtra de todos los nodos seleccionados con la ruta, aquellos que tienen un nodo hijo cuya información coincide con la indicada.
	* /bookstore/book[year>2005]: En este caso se hace una comparación numérica.
	* /bookstore/book/title[@lang="en"]: Ahora la selección se hace con un atributo.
	* /bookstore/book/title[@lang="en"]/text(): Ejemplo igual que el anterior, pero en este caso se selecciona el nodo texto (información).
	* //book[@category="CHILDREN" and price="29.99"]: Se pueden utilizar expresiones lógicas: and y or.

3. Funciones xpath

	* count(book/title): Devuelve el número de nodos seleccionados.
	* sum(//book/price): Devuelve la suma de los valores de los nodos seleccionados.
	* //book/author[contains(text(),'De')]: Devuelve los autores cuya información contine la subcadena "De".

En este [documento](http://www.etsii.urjc.es/~smontalvo/oa/teoria/FUNCIONESXPATH.pdf) puedes ver una lista de las funciones que puedes usar.
