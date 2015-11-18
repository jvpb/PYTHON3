#!/usr/bin/env python3
'''redes'''

# importar modulo

import sys # importa el modulo indicado

print ('VERSION en uso de PYTHON \n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

# importar modulos

import struct # importa el modulo indicado

import pickle # importa el modulo indicado

import socket # importa el modulo indicado

import socketserver # importa el modulo indicado

import gzip # importa el modulo indicado

import threading # importa el modulo indicado 

import copy # importa el modulo indicado

print ('crear clase CLIENTE ; class CLIENTE (object) : \n')

class CLIENTE (object) : # definicion de la clase
	class admistradorSOCKET (object) : # definicion de la clase anidada
		def __enter__ (self) : # definicion metodo especial 
			self.conectar = socket.socket (socket.AF_INET,socket.SOCK_STREAM) # crea el objeto socket con los protocolos indicados -protocolo IPv4 y protocolo TCP-
			self.conectar.connect (('localhost',9653)) # conecta en la ip de localhost en el puerto 9653
			return self.conectar # devuelve el objeto socket -la conexion al servidor-
		
		def __exit__ (self) : # definicion metodo especial
			self.conectar.close () # cierra la conexion con el servidor -cierra el puerto-
			
	def iniciar (self) : # definicion del metodo
		menu = '1 : EDITAR_COCHE - 2 : EDITAR_KILOMETRAJE - 3 : CAMBIAR_PROPIETARIO - 4 : NUEVO_COCHE - P : PARAR_SERVIDOR - S : SALIR ' # asigna menu de opciones
		while True : # bucle while , bucle continuo
			print (menu,'\n') # presenta el menu con sus opciones
			entrada = input ('ELIJA OPCION MENU SUPERIOR >>>> ') # espera entrada teclado
			print ('\n') # salto de linea 
			if entrada == '1' : # condicion . si se cumple
				self.obtenerDetallesCoche () # llama al metodo
			elif entrada == '2' : # condicion . si se cumple
				self.cambiarKilometraje () # llama al metodo 
			elif entrada == '3' : # condicion . si se cumple
				self.cambiarPropietario () # llama al metodo 
			elif entrada == '4' : # condicion . si se cumple
				self.nuevoRegistro () # llama al metodo 
			elif entrada == 'P' or entrada == 'p' : # condicion . si se cumple una de las dos
				self.pararServidor () # llama al metodo 
			elif entrada == 'S' or entrada == 's' : # condicion . si se cumple una de las dos
				self.salir () # llama al metodo 
				
	def obtenerDetallesCoche (self) : # definicion del metodo
		licenciaPrevia = input ('indique numero de licencia -MATRICULA COCHE- ') # asigna el valor indicado
		licencia,coche = self.recuperarDetallesCoche (licenciaPrevia) # desempaqueta la salida del metodo y lo asigna a las variables en el orden correspondiente
		if coche is not None : # condicion , si no esta vacio -None-
			print ('LICENCIA : {0}\nASIENTOS : {1}\nKILOMETRAJE : {2}\nPROPIETARIO : {3}\n'.format (licencia,coche ['asientos'],coche ['kilometraje'],coche ['propietario'])) # presenta la cadena formateada y sus valores
		return licencia # devuelve el valor 
	
	def recuperarDetallesCoche (self,licenciaPrevia) : # definicion del metodo
		licencia = licenciaPrevia # asigna valor de licenciaPrevia
		if not licencia : # condicion , si esta vacio
			return licenciaPrevia,None # devuelve una tupla con los valores indicados
		OK,datos = self.manejarPeticion ('OBTENER_DETALLES_COCHE',licencia) # desempaqueta la salida del metodo y lo asigna a las variables en el orden correspondiente
		if not OK : # condicion , si es False
			print (datos) # presenta el dato -mensaje error-
			return licenciaPrevia,None # devuelve una tupla con los valores indicados
		return licencia,datos # devuelve una tupla de dos elementos  -valor licencia y un diccionario con los valores de datos-
	
	def manejarPeticion (self,*elementos,esperarRepuesta=True) : # definicion del metodo
		tamañoStructura = struct.Struct ('!I') # asigna un valor sin signo en bytes para el tamaño de lectura y escritura binario del objeto devuelto
		datos = pickle.dumps (elementos,3) # guarda los datos serializados en formato pickle -protocolo 3 , compatible con todas las versiones de la rama 3 de python- , devuelve un objeto binario pickle
		try : # control de excepciones
			with self.admistradorSOCKET () as conexion : # abre y cierra el puerto del servidor en la IP por defecto indicado en la clase ; admistradorSOCKET , enlazado como conexion
				conexion.sendall (tamañoStructura.pack (len (datos))) # envia los datos al socket -pack devuelve un objeto contenedor Struct del tamaño indicado por len , len devuelve el numero de elementos del argumento pasado-
				conexion.sendall (datos) # envia los datos al socket -datos serializados en formato pickle-
				if not esperarRepuesta : # condicion , si es False
					return # devuelve None
				tamañoDatos = conexion.recv (tamañoStructura.size) # recibe datos desde el socket -del tamaño indicado en bytes por size-
				tamaño = tamañoStructura.unpack (tamañoDatos) [0] # desempaqueta el bloque de bytes del tamaño indicado recibido por el socket -asigna el valor de la posicion indicada ; 0-
				resultado = bytearray () # asigna la funcion -convierte la cadena binaria en modificable-
				while True : # bucle continuo while -mientras se cumpla la condicion-
					dato = conexion.recv (4000) # recibe datos desde el socket -del tamaño indicado en bytes-
					if not dato : # condicion , si esta vacio -False-
						break # interrumpe el bucle while
					resultado.extend (dato) # añade la cadena binaria del tamaño indicado
					if len (resultado) >= tamaño : # condicion , si el tamaño de la cadena en formato byte es mayor o igual al indicado en ; tamaño
						break # interrumpe el bucle while
			return pickle.loads (resultado) # devuelve los datos serializados en formato pickle del objeto binario -resultado-
		except socket.error as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : esta el SERVIDOR funcionando ?\n'.format (error)) # presenta la cadena formateada con el error de salida
			sys.exit (1) # sale del script que se esta ejecutando con codigo de error ; 1
		
	def cambiarKilometraje (self) : # definicion del metodo
		licenciaPrevia = input ('indique numero de licencia -MATRICULA COCHE- ') # asigna el valor indicado
		licencia,coche = self.recuperarDetallesCoche (licenciaPrevia) # desempaqueta la salida del metodo y lo asigna a las variables en el orden correspondiente
		if coche is None : # condicion , si es None
			return licenciaPrevia # devuelve el valor de entrada
		kilometraje = coche ['kilometraje'] # asigna el valor de kilometraje del diccionario
		if kilometraje [1] == 0 : # condicion , si se cumple
			return licencia # devuelve el valor de licencia
		Kilometraje = input ('INTRODUZCA NUEVO KILOMETRAJE ') # espera entrada teclado -numero de kilometros-
		print ('\n') # salto de linea
		OK,datos = self.manejarPeticion ('CAMBIAR_KILOMETRAJE',licencia,int (kilometraje)) # desempaqueta la salida del metodo y lo asigna a las variables en el orden correspondiente -int convierte la cadena con valor numerico en numero int-
		if not OK : # condicion , si es False
			print (datos) # presenta el dato -mensaje error-
		else : # es True 
			print ('KILOMETRAJE A SIDO CAMBIADO\n') # presenta la cadena
		return licencia # devuelve el valor de licencia
	
	def cambiarPropietario (self) : # definicion del metodo
		licenciaPrevia = input ('indique numero de licencia -MATRICULA COCHE- ') # asigna el valor indicado
		licencia,coche = self.recuperarDetallesCoche (licenciaPrevia) # desempaqueta la salida del metodo y lo asigna a las variables en el orden correspondiente
		if coche is None : # condicion , si es None
			return licenciaPrevia # devuelve el valor de entrada
		propietario = coche ['propietario'] # asigna el valor de propietario del diccionario
		if propietario is None : # condicion , si se cumple
			return licencia # devuelve el valor de licencia
		Propietario = input ('INTRODUZCA NUEVO PROPIETARIO ') # espera entrada teclado -nombre propietario-
		print ('\n') # salto de linea
		OK,datos = self.manejarPeticion ('CAMBIAR_PROPIETARIO',licencia,Propietario) # desempaqueta la salida del metodo y lo asigna a las variables en el orden correspondiente
		if not OK : # condicion , si es False
			print (datos) # presenta el dato -mensaje error-
		else : # es True 
			print ('PROPIETARIO A SIDO CAMBIADO\n') # presenta la cadena
		return licencia # devuelve el valor de licencia

	def nuevoRegistro (self) : # definicion del metodo
		licenciaPrevia = input ('indique numero de licencia -MATRICULA COCHE- ') # asigna el valor indicado
		licencia = licenciaPrevia # asigna el valor de entrada
		diccionario = {} # diccionario vacio
		# asientos , kilometraje , propietario
		for entrada in ('asientos','kilometraje','propietario') : # iterador , bucle for in , pasa las cadenas a entrada
			if entrada in ('asientos','kilometraje') : # condicion , si los valores estan en la tupla -cadena-
				diccionario [entrada] = int (input ('{0} '.format (entrada))) # añade al diccionario la entrada correspondiente -int convierte un numero en formato cadena a numero entero-
			else : # si no esta en la tupla 
				diccionario [entrada] = input ('{0} '.format (entrada)) # añade al diccionario la entrada correspondiente
		self.manejarPeticion ('NUEVO_REGISTRO',licencia,diccionario) # envia al servidor los datos indicados
		print ('ENTRADA REGISTRADA\n') # presenta la cadena
		return licencia # devuelve el valor de licencia
	
	def pararServidor (self) : # definicion del metodo
		self.manejarPeticion ('PARAR_SERVIDOR',esperarRepuesta=False) # envia al servidor los datos indicados -NO ESPERA RESPUESTA-
		sys.exit () # salir del script -deja de ejecutarse-
		
	def salir (self) : # definicion del metodo
		sys.exit () # salir del script -deja de ejecutarse-
	
print ('crear clase SERVIDOR ; class SERVIDOR (object) : \n')

class SERVIDOR (object) : # definicion de la clase
	class servidorRegistracionCoche (socketserver.ThreadingMixIn,socketserver.TCPServer) : # definicion de la clase anidada -hereda ThreadingMixIn y TCPServer de socketserver- , utiliza canales thread -hilos- y protocolo TCP 
		pass # funcion de relleno -no hace nada-
	
	class manejarRepuesta (socketserver.StreamRequestHandler) : # definicion de la clase anidada -hereda StreamRequestHandler- , para protocolo TCP 
		bloquearCoche = threading.Lock () # bloquea el hilo con los datos
		bloquearLLamada = threading.Lock () # bloquea el hilo con los datos
		llamada = dict (OBTENER_DETALLES_COCHE = (lambda self,*argumentos : self.obtenerDetallesCoche (*argumentos)),
							 CAMBIAR_KILOMETRAJE = (lambda self,*argumentos : self.cambiarKilometraje (*argumentos)),
							 CAMBIAR_PROPIETARIO = (lambda self,*argumentos : self.cambiarPropietario (*argumentos)),
							 NUEVO_REGISTRO = (lambda self,*argumentos : self.nuevoRegistro (*argumentos)),
							 PARAR_SERVIDOR = lambda self,*argumentos : self.pararServidor (*argumentos)) # diccionario , guarda las llamadas enviadas por el cliente y el resultado de sus metodos asociados en el servidor
		
		def handle (self) : # definicion del metodo -se llama por defecto cada vez que se hace una solicitud-
			tamañoStructura = struct.Struct ('!I') # asigna un valor sin signo en bytes para el tamaño de lectura y escritura binario del objeto devuelto
			tamañoDatos = self.rfile.read (tamañoStructura.size) # lee los datos que vienen del cliente por el objeto fichero
			tamaño = tamañoStructura.unpack (tamañoDatos) [0] # desempaqueta los datos del formato struct y asigna el valor de la posicion 0
			datos = pickle.loads (self.rfile.read (size)) # devuelve los datos serializados en formato pickle leidos del cliente por el objeto fichero
			try : # control de excepciones
				with self.bloquearLLamada : # abre y cierra el canal -thread- con los datos 
					funcion = llamada [datos [0]] # asigna la funcion correspondiente a la clave del diccionario
				respuesta = funcion (self,datos [1]) # asigna el resultado de la funcion llamada y su argumentos -diccionario de la posicion 1-
			except Finish : # tipo de excepcion
				return # devuelve None
			DATOS = pickle.dumps (respuesta,3) # guarda los datos serializados en formato pickle -protocolo 3 , compatible con todas las versiones de la rama 3 de python- , devuelve un objeto binario pickle
			self.wfile.write (tamañoStructura.pack (len (DATOS))) # devuelve los datos al cliente -pack devuelve un objeto contenedor Struct del tamaño indicado por len , len devuelve el numero de elementos del argumento pasado-
			self.wfile.write (DATOS) # envia los datos en formato pickle
			
		def obtenerDetallesCoche (self,licencia) : # definicion del metodo
			with self.bloquearCoche : # abre y cierra el canal -thread- con los datos
				coche = copy.copy (self.Coche.get (licencia,None)) # hace una copia de los datos de la licencia indicada -diccionario-
				if coche is not None : # condicion , si no es None -contiene los datos-
					return (True,coche) # devuelve una tupla con los valores indicados -OK y diccionario datos coche-
				return (False,'*** ESTA LICENCIA NO ESTA REGISTRADA ***\n') # devuelve una tupla 2 elementos -si la licencia no esta- , False y cadena de error
			
		def cambiarKilometraje (self,licencia,kilometraje) : # definicion del metodo
			if kilometraje < 0 : # condicion , si se cumple la condicion -numero negativo-
				return (False,'el valor de kilometraje no puede ser negativo \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
			with self.bloquearCoche : # abre y cierra el canal -thread- con los datos 
				coche = self.Coche.get (licencia,None) # asigna los datos de la licencia indicada -diccionario- o None si no esta
				if coche is not None : # condicion , no es None -contiene datos-
					if coche ['kilometraje'] < kilometraje : # condicion , si el valor es menor que el del argumento -kilometraje-
						coche ['kilometraje'] = kilometraje # asigna el valor del argumento al del diccionario
						return (True,None) # devuelve el valor True para OK y None
					else : # si el valor es MAYOR  que el del argumento -kilometraje-
						return (False,'no se puede volver atras el kilometraje del contador \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
				else : # el valor es None
					return (False,'*** ESTA LICENCIA NO ESTA REGISTRADA ***\n') # devuelve la tupla con el valor para OK de False y el mensaje de error
				
		def cambiarPropietario (self,licencia,propietario) : # definicion del metodo
			with self.bloquearCoche : # abre y cierra el canal -thread- con los datos 
				coche = self.Coche.get (licencia,None) # asigna los datos de la licencia indicada -diccionario- o None si no esta
				if coche is not None : # condicion , no es None -contiene datos-
					if coche ['propietario'] != propietario : # condicion , si el valor es distinto que el del argumento -propietario-
						coche ['propietario'] = propietario # asigna el valor del argumento al del diccionario
						return (True,None) # devuelve el valor True para OK y None
					else : # si el valor es IGUAL  que el del argumento -propietario-
						return (False,'no se puede cambiar : es el mismo propietario \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
				else : # el valor es None
					return (False,'*** ESTA LICENCIA NO ESTA REGISTRADA ***\n') # devuelve la tupla con el valor para OK de False y el mensaje de error
				
		def nuevoRegistro (self,licencia,diccionario) : # definicion del metodo
			if not licencia : # condicion , si esta vacio -False-
				return (False,'licencia esta vacio \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
			if diccionario ['asientos'] not in (2,4,5,6,7,8,9) : # condicion , si el valor indicado del diccionario no esta en la tupla de valores 
				return (False,'no se puede registrar el coche con el numero indicado de asientos \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
			if diccionario ['kilometraje'] < 0 : # condicion , si se cumple la condicion -numero negativo-
				return (False,'el valor de kilometraje no puede ser negativo \n') # devuelve la tupla con el valor para OK de False y el mensaje de error 
			if not diccionario ['propietario'] : # condicion , si esta vacio -False-
				return (False,'propietario esta vacio \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
			with self.bloquearCoche : # abre y cierra el canal -thread- con los datos
				if licencia not in self.Coche : # condicion , si licencia no esta en el diccionario
					self.Coche [licencia] = diccionario # añade la licencia al diccionario como clave y el diccionario de datos como valor
					return (True,None) # devuelve el valor True para OK y None
				else : # licencia en el diccionario
					return (False,'no se puede registrar una licencia duplicada \n') # devuelve la tupla con el valor para OK de False y el mensaje de error
					
		def pararServidor (self,*ignorarARGUMENTOS) : # definicion del metodo
			self.servidor.shutdown () # para el servidor
			raise Finish () # lanza la excepcion indicada

	def iniciar (self) : # definicion del metodo
		coche = self.cargarFichero () # carga datos del fichero 
		print ('cargados {0} registros coche\n'.format (len (coche))) # presenta una cadena formateada y su valor -numero de registros-
		self.manejarRepuesta.Coche = coche # asigna los datos al atributo externo asignado a la clase ; Coche
		servidor = None # asigna el valor indicado
		try : # control de excepciones
			servidor = self.servidorRegistracionCoche (('',9653),self.manejarRepuesta) # crea el servidor con los argumentos indicados
			servidor.serve_forever () # inicia el servidor
		except Exception as error : # tipo de excepcion , pasa la salida a error
			print ('*** ERROR *** : {0} \n'.format (error)) # presenta una cadena formateada y su valor -salida error-
		finally : # se produzca o no la excepcion , ejecuta el codigo
			if servidor is not None : # condicion , si no es None -False- , contiene datos
				servidor.shutdown () # para el servidor
				self.guardarFichero (coche) # guarda los datos en el fichero -formato pickle-
				print ('guardados {0} registros coche \n'.format (len (coche))) # presenta una cadena formateada y su valor -numero de registros-
			
	def cargarFichero (self) : # definicion del metodo
		try : # control de excepciones
			with gzip.open ('./Escritorio/DATOS_COCHES.dat','rb') as objetoFichero : # abre y cierra el fichero -enlazado como objetoFichero- , abre el fichero en formato comprimido gzip -modo solo lectura binaria-
				return pickle.load (objetoFichero) # devuelve los datos deserializados del fichero en formato pickle
		except pickle.UnpicklingError as error : # tipo de excepcion , pasa la salida a error
			print ('el SERVIDOR no ha encontrado datos de carga : {0}\n'.format (error)) # presenta una cadena formateada y su valor -salida error-
			sys.exit (1) # sale del script que se esta ejecutando con codigo de error ; 1 
		except FileNotFoundError as error : # tipo de excepcion , pasa la salida a error
			print ('fichero NO encontrado : {0} \n'.format (error)) # presenta una cadena formateada y su valor -salida error-
			print ('creando fichero : DATOS_COCHES.dat \n')
			with gzip.open ('./Escritorio/DATOS_COCHES.dat','wb') as objetoFichero : # abre y cierra el fichero -enlazado como objetoFichero- , abre el fichero en formato comprimido gzip -modo solo escritura binaria-
				print ('fichero creado : DATOS_COCHES.dat \n') # presenta la cadena 
				
	def guardarFichero (self,datos) : # definicion del metodo
		try : # control de excepciones
			with gzip.open ('./Escritorio/DATOS_COCHES.dat','wb') as objetoFichero : # abre y cierra el fichero -enlazado como objetoFichero- , abre el fichero en formato comprimido gzip -modo solo escritura binaria-
				DATOS = pickle.dumps (datos,3) # guarda los datos serializados en formato pickle -protocolo 3 , compatible con todas las versiones de la rama 3 de python- , devuelve un objeto binario pickle
				objetoFichero.write (DATOS) # escribe los datos en formato pickle en el fichero comprimido con gzip
		except pickle.PicklingError as error : # tipo de excepcion , pasa la salida a error
			print ('el SERVIDOR no ha podido guardar los datos : {0}\n'.format (error)) # presenta una cadena formateada y su valor -salida error-
			sys.exit (1) # sale del script que se esta ejecutando con codigo de error ; 1 

#################################################################################################################################################

# INICIAR EL CLIENTE : CLIENTE().iniciar ()

#CLIENTE().iniciar () # quitar almohadilla inicio para ejecutar 



#################################################################################################################################################

# INICIAR EL SERVIDOR : SERVIDOR().iniciar ()

#SERVIDOR().iniciar () # quitar almohadilla inicio para ejecutar
	
	
