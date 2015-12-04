#!/usr/bin/env python3
'''programacion de bases de datos'''

# importar modulo

import sys # importa el modulo indicado

print ('VERSION en uso de PYTHON \n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('crear y administrar una base de datos NO RELACIONAL con el modulo ; shelve \n')

print ('importar el modulo shelve ; import shelve \n')

import shelve # importa el modulo indicado

print ('usar pickle para guardar datos como valores de las claves del diccionario ; import pickle \n')

import pickle # importa el modulo indicado

print ('crear la clase baseDEdatos ; class baseDEdatos (object) : \n')

class baseDEdatos (object) : # definicion de la clase
	def iniciar (self) : # definicion del metodo
		menu = '1 : añadirDVD - 2 : editarDVD - 3 : buscarDVD - 4 : listaDVDs - 5 : borrarDVD - S : salir \n' # asigna cadena menu
		baseDATOS = shelve.open ('./Escritorio/baseDatos.db',protocol=pickle.HIGHEST_PROTOCOL) # abre el fichero creado conel modulo shelve , usa el protocolo indicado para almacenar los datos -modulo pickle-
		while True : # bucle while continuo
			print (menu) # presenta el menu
			entradaTeclado = input ('entre opcion >> ') # espera entrada teclado 
			print ('\n') # salto de linea
			if entradaTeclado == '1' : # condicion , si se cumple
				self.añadirDVD (baseDATOS) # llama al metodo con el argumento indicado -objeto shelve-
			elif entradaTeclado == '2' : # condicion , si se cumple
				self.editarDVD (baseDATOS) # llama al metodo con el argumento indicado -objeto shelve-
			elif entradaTeclado == '3' : # condicion , si se cumple
				self.buscarDVD (baseDATOS) # llama al metodo con el argumento indicado -objeto shelve-
			elif entradaTeclado == '4' : # condicion , si se cumple
				self.listaDVDs (baseDATOS) # llama al metodo con el argumento indicado -objeto shelve-
			elif entradaTeclado == '5' : # condicion , si se cumple
				self.borrarDVD (baseDATOS) # llama al metodo con el argumento indicado -objeto shelve-
			elif entradaTeclado == 'S' or entradaTeclado == 's' : # condicion , si se cumple
				baseDATOS.close () # añade los datos y cierra el fichero de la base de datos
				sys.exit (1) # sale del script
			else : # ninguna de las opciones indicadas
				continue # vuelve al inicio del bucle
			
	def añadirDVD (self,BD) : # definicion del metodo
		entrada = input ('introduzca titulo : ') # entrada teclado
		print ('\n') # salto de linea
		try : # control de excepciones
			titulo = BD [entrada] # busca la entrada en la clave del diccionario de la base de datos -lanza excepcion si no existe la clave-
		except KeyError : # tipo de excepcion
			director = input ('introduzca director : ') # entrada teclado
			print ('\n') # salto de linea
			año = input ('introduzca año : ') # entrada teclado
			print ('\n') # salto de linea
			duracion = input ('introduzca duracion en minutos : ') # entrada teclado
			print ('\n') # salto de linea
			BD [entrada] = (director,año,duracion) # crea el diccionario a añadir a la base de datos
			BD.sync () # sincroniza los nuevos datos con los del fichero de la base de datos -añade el diccionario-
			print ('*** DVD añadido ***\n') # presenta texto
			return # devuelve None 
		if titulo : # condicion , si existe el titulo -no es False-
			print ('** EL TITULO YA EXISTE ** 	\n') # presenta la cadena
			return # devuelve None
			
	def editarDVD (self,BD) : # definicion del metodo
		entrada = input ('indique titulo : ') # entrada teclado
		print ('\n') # salto de linea
		try : # control de excepciones
			titulo = BD [entrada] # busca la entrada en la clave del diccionario de la base de datos -lanza excepcion si no existe la clave- 
		except KeyError : # tipo de excepcion
			print ('titulo no encontrado ',entrada,'\n') # presenta la cadena y su valor
			return # devuelve None
		director,año,duracion = titulo # desempaqueta la tupla , asignando los valores en el orden indicado
		while True : # bucle while continuo
			print ('1 : cambiarDIRECTOR - 2 : cambiarAÑO - 3 : cambiarDURACION - S : salir \n') # presenta menu
			opcion = input ('indique opcion : ') # entrada teclado
			print ('\n') # salto de linea
			if opcion == '1' : # condicion , si se cumple
				print ('director ',director,'\n') # presenta el valor actual
				director = input ('NUEVO DIRECTOR :') # entrada teclado
				print ('\n') # salto de linea
			elif opcion == '2' : # condicion , si se cumple
				print ('año ',año,'\n') # presenta el valor actual
				año = input ('NUEVO AÑO :') # entrada teclado
				print ('\n') # salto de linea
			elif opcion == '3' : # condicion , si se cumple
				print ('duracion ',duracion,'\n') # presenta el valor actual
				duracion = input ('NUEVA DURACION -en minutos- :') # entrada teclado
				print ('\n') # salto de linea
			elif opcion == 'S' or opcion == 's' : # condicion , si se cumple
				break # interrumpe el bucle while
		BD [entrada] = (director,año,duracion) # crea el diccionario a añadir a la base de datos 
		BD.sync () # sincroniza los nuevos datos con los del fichero de la base de datos -añade el diccionario-
		print ('*** DVD editado ***\n') # presenta texto
		return # devuelve None
	
	def buscarDVD (self,BD) : # definicion del metodo
		while True : # bucle while continuo
			coincidencias = [] # asigna una lista vacia
			buscar = input ('indique titulo a buscar : -ENTER : salir- ') # entrada teclado
			print ('\n') # salto de linea
			if not buscar : # condicion , si se cumple ; False 
				return # devuelve None
			for titulo in BD : # iterador , bucle for in , pasa los diccionarios de la base de datos a ; titulo
				if titulo == buscar : # condicion , si coinciden -titulo con valor-
					coincidencias.append (titulo) # añade el titulo a la lista de coincidencias
				if titulo.lower () == buscar : # condicion , si coinciden -titulo en minusculas con valor-
					coincidencias.append (titulo) # añade el titulo a la lista de coincidencias
				if titulo.startswith (buscar) : # condicion , si coinciden con el inicio del titulo
					coincidencias.append (titulo) # añade el titulo a la lista de coincidencias
				if titulo.lower ().startswith (buscar.lower ()) : # condicion , si coinciden con el inicio del titulo en minusculas
					coincidencias.append (titulo) # añade el titulo a la lista de coincidencias
			if len (coincidencias) == 0 : # condicion , si la lista esta vacia
				print ('*** NO SE HAN ENCONTRADO COINCIDENCIAS CON : ',buscar,'\n') # presenta la cadena y su valor -titulo a buscar-
				continue # vuelve al inicio del bucle while
			elif len (coincidencias) == 1 : # condicion , si hay un elemento -coincidencia-
				return coincidencias [0] # devuelve el titulo coincidente de la lista
			elif len (coincidencias) > 1 : # condicion , si hay mas de un elemento -coincidencia-
				for numero,elemento in enumerate (set (coincidencias),start=1) : # iterador , bucle for in , pasa los elementos de la lista a elemento y los numeros a numero -enumerate numera los elementos de la lista , empieza en 1-
					print ('Nº {0} - {1} \n'.format (numero,elemento)) # presenta una cadena formateada y su valor -numero elemento y titulo-
				else : # cuando finalice el iterador
					print ('*** FIN DE LA LISTA ***\n') # presenta la cadena
					return # devuelve None
			
	def listaDVDs (self,BD) : # definicion del metodo
		for numero,titulo in enumerate (BD,start=1)  : # iterador , bucle for in , pasa los titulos de la base de datos a ; titulo y los numeros a numero -enumerate numera los elementos de la lista , empieza en 1-
			print ('Nº {0} - {1} : DIRECTOR : {2[0]} - AÑO : {2[1]} - DURACION -minutos- : {2[2]}\n'.format (numero,titulo,BD [titulo])) # presenta una cadena formateada y su valor -numero , titulo y datos-
		else : # cuando finalice el iterador
			print ('*** FIN DE LA LISTA ***\n') # presenta la cadena
			return # devuelve None
		
	def borrarDVD (self,BD) : # definicion del metodo
		borrar = input ('indique titulo a borrar : ') # entrada teclado
		print ('\n') # salto de linea
		try : # control de excepciones
			titulo = BD [borrar] # asigna los datos del diccionario de la base de datos
		except KeyError : # tipo de excepcion
			print ('titulo no encontrado ',borrar,'\n') # presenta la cadena y su valor
			return # devuelve None
		if titulo : # condicion , si existe -True-
			print ('borrando : ',borrar,'\n') # presenta la cadena y su valor
			del BD [borrar] # borra el diccionario indicado
			BD.sync () # sincroniza los nuevos datos con los del fichero de la base de datos -borra el diccionario-
			return # devuelve None
				
print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('iniciar base de datos ; baseDEdatos ().iniciar () \n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

#baseDEdatos ().iniciar () # quitar almohadilla de inicio para ejecutar -inicia la base de datos y su menu-
		



print ('crear y administrar una base de datos SQL -RELACIONAL- con el modulo ; sqlite3 \n')

print ('importar el modulo sqlite3 ; import sqlite3 \n')

import sqlite3 # importa el modulo indicado

print ('importar modulo os.path ; import os.path \n')

import os.path # importa el modulo indicado

print ('crear la clase baseDEdatosSQL ; class baseDEdatosSQL (object) : \n')

class baseDEdatosSQL (object) : # definicion de la clase
	def iniciar (self) : # definicion del metodo
		menu = '1 : añadirDVD - 2 : editarDVD - 3 : buscarDVD - 4 : listaDVDs - 5 : borrarDVD - S : salir \n' # asigna cadena menu
		if os.path.exists ('./Escritorio/baseDatos.sql') : # condicion , si existe el fichero en la ruta indicada devuelve True
			baseDATOS_SQL = sqlite3.connect ('./Escritorio/baseDatos.sql') # abre el fichero creado con el modulo sqlite3 , si no existe lo crea 
		else : # si no existe ; False
			baseDATOS_SQL = sqlite3.connect ('./Escritorio/baseDatos.sql') # abre el fichero creado con el modulo sqlite3 , si no existe lo crea 
			cursor = baseDATOS_SQL.cursor () # crea el objeto que ejecuta las llamadas SQL 
			cursor.execute ('CREATE TABLE dvds (titulo TEXT UNIQUE NOT NULL,director TEXT NOT NULL,año INTEGER NOT NULL,duracion INTEGER NOT NULL)') # ejecuta las llamadas SQL en la base de datos del objeto -crea la tabla dvds con las columnas ; titulo , director , año ,duracion-
			baseDATOS_SQL.commit () # guarda los cambios en el fichero SQL del objeto
		while True : # bucle while continuo
			print (menu) # presenta el menu
			entradaTeclado = input ('entre opcion >> ') # espera entrada teclado 
			print ('\n') # salto de linea
			if entradaTeclado == '1' : # condicion , si se cumple
				self.añadirDVD (baseDATOS_SQL) # llama al metodo con el argumento indicado -objeto sqlite3-
			elif entradaTeclado == '2' : # condicion , si se cumple
				self.editarDVD (baseDATOS_SQL) # llama al metodo con el argumento indicado -objeto sqlite3-
			elif entradaTeclado == '3' : # condicion , si se cumple
				self.buscarDVD (baseDATOS_SQL) # llama al metodo con el argumento indicado -objeto sqlite3-
			elif entradaTeclado == '4' : # condicion , si se cumple
				self.listaDVDs (baseDATOS_SQL) # llama al metodo con el argumento indicado -objeto sqlite3-
			elif entradaTeclado == '5' : # condicion , si se cumple
				self.borrarDVD (baseDATOS_SQL) # llama al metodo con el argumento indicado -objeto sqlite3-
			elif entradaTeclado == 'S' or entradaTeclado == 's' : # condicion , si se cumple
				baseDATOS_SQL.close () # cierra el fichero de la base de datos
				sys.exit (1) # sale del script
			else : # ninguna de las opciones indicadas
				continue # vuelve al inicio del bucle

	def añadirDVD (self,BD) : # definicion del metodo
		cursor = BD.cursor () # crea el objeto que ejecuta las llamadas SQL
		titulo = input ('introduzca titulo : ') # entrada teclado
		print ('\n') # salto de linea
		if not titulo : # condicion , si es False -esta vacio-
			print ('NO A PUESTO EL TITULO \n') # presenta la cadena
			return # devuelve None
		cursor.execute ('SELECT titulo FROM dvds WHERE titulo=?',(titulo,)) # ejecuta las llamadas SQL en la base de datos del objeto -selecciona el valor indicado ; titulo-
		TITULO = cursor.fetchone () # devuelve un registro concordante o cero -datos o None-
		if not TITULO : # condicion , si es None
			director = input ('introduzca director : ') # entrada teclado
		else : # el titulo esta añadido
			print ('el titulo ya esta añadido a la base de datos \n') # presenta el texto
			return # devuelve None
		print ('\n') # salto de linea
		if not director : # condicion , si es False -esta vacio-
			print ('NO A PUESTO EL DIRECTOR \n') # presenta la cadena
			return # devuelve None
		año = input ('introduzca año : ') # entrada teclado
		print ('\n') # salto de linea
		if not año : # condicion , si es False -esta vacio-
			print ('NO A PUESTO EL AÑO \n') # presenta la cadena
			return # devuelve None
		duracion = input ('introduzca duracion en minutos : ') # entrada teclado
		print ('\n') # salto de linea
		if not duracion : # condicion , si es False -esta vacio-
			print ('NO A PUESTO LA DURACION \n') # presenta la cadena
			return # devuelve None
		cursor.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',(titulo,director,año,duracion)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas indicadas los valores indicados en la tupla-
		BD.commit () # guarda los cambios en el fichero SQL del objeto
		print ('*** DVD añadido ***\n') # presenta texto
		return # devuelve None 

	def editarDVD (self,BD) : # definicion del metodo
		entrada_titulo = input ('indique el TITULO   -ENTER : salir- >> ') # entrada teclado -titulo dvd-
		if not entrada_titulo : # condicion , si se cumple ; False
			return # devuelve None
		cursor = BD.cursor () # crea el objeto que ejecuta las llamadas SQL
		cursor.execute ('SELECT director,año,duracion FROM dvds WHERE titulo=?',(entrada_titulo,)) # ejecuta las llamadas SQL en la base de datos del objeto -selecciona año , duracion y director de la tabla dvds-
		datosDVD = cursor.fetchone () # devuelve un registro concordante o cero -datos o None-
		if  not datosDVD : # condicion , si se cumple ; False
			return # devuelve None
		director,año,duracion = datosDVD # desempaqueta los datos de la tupla en las variables indicadas -director , año , duracion-
		while True : # bucle while continuo
			print ('1 : cambiarDIRECTOR - 2 : cambiarAÑO - 3 : cambiarDURACION - S : salir \n') # presenta menu
			opcion = input ('indique opcion : ') # entrada teclado
			print ('\n') # salto de linea
			if opcion == '1' : # condicion , si se cumple
				print ('director ',director,'\n') # presenta el valor actual
				director = input ('NUEVO DIRECTOR :') # entrada teclado
				print ('\n') # salto de linea
			elif opcion == '2' : # condicion , si se cumple
				print ('año ',año,'\n') # presenta el valor actual
				año = input ('NUEVO AÑO :') # entrada teclado
				print ('\n') # salto de linea
			elif opcion == '3' : # condicion , si se cumple
				print ('duracion ',duracion,'\n') # presenta el valor actual
				duracion = input ('NUEVA DURACION -en minutos- :') # entrada teclado
				print ('\n') # salto de linea
			elif opcion == 'S' or opcion == 's' : # condicion , si se cumple
				break # interrumpe el bucle while
		cursor.execute ('UPDATE dvds SET año=:año,duracion=:duracion,director=:director WHERE titulo=:entrada_titulo',locals ()) # ejecuta las llamadas SQL en la base de datos del objeto -actualiza las columnas de la tabla indicada con los valores del diccionario que contiene las variables locales ; locals ()- 
		BD.commit () # guarda los cambios en el fichero SQL del objeto
		print ('*** DVD editado ***\n') # presenta texto
		return # devuelve None
	
	def buscarDVD (self,BD) : # definicion del metodo
		cursor = BD.cursor () # crea el objeto que ejecuta las llamadas SQL
		while True : # bucle while continuo
			buscar = input ('indique titulo a buscar : -ENTER : salir- ') # entrada teclado
			print ('\n') # salto de linea
			if not buscar : # condicion , si se cumple ; False 
				return # devuelve None
			cursor.execute ('SELECT titulo,director,año,duracion FROM dvds WHERE titulo LIKE ? ORDER BY titulo',(buscar,)) # ejecuta las llamadas SQL en la base de datos del objeto -busca las coincidencias y las ordena por titulo-
			coincidencias = cursor.fetchone () # devuelve un registro concordante o cero -titulo coincidente ordenados-
			if not coincidencias : # condicion , si es false -None-
				print ('*** NO SE HAN ENCONTRADO COINCIDENCIAS CON : ',buscar,'\n') # presenta la cadena y su valor -titulo a buscar-
				continue # vuelve al inicio del bucle while
			else : # condicion , si hay un elemento -coincidencia-
				print ('titulo : {0[0]} - director : {0[1]} - año : {0[2]} - duracion : {0[3]} \n'.format (coincidencias)) # presenta el titulo coincidente de la lista en una cadena formateada
				return # devuelve None
			
	def listaDVDs (self,BD) : # definicion del metodo
		cursor = BD.cursor () # crea el objeto que ejecuta las llamadas SQL
		cursor.execute ('SELECT titulo,director,año,duracion FROM dvds ORDER BY titulo') # ejecuta las llamadas SQL en la base de datos del objeto -selecciona los datos indicados de la tabla dvds y los ordena-
		datosSQL = cursor.fetchall () # devuelve todos los registro ordenados por el titulo -tuplas con titulo , director , año y duracion-
		if not datosSQL : # condicion , si es false -None-
			return # devuelve None
		for numero,datos in enumerate (datosSQL,start=1)  : # iterador , bucle for in , pasa las tuplas con los datos de la base de datos SQL a ; datos y los numeros a numero -enumerate numera las tuplas de la lista , empieza en 1-
			print ('Nº {0} - {1[0]}  :  - DIRECTOR : {1[1]} - AÑO : {1[2]} - DURACION -minutos- : {1[3]}\n'.format (numero,datos)) # presenta una cadena formateada y su valor -numero , titulo , director , año y duracion-
		else : # cuando finalice el iterador
			print ('*** FIN DE LA LISTA ***\n') # presenta la cadena
			return # devuelve None
	
	def borrarDVD (self,BD) : # definicion del metodo
		borrar = input ('indique titulo a borrar : -ENTER : salir-  ') # entrada teclado
		print ('\n') # salto de linea
		if not borrar : # condicion , si es False -esta vacio-
			return # devuelve None
		cursor = BD.cursor () # crea el objeto que ejecuta las llamadas SQL
		cursor.execute ('SELECT titulo FROM dvds WHERE titulo=?',(borrar,)) # ejecuta las llamadas SQL en la base de datos del objeto -selecciona el dato indicado ; titulo-
		datosBorrar = cursor.fetchone () # devuelve un registro concordante o cero -tuplas con titulo o None-
		if not datosBorrar : # condicion , si es false -None-
			return # devuelve None
		cursor.execute ('DELETE FROM dvds WHERE titulo=?',(borrar,)) # ejecuta las llamadas SQL en la base de datos del objeto -elimina el titulo indicado-
		BD.commit () # guarda los cambios en el fichero SQL del objeto
		print ('borrado : ',borrar,'\n') # presenta la cadena y su valor
		return # devuelve None
	
print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('iniciar base de datos SQL ; baseDEdatosSQL ().iniciar () \n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

#baseDEdatosSQL ().iniciar () # quitar almohadilla de inicio para ejecutar -inicia la base de datos SQL y su menu-


print ("conectar con la base de datos SQL ; baseDatosSQL = sqlite3.connect ('./Escritorio/PRUEBA.sql') \n")

baseDatosSQL = sqlite3.connect ('./Escritorio/PRUEBA.sql') # abre el fichero creado con el modulo sqlite3 , si no existe lo crea 

print ("crear el objeto cursor para mandar ordenes SQL ; CURSOR = baseDatosSQL.cursor () \n")

CURSOR = baseDatosSQL.cursor () # crea el objeto que ejecuta las llamadas SQL 

print ("ejecutar las ordenes SQL -crear tabla y columnas-; CURSOR.execute ('CREATE TABLE dvds (titulo TEXT UNIQUE NOT NULL,director TEXT NOT NULL,año INTEGER NOT NULL,duracion INTEGER NOT NULL)') \n")

CURSOR.execute ('CREATE TABLE dvds (titulo TEXT UNIQUE NOT NULL,director TEXT NOT NULL,año INTEGER NOT NULL,duracion INTEGER NOT NULL)') # ejecuta las llamadas SQL en la base de datos del objeto -crea la tabla dvds con las columnas ; titulo , director , año ,duracion-

print ("ejecutar las ordenes SQL -añadir valores en la tabla- ; CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO','EL DIRECTOR',2015,120)) \n")

CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO','EL DIRECTOR',2015,120)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados-

print ("ejecutar las ordenes SQL -añadir valores en la tabla- ; CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO1','EL DIRECTOR1',2010,120)) \n")

CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO1','EL DIRECTOR1',2010,120)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados-

print ("ejecutar las ordenes SQL -añadir valores en la tabla- ; CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO2','EL DIRECTOR2',2012,100)) \n")

CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO2','EL DIRECTOR2',2012,100)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados-

print ("ejecutar las ordenes SQL -añadir valores en la tabla- ; CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO3','EL DIRECTOR3',2011,125)) \n")

CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO3','EL DIRECTOR3',2011,125)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados-

print ("ejecutar las ordenes SQL -añadir valores en la tabla- ; CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO4','EL DIRECTOR4',2014,110)) \n")

CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO4','EL DIRECTOR4',2014,110)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados-

print ("guardar los cambios en el fichero SQL ; baseDatosSQL.commit () \n")

baseDatosSQL.commit () # guarda los cambios en el fichero SQL del objeto

print ("ejecutar las ordenes SQL -añadir valores en la tabla- ; CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO5','EL DIRECTOR5',2014,110)) \n")

CURSOR.execute ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',('EL TITULO5','EL DIRECTOR5',2014,110)) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados-

print ("retroceder cualquier transaccion -CURSOR.execute- antes que se guarde -baseDatosSQL.commit- ; baseDatosSQL.rollback () \n")

baseDatosSQL.rollback () # retrocede cualquier transaccion antes de que se guarde 

print ("el numero de filas -lectura/escritura- que devolvera la funcion fetchmany ; CURSOR.arraysize ",CURSOR.arraysize,'\n') # presenta el numero de filas -lectura/escritura- que devolvera la funcion fetchmany

print ("ejecutar las ordenes SQL -seleccionar los valores indicados- ; CURSOR.execute ('SELECT titulo,director,año,duracion FROM dvds ORDER BY titulo') \n")

CURSOR.execute ('SELECT titulo,director,año,duracion FROM dvds ORDER BY titulo') # ejecuta las llamadas SQL en la base de datos del objeto -selecciona los datos indicados de la tabla dvds y los ordena-

print ('cuenta las filas de solo lectura desde la ultima operacion ; CURSOR.rowcount ',CURSOR.rowcount,'\n')

print ("descripcion de las columnas -tupla 7 elementos por columnas- en una secuencia ; CURSOR.description \n")

for numero,columna in enumerate(CURSOR.description) : # iterador , bucle for in , pasa los numeros a numero y las tuplas a columna -enumerate numera los elementos de la tupla-
	print ('Nº {0} - {1} \n'.format (numero,columna)) # presenta la cadena formateada y sus valores -numero y tupla columna-
else : # cuando finalice el iterador
	print ('fin de la descripcion \n') # presenta la cadena 

print ('devolver una sola linea de la orden SELECT ; CURSOR.fetchone () ',CURSOR.fetchone (),'\n') # presenta una linea -la primera-

print ('devolver un numero de lineas indicadas de la orden SELECT ; CURSOR.fetchmany (2) \n')

for numero,columna in enumerate(CURSOR.fetchmany (2)) : # iterador , bucle for in , pasa los numeros a numero y las tuplas a columna -enumerate numera los elementos de la tupla-
	print ('Nº {0} - {1} \n'.format (numero,columna)) # presenta la cadena formateada y sus valores -numero y tupla columna-
else : # cuando finalice el iterador
	print ('fin de las  lineas \n') # presenta la cadena 

print ('devolver todas las lineas de la orden SELECT ; CURSOR.fetchall () \n')

for numero,columna in enumerate(CURSOR.fetchall ()) : # iterador , bucle for in , pasa los numeros a numero y las tuplas a columna -enumerate numera los elementos de la tupla-
	print ('Nº {0} - {1} \n'.format (numero,columna)) # presenta la cadena formateada y sus valores -numero y tupla columna-
else : # cuando finalice el iterador
	print ('fin de las  lineas \n') # presenta la cadena 

print ("ejecutar las ordenes SQL -añadir los valores indicados en una secuencia- ; CURSOR.executemany ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',[('nuevo TITULO','nuevo DIRECTOR',2000,90),('nuevo TITULO1','nuevo DIRECTOR1',1999,70)]) \n")

CURSOR.executemany ('INSERT INTO dvds (titulo,director,año,duracion) VALUES (?,?,?,?)',[('nuevo TITULO','nuevo DIRECTOR',2000,90),('nuevo TITULO1','nuevo DIRECTOR1',1999,70)]) # ejecuta las llamadas SQL en la base de datos del objeto -inserta en la tabla dvds en las columnas los valores indicados en la secuencia ; lista de tuplas-

print ("guardar los cambios en el fichero SQL ; baseDatosSQL.commit () \n")

baseDatosSQL.commit () # guarda los cambios en el fichero SQL del objeto

print ("ejecutar las ordenes SQL -seleccionar los valores indicados- ; CURSOR.execute ('SELECT titulo,director,año,duracion FROM dvds ORDER BY titulo') \n")

CURSOR.execute ('SELECT titulo,director,año,duracion FROM dvds ORDER BY titulo') # ejecuta las llamadas SQL en la base de datos del objeto -selecciona los datos indicados de la tabla dvds y los ordena-

print ('devolver todas las lineas de la orden SELECT ; CURSOR.fetchall () \n')

for numero,columna in enumerate(CURSOR.fetchall ()) : # iterador , bucle for in , pasa los numeros a numero y las tuplas a columna -enumerate numera los elementos de la tupla-
	print ('Nº {0} - {1} \n'.format (numero,columna)) # presenta la cadena formateada y sus valores -numero y tupla columna-
else : # cuando finalice el iterador
	print ('fin de las  lineas \n') # presenta la cadena 

print ("cerrar el objeto cursor ; CURSOR.close () \n")

CURSOR.close () # cierra el objeto cursor
	
print ("cerrar la base de datos SQL ; baseDatosSQL.close () \n")

baseDatosSQL.close () # cierra la base de datos -fichero SQL-



