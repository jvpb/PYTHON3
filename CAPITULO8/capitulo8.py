#!/usr/bin/env python3
'''tecnicas avanzadas de programacion'''

# importar modulo

import sys 

print ('VERSION en uso de PYTHON\n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('bifurcacion con diccionarios \n')

print ('crear funciones a utilizar ; funcionPrimera , funcionSegunda , funcionTercera , funcionCuarta y funcionQuinta \n')

def funcionPrimera () : # definicion de la funcion
	return 'esta es la funcion ; funcionPrimera () que a sido llamada por el diccionario ; funciones' # devuelve la cadena

def funcionSegunda () : # definicion de la funcion
	return 'esta es la funcion ; funcionSegunda () que a sido llamada por el diccionario ; funciones' # devuelve la cadena

def funcionTercera () : # definicion de la funcion
	return 'esta es la funcion ; funcionTercera () que a sido llamada por el diccionario ; funciones' # devuelve la cadena

def funcionCuarta () : # definicion de la funcion
	return 'esta es la funcion ; funcionCuarta () que a sido llamada por el diccionario ; funciones' # devuelve la cadena

def funcionQuinta () : # definicion de la funcion
	return 'esta es la funcion ; funcionQuinta () que a sido llamada por el diccionario ; funciones' # devuelve la cadena

print ('crear el diccionario funciones ; funciones = {1 : funcionPrimera,2 : funcionSegunda,3 : funcionTercera,4 : funcionCuarta,5 : funcionQuinta} \n')

funciones = {1 : funcionPrimera,2 : funcionSegunda,3 : funcionTercera,4 : funcionCuarta,5 : funcionQuinta}

print ('usar el diccionario como bifurcacion : \n')

for clave in funciones : # iterador , bucle for in , pasa las claves del diccionario a clave
	print ('funciones [{0}] () \n'.format (clave)) # presenta la cadena formateada
	print ('EQUIVALE A : \n') # presenta la cadena
	print (funciones [clave].__name__,' ()\n') # presenta el valor de la clave -nombre de la funcion-
	print (funciones [clave] (),'\n')  # ejecuta la funcion asignada a la clave del diccionario funciones y presenta el resultado devuelto pòr la funcion
else : # cuando finalice el iterador
	print ('FIN DE LAS FUNCIONES DE LAS CLAVES DEL DICCIONARIO\n') # presenta la cadena
	

print ('generadores de expresiones y funciones \n')

print ('crear funcion generadora ; ordenarClaveEnElementosCONyield (diccionario) \n')

def ordenarClaveEnElementosCONyield (diccionario) : # definicion de la funcion
	for clave in sorted (diccionario) : # iterador , bucle for in , pasa las claves del diccionario a clave -sorted ordena el diccionario por sus claves-
		yield clave,diccionario [clave] # iterador , almacena el par clave,valor del diccionario ordenado
		
print ("Diccionario = {3 : 'tres',1 : 'uno',4 : 'cuatro',2 : 'dos',5 : 'cinco'} \n")

Diccionario = {3 : 'tres',1 : 'uno',4 : 'cuatro',2 : 'dos',5 : 'cinco'} # diccionario 

print ('iterar el generador ; for elemento in ordenarClaveEnElementosCONyield (Diccionario) : \n')

for elemento in ordenarClaveEnElementosCONyield (Diccionario) : # iterador , bucle for in , pasa el elemento par del generador -yield- a elemento
	print ('PAR : ',elemento,'\n') # presenta la cadena y su valor el par clave,valor

print ('crear funcion generadora ; ordenarClaveEnElementosPORcompresion (diccionario) \n')

def ordenarClaveEnElementosPORcompresion (diccionario) : # definicion de la funcion
	return ((clave,diccionario [clave]) for clave in sorted (diccionario)) # devuelve tupla por compresion con par (clave,valor) 
	
print ('iterar el generador ; for elemento in ordenarClaveEnElementosPORcompresion (Diccionario) : \n')

for elemento in ordenarClaveEnElementosPORcompresion (Diccionario) : # iterador , bucle for in , pasa el elemento par generado por compresion a elemento
	print ('PAR : ',elemento,'\n') # presenta la cadena y su valor el par clave,valor

print ('presentarlo en formato lista con la funcion list ; list (ordenarClaveEnElementosCONyield (Diccionario)) ',list (ordenarClaveEnElementosCONyield (Diccionario)),'\n') # presenta la salida en formato lista

print ('presentarlo en formato tupla con la funcion tuple ; tuple (ordenarClaveEnElementosCONyield (Diccionario)) ',tuple (ordenarClaveEnElementosCONyield (Diccionario)),'\n') # presenta la salida en formato

print ('crear un generador sin limites ; generadorCuartosSINlimites (cuartos=0.0) \n')
	
def generadorCuartosSINlimites (cuartos=0.0) : # definicion de la funcion , valor por defecto
	while True : # bucle while continuo
		yield cuartos # almacena el valor actual
		cuartos += 0.25 # suma el valor al valor actual -asignacion aumentada-
		
print ('iterar ; for Cuarto in generadorCuartosSINlimites () : \n')

for Cuarto in generadorCuartosSINlimites () : # iterador , bucle for in , pasa el elemento de yield a Cuarto -funcion generadora sin limites-
	print (Cuarto,'\n') # presenta el valor actual
	if Cuarto == 1.0 : # condicion , cuando coincida el valor con el indicado
		print ('interrumpido el iterador y el uso del generador mediante ; if Cuarto == 1.0 : break\n') # presenta la cadena
		break # interrumpe el iterador y el uso del generador

print ('generador de cuartos ; cuartos (cuarto=0.0) \n')

def cuartos (cuarto=0.0) : # definicion de la funcion , valor por defecto
	while True : # bucle while continuo
		recibido = (yield cuarto) # asigna el iterador y sus valores
		if recibido is None : # condicion , si el valor es None -0-
			cuarto += 0.25 # suma el valor al valor actual -asignacion aumentada-
		else : # si no esta vacio
			cuarto = recibido # asigna el iterador al parametro -0.25-
			
print ('uso del generador cuartos \n')

resultado = [] # lista vacia

generador = cuartos () # asigna la funcion indicada

while len (resultado) < 10 : # bucle while , mientras se cumpla la condicion
	print ('RESULTADO : {0} - {1} ELEMENTOS \n'.format (resultado,len (resultado))) # prersenta el contenido de la lista actualizado en una cadena formateada
	siguiente = next (generador) # funcion integrada , devuelve el siguiente elemento del iterador
	if abs (siguiente - 0.5) < sys.float_info.epsilon : # condicion , si el valor aaabsoluto es menor al de epsilon
		siguiente = generador.send (1.0) # envia el valor indicado al iterador 
	resultado.append (siguiente) # añade el valor del iterador a la lista -suma un elemento mas a la lista-
	
print ('identificar un Sistema Operativo con ; sys.platform.startswith ("nomenclatura_S_O") \n')

print ('funcion obtenerFicheros -version segun Sistema Operativo- \n')

if sys.platform.startswith ("win") : # condicion , si empieza por la nomenclatura indicada -windows-
	def obtenerFicheros (nombres) : # definicion de la funcion -para windows-
		'''funcion para windows''' # documentacion de la funcion -docstring-
		import glob # importa el modulo indicado
		import os.path # importa el modulo indicado del paquete os
		for nombre in nombres : # iterador , bucle for in , pasa los nombres de la lista a nombre
			if os.path.isfile (nombre) : # condicion , si el fichero existe -True-
				yield nombre # añade el nombre al iterador
			else : # si no es un fichero
				for fichero in glob.iglob (nombre) : # iterador , bucle for in , pasa los elementos similares del iterador -iglob- a fichero
					if not os.path.isfile (fichero) : # condicion , si no es un fichero
						continue # vuelve al siguiente elemento del iterador
					yield fichero # añade el nombre del fichero al iterador 
else : # ES UNIX -no windows-
	def obtenerFicheros (nombres) : # definicion de la funcion -para Sistemas UNIX-
		'''funcion para sistemas UNIX''' # documentacion de la funcion -docstring-
		import os.path # importa el modulo indicado del paquete os
		return (fichero for fichero in nombres if os.path.isfile (fichero)) # devuelve una lista por compresion de nombres de ficheros en una tupla -añade el nombre si cumple la condicion if-

print ('version de la funcion ; obtenerFicheros (nombres) ',obtenerFicheros.__doc__,'\n') # presenta la documentacion de la funcion -version-

print ('evaluar una expresion en formato cadena mediante eval ; eval ("((2 * 5) / 2) - 1") ',eval ("((2 * 5) / 2) - 1"),'\n') # presenta el resultado de la operacion matematica evaluada -4-

print ('ejecutar codigo en una cadena con exec () \n')

codigo = '''
def areaDEesfera (radio) : # definicion de la funcion
   import math # importa el modulo mindicado
   return 4 * math.pi * radio ** 2 # devuelve el area de la esfera
''' # codigo en cadena multilinea

print ('codigo = {0} \n'.format (codigo)) # presenta la cadena formateada

print ('ejecutar el codigo de la cadena ; exec (codigo) \n')

exec (codigo) # ejecuta el codigo de la cadena multilinea

print ('areaDEesfera (2) ',areaDEesfera (2),'\n') # presenta el resultado de la funcion y su argumento

print ('crear clase importacionDinamicaMODULOS \n')

class importacionDinamicaMODULOS (object) : # definicion de la clase
	def principal (self) : # definicion del metodo -si se pone como funcion en un modulo definirlo como ; def main () :-
		import os # importa el modulo indicado
		modulos = self.cargarMODULOS () # asigna el metodo
		obtenerFuncionesTipoFichero = [] # asigna lista vacia
		for modulo in modulos : # iterador , bucle for in , pasa los modulos de la lista a modulo
			obtenerTipoFichero = self.obtenerFuncion (modulo,'obtenerTipoFichero') # asigna el metodo y su argumento
			if obtenerTipoFichero is not None : # condicion , si no es None
				obtenerFuncionesTipoFichero.append (obtenerTipoFichero) # añade la funcion a la lista
		for fichero in self.obtenerFicheros (sys.argv [1 : ]) : # iterador , bucle for in , pasa los nombres de los ficheros de la tupla a fichero
			objetoFichero = None # asignada None
			try : # control de excepciones
				objetoFichero = open (fichero,'rb') # abre el fichero en modo solo lectura binario
				cadenaByte = objetoFichero.read (1000) # lee los primeros 1000 byte's del fichero 
				for obtenerTipoFichero in obtenerFuncionesTipoFichero : # iterador , bucle for in , pasa la lista de funciones a obtenerTipoFichero
					tipoFichero = obtenerTipoFichero (cadenaByte,os.path.splitext (fichero) [1]) # asigna el resultado de la funcion y sus argumentos -cadena binaria , nombre fichero-
					if tipoFichero is not None : #condicion , si no es None
						print ('{0:.<20} {1}'.format (tipoFichero,fichero)) # presenta la cadena formateada y sus valores -funcion , fichero-
						break # interrumpe el iterador -for in-
					else : # si es None
						print ('{0:.<20} {1}'.format ('DESCONOCIDO',fichero)) # presenta la cadena formateada y sus valores -cadena , fichero-
			except EnvironmentError as error : # tipo de excepcion , pasa la salida a error
				print (error) # presenta la salida de error
			finally : # lance la excepcion o no ; ejecuta el codigo
				if objetoFichero is not None : # condicion , si no es None
					objetoFichero.close () # cierra el fichero que enlaza el objeto fichero
	
	def cargarMODULOS (self) : # definicion del metodo
		import os # importa el modulo indicado
		modulos = [] # asigna lista vacia
		for nombre in os.listdir (os.path.dirname (__file__) or '.') : # iterador , bucle for in , pasa la lista del directorio de la ruta indicada o el comodin '.' -punto-
			if nombre.endswith ('.py') and 'cadenaByte' in nombre : # condicion , si el fichero termina en la cadena indicada -'.py'- y la cadena 'cadenaByte' en el nombre del fichero
				nombreFichero = nombre # asigna el nombre del fichero
				nombre = os.path.splitext (nombre) [0] # asigna el nombre del fichero sin extensiones
				if nombre.isidentifier () and nombre not in sys.modules : # condicion , si tiene identificador y no esta en el diccionario de modulos cargados
					objetoFichero = None # asignada None
					try : # control de excepciones
						objetoFichero = open (nombreFichero,'r',encoding='utf8') # abre el fichero en modo solo lectura , codificado en unicode UTF-8
						codigo = objetoFichero.read () # lee el contenido del fichero y lo devuelve en una sola cadena
						modulo = type (sys) (nombre) # asigna el tipo del objeto -modulo y nombre fichero-
						sys.modules [nombre] = modulo # añade el nombre del fichero y el modulo al diccionario de modulos cargados
						exec (codigo,modulo.__dict__) # ejecuta el codigo de la cadena con los argumentos del valor de modulo en formato diccionario -comprueba sys.modules-
						modulos.append (modulo) # añade el modulo a la lista 
					except (EnvironmentError,SyntaxError) as error : # tipo de excepcion , pasa la salida a error
						sys.modules.pop (nombre,None) # elimina el nombre del diccionario de modulos cargados
						print (error) # presenta la salida de error
						print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
						print ('segunda validacion de los modulos\n') # presenta la cadena
						try : # control de excepciones
							exec ('import' + nombre) # ejecuta el codigo de la cadena -importa el modulo-
							modulos.append (sys.modules [nombre]) # añade el modulo a la lista
						except SyntaxError as error : # tipo de excepcion , pasa la salida a error
							print (error) # presenta la salida de error
							print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
							print ('validacion basica de los modulos\n') # presenta la cadena
							try : # control de excepciones
								modulo = __import__ (nombre) # asigna el modulo importado
								modulos.append (modulo) # añade el modulo a la lista
							except (ImportError,SyntaxError) as error : # tipo de excepcion , pasa la salida a error
								print (error) # presenta la salida de error
								print ('FIN DE LAS VALIDACIONES ** ERROR IMPORTACION** \n') # presenta la cadena
					finally : # lance la excepcion o no ; ejecuta el codigo
						if objetoFichero is not None : # condicion , si no es None
							objetoFichero.close () # cierra el fichero que enlaza el objeto fichero
		return modulos # devuelve la lista de modulos cargados -ejecutados-
	
	def obtenerFuncion (self,modulo,nombreFuncion) : # definicion del metodo
		funcion = self.obtenerFuncion.cache.get ((modulo,nombreFuncion),None) # asigna la cache del objeto con los argumentos indicados
		if funcion is None : # condicion , si es None
			try : # control de excepciones
				funcion = getattr (modulo,nombreFuncion) # asigna el atributo del modulo -nombre de la funcion-
				if not hasattr (funcion,'__call__') : # si la funcion no pertenece al modulo llamado -False-
					raise AttributeError () # lanza la excepcion indicada
				self.obtenerFuncion.cache [modulo,nombreFuncion] = funcion # asigna la funcion a la cache del objeto
			except AttributeError : # tipo de excepcion
				funcion = None # asigna None
		return funcion # devuelve None o el diccionario de modulo : funcion
	
	obtenerFuncion.cache = {} # añade atributo externo al metodo de la clase -diccionario vacio-
		
	def obtenerFicheros (self,nombres) : # definicion del metodo -para Sistemas UNIX-
		'''funcion para sistemas UNIX''' # documentacion de la funcion -docstring-
		import os # importa el modulo indicado
		return (fichero for fichero in nombres if os.path.isfile (fichero)) # devuelve una lista por compresion de nombres de ficheros en una tupla -añade el nombre si cumple la condicion if-
	

print ('importar un modulo con el metodo especial __import__ ; importar = __import__ ("os") \n')

importar = __import__ ("os") # asigna el modulo importado

print ("importar.listdir ('/') \n")

print (importar.listdir ('/'),"\n") # presenta el contenido del directorio raiz

print ('compilar el codigo en una cadena con compile ; compilarCadena = compile ("2 + 2","moduloFalso","eval") \n')

compilarCadena = compile ("2 + 2","moduloFalso","eval") # compila la cadena para usarla con eval

print ('evaluar el objeto compilado ; eval (compilarCadena) ',eval (compilarCadena),'\n') # presenta el resultado de la evaluacion del objeto compilado

print ('crear clase con atributo ; claseCONatributo \n')

class claseCONatributo (object) : # definicion de la clase
	atributo = 'este es el unico atributo de la clase ; claseCONatributo ()' # atributo de la clase
	
print ('llamar al atributo de claseCONatributo ; claseCONatributo().atributo ',claseCONatributo().atributo,'\n') # presenta el valor del atributo indicado de la clase

print ('eliminar el atributo de una clase con delattr ; delattr (claseCONatributo,"atributo") \n')

delattr (claseCONatributo,"atributo") # elimina el atributo del objeto

try : # control de excepciones
	print ('llamar al atributo de claseCONatributo ; claseCONatributo().atributo \n')
	print (claseCONatributo().atributo,'\n') # presenta el valor del atributo indicado de la clase
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('ATRIBUTO ELIMINADO : {0} \n'.format (error)) # presenta la cadena formateada y su valor -error de salida-

print ('lista de funciones y metodos a usar con una funcion o objeto con dir ; dir (claseCONatributo) \n')

print (dir (claseCONatributo),'\n') # presenta lista de funciones y metodos a usar 

print ('evaluar codigo en una cadena con eval ; eval ("4 * 2") ',eval ("4 * 2"),'\n') # presenta el valor de la cadena evaluada -8-

print ('ejecutar el codigo en una cadena con exec ; exec ("def funcionEXEC () : return \'esta es la funcion ; funcionEXEC () ejecutada de la cadena\'") \n')

exec ("def funcionEXEC () : return 'esta es la funcion ; funcionEXEC () ejecutada de la cadena' ") # ejecuta las sentencias de la cadena , creando la funcion

print ('funcionEXEC () ',funcionEXEC (),'\n') # presenta la cadena devuelta por la funcion creada con exec 

print ('exec ("class CLASE (object) : ATRIBUTO = \'esta es la cadena de ATRIBUTO de la clase ; CLASE\' ") \n')

exec ("class CLASE (object) : ATRIBUTO = 'esta es la cadena de ATRIBUTO de la clase ; CLASE' ") # ejecuta las sentencias de la cadena , creando la clase

print ('devolver el valor del atributo de una clase con getattr ; getattr (CLASE,"ATRIBUTO") ',getattr (CLASE,"ATRIBUTO"),'\n') # presenta el valor del atributo indicado de la clase

print ('devolver el valor del atributo de una clase con getattr ; getattr (claseCONatributo,"atributo","ERROR : el atributo no existe") \n')

print (getattr (claseCONatributo,"atributo","ERROR : el atributo no existe"),'\n') # presenta la cadena al no existir el atributo indicado de la clase

print ('devolver diccionario con valores globales actuales con globals ; globals () \n')

print (globals (),'\n') # presenta el diccionario de elementos actuales globales

print ('devolver True si el atributo pertenece a la clase con hasattr ; hasattr (CLASE,"ATRIBUTO") ',hasattr (CLASE,"ATRIBUTO"),'\n') # presenta True si el atributo pertenece a la clase , lo contrario False

print ('devolver True si el atributo pertenece a la clase con hasattr ; hasattr (claseCONatributo,"atributo") ',hasattr (claseCONatributo,"atributo"),'\n') # presenta True si el atributo pertenece a la clase , lo contrario False

print ('devolver diccionario con valores locales actuales con locals ; locals () \n')

print ('crear la clase locales \n')

class locales (object) : # definicion de la clase 
	A1 = 'PRIMERO' # atributo de la clase
	A2 = 'SEGUNDO' # atributo de la clase
	A3 = 'TERCERO' # atributo de la clase
	A4 = 'CUARTO' # atributo de la clase
	elementosLocales = locals () # devuelve los elementos locales , atributo de la clase

print ('locales().elementosLocales ',locales().elementosLocales,'\n') # presenta el diccionario de elementos actuales locales de la clase 

try : # control de excepciones
	print ('llamar al atributo de claseCONatributo ; claseCONatributo().atributo \n')
	print (claseCONatributo().atributo,'\n') # presenta el valor del atributo indicado de la clase
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('ATRIBUTO ELIMINADO : {0} \n'.format (error)) # presenta la cadena formateada y su valor -error de salida-

print ('añadir un atributo y su valor a una clase con setattr ; setattr (claseCONatributo,"atributo","nuevo valor del atributo") \n')

setattr (claseCONatributo,"atributo","nuevo valor del atributo") # añade el atributo y su valor a la clase indicada

print ('llamar al atributo de claseCONatributo ; claseCONatributo().atributo ',claseCONatributo().atributo,'\n') # presenta el valor del atributo indicado de la clase

print ('devolver el tipo de un valor u objeto con type ; type (CLASE()) ',type (CLASE()),'\n') # presenta el tipo del objeto

print ('devuelve un diccionario con las variables del objeto con vars ; vars (CLASE) \n')

print (vars (CLASE),'\n') # presenta un diccionario con las variables del objeto

print ('devuelve un diccionario con las variables locales con vars ; vars () \n')

print (vars (),'\n') # presenta un diccionario con las variables locales 

print ('crear funcion recursiva ; funcionRecursiva (valor) \n')

def funcionRecursiva (valor) : # definicion de la funcion
	def funcionLocal (valor) : # definicion de la funcion anidada -funcion local-
		print ('valor actual ',valor,'\n') # presenta la cadena y su valor
		print ('volver a llamar a la funcion recursiva ; funcionRecursiva ({0} * 2) \n'.format (valor)) # presenta la cadena formateada y su valor
	funcionLocal (valor) # llama a la funcion anidada -local- y su argumento
	if valor > 100 : # condicion , si el valor devuelto por la funcion local es mayor que el valor por 10
		return 'fin de la funcion recursiva',valor # devuelta la cadena y sale de la funcion recursiva
	return funcionRecursiva (valor * 2) # se llama a si misma con el argumento indicado -funcion recursiva- 
	
print ('llamar a la funcion recursiva ; funcionRecursiva (2) \n')

print (funcionRecursiva (2),'\n') # llama a la funcion recursiva y presenta las cadena devuelta

ANTES = ['Nometales',
			'	Hidrogeno',
			'	Carbon',
			'	Nitrogeno',
			'	Oxigeno',
			'Transicion',
			'	Lantanidos',
			'	Cerio',
			'	Europio',
			'	Actinidos',
			'	Uranio',
			'	Curio',
			'	Plutonio',
			'Metales alcalinos',
			'	Litio',
			'	Sodio',
			'	Potasio'] # lista
print ('contenido lista ; ANTES \n')

print (ANTES,'\n') # presenta contenido lista

print ('crear la funcion ; ordenarListaIndentada (listaIndentada,indentacion="\\t") \n')

def ordenarListaIndentada (listaIndentada,indentacion="\t") : # definicion de la funcion
	CLAVE,ELEMENTO,HIJO = range (3) # asignacion multiple -desempaquetado de la lista range -0 al 2-
	
	def añadirEntrada (nivel,clave,elemento,hijo) : # definicion de la funcion local -anidada-
		if nivel == 0 : # condicion , si el valor coincide
			hijo.append ((clave,elemento,[])) # añade la tupla de 3 elementos a la lista 
		else : # si no es el valor indicado
			añadirEntrada (nivel - 1,clave,elemento,hijo [-1] [HIJO]) # llama a la funcion recursivamente hasta que nivel sea 0
		
	def actualizarListaIndentada (entrada) : # definicion de la funcion local -anidada-
		listaIndentada.append (entrada [ELEMENTO]) # añade a la lista el elemento de la tupla 
		for subentrada in sorted (entrada [HIJO]) : # iterador , bucle for in , pasa los elementos de la lista ordenada a subentrada -lista de tuplas-
			actualizarListaIndentada (subentrada) # llamada recursiva a la funcion local para añadir los elementos de las listas de las tuplas
			
	entradas = [] # lista vacia
	for elemento in listaIndentada : # iterador , bucle for in , pasa los elementos de la lista a elemento
		nivel = 0 # asigna el valor
		indiceInicio = 0 # asigna el valor
		while elemento.startswith (indentacion,indiceInicio) : # bucle while , mientras se cumpla la condicion , si la cadena comienza con los espacios indicados -tabulador- , desde el indice indicado -indiceInicio-
			indiceInicio += len (indentacion) # suma el valor devuelto por len () al valor actual -asignacion aumentada-
			nivel += 1 # suma uno al valor actual -asignacion aumentada-
		clave = elemento.strip ().lower () # asigna la cadena sin los espacios en minusculas
		añadirEntrada (nivel,clave,elemento,entradas) # llama a la funcion local con sus argumentos
	listaIndentada = [] # asigna una lista vacia
	for entrada in sorted (entradas) : # iterador , bucle for in , pasa los elementos de la lista ordenada a entrada
		actualizarListaIndentada (entrada) # llama a la funcion local con su argumento
	return listaIndentada # devuelve la lista actualizada y ordenada

print ('llamar a la funcion con su argumento ; ordenarListaIndentada (ANTES) \n')

print (ordenarListaIndentada (ANTES),'\n') # presenta la lista ordenada devuelta por la funcion

print ('crear funcion decoradora ; resultadoPositivo (funcion) \n')

def resultadoPositivo (funcion) : # definicion de la funcion
	def envoltura (*listaArgumentos,**diccionarioArgumentoValor) : # definicion de la funcion local -anidada-
		resultado = funcion (*listaArgumentos,**diccionarioArgumentoValor) # asigna el resultado de la funcion con los parametros indicados -lista y diccionario-
		assert resultado >= 0,'{0} () el resultado no es mayor o igual a 0 '.format (funcion.__name__) # regla excepcion , si no se cumple presenta la cadena formateada y su valor -nombre funcion-
		return resultado # devuelve el valor devuelto por la funcion con los parametros indicados -lista y diccionario-
	
	envoltura.__name__ = funcion.__name__ # asigna el nombre de la funcion al de la funcion local envoltura
	envoltura.__doc__ = funcion.__doc__ # asigna el docstring -documentacion- de la funcion al de la funcion local envoltura
	
	return envoltura # devuelve el resultado de la funcion local mas los valores asignados a sus metodos -__name__ y __doc__-

print ('uso de la funcion decorador con la funcion de prueba \n')

print ('funcion decoradora ; @resultadoPositivo \n')

print ('funcion de prueba ; descriminar (a,b,c) \n')

print ('crear funcion de prueba ; descriminar (a,b,c) \n')

@resultadoPositivo # decorador de la funcion de abajo
def descriminar (a,b,c) : # definicion de la funcion
	return (b ** 2) - (4 * a * c) # devuelve el resultado dela operacion

print ('descriminar (0,4,8) ',descriminar (0,4,8),'\n') # presenta el resultado de la funcion y su argumento modificado por el decorador

try : # control de excepciones
	print ('descriminar (2,2,2) \n')
	print (descriminar (2,2,2),'\n') # presenta el resultado de la funcion y su argumento modificado por el decorador
except AssertionError as error : # tipo de excepcion
	print ('ERROR : {0} \n'.format (error)) # presenta la salida en la cadena formateada 

print ('crear funcion decoradora ; delimitador (minimo,maximo) \n')

def delimitador (minimo,maximo) : # definicion de la funcion
	def decorador (funcion) : # definicion de la funcion local -anidada-
		import functools # importa el modulo indicado
		@functools.wraps (funcion) # decorador , decora la funcion de abajo con el metodo del modulo importado
		def envoltura (*listaArgumentos,**diccionarioArgumentoValor) : # definicion de la funcion local -anidada-
			resultado = funcion (*listaArgumentos,**diccionarioArgumentoValor) # asigna el resultado de la funcion con los parametros indicados -lista y diccionario-
			if resultado < minimo : # condicion , si el valor es menor que el indicado
				return minimo # devuelve el minimo
			elif resultado > maximo : # condicion , si el valor es mayor que el indicado
				return maximo # devuelve el maximo
			return resultado # devuelve el resultado
		return envoltura # devuelve la funcion decorada por el decorador ; @functools.wraps (funcion) -envoltura-
	return decorador # devuelve la funcion decorador 

print ('uso de la funcion decorador con la funcion de prueba \n')

print ('funcion decoradora ; @delimitador (0,100) \n')

print ('funcion de prueba ; porcentaje (cantidad,total) \n')

print ('crear funcion de prueba ; porcentaje (cantidad,total) \n')

@delimitador (0,100) # decorador de la funcion inferior
def porcentaje (cantidad,total) : # definicion de la funcion
	return (cantidad / total) * 100 # devuelve el porcentaje de las cantidades indicadas

print ('porcentaje (20,100) ',porcentaje (20,100),'\n') # presenta el resultado de la funcion limitado por el decorador

print ('porcentaje (20,1000) ',porcentaje (20,1000),'\n') # presenta el resultado de la funcion limitado por el decorador

print ('porcentaje (20,10000) ',porcentaje (20,10000),'\n') # presenta el resultado de la funcion limitado por el decorador 

print ('porcentaje (20,10) ',porcentaje (20,10),'\n') #  presenta el resultado de la funcion limitado por el decorador -sin decorador 200.0-

print ('crear funcion decoradora ; registroFuncion (funcion) \n')

def registroFuncion (funcion) : # definicion de la funcion
	if __debug__ : # condicion , si se llama al metodo -True-
		import logging # importa el modulo indicado
		import os # importa el modulo indicado
		import tempfile # importa el modulo indicado
		registro = logging.getLogger ('Logger') # crea el fichero de registro -login-
		registro.setLevel (logging.DEBUG) # asigna el nivel de depuracion
		manejador = logging.FileHandler (os.path.join (tempfile.gettempdir (),'logged.log')) # añade el fichero log al objeto
		registro.addHandler (manejador) # añade el manupilador al objeto de registro
		
		def logged (funcion) : # definicion de la funcion local -anidada-
			import functools # importa el modulo indicado
			@functools.wraps (funcion) # decorador , decora la funcion inferior con el metodo del modulo importado
			def envoltura (*listaArgumentos,**diccionarioArgumentoValor) : # definicion de la funcion local -anidada-
				log = 'llamando : {0} ({1}'.format (funcion.__name__,', '.join (['{0!r}'.format (A) for A in listaArgumentos] + ['{0!s}={1!r}'.format (klave,valor) for klave,valor in diccionarioArgumentoValor.items ()])) # asigna la cadena formateada y sus valores -nombre funcion y argumentos-
				resultado = excepcion = None # asignacion multiple -vinculacion multiple-
				try : # control de excepciones
					resultado = funcion  (*listaArgumentos,**diccionarioArgumentoValor) # asigna la funcion con los argumentos indicados 
					return resultado # devuelve la funcion con los argumentos de la funcion envoltura
				except Exception as error : # tipo de excepcion , pasa la salida a error
					excepcion = error # asigna la salida del error
				finally : # lance excepcion o no , ejecuta el codigo
					log += (') -> ' + str (resultado) if excepcion is None else ') {0} : {1}'.format (type (excepcion),excepcion)) # añade la cadena segun la condicion y el valor devuelto
					registro.debug (log) # añade al registro del objeto la cadena -fichero log-
					if excepcion is not None : # condicion , si el valor no es None
						raise excepcion # lanza la excepcion indicada
			return envoltura # devuelve la funcion modificada por el decorador
		
		return logged (funcion) # devuelve la funcion
	else : # si no se usa el metodo -False-
		def logged (funcion) : # definicion de la funcion local -anidada-
			return funcion # devuelve la funcion sin decoracion
		return logged (funcion) # devuelve la funcion

print ('uso de la funcion decorador con la funcion de prueba \n')

print ('funcion decoradora ; @registroFuncion \n')

print ('funcion de prueba ; precioDescontado (precio,porcentaje,hacerEntero=False) \n')

print ('crear funcion de prueba ; precioDescontado (precio,porcentaje,hacerEntero=False) \n')

@registroFuncion # decorador de la funcion inferior
def precioDescontado (precio,porcentaje,hacerEntero=False) : # definicion de la funcion
	resultado = precio * ((100 - porcentaje) / 100) # asigna el resultado de la operacion
	if not (0 < resultado <= precio) : # condicion , si no se cumple (True)   -False-
		raise ValueError ('precio invalido') # lanza la excepcion indicada con la cadena
	return resultado if not hacerEntero else int (round (resultado)) # devuelve el valor correspondiente a la condicion -False ; resultado- , lo contrario -NO False el valor mas cercano al entero  round ()-

print ('precioDescontado (200,20) ',precioDescontado (200,20),'\n')  # presenta el resultado de la funcion decorada

print ('precioDescontado (200,2) ',precioDescontado (200,2),'\n')  # presenta el resultado de la funcion decorada

print ('precioDescontado (200,10) ',precioDescontado (200,10),'\n')  # presenta el resultado de la funcion decorada

try : # control de excepciones
	print ('precioDescontado (200,200) \n')
	print (precioDescontado (200,200),'\n')  # presenta el resultado de la funcion decorada
except ValueError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : {0} \n'.format (error)) # presenta la cadena formateada con la salida del error

print ('crear funcion con anotaciones y referencia de la funcion ; esCaracterPuntuacionUNICODE (cadena : tipo cadena) -> bool : \n')

def esCaracterPuntuacionUNICODE (cadena : str) -> bool : # definicion de la funcion con anotacion en el parametro y referencia de la funcion
	for Caracter in cadena : # iterador , bucle for in , pasa los elementos de la cadena a Caracter
		if Caracter in "!@#?" : # condicion , si el valor esta en la cadena -pertenencia-
			return True # devuelve True
	return False # devuelve False

print ('esCaracterPuntuacionUNICODE ("cebra") ',esCaracterPuntuacionUNICODE ("cebra"),'\n') # presenta True si lleva puntuacion o False

print ('esCaracterPuntuacionUNICODE ("!cebra") ',esCaracterPuntuacionUNICODE ("!cebra"),'\n') # presenta True si lleva puntuacion o False

print ('esCaracterPuntuacionUNICODE ("!@#?") ',esCaracterPuntuacionUNICODE ("!@#?"),'\n') # presenta True si lleva puntuacion o False

print ('esCaracterPuntuacionUNICODE (("!","@")) ',esCaracterPuntuacionUNICODE (("!","@")),'\n') # presenta True si lleva puntuacion o False

print ('anotaciones y referencias de la funcion ; esCaracterPuntuacionUNICODE.__annotations__ ',esCaracterPuntuacionUNICODE.__annotations__,'\n') # presenta el diccionario con los argumentos y anotaciones

print ('crear decorador ; tipoEstricto (funcion) \n')

def tipoEstricto (funcion) : # definicion de la funcion
	import inspect # importa el modulo
	import functools # importa el modulo
	anotaciones = funcion.__annotations__ # asigna el diccionario de anotaciones de la funcion
	inspeccionarArgumentos = inspect.getfullargspec (funcion) # inspecciona los argumentos de la funcion
	assert 'return' in anotaciones,'tipo no encontrado para el valor return' # regla excepcion , si no se cumple lanza excepcion con la cadena indicada
	for argumento in inspeccionarArgumentos.args + inspeccionarArgumentos.kwonlyargs : # iterador , bucle for in , pasa los elementos de los objetos a argumento
		assert argumento in anotaciones,'tipo no encontrado para : {0} '.format (argumento) # regla excepcion , si no se cumple lanza excepcion con la cadena formateada indicada
		@functools.wraps (funcion) # decorador , decora la funcion inferior con el metodo del modulo importado
		def envoltura (*listaArgumentos,**diccionarioArgumentoValor) : # definicion de la funcion local -anidada-
			for nombre,argumento in (list (zip (inspeccionarArgumentos.args,listaArgumentos)) + list (diccionarioArgumentoValor.items ())) : # iterador , bucle for in , pasa las tuplas 2 elementos desempaquetadas a nombre y argumento
				assert isinstance (argumento,anotaciones [nombre]),'argumento esperado "{0}" de {1} tiene {2} '.format (nombre,anotaciones [nombre],type (argumento)) # regla excepcion , si no se cumple lanza excepcion con la cadena formateada indicada
			resultado = funcion (*listaArgumentos,**diccionarioArgumentoValor) # asigna la funcion con los argumentos indicados
			assert isinstance (resultado,anotaciones ['return']),'return esperado de {0} tengo {1} '.format (anotaciones ['return'],type (resultado)) # regla excepcion , si no se cumple lanza excepcion con la cadena formateada indicada
			return resultado # devuelve la funcion con los argumentos modificada por el decorador
		return envoltura # devuelve la funcion

print ('uso de la funcion decorador con la funcion de prueba \n')

print ('funcion decoradora ; @tipoEstricto \n')

print ('funcion de prueba ; esCaracterPuntuacionUnicode (cadena : str) -> bool : \n')

print ('crear funcion de prueba ; esCaracterPuntuacionUnicode (cadena : str) -> bool : \n')

@tipoEstricto # decorador de la funcion inferior
def esCaracterPuntuacionUnicode (cadena : str) -> bool : # definicion de la funcion con anotacion en el parametro y referencia de la funcion
	for Caracter in cadena : # iterador , bucle for in , pasa los elementos de la cadena a Caracter
		if Caracter in "!@#?" : # condicion , si el valor esta en la cadena -pertenencia-
			return True # devuelve True
	return False # devuelve False

print ('esCaracterPuntuacionUnicode ("cebra") ',esCaracterPuntuacionUnicode ("cebra"),'\n') # presenta True si lleva puntuacion o False

print ('esCaracterPuntuacionUnicode ("!cebra") ',esCaracterPuntuacionUnicode ("!cebra"),'\n') # presenta True si lleva puntuacion o False

print ('esCaracterPuntuacionUnicode ("!@#?") ',esCaracterPuntuacionUnicode ("!@#?"),'\n') # presenta True si lleva puntuacion o False

try : # control de excepciones
	print ('esCaracterPuntuacionUnicode (("!","@")) \n')
	print (esCaracterPuntuacionUnicode (("!","@")),'\n') # presenta True si lleva puntuacion o False
except AssertionError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : {0} \n'.format (error)) # presenta la salida formateada de error

print ('anotaciones y referencias de la funcion ; esCaracterPuntuacionUnicode.__annotations__ ',esCaracterPuntuacionUnicode.__annotations__,'\n') # presenta el diccionario con los argumentos y anotaciones

print ('crear funcion con anotaciones y referencia de la funcion ; \n')

print ('rangeFloat (valor : "el valor tiene que ser un numero") -> "la funcion devuelve una lista de numeros en formato float" : \n')

def rangeFloat (valor : "el valor tiene que ser un numero") -> "la funcion devuelve una lista de numeros en formato float" : # definicion de la funcion con anotacion en el parametro y referencia de la funcion
	return [float (numero) for numero in range (valor)] # devuelve una lista generada por compresion -iterador , bucle for in , pasa los numeros del iterador range () a numero-

print ('anotaciones y referencias de la funcion ; rangeFloat.__annotations__ ',rangeFloat.__annotations__,'\n') # presenta el diccionario con los argumentos y anotaciones

print ('rangeFloat (11) ',rangeFloat (11),'\n') # presenta una lista de numeros en formato float a partir del indicado

print ('crear una clase basica -object- ; class punto (object) : \n')

class punto (object) : # definicion de la clase
	__slots__ = ('x','y') # atributo que contiene una tupla con los atributos de la clase
	def __init__ (self,x=0,y=0) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.x = x # asigna el valor al atributo
		self.y = y # asigna el valor al atributo
	
	def coordenadas (self) : # definicion del metodo
		return (self.x,self.y) # devuelve una tupla con las coordenadas x,y

print ('crear instancia ; P = punto (10,10) \n')

P = punto (10,10) # crea objeto de la clase con el argumento indicado

print ('P.coordenadas () ',P.coordenadas (),'\n') # presenta el valor devuelto por el metodo del objeto -tupla coordenadas punto-

print ('crear clase que procesa atributos automaticamente con __getattr__ ; class valorOrdinal (object) : \n')

class valorOrdinal (object) : # definicion de la clase
	def __getattr__ (self,caracter) : # definicion del metodo especial -objeto.caracter-
		return (caracter,ord (caracter)) # devuelve una tupla con el caracter y su valor ordinal 

print ('instanciar clase ; ordinal = valorOrdinal () \n')

ordinal = valorOrdinal () # crea objeto de la clase 

print ('ordinal.A ',ordinal.A,'\n') # presenta la tupla con el caracter y su valor

print ('ordinal.z ',ordinal.z,'\n') # presenta la tupla con el caracter y su valor

print ('ordinal.a ',ordinal.a,'\n') # presenta la tupla con el caracter y su valor

print ('ordinal.ñ ',ordinal.ñ,'\n') # presenta la tupla con el caracter y su valor

print ('crear clase que crea atributo y su valor del objeto automaticamente con __setattr__ y NO borrarlo con __delattr__ \n')

print ('class atributosClase (object) : \n')

class atributosClase (object) : # definicion de la clase
	def __setattr__ (self,nombre,valor) : # definicion del metodo especial -objeto.atributo = valor-
		if nombre in self.__dict__ : # condicion , si esta en el diccionario de atributos de la clase
			raise ValueError ('no puede cambiarse el atributo , ya existe') # lanza excepcion con la cadena indicada 
		self.__dict__ [nombre] = valor # añade el atributo y su valor al diccionario de atributos de la clase
		
	def __delattr__ (self,nombre) : # definicion del metodo especial -del objeto.atributo-
		if nombre in self.__dict__ : # condicion , si esta en el diccionario de atributos de la clase
			raise ValueError ('no puede eliminarse el atributo ') # lanza excepcion con la cadena indicada
		raise AttributeError ("el atributo '{0}' no es del objeto : {1} ".format (nombre,self.__class__.__name__)) # lanza excepcion con la cadena formateada indicada -nombre atributo y nombre clase-

print ('instanciar clase ; ATRIBUTOS = atributosClase () \n')

ATRIBUTOS = atributosClase () # crea objeto de la clase

print ('ATRIBUTOS.atributo1 = "valor1" \n')

ATRIBUTOS.atributo1 = "valor1" # asigna el atributo y su valor al objeto

print ('ATRIBUTOS.atributo2 = "valor2" \n')

ATRIBUTOS.atributo2 = "valor2" # asigna el atributo y su valor al objeto

print ('ATRIBUTOS.atributo3 = "valor3" \n')

ATRIBUTOS.atributo3 = "valor3" # asigna el atributo y su valor al objeto

print ('ATRIBUTOS.atributo4 = "valor4" \n')

ATRIBUTOS.atributo4 = "valor4" # asigna el atributo y su valor al objeto

print ('ATRIBUTOS.atributo1 ',ATRIBUTOS.atributo1,'\n') # presenta el valor del atributo del objeto

print ('ATRIBUTOS.atributo2 ',ATRIBUTOS.atributo2,'\n') # presenta el valor del atributo del objeto

print ('ATRIBUTOS.atributo3 ',ATRIBUTOS.atributo3,'\n') # presenta el valor del atributo del objeto

print ('ATRIBUTOS.atributo4 ',ATRIBUTOS.atributo4,'\n') # presenta el valor del atributo del objeto

try : # control de excepciones 
	print ('del ATRIBUTOS.atributo4 \n')
	del ATRIBUTOS.atributo4 # intenta eliminar el atributo indicado de la clase -lanza excepcion-
except ValueError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : {0} \n'.format (error)) # presenta la salida de error formateada
	
try : # control de excepciones 
	print ('del ATRIBUTOS.atributo5 \n')
	del ATRIBUTOS.atributo5 # intenta eliminar el atributo indicado de la clase -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : {0} \n'.format (error)) # presenta la salida de error formateada

print ('crear clase con metodos especiales ; __delattr__ , __dir__ , __getattr__ , __getattribute__ y __setattr__ \n')

print ('class metodosEspecialesClase (object) : \n')

class metodosEspecialesClase (object) : # definicion de la clase 
	def __delattr__ (self,atributo) : # definicion del metodo especial -del objeto.atributo-
		if atributo in self.__dict__ : # condicion , si esta en el diccionario de atributos de la clase
			del self.__dict__ [atributo] # elimina el atributo del diccionario de atributos de la clase
			print ('atributo eliminado : "{0}" de la clase : {1} \n'.format (atributo,self.__class__.__name__)) # devuelve la cadena formateada -nombre atributo y nombre clase-
			return # devuelve None -sale del metodo-
		raise AttributeError ("el atributo '{0}' no es de la clase : {1} ".format (atributo,self.__class__.__name__)) # lanza excepcion con la cadena formateada indicada -nombre atributo y nombre clase-
	
	def __dir__ (self) : # definicion del metodo especial -dir (objeto)-
		return dir (self.__class__) # devuelve atributos y metodos clase
	
	def __getattr__ (self,atributo) : # definicion del metodo especial -objeto.atributo-
		if atributo in self.__dict__ : # condicion , si esta en el diccionario de atributos de la clase
			return (atributo,self.__dict__ [atributo]) # devuelve una tupla con el nombre del atributo y su valor
		raise AttributeError ("el atributo '{0}' no es de la clase : {1} ".format (atributo,self.__class__.__name__)) # lanza excepcion con la cadena formateada indicada -nombre atributo y nombre clase-
	'''
	def __getattribute__ (self,atributo) : # definicion del metodo especial -objeto.atributo- 
		if atributo in self.__dict__ : # condicion , si esta en el diccionario de atributos de la clase
			return (atributo,self.__dict__ [atributo]) # devuelve una tupla con el nombre del atributo y su valor
		raise AttributeError ("el atributo '{0}' no es de la clase : {1} ".format (atributo,self.__class__.__name__)) # lanza excepcion con la cadena formateada indicada -nombre atributo y nombre clase-
	'''
	def __setattr__ (self,atributo,valor) : # definicion del metodo especial -objeto.atributo = valor-
		if atributo in self.__dict__ : # condicion , si esta en el diccionario de atributos de la clase
			raise ValueError ('no puede cambiarse el atributo , ya existe') # lanza excepcion con la cadena indicada 
		self.__dict__ [atributo] = valor # añade el atributo y su valor al diccionario de atributos de la clase
		

print ('instanciar clase ; metodosEspeciales = metodosEspecialesClase () \n')

metodosEspeciales = metodosEspecialesClase () # crea objeto de la clase

print ('metodosEspeciales.atributo1 = "valor1" \n')

metodosEspeciales.atributo1 = "valor1" # asigna el atributo y su valor al objeto

print ('metodosEspeciales.atributo2 = "valor2" \n')

metodosEspeciales.atributo2 = "valor2" # asigna el atributo y su valor al objeto

print ('metodosEspeciales.atributo3 = "valor3" \n')

metodosEspeciales.atributo3 = "valor3" # asigna el atributo y su valor al objeto

print ('metodosEspeciales.atributo4 = "valor4" \n')

metodosEspeciales.atributo4 = "valor4" # asigna el atributo y su valor al objeto

try : # control de excepciones 
	print ('metodosEspeciales.atributo4 = "nuevo valor4" \n')
	metodosEspeciales.atributo4 = "nuevo valor4" # asigna el atributo y su valor al objeto -lanza excepcion-
except ValueError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : {0} \n'.format (error)) # presenta la salida de error formateada

print ('metodosEspeciales.atributo1 ',metodosEspeciales.atributo1,'\n') # presenta el valor del atributo del objeto

print ('metodosEspeciales.atributo2 ',metodosEspeciales.atributo2,'\n') # presenta el valor del atributo del objeto

print ('metodosEspeciales.atributo3 ',metodosEspeciales.atributo3,'\n') # presenta el valor del atributo del objeto

print ('metodosEspeciales.atributo4 ',metodosEspeciales.atributo4,'\n') # presenta el valor del atributo del objeto

print ('atributos y metodos del objeto ; dir (metodosEspeciales) \n')

print (dir (metodosEspeciales),'\n') # presenta atributos y metodos del objeto

print ('eliminar un atributo del objeto ; del metodosEspeciales.atributo4 \n')

del metodosEspeciales.atributo4 # elimina el atributo del objeto indicado

try : # control de excepciones 
	print ('del ATRIBUTOS.atributo4 \n')
	del metodosEspeciales.atributo4 # intenta eliminar el atributo indicado de la clase -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : {0} \n'.format (error)) # presenta la salida de error formateada

print ('atributos del objeto ; metodosEspeciales.__dict__  \n')

print (metodosEspeciales.__dict__,'\n') # presenta el diccionario de atributos del objeto

print ('uso de tuplas nombradas para crear constantes \n')

class constanteAlternativa (object) : # definicion de la clase
	import collections # importa el modulo indicado
	constanteNombrada = collections.namedtuple ('_','minimo maximo') (10,100) # crea una tupla nombrada con nombre desechable ; '_' y nombres ; minimo y maximo -se les asigna los valores indicados en el orden-
	MINIMO = constanteNombrada.minimo # asigna el valor 10
	MAXIMO = constanteNombrada.maximo # asigna el valor 100
	offset = collections.namedtuple ('_','identificacion nombre descripcion') (*range (3)) # crea una tupla nombrada con nombre desechable ; '_' y nombres ; identificacion , nombre y descripcion -se les asigna los valores devueltos por range () en el orden dispuesto-
	IDENTIFICACION = offset.identificacion # asigna el valor 0
	NOMBRE = offset.nombre # asigna el valor 1
	DESCRIPCION = offset.descripcion # asigna el valor 2

print ('crear instancia para constanteAlternativa ; Alternativa = constanteAlternativa () \n')

Alternativa = constanteAlternativa () # crea el objeto de la clase

print ('Alternativa.constanteNombrada.MINIMO ',Alternativa.MINIMO,'\n') # presenta el valor de tupla nombrada como constante 

print ('Alternativa.constanteNombrada.MAXIMO ',Alternativa.MAXIMO,'\n') # presenta el valor de tupla nombrada como constante

print ('Alternativa.constanteNombrada.IDENTIFICACION ',Alternativa.IDENTIFICACION,'\n') # presenta el valor de tupla nombrada como constante

print ('Alternativa.constanteNombrada.NOMBRE ',Alternativa.NOMBRE,'\n') # presenta el valor de tupla nombrada como constante

print ('Alternativa.constanteNombrada.DESCRIPCION ',Alternativa.DESCRIPCION,'\n') # presenta el valor de tupla nombrada como constante

print ('crear un functor ; numeroEntero = int \n')

numeroEntero = int # apunta al tipo int -devuelve numeros enteros sin punto flotante-

print ('numeroEntero (0.5) ',numeroEntero (0.5),'\n') # presenta el numero sin la parte del punto flotante -entero-

print ('numeroEntero (5.0) ',numeroEntero (5.0),'\n') # presenta el numero sin la parte del punto flotante -entero-

print ('numeroEntero (10.5) ',numeroEntero (10.5),'\n') # presenta el numero sin la parte del punto flotante -entero-

print ('crear clase functor con el metodo especial __call__ ; class saltar (object) : \n')

class saltar (object) : # definicion de la clase
	def __init__ (self,caracteres) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		self.caracteres = caracteres # asigna el valor al atributo
		
	def __call__ (self,cadena) : # definicion del metodo especial , devuelve al metodo indicado con los argumentos puestos
		return cadena.strip (self.caracteres) # devuelve los argumentos con el metodo strip
	
print ('crear functor ; saltarPuntuacion = saltar (",;:.!?") \n')

saltarPuntuacion = saltar (",;:.!?") # crea el functor

print ('saltarPuntuacion ("hola !, landd ?.") ',saltarPuntuacion ("hola !, landd ?."),'\n') # presenta la cadena sin la puntuacion final 

print ('saltarPuntuacion ("hola!") ',saltarPuntuacion ("hola!"),'\n') # presenta la cadena sin la puntuacion final

print ('crear funcion tipo cierre ; def crearFuncionSaltar (caracteres) : \n')

def crearFuncionSaltar (caracteres) : # definicion de la funcion -tipo cierre-
	def funcionSaltar (cadena) : # definicion de la funcion local -cierre-
		return cadena.strip (caracteres) # devuelve el objeto con el metodo indicado
	return funcionSaltar # devuelve la funcion indicada

print ('crear objeto cierre ; quitarPuntuacion = crearFuncionSaltar (",;:.!?") \n')

quitarPuntuacion = crearFuncionSaltar (",;:.!?") # crea el objeto cierre

print ('quitarPuntuacion ("hola !, landd ?.") ',quitarPuntuacion ("hola !, landd ?."),'\n') # presenta la cadena sin la puntuacion final 

print ('quitarPuntuacion ("hola!") ',quitarPuntuacion ("hola!"),'\n') # presenta la cadena sin la puntuacion final

print ('crear la clase functor ; ordenarClave \n')

class ordenarClave (object) : # definicion de la clase
	def __init__ (self,*nombresAtributo) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombresAtributo = nombresAtributo # asigna la lista de argumentos al atributo
		
	def __call__ (self,instancia) : # definicion del metodo especial , devuelve lista de argumentos validos
		ListaArgumentos = [] # asigna lista vacia
		for nombreAtributo in self.nombresAtributo : # iterador , bucle for in , pasa los argumentos de la lista a nombreAtributo
			ListaArgumentos.append (getattr (instancia,nombreAtributo)) # añade el atributo a la lista si pertenece a la instancia -devuelto por getattr-
		return ListaArgumentos # devuelve la lista de argumentos validos para la instancia
	
print ('crear clase persona \n')

class persona (object) : # definicion de la clase
	def __init__ (self,NOMBRE,APELLIDO,EMAIL) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.NOMBRE = NOMBRE # asigna el valor al atributo
		self.APELLIDO = APELLIDO # asigna el valor al atributo
		self.EMAIL = EMAIL # asigna el valor al atributo

print ('crear lista de objetos persona : \n')

print ('gente = [persona ("maria","anton","maria_anton@correo.com"),persona ("pepe","lui","pepe@mail.org"),persona ("luis","lu","lulu@tulus.com")] \n')

gente = [persona ("maria","anton","maria_anton@correo.com"),persona ("pepe","lui","pepe@mail.org"),persona ("luis","lu","lulu@tulus.com")] # lista de objetos persona

print ('ordenar la lista de objetos con la clase functor ordenarClave ; sorted (gente,key=ordenarClave ("APELLIDO")) \n')

for objetoOrdenado in sorted (gente,key=ordenarClave ("APELLIDO")) : # iterador , bucle for in , pasa los objetos ordenados por el atributo indicado a objetoOrdenado
	print ('persona ',objetoOrdenado.NOMBRE,objetoOrdenado.APELLIDO,objetoOrdenado.EMAIL,'\n') # presenta la cadena y los valores de los atributos del objeto
else : # cuando finalice el iterador
	print ('FIN OBJETOS ORDENADOS \n') # presenta la cadena

print ('ordenar sin usar el functor con la funcion attrgetter del modulo operator ; importar modulo operator : import operator \n')

import operator # importa el modulo indicado

print ('ordenar la lista ; sorted (gente,key=operator.attrgetter ("NOMBRE") \n')

for objetoOrdenado1 in sorted (gente,key=operator.attrgetter ("NOMBRE")) : # iterador , bucle for in , pasa los objetos ordenados por el atributo indicado a objetoOrdenado1
	print ('persona ',objetoOrdenado1.NOMBRE,objetoOrdenado1.APELLIDO,objetoOrdenado1.EMAIL,'\n') # presenta la cadena y los valores de los atributos del objeto
else : # cuando finalice el iterador
	print ('FIN OBJETOS ORDENADOS \n') # presenta la cadena

print ('uso de administradores de contexto : uso de with con objetos de archivo \n')

print ('with open ("./Escritorio/capitulo8.py~","r") as abrirFichero : \n')

with open ("./Escritorio/capitulo8.py~","r") as abrirFichero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como abrirFichero-
	for Linea in abrirFichero : # iterador , bucle for in , pasa el contenido -iterador- del fichero a Linea
		print (Linea) # presenta la linea actual del fichero
	else : # cuando finalice el iterador
		print ('//////////////////////////////////////////////\n')
		print ('FIN CONTENIDO {0} \n'.format (abrirFichero.name.split ('/') [-1])) # presenta la cadena formateada con el nombre del fichero -split devuelve una lista con los elementos de la cadena separados por el caracter indicado , devuelve el ultimo elemento de la lista-
		print ('//////////////////////////////////////////////\n')

print ('uso de administradores de contexto anidados -locales- \n')

with open ("./Escritorio/capitulo8.py~","r") as ficheroFuente : # abre y cierra el fichero indicado en modo solo lectura -enlazado como ficheroFuente-
	with open ("./Escritorio/capitulo8.back","w") as ficheroDestino : # abre y cierra el fichero indicado en modo escritura -enlazado como ficheroDestino-
		print ('escribiendo el contenido de : {0}  en   {1} \n'.format (ficheroFuente.name.split ('/') [-1],ficheroDestino.name.split ('/') [-1])) # presenta la cadena formateada con el nombre del fichero de origen y destino -split devuelve una lista con los elementos de la cadena separados por el caracter indicado , devuelve el ultimo elemento de la lista-
		for Linea in ficheroFuente : # iterador , bucle for in , pasa el contenido -iterador- del fichero a Linea
			ficheroDestino.write (Linea) # escribe el contenido de Linea en el fichero del objeto 
		else : # cuando finalice el iterador
			print ('//////////////////////////////////////////////\n')
			print ('FIN ESCRITURA CONTENIDO EN {0} \n'.format (ficheroDestino.name.split ('/') [-1])) # presenta la cadena formateada con el nombre del fichero -split devuelve una lista con los elementos de la cadena separados por el caracter indicado , devuelve el ultimo elemento de la lista-
			print ('//////////////////////////////////////////////\n')

print ('crear un administrador de contexto ; class multiOpen (object) : \n')

class multiOpen (object) : # definicion de la clase -administrador de contexto-
	def __init__ (self,*objetosFichero) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.objetosFichero = objetosFichero # asigna la lista al atributo
		
	def __enter__ (self) : # definicion del metodo especial -inicia-
		return self.objetosFichero # devuelve una tupla con los objetos fichero
			
	def __exit__ (self,*salida) : # definicion del metodo especial -termina-
		for fichero in self.objetosFichero : # iterador , bucle for in , pasa los elementos -objetos fichero- a fichero
			if fichero.closed : # condicion , si devuelve True , el fichero esta cerrado
				continue # vuelve al siguiente elemento -objeto fichero-
			else : # si es False , el fichero no esta cerrado
				fichero.close () # cierra el fichero del objeto fichero
		else : # cuando finalice el iterador
			return salida # devuelve la tupla 
		
print ('usar del administrador de contexto ; multiOpen \n')

print ('with multiOpen (open ("./Escritorio/capitulo8.back","r"),open ("./Escritorio/capitulo8.backup","w")) as ORIGEN_DESTINO : \n')

with multiOpen (open("./Escritorio/capitulo8.back","r"),open("./Escritorio/capitulo8.backup","w")) as ORIGEN_DESTINO : # abre y cierra los ficheros enla secuencia indicada -enlazado como ORIGEN_DESTINO , se inicia el metodo __enter__-
	print ('escribiendo el contenido de : {0}  en   {1} \n'.format (ORIGEN_DESTINO [0].name.split ('/') [-1],ORIGEN_DESTINO [1].name.split ('/') [-1])) # presenta la cadena formateada con el nombre del fichero de origen y destino -split devuelve una lista con los elementos de la cadena separados por el caracter indicado , devuelve el ultimo elemento de la lista-
	for Linea in ORIGEN_DESTINO [0] : # iterador , bucle for in , pasa el contenido -iterador- del fichero a Linea -primer objeto fichero de la tupla , indice (posicion) 0-
			ORIGEN_DESTINO [1].write (Linea) # escribe el contenido de Linea en el fichero del objeto -fichero objeto segun indice (posicion) 1-
	else : # cuando finalice el iterador
		print ('//////////////////////////////////////////////\n')
		print ('FIN ESCRITURA CONTENIDO EN {0} \n'.format (ORIGEN_DESTINO [1].name.split ('/') [-1])) # presenta la cadena formateada con el nombre del fichero -split devuelve una lista con los elementos de la cadena separados por el caracter indicado , devuelve el ultimo elemento de la lista-
		print ('//////////////////////////////////////////////\n') # al finalizar la ultima sentencia se inicia el metodo __exit__ , que ejecuta su codigo
		
print ('crear descriptor usando los metodos especiales __get__ , __set__ y __delete__ \n')

print ('crear una clase descriptor con  __get__ ; class sombraXml (object) : \n')

class sombraXml (object) : # definicion de la clase -descriptor-
	def __init__ (self,nombreAtributo) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombreAtributo = nombreAtributo # asigna el valor al atributo
		
	def __get__ (self,instancia,propietario=None) : # definicion del metodo especial
		import xml.sax.saxutils # importa el modulo indicado del paquete xml.sax  
		return xml.sax.saxutils.escape (getattr (instancia,self.nombreAtributo)) # devuelve el valor en formato xml 
	
print ('crear clase producto ; class producto (object) : \n')

class producto (object) : # definicion de la clase
	__slots__ = ('nombre','descripcion','precio') # tupla de atributos
	
	nombreCOMOxml = sombraXml ('nombre') # devuelve la cadena en formato xml 
	descripcionCOMOxml = sombraXml ('descripcion') # devuelve la cadena en formato xml
	
	def __init__ (self,nombre,descripcion,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombre = nombre # asigna el valor al atributo privado
		self.descripcion = descripcion # asigna el valor al atributo
		self.precio = precio # asigna el valor al atributo

print ('uso del descriptor en la clase producto -sombraXml- ; PRODUCTO = producto ("cincel <3cm>","cincel & cap",45.25) \n')

PRODUCTO = producto ("cincel <3cm>","cincel & cap",45.25) # instancia la clase con los atributos indicados

print ('contenido de los atributos : \n')

print ('PRODUCTO.nombre ',PRODUCTO.nombre,'\n') # presenta el valor del atributo del objeto

print ('PRODUCTO.nombreCOMOxml ',PRODUCTO.nombreCOMOxml,'\n') # presenta el valor del atributo del objeto

print ('PRODUCTO.descripcionCOMOxml ',PRODUCTO.descripcionCOMOxml,'\n') # presenta el valor del atributo del objeto

print ('crear una clase descriptor con  __get__ ; class cacheSombraXml (object) : \n')

class cacheSombraXml (object) : # definicion de la clase -descriptor-
	def __init__ (self,nombreAtributo) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombreAtributo = nombreAtributo # asigna el valor al atributo
		self.cache = {} # asigna diccionario vacio al atributo
		
	def __get__ (self,instancia,propietario=None) : # definicion del metodo especial
		import xml.sax.saxutils # importa el modulo indicado del paquete xml.sax  
		textoXML = self.cache.get (id (instancia)) # añade el identificador devuelto por id al diccionario como clave
		if textoXML is not None : # condicion , si el valor de la clave del diccionario NO es None
			return textoXML # devuelve el diccionario
		return self.cache.setdefault (id (instancia),xml.sax.saxutils.escape (getattr (instancia,self.nombreAtributo))) # devuelve el diccionario con el identificador como clave y el valor del atributo en formato xml en valor 

print ('crear clase Producto ; class Producto (object) : \n')

class Producto (object) : # definicion de la clase
	__slots__ = ('nombre','descripcion','precio') # tupla de atributos
	
	nombreCOMOxml = cacheSombraXml ('nombre') # devuelve la cadena en formato xml 
	descripcionCOMOxml = cacheSombraXml ('descripcion') # devuelve la cadena en formato xml
	
	def __init__ (self,nombre,descripcion,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombre = nombre # asigna el valor al atributo 
		self.descripcion = descripcion # asigna el valor al atributo
		self.precio = precio # asigna el valor al atributo

print ('uso del descriptor en la clase Producto -cacheSombraXml- ; PRODUCTO_ = Producto ("buril <3cm>","buril & cap",5.25) \n')

PRODUCTO_ = Producto ("buril <3cm>","buril & cap",5.25) # instancia la clase con los atributos indicados

print ('contenido de los atributos : \n')

print ('PRODUCTO_.nombre ',PRODUCTO_.nombre,'\n') # presenta el valor del atributo del objeto

print ('PRODUCTO_.nombreCOMOxml ',PRODUCTO_.nombreCOMOxml,'\n') # presenta el valor del atributo del objeto

print ('PRODUCTO_.descripcionCOMOxml ',PRODUCTO_.descripcionCOMOxml,'\n') # presenta el valor del atributo del objeto

print ('crear una clase descriptor con  __get__ y __set__ ; class almacenamientoEXTERNO (object) : \n')

class almacenamientoEXTERNO (object) : # definicion de la clase -descriptor-
	__slots__ = ('nombreAtributo') # tupla de atributos
	__almacenamiento = {} # asigna diccionario vacio al atributo privado
	
	def __init__ (self,nombreAtributo) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombreAtributo = nombreAtributo # asigna el valor al atributo
		
	def __set__ (self,instancia,valor) : # definicion del metodo especial
		self.__almacenamiento [id (instancia),self.nombreAtributo] = valor # añade la clave : valor al diccionario
		
	def __get__ (self,instancia,propiedad=None) : # definicion del metodo especial
		if instancia is None : # condicion , si el valor es None
			return self # devuelve el objeto
		return self.__almacenamiento [id (instancia),self.nombreAtributo] # devuelve el valor de la clave indicada del DICCIONARIO 

print ('crear clase PUNTO ; class PUNTO (object) : \n')

class PUNTO (object) : # definicion de la clase
	__slots__ = () # asigna una tupla vacia de atributos -no dejar usar __dict__ de atributos , diccionario atributos clase-
	
	x = almacenamientoEXTERNO ('x') # guarda el atributo con el valor por defecto -en el diccionario del descriptor-
	y = almacenamientoEXTERNO ('y') # guarda el atributo con el valor por defecto -en el diccionario del descriptor-
	
	def __init__ (self,x=0,y=0) : # definicion del metodo , inicializa la clase con los argumentos indicados -valores por defecto-
		self.x = x # asigna el valor al atributo
		self.y = y # asigna el valor al atributo

print ('uso del descriptor en la clase PUNTO -almacenamientoEXTERNO- ; PUNTO_ = PUNTO (53,33) \n')

PUNTO_ = PUNTO (53,33) # instancia la clase con los atributos indicados

print ('clase objeto ',PUNTO_.__class__,'\n') # presenta la clase del objeto

print ('nombre clase objeto ',PUNTO_.__class__.__name__,'\n') # presenta el nombre de la clase

print ('contenido de los atributos : \n')

print ('PUNTO_.x ',PUNTO_.x,'\n') # presenta el valor del atributo del objeto

print ('PUNTO_.y ',PUNTO_.y,'\n') # presenta el valor del atributo del objeto

print ('crear una clase descriptor con  __get__ y __set__ ; class propiedades (object) : \n')

class propiedades (object) : # definicion de la clase -descriptor-
	def __init__ (self,adquirir,conjunto=None) : # definicion del metodo , inicializa la clase con los argumentos indicados -valor por defecto-
		self.__adquirir = adquirir # asigna el valor al atributo privado
		self.__conjunto = conjunto # asigna el valor al atributo privado
		self.__name__ = adquirir.__name__ # asigna el valor al metodo del objeto -nombre-
		
	def __get__ (self,instancia,propiedad=None) : # definicion del metodo especial
		if instancia is None : # condicion , si el valor es None
			return self # devuelve el objeto
		return self.__adquirir (instancia) # devuelve la funcion con el argumento 
	
	def __set__ (self,instancia,valor) : # definicion del metodo especial
		if self.__conjunto is None : # condicion , si el valor es None
			raise AttributeError ('"{0}" es solo lectura'.format (self.__name__)) # lanza excepcion indicada con la cadena formateada -nombre objeto-
		return self.__conjunto (instancia,valor) # devuelve la funcion con el argumento
	
	def conjunto (self,conjunto) : # definicion del metodo
		self.__conjunto = conjunto # asigna el valor al atributo privado
		return self.__conjunto # devuelve la funcion o valor
	
print ('crear clase nombreYextension ; class nombreYextension (object) : \n')

class nombreYextension (object) : # definicion de la clase
	def __init__ (self,nombre,extension) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.__nombre = nombre # asigna el valor al atributo privado
		self.extension = extension # asigna el valor al atributo
		
	@propiedades # decorador , decora la funcion inferior con la clase propia -propiedades , descriptor-
	def nombre (self) : # definicion del metodo
		return self.__nombre # devuelve el valor del atributo privado
	
	@propiedades # decorador , decora la funcion inferior con la clase propia -propiedades , descriptor-
	def extension (self) : # definicion del metodo
		return self.__extension # devuelve el valor del atributo privado
	
	@extension.conjunto # decorador , decora la funcion inferior con el metodo la clase propia -propiedades , descriptor-
	def extension (self,extension) : # definicion del metodo
		self.__extension = extension # asigna el valor al atributo privado
	
print ('uso del descriptor en la clase nombreYextension -propiedades- ; nombreExtension = nombreYextension ("capitulo8","backup") \n')

nombreExtension = nombreYextension ("capitulo8","backup") # instancia la clase con los atributos indicados

print ('clase objeto ',nombreExtension.__class__,'\n') # presenta la clase del objeto

print ('nombre clase objeto ',nombreExtension.__class__.__name__,'\n') # presenta el nombre de la clase

print ('contenido de los atributos : \n')

print ('nombreExtension.nombre ',nombreExtension.nombre,'\n') # presenta el valor del atributo del objeto

print ('nombreExtension.extension ',nombreExtension.extension,'\n') # presenta el valor del atributo del objeto

print ('crear decorador de clase ; def delegar (nombreAtributo,nombresMetodo) : \n')

def delegar (nombreAtributo,nombresMetodo) : # definicion de la funcion -decorador de clase-
	def decorador (clase) : # definicion de la funcion local -anidada-
		nonlocal nombreAtributo # indica el atributo como no local -alcanza funcion delegar-
		if nombreAtributo.startswith ('__') : # condicion , si el nombre del atributo empieza con dos guiones bajos -True-
			nombreAtributo = '_{0}{1}'.format (clase.__name__,nombreAtributo.__name__) # asigna la cadena formateada -nombre de la clase y nombre del atributo-
		for nombre in nombresMetodo : # iterador , bucle for in , pasa los metodos a nombre
			setattr (clase,nombre,eval ('lambda self,*lista,**diccionario : self.{0}.{1} (*lista,**diccionario)'.format (nombreAtributo,nombre))) # devuelve un nuevo metodo con la secuencia evaluada por eval
		return clase # devuelve la clase con metodos creados por eval 
	return decorador # devuelve el decorador de clases con los metodos creados

print ('crear decorador de clase ; def completarComparaciones (clase) : \n')

def completarComparaciones (clase) : # definicion de la funcion -decorador de clase-
	assert clase.__lt__ is not object.__lt__,('{0} debe definir < e idealmente =='.format (clase.__name__)) # regla excepcion , si no se cumple lanza excepcion con la cadena formateada indicada -nombre de la clase-
	if clase.__eq__ is object.__eq__ : # condicion , si la pertenencia se cumple 
		clase.__eq__ = lambda self,otro : (not (clase.__lt__ (self,otro) or clase.__lt__ (otro,self))) # asigna el resultado de la funcion lambda
	clase.__ne__ = lambda self,otro : not clase.__eq__ (self,otro) # asigna el resultado de la funcion lambda
	clase.__gt__ = lambda self,otro : clase.__lt__ (self,otro) # asigna el resultado de la funcion lambda
	clase.__le__ = lambda self,otro : not clase.__lt__ (self,otro) # asigna el resultado de la funcion lambda
	clase.__ge__ = lambda self,otro : not clase.__lt__ (self,otro) # asigna el resultado de la funcion lambda
	return clase # devuelve la clase decorada con los metodos especiales de comparacion y sus valores asignados

print ('clases de base abstracta \n')

print ('integradas en python ; numbers y collections \n')

print ('importar numbers ; import numbers \n')

import numbers # importa el modulo indicado

print ('crear clase propia para la clase base abstracta numbers.Number ; class numero (numbers.Number) : \n')

class numero (numbers.Number) : # definicion de la clase -hereda de la clase base abstracta Number-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados
		print ('comprobar si el argumento : {0} es tipo {2} , numero : {1}'.format (valor,'VERDADERO\n' if isinstance (valor,numbers.Number) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no
		

print ('uso de metodos heredados de numbers.Number : \n')

print ('numero (33) \n')

numero (33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero ("33") \n')

numero ("33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero (3.3) \n')

numero (3.3) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero (.33) \n')

numero (.33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero (33j) \n')

numero (33j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero ("tres33") \n')

numero ("tres33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero ("tres") \n')

numero ("tres") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('numero ("hola") \n')

numero ("hola") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero o no

print ('crear clase propia para la clase base abstracta numbers.Complex ; class complejo (numbers.Complex) : \n')

class complejo (numbers.Complex) : # definicion de la clase -hereda de la clase base abstracta Complex-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados
		print ('comprobar si el argumento : {0} es tipo {2} , numero complejo : {1}'.format (valor,'VERDADERO\n' if type (valor) == complex else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero complejo
		
	def __abs__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __complex__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __add__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __eq__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __truediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pos__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __radd__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rpow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rtruediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __neg__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def conjugate (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def imag (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def real (self) : pass # definicion metodo especial -sin definir , no hace nada-
	

print ('uso de metodos heredados de numbers.Complex : \n')

print ('complejo (33) \n')

complejo (33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo ("33") \n')

complejo ("33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo (3.3) \n')

complejo (3.3) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo (.33) \n')

complejo (.33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo (33j) \n')

complejo (33j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo ("tres33") \n')

complejo ("tres33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo ("tres") \n')

complejo ("tres") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo ("hola") \n')

complejo ("hola") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('complejo (.0j) \n')

complejo (.0j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un complejo o no

print ('crear clase propia para la clase base abstracta numbers.Real ; class real (numbers.Real) : \n')

class real (numbers.Real) : # definicion de la clase -hereda de la clase base abstracta Real-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados
		print ('comprobar si el argumento : {0} es tipo {2} , numero real : {1}'.format (valor,'VERDADERO\n' if type (valor) in (int,float) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero real
	def __abs__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ceil__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __add__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __eq__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __truediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pos__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __radd__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rpow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rtruediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __float__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __floor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __floordiv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __le__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __lt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mod__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rfloordiv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmod__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __round__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __trunc__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __neg__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
print ('uso de metodos heredados de numbers.Real : \n')

print ('real (33) \n')

real (33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real ("33") \n')

real ("33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real (3.3) \n')

real (3.3) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real (.33) \n')

real (.33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real (33j) \n')

real (33j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real ("tres33") \n')

real ("tres33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real ("tres") \n')

real ("tres") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real ("hola") \n')

real ("hola") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real (.0j) \n')

real (.0j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('real (-33 / 15) \n')

real (-33 / 15) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un real o no

print ('crear clase propia para la clase base abstracta numbers.Rational ; class racional (numbers.Rational) : \n')

class racional (numbers.Rational) : # definicion de la clase -hereda de la clase base abstracta Rational-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.valor = valor # asigna el valor al atributo
		print ('comprobar si el argumento : {0} es tipo {2} , numero racional : {1}'.format (valor,'VERDADERO\n' if self.fraccion () else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero racional
	
	def fraccion (self) : # definicion metodo
		if type (self.valor) == str and len (self.valor.split ()) == 3 and '/' == self.valor.split () [1]  : # condicion , si se cumple las tres condiciones -cadena y contiene el caracter / , lista de 3 elementos-
			if '.' in self.valor.split () [0] or '.' in self.valor.split () [2] : # condicion , si contiene un punto cualquiera de los dos valores -numero decimal-
				return False # devuelve False -falso-
			else : # si no contienen un punto ninguno de los valores -no son numeros con decimal-
				if int (self.valor.split () [2]) > 0 : # condicion , el segundo valor es un numero natural positivo 
					return True # devuelve True -verdadero-
	
	def __abs__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ceil__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __add__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __eq__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __truediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pos__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __radd__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rpow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rtruediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __floor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __floordiv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __le__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __lt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mod__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rfloordiv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmod__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __round__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __trunc__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __neg__ (self) : pass # definicion metodo especial -sin definir , no hace nada- 
	
	def denominator (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def numerator (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
print ('uso de metodos heredados de numbers.Rational : \n')

print ('racional (33) \n')

racional (33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("33") \n')

racional ("33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional (3.3) \n')

racional (3.3) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional (.33) \n')

racional (.33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional (33j) \n')

racional (33j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("tres33") \n')

racional ("tres33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("tres") \n')

racional ("tres") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("hola") \n')

racional ("hola") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional (.0j) \n')

racional (.0j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional (-33 / 15) \n')

racional (-33 / 15) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("-33 / 15") \n')

racional ("-33 / 15") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("-33 / 1") \n')

racional ("-33 / 1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("-33 / -1") \n')

racional ("-33 / -1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("33 / 1") \n')

racional ("33 / 1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('racional ("3 / 0") \n')

racional ("3 / 0") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un racional o no

print ('crear clase propia para la clase base abstracta numbers.Integral ; class entero (numbers.Integral) : \n')

class entero (numbers.Integral) : # definicion de la clase -hereda de la clase base abstracta Integral-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados
		print ('comprobar si el argumento : {0} es tipo {2} , numero entero : {1}'.format (valor,'VERDADERO\n' if type (valor) is int else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un numero entero

	def __abs__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ceil__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __add__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __eq__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __truediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pos__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __pow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __radd__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmul__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rpow__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rtruediv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __floor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __floordiv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __le__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __lt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __mod__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rfloordiv__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __rmod__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __round__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __trunc__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __neg__ (self) : pass # definicion metodo especial -sin definir , no hace nada- 
	
	def __and__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __int__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __invert__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __lshift__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __or__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __rand__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __rlshift__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ror__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __rrshift__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __rshift__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __rxor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __xor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('uso de metodos heredados de numbers.Integral : \n')

print ('entero (33) \n')

entero (33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("33") \n')

entero ("33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero (3.3) \n')

entero (3.3) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero (.33) \n')

entero (.33) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero (33j) \n')

entero (33j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("tres33") \n')

entero ("tres33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("tres") \n')

entero ("tres") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("hola") \n')

entero ("hola") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero (.0j) \n')

entero (.0j) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero (-33 / 15) \n')

entero (-33 / 15) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("-33 / 15") \n')

entero ("-33 / 15") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("-33 / 1") \n')

entero ("-33 / 1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("-33 / -1") \n')

entero ("-33 / -1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("33 / 1") \n')

entero ("33 / 1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('entero ("3 / 0") \n')

entero ("3 / 0") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un entero o no

print ('importar collections ; import collections \n')

import collections # importa el modulo indicado

print ('crear funcion de prueba ; def funcionPrueba () : pass \n')

def funcionPrueba () : pass # definicion de la funcion , no hace nada -devuelve None- , pass funcion de relleno -no hace nada-

print ('crear clase propia para la clase base abstracta collections.Callable ; class llamable (collections.Callable) : \n')

class llamable (collections.Callable)  : # definicion de la clase -hereda de la clase base abstracta Callable-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados
		print ('comprobar si el argumento : {0} es tipo {2} , es llamable : {1}'.format (valor,'VERDADERO\n' if valor in (None,True,False) or type (valor) in (int,float,complex,str,tuple,list,dict,object) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo 
	
	def __call__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('uso de metodos heredados de collections.Callable : \n')

print ('llamable (funcionPrueba ()) \n')

llamable (funcionPrueba ()) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo

print ('llamable (funcionPrueba) \n')

llamable (funcionPrueba) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo

print ('crear clase propia para la clase base abstracta collections.Container ; class contenedor (collections.Container) : \n')

class contenedor (collections.Container) : # definicion de la clase -hereda de la clase base abstracta Container-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  contenedor in  : {1}'.format (valor,'VERDADERO\n' if len (valor.split ()) == 3 and valor.split () [1] == 'in' else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; in
		
	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada- 

print ('uso de metodos heredados de collections.Container : \n')

print ('contenedor ("33") \n')

contenedor ("33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("3.3") \n')

contenedor ("3.3") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (".33") \n')

contenedor (".33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("33j") \n')

contenedor ("33j") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("tres33") \n')

contenedor ("tres33") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("tres") \n')

contenedor ("tres") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("hola") \n')

contenedor ("hola") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (".0j") \n')

contenedor (".0j") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("-33 / 15") \n')

contenedor ("-33 / 15") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("-33 / 15") \n')

contenedor ("-33 / 15") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("-33 / 1") \n')

contenedor ("-33 / 1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("-33 / -1") \n')

contenedor ("-33 / -1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("33 / 1") \n')

contenedor ("33 / 1") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor ("3 / 0") \n')

contenedor ("3 / 0") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (\"\'/\' in \'/\'") \n')

contenedor ("'/' in '/'") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (\"\'/\'in\'/\'") \n')

contenedor ("'/'in'/'") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (\"\'/\' in (\'/\',\'!\')") \n')

contenedor ("'/' in ('/','!')") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (\"\'/\' in [\'/\',\'!\']") \n')

contenedor ("'/' in ['/','!']") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('contenedor (\"\'/\' == \'/\'") \n')

contenedor ("'/' == '/'") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un contenedor o no

print ('crear clase propia para la clase base abstracta collections.Hashable ; class cabeceraResumen (collections.Hashable) : \n')

class cabeceraResumen (collections.Hashable) : # definicion de la clase -hereda de la clase base abstracta Hashable-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  hash  : {1}'.format (valor,'VERDADERO\n' if len (valor.split ()) == 2 and valor.split () [0] == 'hash' else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; hash 
		
	def __hash__ (self) : pass # definicion metodo especial -sin definir , no hace nada- 

print ('uso de metodos heredados de collections.Hashable : \n')

print ('cabeceraResumen ("hash (\'prueba\')") \n')

cabeceraResumen ("hash ('prueba')") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un hash o no

print ('cabeceraResumen ("hash") \n')

cabeceraResumen ("hash") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un hash o no

print ('crear clase propia para la clase base abstracta collections.Iterable ; class iterable (collections.Iterable) : \n')

class iterable (collections.Iterable) : # definicion de la clase -hereda de la clase base abstracta Iterable-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  iterable  : {1}'.format (valor,'VERDADERO\n' if type (valor) in (str,tuple,list,dict,set) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; iterable 
		
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('uso de metodos heredados de collections.Iterable : \n')

print ('iterable ("prueba") \n')

iterable ("prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterable o no

print ('iterable (("prueba",1,.6)) \n')

iterable (("prueba",1,.6)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterable o no

print ('iterable (["prueba",1,.6]) \n')

iterable (["prueba",1,.6]) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterable o no

print ('iterable ({"prueba" : 1}) \n')

iterable ({"prueba" : 1}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterable o no

print ('iterable (set ({"prueba" : 1})) \n')

iterable (set ({"prueba" : 1})) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterable o no

print ('iterable (123856479) \n')

iterable (123856479) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterable o no

print ('crear clase propia para la clase base abstracta collections.Iterator ; class iterador (collections.Iterator) : \n')

class iterador (collections.Iterator) : # definicion de la clase -hereda de la clase base abstracta Iterator-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  objeto iterador  : {1}'.format (valor,'VERDADERO\n' if 'iterator' in type (valor).__name__ else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; iterador 
		
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __next__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('uso de metodos heredados de collections.Iterator : \n')

print ('iterador (iter ("prueba")) \n')

iterador (iter ("prueba")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterador o no

print ('iterador (iter (("prueba",1,.6))) \n')

iterador (iter (("prueba",1,.6))) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterador o no

print ('iterador (iter (["prueba",1,.6])) \n')

iterador (iter (["prueba",1,.6])) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterador o no

print ('iterador (iter ({"prueba" : 1})) \n')

iterador (iter ({"prueba" : 1})) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterador o no

print ('iterador (iter (set ({"prueba" : 1}))) \n')

iterador (iter (set ({"prueba" : 1}))) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterador o no

print ('iterador (iter (123856479)) \n')

try : # control de excepciones
	iterador (iter (123856479)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un iterador o no
except TypeError as error : # tipo de excepcion
	print ('NO se puede convertir en objeto iterador - {0} - \n'.format (error)) # presenta la cadena formateada con la salida de error -excepcion-

print ('crear clase propia para la clase base abstracta collections.Sized ; class tamaño (collections.Sized) : \n')

class tamaño (collections.Sized) : # definicion de la clase -hereda de la clase base abstracta Sized-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  len   : {1}'.format (valor,'VERDADERO\n' if len (valor.split ()) == 2 and valor.split () [0] == 'len' else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; len 
		
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('uso de metodos heredados de collections.Sized : \n')

print ('tamaño ("iter ("prueba")") \n')

tamaño ("iter (\"prueba\")") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un len o no

print ('tamaño ("len") \n')

tamaño ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un len o no

print ('tamaño ("len (["prueba",1,.6])") \n')

tamaño ("len (['prueba',1,.6])") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un len o no

print ('crear clase propia para la clase base abstracta collections.Mapping ; class mapear (collections.Mapping) : \n')

class mapear (collections.Mapping) : # definicion de la clase -hereda de la clase base abstracta Mapping-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  dict   : {1}'.format (valor,'VERDADERO\n' if type (valor) == dict else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; dict 
		
	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __eq__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ne__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __getitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-  

print ('uso de metodos heredados de collections.Mapping : \n')

print ('mapear ("iter ("prueba")") \n')

mapear ("iter (\"prueba\")") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('mapear ("len") \n')

mapear ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('mapear ("len (["prueba",1,.6])") \n')

mapear ("len (['prueba',1,.6])") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('mapear ({"len" : ["prueba",1,.6]}) \n')

mapear ({"len" : ["prueba",1,.6]}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('crear clase propia para la clase base abstracta collections.MutableMapping ; class mapearMutable (collections.MutableMapping) : \n')

class mapearMutable (collections.MutableMapping) : # definicion de la clase -hereda de la clase base abstracta MutableMapping-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  dict   : {1}'.format (valor,'VERDADERO\n' if type (valor) == dict else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; dict 
		
	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __eq__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ne__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __getitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __setitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __delitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
print ('uso de metodos heredados de collections.MutableMapping : \n')

print ('mapearMutable ("iter ("prueba")") \n')

mapearMutable ("iter (\"prueba\")") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('mapearMutable ("len") \n')

mapearMutable ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('mapearMutable ("len (["prueba",1,.6])") \n')

mapearMutable ("len (['prueba',1,.6])") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('mapearMutable ({"len" : ["prueba",1,.6]}) \n')

mapearMutable ({"len" : ["prueba",1,.6]}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es un dict o no

print ('crear clase propia para la clase base abstracta collections.Sequence ; class secuencia (collections.Sequence) : \n')

class secuencia (collections.Sequence) : # definicion de la clase -hereda de la clase base abstracta Sequence-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  secuencia   : {1}'.format (valor,'VERDADERO\n' if type (valor) in (str,tuple,list,bytes,bytearray) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; secuencia 
		
	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __getitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __reversed__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
print ('uso de metodos heredados de collections.Sequence : \n')

print ('secuencia (iter ("prueba")) \n')

secuencia (iter ("prueba")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia ("len") \n')

secuencia ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia ((["prueba",1,.6],)) \n')

secuencia ((['prueba',1,.6],)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia ({"len" : ["prueba",1,.6]}) \n')

secuencia ({"len" : ["prueba",1,.6]}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia (["prueba",1,.6]) \n')

secuencia (['prueba',1,.6]) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia (b"prueba") \n')

secuencia (b"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia (B"prueba") \n')

secuencia (B"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuencia (bytearray ("prueba","utf8")) \n')

secuencia (bytearray ("prueba","utf8")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no
	
print ('crear clase propia para la clase base abstracta collections.MutableSequence ; class secuenciaMutable (collections.MutableSequence) : \n')

class secuenciaMutable (collections.MutableSequence) : # definicion de la clase -hereda de la clase base abstracta MutableSequence-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  secuencia mutable  : {1}'.format (valor,'VERDADERO\n' if type (valor) in (list,bytearray) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; secuencia 
	
	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __getitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __reversed__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __setitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __delitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def insert (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('uso de metodos heredados de collections.MutableSequence : \n')

print ('secuenciaMutable (iter ("prueba")) \n')

secuenciaMutable (iter ("prueba")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable ("len") \n')

secuenciaMutable ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable ((["prueba",1,.6],)) \n')

secuenciaMutable ((['prueba',1,.6],)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable ({"len" : ["prueba",1,.6]}) \n')

secuenciaMutable ({"len" : ["prueba",1,.6]}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable (["prueba",1,.6]) \n')

secuenciaMutable (['prueba',1,.6]) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable (b"prueba") \n')

secuenciaMutable (b"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable (B"prueba") \n')

secuenciaMutable (B"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('secuenciaMutable (bytearray ("prueba","utf8")) \n')

secuenciaMutable (bytearray ("prueba","utf8")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una secuencia o no

print ('crear clase propia para la clase base abstracta collections.Set ; class conjunto (collections.Set) : \n')

class conjunto (collections.Set) : # definicion de la clase -hereda de la clase base abstracta Set-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  conjunto  : {1}'.format (valor,'VERDADERO\n' if type (valor) in (set,frozenset) else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; conjunto 

	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __le__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __lt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __ne__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __gt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ge__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __and__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __or__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __sub__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __xor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
print ('uso de metodos heredados de collections.Set : \n')

print ('conjunto (iter ("prueba")) \n')

conjunto (iter ("prueba")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto ("len") \n')

conjunto ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto ((["prueba",1,.6],)) \n')

conjunto ((['prueba',1,.6],)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto ({"len" : ["prueba",1,.6]}) \n')

conjunto ({"len" : ["prueba",1,.6]}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto (["prueba",1,.6]) \n')

conjunto (['prueba',1,.6]) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto (b"prueba") \n')

conjunto (b"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto (B"prueba") \n')

conjunto (B"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto (bytearray ("prueba","utf8")) \n')

conjunto (bytearray ("prueba","utf8")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto (set (["prueba",1,.6])) \n')

conjunto (set (['prueba',1,.6])) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('conjunto (frozenset ("esta es la cadena a iterar que devuelve un conjunto set")) \n')

conjunto (frozenset ("esta es la cadena a iterar que devuelve un conjunto set")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto o no

print ('crear clase propia para la clase base abstracta collections.MutableSet ; class conjuntoMutable (collections.MutableSet) : \n')

class conjuntoMutable (collections.MutableSet) : # definicion de la clase -hereda de la clase base abstracta MutableSet-
	def __init__ (self,valor) : # definicion del metodo , inicializa la clase con los argumentos indicados 
		print ('comprobar si el argumento : {0} es tipo {2} , es  conjunto mutable : {1}'.format (valor,'VERDADERO\n' if type (valor) is set else 'FALSO\n',type (valor).__name__)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO dependiendo del tipo ; conjunto mutable

	def __contains__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __le__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iter__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __lt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __ne__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __gt__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __ge__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __and__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __or__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __sub__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __xor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __ior__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __iand__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __ixor__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def __isub__ (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def add (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	def discard (self) : pass # definicion metodo especial -sin definir , no hace nada-
	
	#, , __ixor__, and __isub__  add, discard
print ('uso de metodos heredados de collections.MutableSet : \n')

print ('conjuntoMutable (iter ("prueba")) \n')

conjuntoMutable (iter ("prueba")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable o no

print ('conjuntoMutable ("len") \n')

conjuntoMutable ("len") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable ((["prueba",1,.6],)) \n')

conjuntoMutable ((['prueba',1,.6],)) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable ({"len" : ["prueba",1,.6]}) \n')

conjuntoMutable ({"len" : ["prueba",1,.6]}) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable (["prueba",1,.6]) \n')

conjuntoMutable (['prueba',1,.6]) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable (b"prueba") \n')

conjuntoMutable (b"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable (B"prueba") \n')

conjuntoMutable (B"prueba") # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable (bytearray ("prueba","utf8")) \n')

conjuntoMutable (bytearray ("prueba","utf8")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable (set (["prueba",1,.6])) \n')

conjuntoMutable (set (['prueba',1,.6])) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('conjuntoMutable (frozenset ("esta es la cadena a iterar que devuelve un conjunto set")) \n')

conjuntoMutable (frozenset ("esta es la cadena a iterar que devuelve un conjunto set")) # presenta una cadena formateada indicando el argumento , tipo de argumento y VERDADERO o FALSO si es una conjunto mutable  o no

print ('clase con herencia de clase base abstracta ; class listaOrdenada (collections.Sequence) : pass \n')

class listaOrdenada (collections.Sequence) : # definicion de la clase  -hereda de collections.Sequence- 
	def __getitem__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

	def __len__ (self) : pass # definicion metodo especial -sin definir , no hace nada-

print ('comprobar si la instancia o clase pertenece a CBA ; if isinstance (listaOrdenada (),collections.Sequence) : \n')

if isinstance (listaOrdenada (),collections.Sequence) : # condicion , si devuelve True
	print ('listaOrdenada () es de la clase base abstracta ; collections.Sequence \n') # presenta el texto 
else : # si devuelve False
	print ('listaOrdenada () NO es de la clase base abstracta ; collections.Sequence \n') # presenta el texto

print ('crear la clase CBA ; ELECTRODOMESTICOS \n')

class ELECTRODOMESTICOS (object) : # definicion de la clase
	import abc # importa el modulo indicado
	
	class aparato (metaclass=abc.ABCMeta) : # definicion de la clase anidada -local- , hereda metaclase abc.ABCMeta
		import abc # importa el modulo indicado
		@abc.abstractmethod # decorador , decora la funcion inferior con la funcion del modulo -metodo abstracto-
		def __init__ (self,modelo,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
			self.__modelo = modelo # asigna el valor al atributo privado
			self.precio = precio # asigna el valor al atributo
		
		def obtenerPrecio (self) : # definicion del metodo
			return self.__precio # devuelve el valor del atributo privado
			
		def valorPrecio (self,precio) : # definicion del metodo
			self.__precio = precio # asigna el valor al atributo privado
			
		precio = abc.abstractproperty (obtenerPrecio,valorPrecio) # atributo , asigna las propiedades de los metodos indicados
		
		@property # decorador , decora la funcion inferior con la funcion indicada -propiedades del metodo-
		def modelo (self) : # definicion del metodo
			return self.__modelo # devuelve el valor del atributo privado
		
	class cocina (aparato) : # definicion de la clase anidada -local- , hereda aparato
		def __init__ (self,modelo,precio,combustible) : # definicion del metodo , inicializa la clase con los argumentos indicados
			super ().__init__ (modelo,precio) # inicializa los atributos del metodo padre
			self.combustible = combustible # asigna el valor al atributo
			
		precio = property (lambda self : super ().precio,lambda self,precio : super ().valorPrecio (precio)) # asigna al atributo las propiedades de las funciones lambda -valor clase padre del objeto , valor devuelto por el metodo de la clase padre del objeto-
		
	class frigorifico (aparato) : # definicion de la clase anidada -local- , hereda aparato
		def __init__ (self,modelo,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
			super ().__init__ (modelo,precio) # inicializa los atributos del metodo padre
			
		precio = property (lambda self : super ().precio,lambda self,precio : super ().valorPrecio (precio)) # asigna al atributo las propiedades de las funciones lambda -valor clase padre del objeto , valor devuelto por el metodo de la clase padre del objeto-

	class tostador (aparato) : # definicion de la clase anidada -local- , hereda aparato
		def __init__ (self,modelo,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
			super ().__init__ (modelo,precio) # inicializa los atributos del metodo padre
			
		precio = property (lambda self : super ().precio,lambda self,precio : super ().valorPrecio (precio)) # asigna al atributo las propiedades de las funciones lambda -valor clase padre del objeto , valor devuelto por el metodo de la clase padre del objeto-

	class lavadora (aparato) : # definicion de la clase anidada -local- , hereda aparato
		def __init__ (self,modelo,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
			super ().__init__ (modelo,precio) # inicializa los atributos del metodo padre
			
		precio = property (lambda self : super ().precio,lambda self,precio : super ().valorPrecio (precio)) # asigna al atributo las propiedades de las funciones lambda -valor clase padre del objeto , valor devuelto por el metodo de la clase padre del objeto-

	class televisor (aparato) : # definicion de la clase anidada -local- , hereda aparato
		def __init__ (self,modelo,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
			super ().__init__ (modelo,precio) # inicializa los atributos del metodo padre
			
		precio = property (lambda self : super ().precio,lambda self,precio : super ().valorPrecio (precio)) # asigna al atributo las propiedades de las funciones lambda -valor clase padre del objeto , valor devuelto por el metodo de la clase padre del objeto-

print ('crear la clase CBA ; TEXTO \n')

class TEXTO (object) : # definicion de la clase
	import abc # importa el modulo indicado
	
	class filtrarTexto (metaclass=abc.ABCMeta) : # definicion de la clase anidada -local- , hereda metaclase abc.ABCMeta
		import abc # importa el modulo indicado
		@abc.abstractproperty # decorador , decora la funcion inferior con la funcion del modulo -propiedades del metodo-
		def esTransformador (self) : # definicion del metodo
			raise NotImplementedError () # lanza la excepcion indicada
		
		@abc.abstractmethod # decorador , decora la funcion inferior con la funcion del modulo -abstracion metodo-
		def __call__ (self) : # definicion del metodo especial
			raise NotImplementedError () # lanza la excepcion indicada
		
	class contadorCaracteres (filtrarTexto) : # definicion de la clase anidada -local- , hereda filtrarTexto
		@property # decorador , decora la funcion inferior con la funcion -propiedades del metodo-
		def esTransformador (self) : # definicion del metodo
			return False # devuelve False
		
		def __call__ (self,texto,caracter) : # definicion del metodo especial
			contador = 0 # asigna valor cero al contador
			for Caracter in texto : # iterador , bucle for in , pasa los caracteres de la cadena a Caracter
				if Caracter in caracter : # condicion , si el valor -caracter-  esta en caracter
					contador += 1 # suma uno al valor actual del contador
			return contador # devuelve el valor del contador
		
	class ejecutorCodificadorLongitud (filtrarTexto) : # definicion de la clase anidada -local- , hereda filtrarTexto
		@property # decorador , decora la funcion inferior con la funcion -propiedades del metodo-
		def esTransformador (self) : # definicion del metodo
			return True # devuelve True
		
		def __call__ (self,Bytes) : # definicion del metodo especial
			return bytes (Bytes,'utf8') # # devuelve un objeto en formato byte codificado en utf-8
		
	class ejecutorDecodificadorLongitud (filtrarTexto) : # definicion de la clase anidada -local- , hereda filtrarTexto
		@property # decorador , decora la funcion inferior con la funcion -propiedades del metodo-
		def esTransformador (self) : # definicion del metodo
			return True # devuelve True

		def __call__ (self,Bytes) : # definicion del metodo especial
			return Bytes.decode ('utf8') # devuelve un objeto byte en formato cadena utf-8 -decodifica byte a utf8-

print ('instanciar la clase anidada -local-  contadorCaracteres ; contarVocales = TEXTO ().contadorCaracteres () \n')

contarVocales = TEXTO ().contadorCaracteres () # instancia la clase anidada indicada

print ('contarVocales ("perro pez y gato pez","aeiou") ',contarVocales ("perro pez y gato pez","aeiou"),'\n') # presenta el numero de vocales coincidentes

print ('instanciar la clase anidada -local-  ejecutorCodificadorLongitud ; CODIFICARtexto = TEXTO ().ejecutorCodificadorLongitud () \n')

CODIFICARtexto = TEXTO ().ejecutorCodificadorLongitud () # instancia la clase anidada indicada

print ('codificarTexto = CODIFICARtexto ("este es el texto a codificar") \n')

codificarTexto = CODIFICARtexto ("este es el texto a codificar") # devuelve un objeto byte codificado en formato utf-8

print ('codificarTexto ',codificarTexto,'\n') # presenta el objeto byte 

print ('instanciar la clase anidada -local-  ejecutorDecodificadorLongitud ; DECODIFICARtexto = TEXTO ().ejecutorDecodificadorLongitud () \n')

DECODIFICARtexto = TEXTO ().ejecutorDecodificadorLongitud () # instancia la clase anidada indicada

print ('DECODIFICARtexto (codificarTexto) ',DECODIFICARtexto (codificarTexto),'\n') # presenta una cadena en formato utf-8

print ('crear la clase CBA ; API \n')

class API (object) : # definicion de la clase
	import abc # importa el modulo indicado
	
	class DESHACER (metaclass=abc.ABCMeta) : # definicion de la clase anidada -local- , hereda metaclase abc.ABCMeta
		import abc # importa el modulo indicado
		
		@abc.abstractmethod # decorador , decora la funcion inferior con la funcion del modulo -abstracion metodo-
		def __init__ (self) : # definicion del metodo , inicializa la clase sin argumentos indicados
			self.__undos = [] # asigna lista vacia al atributo privado
			
		@abc.abstractproperty # decorador , decora la funcion inferior con la funcion del modulo -propiedades del metodo-
		def poderDeshacer (self) : # definicion del metodo
			return bool (self.__undos) # devuelve True si la lista no esta vacia , lo contrario False
		
		@abc.abstractmethod # decorador , decora la funcion inferior con la funcion del modulo -abstracion metodo-
		def deshacer (self) : # definicion del metodo
			assert self.__undos,'NADA QUE DESHACER' # regla excepcion , si no se cumple lanza excepcion con la cadena
			self.__undos.pop (self) # elimina un elemento de la lista del objeto y lo devuelve
			
		def añadirDeshacer (self,deshacer) : # definicion del metodo
			self.__undos.append (deshacer) # añade al final de la lista el elemento
		
		def limpiar (self) : # definicion del metodo
			self.__undos = [] # asigna una lista vacia al atributo privado
			
	class APILAR (DESHACER) : # definicion de la clase anidada -local- , hereda DESHACER
		def __init__ (self) : # definicion del metodo , inicializa la clase sin argumentos indicados
			super ().__init__ () # inicializa los atributos del metodo padre 
			self.__apilar = [] # asigna lista vacia al atributo privado
			
		@property # decorador , decora la funcion inferior con la funcion -propiedades del metodo-
		def poderDeshacer (self) : # definicion del metodo
			return super ().poderDeshacer # metodo de la clase padre  -devuelve True si la lista no esta vacia , lo contrario False-
		
		def deshacer (self) : # definicion del metodo
			super ().undo () # metodo de la clase padre  -ejecuta el metodo-
			
		def poner (self,elemento) : # definicion del metodo
			self.__apilar.append (elemento) # añade el elemento al final de la lista del atributo privado
			self.añadirDeshacer (lambda self : self.__apilar.pop ()) # añade el elemento eliminado de la lista del objeto a la lista padre
			
		def pop (self) : # definicion del metodo
			elemento = self.__apilar.pop () # asigna el elemento eliminado de la lista 
			self.añadirDeshacer (lambda self : self.__apilar.append (elemento)) # añade el elemento indicado a la lista del objeto y la lista a la lista padre
			return elemento # devuelve el elemento eliminado
		
	class CARGAR_SALVAR (object) : # definicion de la clase anidada -local-
		def __init__ (self,nombreFichero,*nombresAtributo) : # definicion del metodo , inicializa la clase con los argumentos indicados
			self.nombreFichero = nombreFichero # asigna el valor al atributo
			self.__nombresAtributo = [] # asigna una lista vacia al atributo privado
			for nombre in nombresAtributo : # iterador , bucle for in , pasa los elementos de la tupla a nombre
				if nombre.startswith ('__') : # condicion , si la cadena comienza con dos guiones bajos -True-
					nombre = '_{0}{1}'.format (self.__class__.__name__,nombre) # asigna una cadena formateada -nombre de la clase del objeto y nombre atributo-
				self.__nombresAtributo.append (nombre) # añade el nuevo nombre a la lista 
				
		def salvar (self) : # definicion del metodo
			import pickle # importa el modulo indicado
			with open (self.nombreFichero,'wb') as guardarDatos : # abre y cierra el fichero indicado , asignado como guardarDatos
				datos = [] # asigna una lista vacia
				for nombre in self.__nombresAtributo : # iterador , bucle for in , pasa los elementos de la lista del atributo privado a nombre
					datos.append (getattr (self,nombre)) # añade el atributo si pertenece al objeto
				pickle.dump (datos,guardarDatos,pickle.HIGHEST_PROTOCOL) # guarda los datos en formato pickle en el fichero del objeto
				
		def cargar (self) : # definicion del metodo
			import pickle # importa el modulo indicado
			with open (self.nombreFichero,'rb') as cargarDatos : # abre y cierra el fichero indicado , asignado como cargarDatos
				datos = pickle.load (cargarDatos) # carga los datos almacenados en formato pickle en el objeto fichero
				for nombre,valor in zip (self.__nombresAtributo,datos) : # iterador , bucle for in , pasa los elementos de la lista del atributo privado a nombre y los datos a valor -zip devuelve una tupla de dos elementos con un elemento de cada iterador-
					setattr (self,nombre,valor) # asigna el nombre y valor al objeto
					
	class ficheroAPILAR (DESHACER,CARGAR_SALVAR) : # definicion de la clase anidada -local- , herencia multiple ; hereda DESHACER y CARGAR_SALVAR
		def __init__ (self,nombreFichero) : # definicion del metodo , inicializa la clase con los argumentos indicados
			DESHACER.__init__ (self) # inicializa los atributos del metodo de la clase DESHACER
			CARGAR_SALVAR.__init__ (self,nombreFichero,'__apilar') # inicializa los atributos del metodo de la clase CARGAR_SALVAR
			self.__apilar = [] # asigna una lista vacia al atributo privado
			
		def cargar (self) : # definicion del metodo
			super ().cargar () # llama al metodo de la clase padre
			self.limpiar () # limpia el objeto -la lista del objeto-
		
print ('comprobar si una clase con herencia es subclase -hijo- de una clase -padre- con issubclass \n')

print ('issubclass (listaOrdenada,collections.Sequence) ',issubclass (listaOrdenada,collections.Sequence),'\n') # presenta True si es una subclase de la clase indicada , lo contrario False

print ('clase sin herencia CBA -clase base abstracta- ; class claseSinHerencia_CBA (object) : pass \n')

class claseSinHerencia_CBA (object) : pass # clase sin definir -pass no hace nada , funcion de relleno-

print ('registrar una clase SIN herencia como una clase base abstracta CBA con la funcion register \n')

print ('collections.Sequence.register (claseSinHerencia_CBA) \n')

collections.Sequence.register (claseSinHerencia_CBA) # registra la clase sin herencia CBA como subclase CBA de collections.Sequence

print ('comprobar si es subclase -hijo- de la clase -padre- ; issubclass (claseSinHerencia_CBA,collections.Sequence) ',issubclass (claseSinHerencia_CBA,collections.Sequence),'\n') # presenta True si es una subclase de la clase indicada , lo contrario False

print ('crear una metaclase ; class cargableSalvable (type) : \n')

class cargableSalvable (type) : # definicion de la clase , hereda de la clase type -uso como metaclase-
	def __init__ (self,clase,nombreClase,bases,**diccionario) : # definicion del metodo , inicializa la clase con los argumentos indicados
		super ().__init__ (nombreClase,bases,diccionario) # llama al metodo de la clase padre -type- con los argumentos indicados 
		if 'cargar' not in bases : # condicion , si la cadena -clave- no esta en el diccionario de atributos 
			raise TypeError ('clase "{0}" debe proporcionar un metodo cargar ()'.format (clase)) # lanza la excepcion indicada con la cadena formateada
		
		if 'salvar' not in bases : # condicion , si la cadena -clave- no esta en el diccionario de atributos
			raise TypeError ('clase "{0}" debe proporcionar un metodo salvar ()'.format (clase)) # lanza la excepcion indicada con la cadena formateada
		
print ('crear una clase erronea con metaclase cargableSalvable ; class claseMALA (metaclass=cargableSalvable) : \n')

try : # control de excepciones
	class claseMALA (metaclass=cargableSalvable) : # definicion de la clase , usa la metaclase ; cargableSalvable
		def unmetodo (self) : pass # metodo sin definir -pass no hace nada , funcion de relleno- 
except TypeError as error : # tipo de excepcion , pasa la salida a error
	print ('** ERROR **  {0} \n'.format (error)) # presenta el mensaje de error en la cadena formateada
	
print ('crear una clase buena con metaclase cargableSalvable ; class claseBUENA (metaclass=cargableSalvable) : \n')

class claseBUENA (metaclass=cargableSalvable) : # definicion de la clase , usa la metaclase ; cargableSalvable
	def cargar (self) : pass # metodo sin definir -pass no hace nada , funcion de relleno-

	def salvar (self) : pass # metodo sin definir -pass no hace nada , funcion de relleno-

print ('crear metaclase ; class propiedadesAutoSlot (type) : \n')

class propiedadesAutoSlot (type) : # definicion de la clase , hereda de la clase type -uso como metaclase-
	def __new__ (self,clase,nombreClase,bases,**diccionario) : # definicion metodo especial , inicializa la clase con los nuevos argumentos indicados
		GET = [clave for clave in bases if clave.startswith ('get_')]
		if not GET :
			raise TypeError ('la clase : {0}   no contiene ningun metodo get_ '.format (clase))
		SET = [clave for clave in bases if clave.startswith ('set_')]
		if not SET :
			raise TypeError ('la clase : {0}   no contiene ningun metodo set_ '.format (clase))
		slots = [] 
		for obtenerNombre in GET : # iterador , bucle for in , pasa las claves que empiezan por la cadena indicada en el condicional de la lista por compresion a nombre
			if isinstance (bases [obtenerNombre],collections.Callable) : # condicion , si el atributo pertenece a la clase
				nombre = obtenerNombre [4 : ] # asigna el nombre del atributo sin el prefijo ; get_
				slots.append ('__' + nombre) # añade a la lista el nombre del atributo con el prefijo ; __ -doble guion bajo-
				obtenerELIMINADO = bases.pop (obtenerNombre) # asigna el atributo eliminado del diccionario devuelto por pop
				conjuntoNombre = 'set_' + nombre # asigna el nombre del atributo con el prefijo ; set_
				conjunto = bases.get (conjuntoNombre,None) # asigna el atributo indicado del diccionario
				if (conjunto is not None and isinstance (conjunto,collections.Callable)) : # condicion , si se cumplem las dos condiciones -el valor no es None y pertenece a la clase-
					del bases [conjuntoNombre] # elimina el atributo del diccionario
				bases [nombre] = property (obtenerELIMINADO,conjunto) # asigna al diccionario la clave -nombre- y como valor las propiedades de los atributos indicados en obtenerELIMINADO y conjunto
		bases ['__slots__'] = tuple (slots) # añade al diccionario la clave y su valor -clave ; __slots__ y valor ; tupla con los elementos de la lista-
		return super ().__new__ (self,clase,nombreClase,bases) # devuelve los nuevos argumentos asignados a la clase padre 
		
print ('crear una clase con la metaclase propiedadesAutoSlot ; class Producto (metaclass=propiedadesAutoSlot) : \n')

class Producto (metaclass=propiedadesAutoSlot) : # definicion de la clase , usa la metaclase ; propiedadesAutoSlot 
	def __init__ (self,codigoBarras,descripcion) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.__codigoBarras = codigoBarras # asigna el valor al atributo privado
		self.descripcion = descripcion # asigna el valor al atributo
		
	def get_obtenerCodigoBarras (self) : # definicion del metodo 
		return self.__codigoBarras # devuelve el valor del atributo privado
	
	def get_obtenerDescripcion (self) : # definicion del metodo 
		return self.__descripcion # devuelve el valor del atributo privado
	
	def set_valorDescripcion (self,descripcion) : # definicion del metodo con argumento
		if descripcion is None or len (descripcion) < 3 : # condicion , si se cumple una de las condiciones -el valor es None o tiene menos de tres caracteres-
			self.__descripcion = '<DESCRIPCION INVALIDA>' # asigna la cadena al atributo privado
		else : # si contiene una cadena mayor de 3 caracteres
			self.__descripcion = descripcion # asigna el valor al atributo privado
			
print ("instanciar clase con metaclase ; p = Producto ('101110110','tuerca 8mm') \n")

try : # control de excepciones
	p = Producto ('101110110','tuerca 8mm') # instancia la clase , modificada por la metaclase ; atributos y metodos -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('error atributos :  {0} \n'.format (error)) # presenta una cadena formateada con el error de salida

print ("asignacion de valor por atributo ; Producto.codigoBarras = '101110110' \n")

Producto.codigoBarras = '101110110' # asigna el valor mediante el atributo

print ("asignacion de valor por atributo ; Producto.descripcion = 'tuerca 8mm' \n")

Producto.descripcion = 'tuerca 8mm' # asigna el valor mediante el atributo

print ('Producto.get_obtenerCodigoBarras() \n')

try : # control de excepciones
	Producto.get_obtenerCodigoBarras() # llama al metodo modificado por la metaclase ; modifica nombre -lanza excepcion- 
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('error atributos :  {0} \n'.format (error)) # presenta una cadena formateada con el error de salida

print ('Producto.get_obtenerDescripcion() \n')

try : # control de excepciones
	Producto.get_obtenerDescripcion() # llama al metodo modificado por la metaclase ; modifica nombre -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
	print ('error atributos :  {0} \n'.format (error)) # presenta una cadena formateada con el error de salida

print ('Producto.codigoBarras ',Producto.codigoBarras,'\n') # presenta el valor del atributo

print ('Producto.descripcion ',Producto.descripcion,'\n') # presenta el valor del atributo

print ("Producto.set_valorDescripcion (Producto,'tuerca 8mm larga') \n")

Producto.set_valorDescripcion (Producto,'tuerca 8mm larga') # asigna la clase y valor del metodo modificado de la clase

print ('Producto.codigoBarras ',Producto.codigoBarras,'\n') # presenta el valor del atributo

print ('Producto.descripcion ',Producto.descripcion,'\n') # presenta el valor del atributo

print ('programacion funcional con funciones y secuencias -mapear una funcion y un iterable- : uso de map (funcion,iterable) \n')

print ('mapeo = map (lambda x : x ** 2,[1,2,3,4]) \n')

mapeo = map (lambda x : x ** 2,[1,2,3,4]) # devuelve un iterador con el resultado del procesado del iterador por la funcion -valor elevado a la potencia de dos-

print ('iterar el objeto mapeado : mapeo ; for valor in mapeo : \n')

for valorMapeo in mapeo : # iterador , bucle for in , pasa los elementos del iterador a valorMapeo
	print (valorMapeo,end=' - ') # presenta el valor mas la cadena final indicada -sustituye salto de linea-
else : # cuando finalice el iterador
	print ('\n\n FIN DEL MAPEO \n') # presenta la cadena
	
print ('convertir un mapeo en lista mediante la funcion list ; list (map (lambda x : x ** 2,[1,2,3,4])) ',list (map (lambda x : x ** 2,[1,2,3,4])),'\n') # presenta una lista con los valores mapeados

print ('crear un mapeo por compresion en una lista ; [X ** 2 for X in [1,2,3,4]] ',[X ** 2 for X in [1,2,3,4]],'\n') # presenta una lista por compresion con los valores mapeados

print ('crear un generador mapeo por compresion ; (X ** 2 for X in [1,2,3,4]) ',(X ** 2 for X in [1,2,3,4]),'\n') # presenta un generador de mapeo

print ('iterar el generador ; for valorGenerador in (X ** 2 for X in [1,2,3,4]) : \n')

for valorGenerador in (X ** 2 for X in [1,2,3,4]) : # iterador , bucle for in , pasa los elementos del generador a valorGenerador
	print (valorGenerador,end=' - ') # presenta el valor mas la cadena final indicada -sustituye salto de linea-
else : # cuando finalice el iterador
	print ('\n\n FIN DEL GENERADOR \n') # presenta la cadena

print ('filtrado de los valores por mapeo : uso de la funcion filter ; filtroMapeo = filter (lambda x : x > 0,[1,-2,3,-4]) \n')

filtroMapeo = filter (lambda x : x > 0,[1,-2,3,-4]) # devuelve un iterador con los valores que cumplen la regla de la funcion lambda

print ('iterar el objeto mapeado : filtroMapeo ; for valorFiltrado in filtroMapeo : \n')

for valorFiltrado in filtroMapeo : # iterador , bucle for in , pasa los elementos del iterador a valorFiltrado
	print (valorFiltrado,end=' - ') # presenta el valor mas la cadena final indicada -sustituye salto de linea-
else : # cuando finalice el iterador
	print ('\n\n FIN DEL FILTRADO \n') # presenta la cadena

print ('convertir un filtro mapeado en lista mediante la funcion list ; list (filter (lambda x : x > 0 ,[1,-2,3,-4])) ',list (filter (lambda x : x > 0,[1,-2,3,-4])),'\n') # presenta una lista con los valores filtrados

print ('crear un filtro mapeado por compresion en una lista ; [X for X in [1,-2,3,-4] if X > 0] ',[X for X in [1,-2,3,-4] if X > 0],'\n') # presenta una lista por compresion con los valores filtrados mapeados

print ('crear un generador mapeo por compresion ; (X for X in [1,-2,3,-4] if X > 0) ',(X for X in [1,-2,3,-4] if X > 0),'\n') # presenta un generador de filtrado mapeado

print ('iterar el generador ; for valorFiltradoGenerador in (X for X in [1,-2,3,-4] if X > 0) : \n')

for valorFiltradoGenerador in (X for X in [1,-2,3,-4] if X > 0) : # iterador , bucle for in , pasa los elementos filtrados del generador a valorFiltradoGenerador
	print (valorFiltradoGenerador,end=' - ') # presenta el valor mas la cadena final indicada -sustituye salto de linea-
else : # cuando finalice el iterador
	print ('\n\n FIN DEL FILTRO GENERADOR \n') # presenta la cadena

print ('uso del modulo ; functools para mapeo ; import functools \n')

import functools # importar modulo indicado

print ('uso de la funcion reduce ; functools.reduce (lambda x,y : x * y,[1,2,3,4]) ',functools.reduce (lambda x,y : x * y,[1,2,3,4]),'\n') # presenta el valor total del iterador

print ('uso del modulo ; operator en mapeo ; import operator \n')

import operator # importar modulo indicado

print ('uso de la funcion mul de operator en reduce ; functools.reduce (operator.mul,[1,2,3,4]) ',functools.reduce (operator.mul,[1,2,3,4]),'\n') # presenta el valor total del iterador -multiplicacion-

print ('funciones integradas de reduccion -all- ; all ([1,2,3,4]) ',all ([1,2,3,4]),'\n') # presenta True , si todos los elementos devuelven True con bool () 

print ('funciones integradas de reduccion -all- ; all ([1,2,3,4,0]) ',all ([1,2,3,4,0]),'\n') # presenta True , si todos los elementos devuelven True con bool () -0 equivale a False en bool ()- , devuelve False

print ('funciones integradas de reduccion -any- ; any ([1,2,3,4]) ',any ([1,2,3,4]),'\n') # presenta True , si uno de los elementos devuelven True con bool () 

print ('funciones integradas de reduccion -any- ; any ([1,2,3,4,0]) ',any ([1,2,3,4,0]),'\n') # presenta True , si uno de los elementos devuelven True con bool ()

print ('funciones integradas de reduccion -max- ; max ([1,2,3,4,0]) ',max ([1,2,3,4,0]),'\n') # presenta el valor mas grande del iterador

print ('funciones integradas de reduccion -min- ; min ([1,2,3,4,0]) ',min ([1,2,3,4,0]),'\n') # presenta el valor mas pequeño del iterador

print ('funciones integradas de reduccion -sum- ; sum ([1,2,3,4,0]) ',sum ([1,2,3,4,0]),'\n') # presenta la suma total de todos los valores

print ('importar modulo os ; import os \n')

import os # importar modulo indicado

print ('uso de la funcion add de operator en reduce : \n')

print ('functools.reduce (operator.add,(os.path.getsize ("./Escritorio/{0}".format (fichero)) for fichero in (fichero for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")))) ',functools.reduce (operator.add,(os.path.getsize ("./Escritorio/{0}".format (fichero)) for fichero in (fichero for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")))),'\n') # presenta el valor total del iterador -suma- , getsize obtiene el tamaño del fichero , generador mapeo ; listdir devuelve una lista del contenido del directorio indicado que empiecen por la cadena indicada en startswith -capitulo8-

print ('uso de la funcion add de operator en reduce con map -mapeado- : \n')

print ('functools.reduce (operator.add,map (os.path.getsize,("./Escritorio/{0}".format (fichero) for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")))) ',functools.reduce (operator.add,map (os.path.getsize,("./Escritorio/{0}".format (fichero) for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")))),'\n') # presenta el valor total del iterador -suma- , getsize obtiene el tamaño del fichero , generador mapeo ; listdir devuelve una lista del contenido del directorio indicado que empiecen por la cadena indicada en startswith -capitulo8-

print  ('uso de la funcion integrada de reduccion sum : \n')

print ('sum (os.path.getsize ("./Escritorio/{0}".format (fichero)) for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")) ',sum (os.path.getsize ("./Escritorio/{0}".format (fichero)) for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")),'\n') # presenta el valor total de los tamaños de los ficheros obtenidos con getsize

print ('funcion parcial ; uso de una funcion existente y unos argumentos para generar una nueva funcion que sustituye a la funcion existente con argumentos fijos \n')

print ('crear funcion parcial con la funcion existente enumerate ; funcionPARCIAL = functools.partial (enumerate,start=1) \n')

funcionPARCIAL = functools.partial (enumerate,start=1) # crea una funcion parcial con la funcion enumerate y el argumento fijo ; start=1

print ('uso de la funcion parcial : \n')

print ('for numeroLinea,fichero in funcionPARCIAL (["./Escritorio/{0}".format (fichero) for fichero in os.listdir ("./Escritorio") if fichero.startswith ("capitulo8")]) : \n')

for numeroLinea,fichero in funcionPARCIAL (["./Escritorio/{0}".format (fichero) for fichero in os.listdir ("./Escritorio")]) : # iterador , bucle for in , pasa los elementos de la lista por compresion a fichero , el numero asignado a numeroLinea , funcionPARCIAL numera los elementos de la lista comenzando por el numero 1
	print ('Nº {0} - {1} \n'.format (numeroLinea,fichero)) # presenta la cadena formateada y sus valores -numero de linea y ruta/nombrefichero-
else : # cuando finalice el iterador
	print ('*** FIN DE LA SECUENCIA ***\n') # presenta la cadena

print ('crear funcion parcial leerFICHERO ; leerFICHERO = functools.partial (open,mode="r",encoding="utf8") \n')

leerFICHERO = functools.partial (open,mode="r",encoding="utf8") # crea la funcion parcial con la funcion open y sus argumentos fijos ; mode y encoding

print ('uso de la funcion parcial leerFICHERO ; with leerFICHERO ("./Escritorio/capitulo8.back") as contenidoFichero : \n')

with leerFICHERO ("./Escritorio/capitulo8.back") as contenidoFichero : # abre y cierra el fichero indicado en la funcion parcial -enlazado como contenidoFichero-
	print (contenidoFichero.read ()) # presenta el contenido del fichero en una sola cadena 
	print ('----- FIN DEL CONTENIDO -----\n') # presenta la cadena

print ('crear funcion parcial crearFICHERO ; crearFICHERO = functools.partial (open,mode="w",encoding="utf8") \n')

crearFICHERO = functools.partial (open,mode="w",encoding="utf8") # crea la funcion parcial con la funcion open y sus argumentos fijos ; mode y encoding

print ('uso de la funcion parcial crearFICHERO ; with crearFICHERO ("./Escritorio/capitulo8") as crearFichero : \n')

with crearFICHERO ("./Escritorio/capitulo8") as crearFichero : # abre y cierra el fichero indicado en la funcion parcial -enlazado como crearFichero-
	print ('----- CREAR FICHERO -----\n') # presenta la cadena
	print ('--- ESCRIBIR CONTENIDO ---\n') # presenta la cadena
	crearFichero.writelines (['#!/usr/bin/env python3 \n','"""fichero creado con la funcion parcial ; crearFICHERO"""\n','\n','esta es la linea escrita en el fichero de capitulo8 \n']) # escribe las cadenas de la secuencia en el fichero que enlaza el objeto
	print ('--- CERRANDO EL FICHERO ---\n') # presenta la cadena 

print ('uso de la funcion parcial leerFICHERO ; with leerFICHERO ("./Escritorio/capitulo8") as contenidoFICHERO : \n')

with leerFICHERO ("./Escritorio/capitulo8") as contenidoFICHERO : # abre y cierra el fichero indicado en la funcion parcial -enlazado como contenidoFICHERO-
	print (contenidoFICHERO.read ()) # presenta el contenido del fichero en una sola cadena 
	print ('----- FIN DEL CONTENIDO -----\n') # presenta la cadena

print ('crear clase descriptorGENERICO ; class descriptorGENERICO (object) : \n')

class descriptorGENERICO (object) : # definicion de la clase
	def __init__ (self,adquirir,valorar) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.adquirir = adquirir # asigna al atributo el valor
		self.valorar = valorar # asigna al atributo el valor
		
	def __get__ (self,instancia,propiedad=None) : # definicion del atributo especial -obtiene la instancia-
		if instancia is None : # condicion , si es none
			return self # devuelve el objeto
		return self.adquirir (instancia) # devuelve el atributo de la instancia
	
	def __set__ (self,instancia,valor) : # definicion del atributo especial -obtiene el atributo y su valor-
		return self.valorar (instancia,valor) # devuelve el atributo y su valor

print ('crear funcion decorador validarCadena ; def validarCadena (nombreAtributo,permetirVacio=True,registro=None,aceptable=None) : \n')

def validarCadena (nombreAtributo,permetirVacio=True,registro=None,aceptable=None) : # definicion de la funcion
	def decorador (clase) : # definicion funcion anidada
		nombre = '__' + nombreAtributo # asigna la nueva cadena -guiones bajos y nombre del atributo
		def adquirir (self) : # definicion funcion anidada
			return getattr (self,nombre) # devuelve el atributo de la clase
		
		def valorar (self,valor) : # definicion funcion anidada
			assert isinstance (valor,str),'{0} debe ser una cadena '.format (nombreAtributo) # regla excepcion , si no se cumple lanza excepcion con la cadena formateada indicada -si valor es una instancia de tipo str (cadena)-
			if not permetirVacio and not valor : # condicion , si los dos valores son falsos -False-
				raise ValueError ('{0} no deberia estar vacio '.format (nombreAtributo)) # lanza excepcion indicada con la cadena formateada
			if ((aceptable is not None and valor not in aceptable) or (registro is not None and not registro.match (valor))) : # condicion , si se cumplem las dos condiciones , aceptable no es None y valor no esta en aceptable y si registro no es None y registro no coincide con valor
				raise ValueError ('{0} no se puede establecer en {1} '.format (nombreAtributo,valor)) # lanza excepcion indicada con la cadena formateada
			setattr (self,nombre,valor) # asigna el atributo y su valor al objeto
		setattr (clase,nombreAtributo,descriptorGENERICO (adquirir,valorar)) # asigna a la clase el atributo y el valor devuelto por la funcion y sus argumentos
		return clase # devuelve la clase con los nuevos atributos asignados por el decorador
	return decorador # devuelve la clase decorada por el decorador

print ('crear funcion decorador validarNumero ; def validarNumero (nombreAtributo,permetirVacio=True,registro=None,aceptable=None) : \n')

def validarNumero (nombreAtributo,permetirVacio=True,registro=None,aceptable=None) : # definicion de la funcion
	def decorador (clase) : # definicion funcion anidada
		nombre = '__' + nombreAtributo # asigna la nueva cadena -guiones bajos y nombre del atributo
		def adquirir (self) : # definicion funcion anidada
			return getattr (self,nombre) # devuelve el atributo de la clase
		
		def valorar (self,valor) : # definicion funcion anidada
			assert isinstance (valor,(int,float)),'{0} debe ser un numero '.format (nombreAtributo) # regla excepcion , si no se cumple lanza excepcion con la cadena formateada indicada -si valor es una instancia de tipo int o float (numero)-
			if not permetirVacio and not valor : # condicion , si los dos valores son falsos -False-
				raise ValueError ('{0} no deberia estar vacio '.format (nombreAtributo)) # lanza excepcion indicada con la cadena formateada
			if ((aceptable is not None and valor not in aceptable) or (registro is not None and not registro.match (valor))) : # condicion , si se cumplem las dos condiciones , aceptable no es None y valor no esta en aceptable y si registro no es None y registro no coincide con valor
				raise ValueError ('{0} no se puede establecer en {1} '.format (nombreAtributo,valor)) # lanza excepcion indicada con la cadena formateada
			setattr (self,nombre,valor) # asigna el atributo y su valor al objeto
		setattr (clase,nombreAtributo,descriptorGENERICO (adquirir,valorar)) # asigna a la clase el atributo y el valor devuelto por la funcion y sus argumentos
		return clase # devuelve la clase con los nuevos atributos asignados por el decorador
	return decorador # devuelve la clase decorada por el decorador

print ('usar los decoradores validarCadena y validarNumero : \n')

import re # importa el modulo indicado

@validarCadena ('nombre',permetirVacio=False) # decorador -valida la cadena con el argumento en False-
@validarCadena ('producto',permetirVacio=False,registro=re.compile (r'[A-Z] {3}\d{4}')) # decorador -valida la cadena con los argumentos-
@validarCadena ('categoria',permetirVacio=False,aceptable=frozenset (['consumible','hardware','software','media'])) # decorador -valida la cadena con los argumentos-
@validarNumero ('precio') # decorador -valida la cadena-
@validarNumero ('cantidad') # decorador -valida la cadena-
class stockPRODUCTO (object) : # definicion de la clase
	def __init__ (self,nombre,producto,categoria,precio,cantidad) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.nombre = nombre # asigna al atributo el valor
		self.producto = producto # asigna al atributo el valor
		self.categoria = categoria # asigna al atributo el valor
		self.precio = precio # asigna al atributo el valor
		self.cantidad = cantidad # asigna al atributo el valor























