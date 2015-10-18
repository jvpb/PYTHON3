#!/usr/bin/env python3
'''control de archivos'''

import sys

print ('VERSION en uso de PYTHON\n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('crear excepcion propia ; class errorIncidente (Exception) : \n')

class errorIncidente (Exception) : # definicion de la clase -hereda de Exception-
	pass # funcion de relleno -no hace nada-

print ('crear clase incidente ; class incidente (object) : \n')

class incidente (object) : # definicion de la clase 
	def __init__ (self,IDinforme,datos,aeropuerto,IDavion,TIPOavion,PORCENTAGEsobreTiposDEhorasPILOTO,HORAStotalesPILOTO,MEDIAaire,narrativa='') : # definicion del metodo , inicializa la clase con los parametros indicados
		assert len (IDinforme) >= 8 and len (IDinforme.split()) == 1,'ID INFORME INVALIDO' # regla excepcion , si no se cumple lanza excepcion con mensaje
		self.__IDinforme = IDinforme # asigna el valor al atributo privado
		self.datos = datos # asigna el valor al atributo
		self.aeropuerto = aeropuerto # asigna el valor al atributo
		self.IDavion = IDavion # asigna el valor al atributo
		self.TIPOavion = TIPOavion # asigna el valor al atributo
		self.PORCENTAGEsobreTiposDEhorasPILOTO = PORCENTAGEsobreTiposDEhorasPILOTO # asigna el valor al atributo
		self.HORAStotalesPILOTO = HORAStotalesPILOTO # asigna el valor al atributo
		self.MEDIAaire = MEDIAaire # asigna el valor al atributo
		self.narrativa = narrativa # asigna el valor al atributo
		import datetime # importa el modulo indicados
		
	@property # decorador , funcion property -modifica el metodo con las propiedades de la funcion property-
	def datos (self) : # definicion del metodo
		return self.__datos # devuelve el valor del atributo privado
	
	@datos.setter # decorador , valor datos -modifica el metodo con las propiedades de setter de la funcion datos.setter-
	def datos (self,dato) : # definicion del metodo
		assert isinstance (dato,datetime.date),'DATO INVALIDO' # regla excepcion , si no se cumple lanza excepcion con mensaje -si no devuelve True , el valor de dato pertenece a una instancia datetime.date-
		self.__datos = dato # asigna el valor al atributo privado
		
print ('crear clase coleccionINCIDENTES -hereda de dict (diccionario)- ; class coleccionINCIDENTES (dict) : \n')

class coleccionINCIDENTES (dict) : # definicion de la clase -hereda de dict (diccionario)-
	def valores (self) : # definicion del metodo
		for IDinforme in self.keys () : # iterador , bucle for in , pasa las claves del diccionario a IDinforme
			yield self [IDinforme] # crea un iterador con los valores de las claves de IDinforme
			
	def elementos (self) : # definicion del metodo
		for IDinforme in self.keys () : # iterador , bucle for in , pasa las claves del diccionario a IDinforme
			yield self (IDinforme,self [IDinforme]) # crea un iterador con tuplas (clave,valor)
			
	def __iter__ (self) : # definicion del metodo especial
		for IDinforme in sorted (super().keys ()) : # iterador , bucle for in , pasa las claves ordenadas del diccionario de la clase padre a IDinforme
			yield IDinforme # crea un iterador con las claves del diccionario
			
	claves = __iter__ # asigna el metodo especial al atributo

	import gzip # importa el modulo indicado
	import pickle # importa el modulo indicado
	import os.path # importa el modulo indicado del paquete os
	
	def EXPORTARpickle (self,nombreFichero,compresion=False) : # definicion del metodo
		cabeceraFichero = None # asigna el valor al objeto fichero 
		try : # control de excepciones
			if compresion : # condicion , si es True
				cabeceraFichero = gzip.open (nombreFichero,'wb') # abre el fichero tipo gzip en modo escritura binaria
			else : # si no es True -False-
				cabeceraFichero = open (nombreFichero,'wb') # abre el fichero en modo escritura binaria
			pickle.dump (self,cabeceraFichero,pickle.HIGHEST_PROTOCOL) # añade los datos del objeto serializados al fichero indicado
			return True # devuelve True -1-
		except (EnvironmentError,pickle.PicklingError) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error exportacion PICKLE : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
			
	def IMPORTARpickle (self,nombreFichero) : # definicion del metodo
		BYTESidentificadorGZIP = b'\x1F\x8B' # cadena binaria identificacion fichero gzip
		cabeceraFichero = None # asigna el valor al objeto fichero 
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'rb') # abre el fichero en modo solo lectura binaria
			cabeceraGZIP = cabeceraFichero.read (len (BYTESidentificadorGZIP)) # lee los primeros bytes del fichero -numeros de bytes indicado por len (BYTESidentificadorGZIP)-
			if cabeceraGZIP == BYTESidentificadorGZIP : # condicion , si coinciden las dos cadenas binarias
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				cabeceraFichero = gzip.open (nombreFichero,'rb') # abre el fichero tipo gzip en modo solo lectura binaria
			else : # si no coinciden
				cabeceraFichero.seek (0) # mueve el puntero de lectura al inicio del fichero
			self.clear () # limpia el diccionario del objeto -asigna un diccionario vacio-
			self.update (pickle.load (cabeceraFichero)) # actualiza el diccionario del objeto con los datos del fichero pickle cargados
			return True # devuelve True -1-
		except (EnvironmentError,pickle.PicklingError) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion PICKLE : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero

print ('crear clase conversorIncidentes ; class conversorIncidentes (object) : \n')

class conversorIncidentes (object) : # definicion de la clase
	import struct # importa el modulo indicado
	import gzip # importa el modulo indicado
	import os.path # importa el modulo indicado del paquete os
	import datetime # importa el modulo indicados
	import textwrap # importa el modulo indicado
	import re # importa el modulo indicado
	import xml.etree # importa el modulo indicado del paquete xml
	import xml.dom # importa el modulo indicado del paquete xml
	import xml.sax # importa el modulo indicado del paquete xml 
	BYTESidentificadorGZIP = b'\x1F\x8B' # cadena binaria identificacion fichero gzip
	identificadorFichero = b'AIB\x00' # asigna byte como identificador fichero
	versionFormato = b'\x00\x01' # asigna byte como identificador version
	numeroEstructura = struct.Struct ('<Idi?') # formato numeros orden bytes little-endian
	def exportarBINARIO (self,nombreFichero,compresion=False) : # definicion del metodo
		def enpaquetarCadena (cadena) : # definicion de la funcion integrada en el metodo
			datos = cadena.encode ('utf-8') # asigna la cadena codificada en formato utf-8
			formato = '<H{0}s'.format (len (datos)) # asigna una cadena formateada que representa a un formato struct
			return struct.pack (formato,len (datos),datos) # devuelve un objeto tipo byte con todos los datos empaquetados
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			if compresion : # condicion , si es True
				cabeceraFichero = gzip.open (nombreFichero,'wb') # abre el fichero tipo gzip en modo escritura binaria
			else : # si no es True -False-
				cabeceraFichero = open (nombreFichero,'wb') # abre el fichero en modo escritura binaria
			cabeceraFichero.write (self.identificadorFichero) # escribe en el fichero la cadena binaria -identificador-
			cabeceraFichero.write (self.versionFormato) # escribe en el fichero la cadena binaria -version-
			for incidente in self.values () : # iterador , bucle for in , pasa los valores del diccionario a incidente
				datosByteArray = bytearray () # asigna la funcion 
				datosByteArray.extend (enpaquetarCadena (incidente.IDinforme)) # añade a la cadena bytearray el valor enpaquetado con struct
				datosByteArray.extend (enpaquetarCadena (incidente.aeropuerto)) # añade a la cadena bytearray el valor enpaquetado con struct
				datosByteArray.extend (enpaquetarCadena (incidente.IDavion)) # añade a la cadena bytearray el valor enpaquetado con struct
				datosByteArray.extend (enpaquetarCadena (incidente.TIPOavion)) # añade a la cadena bytearray el valor enpaquetado con struct
				datosByteArray.extend (enpaquetarCadena (incidente.narrativa.strip())) # añade a la cadena bytearray el valor enpaquetado con struct -strip elimina los espacios en blanco delante y detras de la cadena 
				datosByteArray.extend (self.numeroEstructura.pack (incidente.datos.toordinal(),incidente.PORCENTAGEsobreTiposDEhorasPILOTO,incidente.HORAStotalesPILOTO,incidente.MEDIAaire)) # añade a la cadena bytearray los datos enpaquetados con struct
				cabeceraFichero.write (datos) # escribe en el fichero la cadena binaria con todos los datos añadidos al bytearray
			return True # devuelve True -1-
		except EnvironmentError as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error exportacion BINARIO : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				
	def importarBINARIO (self,nombreFichero) : # definicion del metodo
		def desenpaquetarCadena (cabeceraFichero,eofError=True) : # definicion de la funcion integrada en el metodo
			uint16 = struct.Struct ('<H') # formato cadena binaria de 16 bits
			longitudDatos = cabeceraFichero.read (uint16.size) # lee los 16 byte primeros
			if not longitudDatos : # condicion , si esta vacia -no es True-
				if eofError : # condicion , si es True
					raise ValueError ('tamaño de cadena corrupto o perdido') # lanza excepcion indicada con el mensaje de la cadena
				return None # devuelve None
			longitud = uint16.unpack (longitudDatos) [0] # desenpaqueta la cadena binaria y asigna el primer elemento -posicion 0-
			if longitud == 0 : # condicion , si el valor es cero
				return '' # devuelve una cadena vacia
			datos = cabeceraFichero.read (longitud) # lee los byte indicados del fichero
			if not datos or len (datos) != longitud : # condicion , si datos esta vacio -no es True- o el tamaño no es igual a longitud
				raise ValueError ('tamaño de cadena corrupto o perdido') # lanza excepcion indicada con el mensaje de la cadena
			formato = '<{0}s'.format (longitud) # asigna una cadena formateada -formato de los datos enpaquetados-
			return struct.unpack (formato,datos) [0].decode ('utf8') # desenpaqueta los datos en el formato indicado y pasa el primer elemento -posicion 0- a codificacion utf-8 -unicode- y lo devuelve
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'rb') # abre el fichero en modo solo lectura binaria
			identificador = cabeceraFichero.read (len (self.BYTESidentificadorGZIP)) # asigna el numero de bytes indicados leidos -tamaño igual al de la cadena indicada-
			if identificador == self.BYTESidentificadorGZIP : # condicion , si la cadena leida de byte es igual al de identificador Fichero gzip
				cabeceraFichero.close () # cierra el fichero enlazado al objeto
				cabeceraFichero = gzip.open (nombreFichero,'rb') # abre el fichero tipo gzip en modo solo lectura binaria 
			else : # si no coinciden
				cabeceraFichero.seek (0) # mueve el puntero de lectura al inicio del fichero
			identificador = cabeceraFichero.read (len (self.identificadorFichero)) # asigna el numero de bytes indicados leidos -tamaño igual al de la cadena indicada-
			if identificador != self.identificadorFichero : # condicion , si las cadenas NO coinciden
				raise ValueError ('formato fichero .aib invalido') # lanza excepcion indicada con el mensaje de la cadena
			version = cabeceraFichero.read (len (self.versionFormato)) # asigna el numero de bytes indicados leidos -tamaño igual al de la cadena indicada-
			if version > self.versionFormato : # condicion , si el valor es mayor al de versionFormato
				raise ValueError ('version fichero .aib NO reconocido') # lanza excepcion indicada con el mensaje de la cadena
			self.clear () # limpia el diccionario del objeto 
			while True : # bucle while continuo -mientras se cumpla la condicion
				IDinforme = desenpaquetarCadena (cabeceraFichero,False) # asigna los datos desenpaquetados por la funcion integrada
				if IDinforme is None : # condicion , si el valor devuelto es None
					break # interrumpe el bucle continuo while
				datos = {} # asigna un diccionario vacio
				datos ['IDinforme'] = IDinforme # añade al diccionario la clave : valor
				for nombre in ('aeropuerto','IDavion','TIPOavion','narrativa') : # iterador , bucle for in , pasa las cadenas a nombre
					datos [nombre] = desenpaquetarCadena (cabeceraFichero) # añade las claves y las cadenas desenpaquetas de 16 byte al diccionario
				otrosDatos = cabeceraFichero.read (self.numeroEstructura.size) # asigna el numero de bytes indicados leidos -tamaño igual al valor-
				numeros = self.numeroEstructura.unpack (otrosDatos) # desenpaqueta el bloque -cadena- binario del tamaño indicado
				datos ['datos'] = datetime.date.fromordinal (numeros [0]) # añade la clave : valor al diccionario -fecha en formato ordinario-
				datos ['PORCENTAGEsobreTiposDEhorasPILOTO'] = numeros [1] # añade la clave : valor al diccionario -tipo de horas piloto PORCENTAGE-
				datos ['HORAStotalesPILOTO'] = numeros [2] # añade la clave : valor al diccionario -horas totales piloto-
				datos ['MEDIAaire'] = numeros [3] # añade la clave : valor al diccionario -media aire-
				INCIDENTE = incidente (**datos) # llama a la clase con los argumentos indicados -diccionario-
				self [INCIDENTE.IDinforme] = INCIDENTE # asigna el objeto que enlaza la clase incidente con su argumento al atributo indicado -clave del diccionario-
			return True # devuelve True -1-
		except EnvironmentError as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion BINARIO : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				
	def exportarTEXTO (self,nombreFichero) : # definicion del metodo
		envolturaTexto = textwrap.TextWrapper (sangradoInicial='    ',sangradoPosterior='    ') # objeto envoltura texto con sagrado y formato linea texto predeterminado
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'w') # abre el fichero en modo escritura
			for incidente in self.values () : # iterador , bucle for in , pasa los valores del diccionario a incidente
				narrativa = '\n'.join (envolturaTexto.wrap (incidente.narrativa.strip())) # une todas las lineas modificadas por el objeto envolturaTexto con salto de linea para cada una 
				cabeceraFichero.write ('[{0.IDinforme}]\ndatos={0.datos!s}\nIDavion={0.IDavion}\nTIPOavion={0.TIPOavion}\naeropuerto={aeropuerto}\nPORCENTAGEsobreTiposDEhorasPILOTO={0.PORCENTAGEsobreTiposDEhorasPILOTO}\nHORAStotalesPILOTO={0.HORAStotalesPILOTO}\nMEDIAaire={0.MEDIAaire:d}\n.INICIO_NARRATIVA.\n{narrativa}\n.FIN_NARRATIVA.\n\n'.format (incidente,aeropuerto=incidente.aeropuerto.strip(),narrativa=narrativa)) # escribe cada cadena formateada con salto de linea en el fichero
			return True # devuelve True -1- 
		except EnvironmentError as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error exportacion TEXTO : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				
	def importarTEXTOmanual (self,nombreFichero) : # definicion del metodo
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'r') # abre el fichero en modo solo lectura
			self.clear () # limpia el diccionario del objeto -diccionario vacio-
			datos = {} # diccionario vacio
			narrativa = None # asigna el valor -estado-
			for numeroLinea,linea in enumerate (cabeceraFichero,start=1) : # iterador , bucle for in , enumerate ; numera los elementos de la lista , numeros a numeroLinea y lineas a linea
				linea = linea.rstrip () # separa la linea a partir de la derecha -salto de linea-
				if not linea and narrativa is None : # condicion , si esta vacia la lineas y narrativa es None
					continue # vuelve al siguiente elemento de la lista
				if narrativa is not None : # condicion , si narrativa NO es None -contiene una cadena-
					if linea == '.FIN_NARRATIVA.' : # condicion , si coincide con la cadena
						datos ['narrativa'] = textwrap.dedent (narrativa).strip () # separa separa las cadenas y quita el sangrado añadido con TextWrapper , añade la clave : valor al diccionario
						if len (data) != 9 : # condicion , si el tamaño del diccionario es distinto del valor indicado
							raise errorIncidente ('falta dato en linea numero : {0}'.format (numeroLinea)) # lanza excepcion indicada con el mensaje de la cadena formateada
						INCIDENTE = incidente (**datos) # llama a la clase con el diccionario como argumento
						self [INCIDENTE.IDinforme] = INCIDENTE # añade al diccionario del objeto , el objeto INCIDENTE -datos del diccionario-
						datos = {} # asigna un diccionario vacio
						narrativa = None # asigna el valor -estado-
					else : # si no coincide la cadena 
						narrativa += linea + '\n' # asignacion incremental , añade la linea mas el salto de linea 
				elif (not datos and linea [0] == '[' and linea [-1] == ']') : # condicion , si el diccionario esta vacio y la cadena comienza y termina en parentesis angulares
					datos ['IDinforme'] = linea [1 : -1] # asigna la cadena sin los parentesis angulares al diccionario
				elif '=' in linea : # condicion , si el caracter indicado esta en la cadena 
					clave,valor = linea.split ('=',1) # asignacion multiple , devuelve una lista con los elementos separados asignados en el orden indicado
					if clave == 'datos' : # condicion , si coinciden las dos cadenas
						datos [clave] = datetime.datetime.strptime (valor,'%Y-%m-%d').date () # añade al diccionario la clave : valor -fecha en el formato indicado-
					elif clave == 'PORCENTAGEsobreTiposDEhorasPILOTO' : # condicion , si coinciden las dos cadenas
						datos [clave] = float (valor) # añade al diccionario la clave : valor -valor en punto flotante-
					elif clave == 'HORAStotalesPILOTO' : # condicion , si coinciden las dos cadenas
						datos [clave] = int (valor) # añade al diccionario la clave : valor -valor entero , sin decimales-
					elif clave == 'MEDIAaire' : # condicion , si coinciden las dos cadenas
						datos [clave] = bool (int (valor)) # añade al diccionario la clave : valor -True o False segun el valor-
					else : # si no coincide
						datos [clave] = valor # añade al diccionario la clave : valor
				elif linea == '.INICIO_NARRATIVA.' : # condicion , si coinciden las dos cadenas
					narrativa = '' # asigna la cadena vacia
				else : # si no coincide
					raise KeyError ('error analisis en linea {0}'.format (numeroLinea)) # lanza excepcion indicada con el mensaje de la cadena formateada
			return True # devuelve True -1- 
		except (EnvironmentError,ValueError,KeyError,errorIncidente) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion TEXTO manual : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				
	def importarTEXTOexpresionRegular (self,nombreFichero) : # definicion del metodo
		expresionRegularINCIDENTE = re.compile (r'\[(?P<id>[^]]+)\] (?P<clavevalor>.+?)' r'^\.INICIO_NARRATIVA\.$(?P<narrativa>.*?)' r'^\.FIN_NARRATIVA\.$',re.DOTALL | re.MULTILINE) # compila las expresiones regulares de busqueda texto incidente completo
		expresionRegularClaveValor = re.compile (r'^\s*(?P<clave>[^=]+)\s*=\s*' r'(?P<valor>.+)\s*$',re.MULTILINE) # compila las expresiones regulares de busqueda clave = valor
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'r') # abre el fichero en modo solo lectura
			self.clear () # limpia el diccionario del objeto -diccionario vacio-
			for coincidenciaIncidente in expresionRegularINCIDENTE.finditer (cabeceraFichero.read ()) : # iterador , bucle for in , busca con las expresiones regulares compiladas en el texto devuelto por el fichero y pasa las coincidencias a coincidenciaIncidente
				datos = {} # diccionario vacio
				datos ['IDinforme'] = coincidenciaIncidente.group ('id') # añade al diccionario la clave : valor -el valor de la variable id de la expresion regular compilada-
				datos ['narrativa'] = textwrap.dedent (coincidenciaIncidente.group ('narrativa')).strip () # añade al diccionario la clave : valor , separa el texto en lineas y quita el sangrado a cada linea -el valor de la variable narrativa de la expresion regular compilada-
				claveValor = coincidenciaIncidente.group ('clavevalor') # asigna el valor de la variable clavevalor de la expresion regular compilada
				for coincidencia in expresionRegularClaveValor.finditer (claveValor) : # iterador , bucle for in , busca con las expresiones regulares compiladas en claveValor y las coincidencias las pasa a coincidencia
					datos [coincidencia.group ('clave')] = coincidencia.group ('valor') # añade al diccionario la clave : valor de las variables clave , valor de la expresion regular
				datos ['datos'] = datetime.datetime.strptime (datos ['datos'],'%Y-%m-%d').date () # añade al diccionario la clave : valor , la fecha en el formato indicado
				datos ['PORCENTAGEsobreTiposDEhorasPILOTO'] = (float (datos ['PORCENTAGEsobreTiposDEhorasPILOTO'])) # añade al diccionario la  clave : valor , valor en punto flotante
				datos ['HORAStotalesPILOTO'] = int (datos ['HORAStotalesPILOTO']) # añade al diccionario la  clave : valor , valor entero -sin decimales-
				datos ['MEDIAaire'] = bool (int (datos ['MEDIAaire'])) # añade al diccionario la  clave : valor , valor True o False
				if len (data) != 9 : # condicion , si el tamaño del diccionario es distinto del valor indicado
					raise errorIncidente ('falta dato') # lanza excepcion indicada con el mensaje de la cadena 
				INCIDENTE = incidente (**datos) # llama a la clase con el diccionario como argumento
				self [INCIDENTE.IDinforme] = INCIDENTE # añade al diccionario del objeto , el objeto INCIDENTE -datos del diccionario-
			return True # devuelve True -1-
		except (EnvironmentError,ValueError,KeyError,errorIncidente) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion TEXTO expresion regular : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
	
	def exportarXMLarbol (self,nombreFichero) : # definicion del metodo
		raiz = xml.etree.ElementTree.Element ('INCIDENTES') # añade el elemento indicado  
		for incidente in self.values () : # iterador , bucle for in , pasa los valores del diccionario del objeto a incidente
			elemento = xml.etree.ElementTree.Element ('INCIDENTE',IDinforme=incidente.IDinforme,datos=incidente.datos.isoformat (),IDavion=incidente.IDavion,TIPOavion=incidente.TIPOavion,PORCENTAGEsobreTiposDEhorasPILOTO=str (incidente.PORCENTAGEsobreTiposDEhorasPILOTO),HORAStotalesPILOTO=str (incidente.HORAStotalesPILOTO),MEDIAaire=str (int (incidente.MEDIAaire))) # añade el elemento y sus valores indicados 
			aeropuerto = xml.etree.ElementTree.SubElement (elemento,'aeropuerto') # añade el subelemento indicado al elemento
			aeropuerto.texto = incidente.aeropuerto.strip () # asigna la cadena sin espacios ni saltos de linea
			narrativa = xml.etree.ElementTree.SubElement (elemento,'narrativa') # añade el subelemento indicado al elemento
			narrativa.texto = incidente.narrativa.strip () # asigna las cadenas sin espacios ni saltos de linea
			raiz.append (elemento) # añade los valores de elemento al arbol de elementos -elemento , subelementos y valores-
		arbol = xml.etree.ElementTree.ElementTree (raiz) # añade los elementos al arbol de elementos
		try : # control de excepciones
			tree.write (nombreFichero,'UTF-8') # crea con el nombre indicado el fichero y escribe los datos del arbol de elementos -codificado en utf-8-
		except EnvironmentError as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error exportacion XML arbol : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		return True # devuelve True -1-
	
	def importarXMLarbol (self,nombreFichero) : # definicion del metodo
		try : # control de excepciones
			arbol = xml.etree.ElementTree.parse (nombreFichero) # analiza el contenido del fichero xml -arbol de elementos-
		except (EnvironmentError,xml.parsers.expat.ExpatError) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion XML arbol : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		self.clear () # limpia el diccionario del objeto -diccionario vacio-
		for elemento in arbol.findall ('incidente') : # iterador , bucle for in , busca el elemento indicado en el arbol de elementos y lo pasa a elemento
			try : # control de excepciones
				datos = {} # diccionario vacio
				for atributo in ('IDinforme','datos','IDavion','TIPOavion','PORCENTAGEsobreTiposDEhorasPILOTO','HORAStotalesPILOTO','MEDIAaire') : # iterador , bucle for in , pasa el elemento de la lista a atributo
					datos [atributo] = elemento.get (atributo) # añade el atributo y su valor al diccionario
				datos ['datos'] = datetime.datetime.strptime (datos ['datos'],'%Y-%m-%d').date () # añade al diccionario la clave : valor , la fecha en el formato indicado
				datos ['PORCENTAGEsobreTiposDEhorasPILOTO'] = (float (datos ['PORCENTAGEsobreTiposDEhorasPILOTO'])) # añade al diccionario la clave : valor , valor en float , punto decimal 
				datos ['HORAStotalesPILOTO'] = int (datos ['HORAStotalesPILOTO']) # añade al diccionario la clave : valor , valor en numero entero
				datos ['MEDIAaire'] = bool (int (datos ['MEDIAaire'])) # añade al diccionario la clave : valor , True o False
				datos ['aeropuerto'] = elemento.find ('aeropuerto').texto.strip () # añade al diccionario la clave : valor , cadenas sin espacios ni saltos de linea
				narrativa = elemento.find ('narrativa').texto # asigna el texto del elemento narrativa
				datos ['narrativa'] = (narrativa.strip () if narrativa is not None else '') # añade al diccionario la clave : valor , cadenas sin espacios ni saltos de linea -condicion si no es None , si el valor es None añade una cadena vacia
				INCIDENTE = incidente (**datos) # instancia la clase con el argumento indicado 
				self [INCIDENTE.IDinforme] = INCIDENTE # añade al diccionario del objeto , el objeto INCIDENTE -datos del diccionario-
			except (ValueError,LookupError,errorIncidente) as error : # tipo de excepcion , pasa la salida a error
				print ('{0} : error importacion XML arbol : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
				return False # devuelve False -0-
		return True # devuelve True -1-
	
	def exportarXMLdom (self,nombreFichero) : # definicion del metodo
		dom = xml.dom.minidom.getDOMImplementation () # crea el objeto dom 
		arbol = dom.createDocument (None,'incidentes',None) # crea el documento dom incidentes
		raiz = arbol.documentElement # crea el objeto elemento documento dom 
		for incidente in self.values () : # iterador , bucle for in , pasa los valores del diccionario del objeto a incidente
			elemento = arbol.createElement ('incidente') # crea el elemento incidente del documento dom incidentes
			for atributo,valor in (('IDinforme',incidente.IDinforme),('datos',incidente.datos.isoformat ()),('IDavion',incidente.IDavion),('TIPOavion',incidente.TIPOavion),('PORCENTAGEsobreTiposDEhorasPILOTO',str (incidente.PORCENTAGEsobreTiposDEhorasPILOTO)),('HORAStotalesPILOTO',str (incidente.HORAStotalesPILOTO)),('MEDIAaire',str (int (incidente.MEDIAaire)))) : # iterador , bucle for in , pasa las tuplas desenpaquetadas a atributo y valor 
				elemento.setAttribute (atributo,valor) # añade el atributo y su valor al elemento del documento dom -incidente-
			for nombre,texto in (('aeropuerto',incidente.aeropuerto),('narrativa',incidente.narrativa)) : # iterador , bucle for in , pasa las tuplas desenpaquetadas a nombre y texto
				elementoTexto = arbol.createTextNode (texto) # crea nodo texto del documento dom 
				elementoNombre = arbol.createElement (nombre) # crea el elemento indicado del documento dom 
				elementoNombre.appendChild (elementoTexto) # añade el nodo texto al elemento creado para el documento dom 
				elemento.appendChild (elementoNombre) # añade los elementos hijos y su valor al elemento padre ; incidente
			raiz.appendChild (elemento) # añade el elemento y subelementos y  sus valores al documento dom ; incidentes
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'w',encoding='utf8') # abre el fichero en modo escritura codificando en utf-8
			arbol.writexml (cabeceraFichero,encoding='UTF-8') # escribe el documento dom en el fichero que enlaza el objeto
			return True # devuelve True -1-
		except (EnvironmentError,ValueError,KeyError,errorIncidente) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error exportacion XML dom : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				
	def importarXMLdom (self,nombreFichero) : # definicion del metodo
		def cogerTexto (listaNodos) : # definicion funcion anidada
			texto = [] # lista vacia
			for nodo in listaNodos : # iterador , bucle for in , pasa los elementos -nodos- a nodo
				if nodo.nodeType == node.TEXT_NODE : # condicion , si los dos valores son iguales
					texto.append (node.data) # añade el texto del nodo a la lista
			return ''.join (texto).strip () # devuelve una cadena sin espacios en blanco de inicio y final 
		try : # control de excepciones
			dom = xml.dom.minidom.parse (nombreFichero) # analiza el fichero xml dom 
		except (EnvironmentError,xml.parsers.expat.ExpatError) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion XML dom : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		self.clear () # limpia el diccionario del objeto -diccionario vacio-
		for elemento in dom.getElementsByTagName ('incidente') : # iterador , bucle for in , pasa los elementos hijos del elemento indicado a elemento
			try : # control de excepciones
				datos = {} # diccionario vacio
				for atributo in ('IDinforme','datos','IDavion','TIPOavion','PORCENTAGEsobreTiposDEhorasPILOTO','HORAStotalesPILOTO','MEDIAaire') : # iterador , bucle for in , pasa el elemento de la lista a atributo
					datos [atributo] = elemento.getAttribute (atributo) # añade el atributo y su valor al diccionario
				datos ['datos'] = datetime.datetime.strptime (datos ['datos'],'%Y-%m-%d').date () # añade al diccionario la clave : valor , la fecha en el formato indicado
				datos ['PORCENTAGEsobreTiposDEhorasPILOTO'] = (float (datos ['PORCENTAGEsobreTiposDEhorasPILOTO'])) # añade al diccionario la clave : valor , valor en float , punto decimal 
				datos ['HORAStotalesPILOTO'] = int (datos ['HORAStotalesPILOTO']) # añade al diccionario la clave : valor , valor en numero entero
				datos ['MEDIAaire'] = bool (int (datos ['MEDIAaire'])) # añade al diccionario la clave : valor , True o False
				aeropuerto = elemento.getElementsByTagName ('aeropuerto') [0] # asigna el elemento hijo de la posicion indicada del elemento aeropuerto
				datos ['aeropuerto'] = cogerTexto (aeropuerto.childNodes) # añade al diccionario la clave : valor , texto del nodo hijo de aeropuerto , devuelto por la funcion anidada cogerTexto
				narrativa = elemento.getElementsByTagName ('narrativa') [0] # asigna el elemento hijo de la posicion indicada del elemento narrativa
				datos ['narrativa'] = cogerTexto (narrativa.childNodes) # añade al diccionario la clave : valor , texto del nodo hijo de narrativa , devuelto por la funcion anidada cogerTexto
				INCIDENTE = incidente (**datos) # instancia la clase con el argumento indicado 
				self [INCIDENTE.IDinforme] = INCIDENTE # añade al diccionario del objeto , el objeto INCIDENTE -datos del diccionario-
			except (ValueError,LookupError,errorIncidente) as error : # tipo de excepcion , pasa la salida a error
				print ('{0} : error importacion XML dom : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
				return False # devuelve False -0-
		return True # devuelve True -1-
	
	def exportarXMLmanual (self,nombreFichero) : # definicion del metodo
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			cabeceraFichero = open (nombreFichero,'w',encoding='utf8') # abre el fichero en modo escritura codificacion utf-8
			cabeceraFichero.write ('<?xml version="1.0" encoding="UTF-8"?>\n') # escribe la cadena en el fichero
			cabeceraFichero.write ('<incidentes>\n') # escribe la cadena en el fichero
			for incidente in self.values () : # iterador , bucle for in , pasa los valores del diccionario del objeto a incidente
				cabeceraFichero.write ('<incidente IDinforme={IDinforme} datos="{0.datos!s}" IDavion={IDavion} TIPOavion={TIPOavion} PORCENTAGEsobreTiposDEhorasPILOTO="{0.PORCENTAGEsobreTiposDEhorasPILOTO}" HORAStotalesPILOTO="{0.HORAStotalesPILOTO}" MEDIAaire="{0.MEDIAaire:d}">\n<aeropuerto>{aeropuerto}</aeropuerto>\n<narrativa>\n{narrativa}\n</narrativa>\n</incidente>\n'.format (incidente,IDinforme=xml.sax.saxutils.quoteattr (incidente.IDinforme),IDavion=xml.sax.saxutils.quoteattr (incidente.IDavion),TIPOavion=xml.sax.saxutils.quoteattr (incidente.TIPOavion),aeropuerto=xml.sax.saxutils.quoteattr (incidente.aeropuerto),narrativa='\n'.join (textwrap.wrap (xml.sax.saxutils.escape (incidente.narrativa.strip ()),70)))) # escribe la cadena formateada en el fichero
			cabeceraFichero.write ('</incidentes>\n') # escribe la cadena en el fichero
			return True # devuelve True -1- 
		except (EnvironmentError,ValueError,KeyError,errorIncidente) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error exportacion XML manual : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		finally : # lance excepcion o no , ejecuta el codigo
			if cabeceraFichero is not None : # condicion , si el valor no es None
				cabeceraFichero.close () # cierra el fichero enlazado en el objeto fichero
				
	def importarXMLsax (self,nombreFichero) : # definicion del metodo
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones
			manejador = manejadorIncidenteSax (self) # instancia la clase indicada con el objeto como argumento
			analizador = xml.sax.make_parser () # objeto creador analizador
			analizador.setContentHandler (manejador) # añade el objeto manejador al analizador
			parser.parse (nombreFichero) # analiza el fichero indicado
			return True # devuelve True -1-
		except (EnvironmentError,ValueError,errorIncidente,xml.sax.SAXParseException) as error : # tipo de excepcion , pasa la salida a error
			print ('{0} : error importacion XML sax : {1}'.format (os.path.basename (sys.argv [0]),error)) # presenta la cadena formateada y  sus valores
			return False # devuelve False -0-
		
	class manejadorIncidenteSax (xml.sax.handler.ContentHandler) : # definicion de la clase anidada -hereda xml.sax.handler.ContentHandler-
		def __init__ (self,incidentes) : # definicion del metodo , inicializa la clase con los argumentos y atributos indicados
			super ().__init__ () # inicializa el metodo especial __init__ de la clase padre -clase heredada-
			self.__datos = {} # asigna un diccionario vacio al atributo
			self.__texto = '' # asigna una cadena vacia al atributo privado
			self.__incidentes = incidentes # asigna el valor al atributo privado
			self.__incidentes.clear () # limpia el diccionario del objeto -diccionario vacio-
		
		def startElement (self,nombre,atributos) : # definicion del metodo
			if nombre == 'incidente' : # condicion , si el valor es igual a la cadena
				self.__datos = {} # asigna un diccionario vacio al atributo privado
				for clave,valor in atributos.items () : # iterador , bucle for in , pasa las tuplas de dos elementos del diccionario desenpaquetadas a clave y valor
					if clave == 'datos' : # condicion , si el valor es igual a la cadena
						self.__datos [clave] = datetime.datetime.strptime (valor,'%Y-%m-%d').date () # añade la clave : valor al diccionario , asigna la fecha en el formato indicado
					elif clave == 'PORCENTAGEsobreTiposDEhorasPILOTO' : # condicion , si el valor es igual a la cadena
						self.__datos [clave] = float (valor) # añade la clave : valor al diccionario , asigna valor en punto flotante
					elif clave == 'HORAStotalesPILOTO' : # condicion , si el valor es igual a la cadena
						self.__datos [clave] = int (valor) # añade la clave : valor al diccionario , asigna valor en numero entero
					elif clave == 'MEDIAaire' : # condicion , si el valor es igual a la cadena
						self.__datos [clave] = bool (int (valor)) # añade la clave : valor al diccionario , True o False
					else : # si no coincide con las anteriores cadenas
						self.__datos [clave] = valor # añade la clave : valor al diccionario
			self.__texto = '' # asigna una cadena vacia al atributo privado 
			
		def endElement (self,nombre) : # definicion del metodo
			if nombre == 'incidente' : # condicion , si el valor es igual a la cadena
				if len (self.__datos) != 9 : # condicion , si el valor es distinto del indicado - 9 -
					raise errorIncidente ('faltan datos') # lanza la excepcion indicada con el mensaje de la cadena
				INCIDENTE = incidente (**self.__datos) # crea el objeto de la clase incidente con el argumento del atributo privado
				self.__incidentes [INCIDENTE.IDinforme] = INCIDENTE # añade al diccionario del objeto la clave : valor , el objeto incidente 
			elif name in frozenset ({'aeropuerto','narrativa'}) : # condicion , si el valor esta en los elementos del conjunto devuelto por frozenset 
				self.__datos [nombre] = self.__texto.strip () # añade la clave : valor al diccionario , el texto separado por lineas en una lista
			self.__texto = '' # asigna una cadena vacia al atributo privado
			
		def characters (self,texto) : # definicion del metodo
			self.__texto += texto # asignacion aumentada , añade el texto al contenido actual 

print ('metodos para bytes y bytearray : \n')

print ('cadenaByte = b"lamina" \n')

cadenaByte = b"lamina" # asigna una cadena en formato binario -byte , inmutable ; no se puede modificar-

print ('cadenaByteArray = bytearray (cadenaByte) \n')

cadenaByteArray = bytearray (cadenaByte) # asigna una cadena en formato binario modificable 

print ('añadir valor int 0-255 a bytearray con append ; cadenaByteArray.append (65) \n')

cadenaByteArray.append (65) # añade el valor binario a la cadena bytearray

print ('cadenaByteArray ',cadenaByteArray,'\n') #presenta la cadena bytearray modificada

print ('devolver una copia de la cadena byte con el primer caracter en mayusculas con capitalize ; cadenaByte.capitalize () ',cadenaByte.capitalize (),'\n') # presenta una copia de la cadena byte con el primer caracter en mayusculas

print ('devolver una copia de la cadena bytearray con el primer caracter en mayusculas con capitalize ; cadenaByteArray.capitalize () ',cadenaByteArray.capitalize (),'\n') # presenta una copia de la cadena bytearray con el primer caracter en mayusculas

print ('devolver una copia de la cadena byte centrada en el ancho indicado con center ; cadenaByte.center (25,b"64") ',cadenaByte.center (25,b'@'),'\n') # presenta una copia de la cadena byte centrada en el ancho indicado

print ('devolver el numero de veces que se repite el byte indicado en la cadena byte y bytearray con count : \n')

print ('cadenaByte.count (b"a") ',cadenaByte.count (b"a"),'\n') # presenta el numero de repeticiones del byte indicado

print ('cadenaByteArray.count (b"a") ',cadenaByteArray.count (b"a"),'\n') # presenta el numero de repeticiones del bytearray indicado

print ('devolver un objeto str que representa los byte que utilizan la codificacion indicada -utf-8- con decode ; cadenaByte.decode () ',cadenaByte.decode (),'\n') # presenta un string -cadena- con los bytes en utf-8

print ('devolver True si la cadena byte termina en el byte indicado con endswith ; cadenaByte.endswith ((b"a",b"A")) ',cadenaByte.endswith ((b"a",b"A")),'\n') # presenta True si la cadena byte termina en el byte indicado , lo contrario False

print ('devolver True si la cadena bytearray termina en el byte indicado con endswith ; cadenaByteArray.endswith ((b"a",b"A")) ',cadenaByteArray.endswith ((b"a",b"A")),'\n') # presenta True si la cadena byte termina en el byte indicado , lo contrario False

print ('devolver una copia de la cadena byte con los tabuladores sustituidos por espacios en blanco del tamaño indicado con expandtabs -8- : \n')

print ('cadenaByte.expandtabs () ',cadenaByte.expandtabs (),'\n') # presenta una copia de la cadena byte con los tabuladores sustituidos por espacios en blanco del tamaño indicado

print ('cadenaByteArray.expandtabs () ',cadenaByteArray.expandtabs (),'\n') # presenta una copia de la cadena bytearray con los tabuladores sustituidos por espacios en blanco del tamaño indicado

print ('amplia la cadena bytearray con todos los byte indicados en una secuencia con extend ; cadenaByteArray.extend ((64,66,67,68)) \n')

cadenaByteArray.extend ((64,66,67,68)) # extiende la cadena bytearray con la secuencia indicada

print ('cadenaByteArray ',cadenaByteArray,'\n') # presenta la nueva cadena bytearray

print ('devuelve la posicion mas a la izquierda encontrado del byte indicado en la cadena byte con find ; cadenaByte.find (b"a") ',cadenaByte.find (b"a"),'\n') # presenta la posicion mas a la izquierda de la coincidencia

print ('devuelve la posicion mas a la izquierda encontrado del byte indicado en la cadena bytearray con find ; cadenaByteArray.find (b"a") ',cadenaByteArray.find (b"a"),'\n') # presenta la posicion mas a la izquierda de la coincidencia

print ('devuelve la posicion mas a la derecha encontrado del byte indicado en la cadena byte con rfind ; cadenaByte.rfind (b"a") ',cadenaByte.rfind (b"a"),'\n') # presenta la posicion mas a la derecha de la coincidencia

print ('devuelve la posicion mas a la derecha encontrado del byte indicado en la cadena bytearray con rfind ; cadenaByteArray.rfind (b"a") ',cadenaByteArray.rfind (b"a"),'\n') # presenta la posicion mas a la derecha de la coincidencia

print ('devuelve un objeto byte con los bytes que correspondan con los valores hexadecimales en la cadena indicada con fromhex : \n')

print ('cadenaByte.fromhex (b"97") ',cadenaByte.fromhex ("97"),'\n')

print ('devuelve la posicion mas a la izquierda del valor indicado de la cadena byte con index ; cadenaByte.index ("a") ',cadenaByte.index (b"a"),'\n')

print ('devuelve la posicion mas a la derecha del valor indicado de la cadena byte con rindex ; cadenaByte.rindex ("a") ',cadenaByte.rindex (b"a"),'\n')

print ('insertar un valor 0-255 en la posicion indicada de la cadena bytearray con insert ; cadenaByteArray.insert (2,64) \n')

cadenaByteArray.insert (2,64) # inserta en la posicion indicada el valor indicado

print ('cadenaByteArray ',cadenaByteArray,'\n') # presenta la nueva cadena bytearray

print ('devuelve True si la cadena byte no esta vacia y es alfanumerica con isalnum ; cadenaByte.isalnum () ',cadenaByte.isalnum (),'\n') # presenta True si es una cadena byte alfanumerica

print ('devuelve True si la cadena cadenaByteArray no esta vacia y es alfanumerica con isalnum ; cadenaByteArray.isalnum () ',cadenaByteArray.isalnum (),'\n') # presenta True si es una cadena bytearray alfanumerica

print ('devuelve True si la cadena byte no esta vacia y es alfabetica con isalpha ; cadenaByte.isalpha () ',cadenaByte.isalpha (),'\n') # presenta True si es una cadena byte alfabetica

print ('devuelve True si la cadena cadenaByteArray no esta vacia y es alfabetica con isalpha ; cadenaByteArray.isalpha () ',cadenaByteArray.isalpha (),'\n') # presenta True si es una cadena bytearray alfabetica

print ('devuelve True si la cadena byte no esta vacia y son digitos con isdigit ; cadenaByte.isdigit () ',cadenaByte.isdigit (),'\n') # presenta True si es una cadena byte con numeros

print ('devuelve True si la cadena cadenaByteArray no esta vacia y son digitos con isdigit ; cadenaByteArray.isdigit () ',cadenaByteArray.isdigit (),'\n') # presenta True si es una cadena bytearray con numeros

print ('devuelve True si la cadena byte tiene al menos un caracter en minisculas y caracteres alfabeticos con islower ; cadenaByte.islower () ',cadenaByte.islower (),'\n') # presenta True si es una cadena byte con al menos un caracter en minisculas

print ('devuelve True si la cadena cadenaByteArray tiene al menos un caracter en minisculas y caracteres alfabeticos con islower ; cadenaByteArray.islower () ',cadenaByteArray.islower (),'\n') # presenta True si es una cadena bytearray con al menos un caracter en minisculas

print ('devuelve True si la cadena byte no esta vacia y son espacios en blanco con isspace ; cadenaByte.isspace () ',cadenaByte.isspace (),'\n') # presenta True si es una cadena byte con espacios en blanco

print ('devuelve True si la cadena cadenaByteArray no esta vacia y son espacios en blanco con isspace ; cadenaByteArray.isspace () ',cadenaByteArray.isspace (),'\n') # presenta True si es una cadena bytearray con espacios en blanco

print ('devuelve True si la cadena byte no esta vacia y es estilo titulo con istitle ; cadenaByte.istitle () ',cadenaByte.istitle (),'\n') # presenta True si es una cadena byte con estilo titulo

print ('devuelve True si la cadena bytearray no esta vacia y es estilo titulo con istitle ; cadenaByteArray.istitle () ',cadenaByteArray.istitle (),'\n') # presenta True si es una cadena bytearray con estilo titulo

print ('devuelve True si la cadena byte tiene al menos un caracter en mayusculas y caracteres alfabeticos con isupper ; cadenaByte.isupper () ',cadenaByte.isupper (),'\n') # presenta True si es una cadena byte con al menos un caracter en mayusculas

print ('devuelve True si la cadena cadenaByteArray tiene al menos un caracter en mayusculas y caracteres alfabeticos con isupper ; cadenaByteArray.isupper () ',cadenaByteArray.isupper (),'\n') # presenta True si es una cadena bytearray con al menos un caracter en mayusculas

print ('devuelve la concatenacion de la cadena byte concatenada con la secuencia indicada con join ; cadenaByte.join ((b"A",b" ")) ',cadenaByte.join ((b"A",b" ")),'\n') # presenta la concatenacion de la cadena byte con la secuencia

print ('devuelve la concatenacion de la cadena bytearray concatenada con la secuencia indicada con join ; cadenaByteArray.join ((b"A",b" ")) ',cadenaByteArray.join ((b"A",b" ")),'\n') # presenta la concatenacion de la cadena bytearray con la secuencia

print ('devuelve una copia de la cadena byte alineada a la izquierda con el ancho indicado con ljust ; cadenaByte.ljust (25,b"@") \n')

print (cadenaByte.ljust (25,b"@"),'\n') # presenta la cadena byte alineada a la izquierda con el ancho indicado y relleno

print ('devuelve una copia de la cadena bytearray alineada a la izquierda con el ancho indicado con ljust ; cadenaByteArray.ljust (25,b"@") \n')

print (cadenaByteArray.ljust (25,b"@"),'\n') # presenta la cadena byte alineada a la izquierda con el ancho indicado y relleno

print ('devuelve una copia de la cadena byte alineada a la derecha con el ancho indicado con rjust ; cadenaByte.rjust (25,b"@") \n')

print (cadenaByte.rjust (25,b"@"),'\n') # presenta la cadena byte alineada a la derecha con el ancho indicado y relleno

print ('devuelve una copia de la cadena bytearray alineada a la derecha con el ancho indicado con rjust ; cadenaByteArray.rjust (25,b"@") \n')

print (cadenaByteArray.rjust (25,b"@"),'\n') # presenta la cadena byte alineada a la derecha con el ancho indicado y relleno

print ('devuelve una copia en minusculas de la cadena byte con lower ; cadenaByte.lower () ',cadenaByte.lower (),'\n') # presenta la cadena byte en minisculas

print ('devuelve una copia en minusculas de la cadena bytearray con lower ; cadenaByteArray.lower () ',cadenaByteArray.lower (),'\n') # presenta la cadena bytearray en minisculas

print ('devuelve una tupla de 3 elementos separados de la cadena byte por el separador indicado desde la izquierda con partition ; cadenaByte.partition (b"m") \n')

print (cadenaByte.partition (b"m"),'\n') # presenta la tupla separada desde la izquierda

print ('devuelve una tupla de 3 elementos separados de la cadena bytearray por el separador indicado desde la izquierda con partition ; cadenaByteArray.partition (b"@") \n')

print (cadenaByteArray.partition (b"@"),'\n') # presenta la tupla separada desde la izquierda

print ('devuelve una tupla de 3 elementos separados de la cadena byte por el separador indicado desde la derecha con rpartition ; cadenaByte.rpartition (b"m") \n')

print (cadenaByte.rpartition (b"m"),'\n') # presenta la tupla separada desde la derecha

print ('devuelve una tupla de 3 elementos separados de la cadena bytearray por el separador indicado desde la derecha con rpartition ; cadenaByteArray.rpartition (b"@") \n')

print (cadenaByteArray.rpartition (b"@"),'\n') # presenta la tupla separada desde la derecha

print ('eliminar y devolver el valor de la posicion indicada en la cadena bytearray con pop ; cadenaByteArray.pop (-4) ',cadenaByteArray.pop (-4),'\n') # presenta el elemento eliminado del indice indicado de la cadena bytearray

print ('eliminar la primera coincidencia indicada de la cadena bytearray con remove ; cadenaByteArray.remove (64) \n')

cadenaByteArray.remove (64) # elimina la primera coincidencia indicada de la cadena bytearray  

print ('cadenaByteArray ',cadenaByteArray,'\n') # presenta la cadena bytearray

print ("devuelve una copia de la cadena byte con el primer byte indicado reemplazado por el segundo byte con replace ; cadenaByte.replace (b'a',b'A') \n")

print (cadenaByte.replace (b'a',b'A'),'\n') # presenta una copia con los caracteres cambiados coincidentes cambiados por el segundo

print ("devuelve una copia de la cadena bytearray con el primer byte indicado reemplazado por el segundo byte con replace ; cadenaByteArray.replace (b'a',b'A') \n")

print (cadenaByteArray.replace (b'a',b'A'),'\n') # presenta una copia con los caracteres cambiados coincidentes cambiados por el segundo

print ('invertir los bytearray de la cadena con reverse ; cadenaByteArray.reverse () \n')

cadenaByteArray.reverse () # invierte los bytearray de la cadena

print ('cadenaByteArray ',cadenaByteArray,'\n') # presenta la cadena bytearray

print ('devuelve una lista con la cadena separada por el espacio en blanco o byte indicado con split ; cadenaByte.split (b"a") ',cadenaByte.split (b"a"),'\n') # presenta una lista con la cadena separada por el byte indicado 

print ('devuelve una lista con la cadena separada por el espacio en blanco o byte indicado con split ; cadenaByteArray.split (b"a") \n')

print (cadenaByteArray.split (b"a"),'\n') # presenta una lista con la cadena separada por el byte indicado

print ('devuelve una lista con la cadena separada por la derecha por espacio en blanco o byte indicado con split ; cadenaByte.rsplit (b"a") ',cadenaByte.rsplit (b"a"),'\n') # presenta una lista con la cadena separada por la derecha por el byte indicado 

print ('devuelve una lista con la cadena separada por la derecha por el espacio en blanco o byte indicado con split ; cadenaByteArray.rsplit (b"a") \n')

print (cadenaByteArray.rsplit (b"a"),'\n') # presenta una lista con la cadena separada por la derecha por el byte indicado

print ('devuelve una lista de la cadena byte con las lineas con salto de linea -\\n- con splitlines ; cadenaByte.splitlines() ',cadenaByte.splitlines(),'\n') # presenta una lista con la cadena separada por las lineas con salto de linea

print ('devuelve una lista de la cadena bytearray con las lineas con salto de linea -\\n- con splitlines ; cadenaByteArray.splitlines() ',cadenaByteArray.splitlines(),'\n') # presenta una lista con la cadena separada por las lineas con salto de linea

print ('devuelve True si el byte indicado esta al comienzo de la cadena byte con startwith ; cadenaByte.startswith ((b"l",b"a")) ',cadenaByte.startswith ((b"l",b"a")),'\n') # presenta True si el byte indicado esta al comienzo de la cadena byte

print ('devuelve True si el byte indicado esta al comienzo de la cadena bytearray con startwith ; cadenaByteArray.startswith (b"a") ',cadenaByteArray.startswith (b"a"),'\n') # presenta True si el byte indicado esta al comienzo de la cadena bytearray

print ('devuelve una copia de la cadena byte con el espacio en blanco delantero y final eliminados o el byte indicado con strip ; cadenaByte.strip (b"a") \n')

print (cadenaByte.strip (b"a"),'\n') # presenta una copia de la cadena byte con el byte indicado eliminado

print ('devuelve una copia de la cadena bytearray con el espacio en blanco delantero y final eliminados o el byte indicado con strip ; cadenaByteArray.strip (b"a") \n')

print (cadenaByteArray.strip (b"a"),'\n') # presenta una copia de la cadena bytearray con el byte indicado eliminado

print ('devuelve una copia de la cadena byte con el espacio en blanco delantero eliminados o el byte indicado con lstrip ; cadenaByte.lstrip (b"l") \n')

print (cadenaByte.lstrip (b"l"),'\n') # presenta una copia de la cadena byte con el byte indicado eliminado solo delante -izquierda-

print ('devuelve una copia de la cadena bytearray con el espacio en blanco delantero eliminados o el byte indicado con lstrip ; cadenaByteArray.lstrip (b"a") \n')

print (cadenaByteArray.lstrip (b"a"),'\n') # presenta una copia de la cadena bytearray con el byte indicado eliminado solo delante -izquierda-

print ('devuelve una copia de la cadena byte con el espacio en blanco final eliminados o el byte indicado con rstrip ; cadenaByte.rstrip (b"a") \n')

print (cadenaByte.rstrip (b"a"),'\n') # presenta una copia de la cadena byte con el byte indicado eliminado solo al final -derecha-

print ('devuelve una copia de la cadena bytearray con el espacio en blanco final eliminados o el byte indicado con rstrip ; cadenaByteArray.rstrip (b"l") \n')

print (cadenaByteArray.rstrip (b"l"),'\n') # presenta una copia de la cadena bytearray con el byte indicado eliminado solo al final -derecha-

print ('devuelve una copia de la cadena byte cambiando las mayusculas a minusculas y viciversa con swapcase ; cadenaByte.swapcase () ',cadenaByte.swapcase (),'\n') # presenta una copia de la cadena byte con las mayusculas a minusculas y viciversa

print ('devuelve una copia de la cadena bytearray cambiando las mayusculas a minusculas y viciversa con swapcase ; cadenaByteArray.swapcase () \n')

print (cadenaByteArray.swapcase (),'\n') # presenta una copia de la cadena bytearray con las mayusculas a minusculas y viciversa

print ('devuelve una copia de la cadena byte cambiando la primera letra a mayusculas con title ; cadenaByte.title () ',cadenaByte.title (),'\n') # presenta una copia de la cadena byte con la primera letra a  mayusculas 

print ('devuelve una copia de la cadena bytearray cambiando la primera letra a mayusculas con title ; cadenaByteArray.title () \n')

print (cadenaByteArray.title (),'\n') # presenta una copia de la cadena bytearray con la primera letra a  mayusculas

print ('devuelve una copia de la cadena byte que no contiene los bytes de una segunda cadena indicada y el resto esta sustituido por la tabla de traslacion -256caracteres- del primer argumento con translate : \n')

print ('cadenaByte.translate (None,b"aeiou") ',cadenaByte.translate (None,b"aeiou"),'\n') # presenta una copia de la cadena byte que no contiene los bytes de una segunda cadena indicada y el resto esta sustituido por el byte de la tabla de translacion del primer argumento 

print ('devuelve una copia de la cadena bytearray que no contiene los bytes de una segunda cadena indicada y el resto esta sustituido por la tabla de traslacion -256caracteres- del primer argumento con translate : \n')

print ('cadenaByteArray.translate (None,b"aeiou") ',cadenaByteArray.translate (None,b"aeiou"),'\n') # presenta una copia de la cadena byte que no contiene los bytes de una segunda cadena indicada y el resto esta sustituido por el byte de la tabla de translacion del primer argumento 

print ('devuelve una copia de la cadena byte en mayusculas con upper ; cadenaByte.upper () ',cadenaByte.upper (),'\n') # presenta una copia de la cadena byte con la cadena en mayusculas 

print ('devuelve una copia de la cadena bytearray en mayusculas con upper ; cadenaByteArray.upper () ',cadenaByteArray.upper (),'\n') # presenta una copia de la cadena bytearray con la cadena en mayusculas

print ('devuelve una copia de la cadena byte con el ancho indicado , rellenando con ceros delante con zfill ; cadenaByte.zfill (20) ',cadenaByte.zfill (20),'\n') # presenta una copia de la cadena byte con la cadena en el ancho indicado con ceros delante 

print ('devuelve una copia de la cadena bytearray con el ancho indicado , rellenando con ceros delante con zfill ; cadenaByteArray.zfill (20) \n')

print (cadenaByteArray.zfill (20),'\n') # presenta una copia de la cadena bytearray con la cadena en el ancho indicado con ceros delante 

print ('atributos y metodos de un objeto fichero \n')

print ('crear una copia de capitulo7.py~ \n')

with open ('./Escritorio/capitulo7.py~','r') as leerFichero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como leerFichero , objeto fichero-
	contenidoLeerFichero = leerFichero.read () # asigna el contenido del fichero enlazado -en una sola cadena-
	
print ('comprobar si el fichero esta cerrado con closed ; leerFichero.closed ',leerFichero.closed,'\n') # presenta True si el fichero esta cerrado , lo contrario False 

ficheroCopia = open ('./Escritorio/capitulo7.COPIA','w') # crea el fichero con el nombre indicado y su ruta en modo escritura

ficheroCopia.write (contenidoLeerFichero) # escribe el contenido en el fichero que enlaza el objeto fichero

print ('devolver el descriptor del archivo -si lo tiene- con fileno ; ficheroCopia.fileno () ',ficheroCopia.fileno (),'\n') # presenta el descriptor del archivo

print ('limpiar el objeto fichero con flush ; ficheroCopia.flush () \n')

ficheroCopia.flush () # limpia el objeto fichero

print ('comprobar si el archivo esta asociado a la consola con isatty ; ficheroCopia.isatty () ',ficheroCopia.isatty (),'\n') # presenta True si esta asociado a la consola , lo contrario False

print ('modo en el que se abrio el fichero con mode ; ficheroCopia.mode ',ficheroCopia.mode,'\n') # presenta el modo en el que se abrio el fichero

print ('nombre del fichero enlazado en el objeto fichero con name ; ficheroCopia.name ',ficheroCopia.name,'\n') # presenta el nombre del fichero enlazado en el objeto fichero

print ('tipo de cadena para el salto de linea en el archivo con newlines ; ficheroCopia.newlines ',ficheroCopia.newlines,'\n') # presenta la cadena para el salto de linea encontrado en el fichero

print ('cerrar un fichero con close ; ficheroCopia.close () \n') 

ficheroCopia.close () # cierra el fichero enlazado en el objeto

print ('comprobar si el fichero esta cerrado con closed ; ficheroCopia.closed ',ficheroCopia.closed,'\n') # presenta True si el fichero esta cerrado , lo contrario False

print ('codificacion utilizada para conversion de texto a binario y viciversa con encoding ; ficheroCopia.encoding ',ficheroCopia.encoding,'\n') # presenta la codificacion utilizada para conversion de texto a binario y viciversa

print ('devolver la linea siguiente del fichero con __next__  ; with open ("./Escritorio/capitulo7.COPIA","r") as abrirFichero : abrirFichero.__next__ () \n')

with open ("./Escritorio/capitulo7.COPIA","r") as abrirFichero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como abrirFichero , objeto fichero-
	print (abrirFichero.__next__ ()) # presenta una linea del fichero -la primera linea del fichero-

print ('devolver el numero de byte indicado sin mover la posicion del puntero del archivo con peek ; with open ("./Escritorio/capitulo7.COPIA","rb") as abrirFicheroByte : abrirFicheroByte.peek (40)\n')

with open ("./Escritorio/capitulo7.COPIA","rb") as abrirFicheroByte : # abre y cierra el fichero indicado en modo solo lectura -enlazado como abrirFicheroByte , objeto fichero-
	print (abrirFicheroByte.peek (40),'\n') # presenta los byte indicados 

print ('leer todo el contenido del fichero o el numero de byte indicados con read ; with open ("./Escritorio/capitulo7.COPIA","r") as leerContenido : leerContenido.read () \n') 

with open ("./Escritorio/capitulo7.COPIA","r") as leerContenido : # abre y cierra el fichero indicado en modo solo lectura -enlazado como leerContenido , objeto fichero- 
	print (leerContenido.read ()) # presenta el contenido del fichero

ficheroSoloLectura = open ("./Escritorio/capitulo7.COPIA","r") # objeto fichero , abierto en modo solo lectura

print ('comprobar si un objeto fichero esta abierto en modo solo lectura - r - con readable ; ficheroSoloLectura.readable () ',ficheroSoloLectura.readable (),'\n') # presenta True si es solo lectura , lo contrario False

ficheroSoloLectura.close () # cierra el objeto fichero

print ('leer los bytearray  indicados de un fichero binario y devolver el numero de byte con readinto :  \n')

print ('with open ("./Escritorio/capitulo7.COPIA","rb") as leerContenidoBinario : leerContenidoBinario.readinto (bytearray(leerContenidoBinario.__next__ ())) \n')

with open ("./Escritorio/capitulo7.COPIA","rb") as leerContenidoBinario : # abre y cierra el fichero indicado en modo solo lectura binaria -enlazado como leerContenidoBinario , objeto fichero- 
	print ('numero de byte : {0} \n'.format (leerContenidoBinario.readinto (bytearray(leerContenidoBinario.__next__ ())))) # presenta el numero de byte's leidos de la cadena bytearray indicada

print ('leer una linea o hasta los byte indicados de la linea con readline : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","r") as leerLinea : leerLinea.readline () \n')

with open ("./Escritorio/capitulo7.COPIA","r") as leerLinea : # abre y cierra el fichero indicado en modo solo lectura -enlazado como leerLinea , objeto fichero- 
	print (leerLinea.readline (),'\n') # presenta la linea leida del objeto fichero

print ('leer el contenido del fichero y devolverlo en una lista de lineas con readlines : \n')
	
print ('with open ("./Escritorio/capitulo7.COPIA","r") as leerLineas : leerLineas.readlines () \n')

with open ("./Escritorio/capitulo7.COPIA","r") as leerLineas : # abre y cierra el fichero indicado en modo solo lectura -enlazado como leerLineas , objeto fichero- 
	contenidoFichero = leerLineas.readlines () # asigna la lista devuelta por readlines del objeto fichero

for linea in contenidoFichero : # iterador , bucle for in , pasa los elementos de la lista a linea
	if not linea : # condicion , si es una cadena vacia -False-
		continue # vuelve a la siguiente linea del iterador
	print (linea [ : -1]) # presenta la cadena menos el ultimo caracter -salto de linea-
else : # cuando finalice el iterador 
	print ('numero de lineas : ',len (contenidoFichero),'\n') # presenta la cadena y su valor -numero de lineas-

print ('mover el puntero del archivo hasta la posicion indicada en byte con seek : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","r") as ponerPuntero : ponerPuntero.seek (24) \n')

with open ("./Escritorio/capitulo7.COPIA","r") as ponerPuntero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como ponerPuntero , objeto fichero- 
	ponerPuntero.seek (24) # pone el puntero del fichero en el byte indicado -\n  salto de linea-
	print (ponerPuntero.__next__ ()) # presenta la siguiente linea al salto de linea -posicion del puntero-
	
print ('comprobar si soporta el acceso aleatorio -seek- con seekable : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","r") as accesoPuntero : accesoPuntero.seekable () \n')

with open ("./Escritorio/capitulo7.COPIA","r") as accesoPuntero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como accesoPuntero , objeto fichero- 
	print ('acceso aleatorio ',accesoPuntero.seekable (),'\n') # presenta True si es accesible aleatoriamente , lo contrario False
	
print ('devolver la posicion del puntero del fichero con tell : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","r") as posicionPuntero : posicionPuntero.tell () \n')

with open ("./Escritorio/capitulo7.COPIA","r") as posicionPuntero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como posicionPuntero , objeto fichero- 
	print ('posicion del puntero en el fichero ',posicionPuntero.tell (),'\n') # presenta la posicion actual del puntero

print ('truncar -cortar- el fichero en la posicion actual del puntero o en el tamaño indicado en byte con truncate : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","a") as truncarFichero : truncarFichero.truncate (23) \n')

with open ("./Escritorio/capitulo7.COPIA","a") as truncarFichero : # abre y cierra el fichero indicado en modo añadir -enlazado como truncarFichero , objeto fichero- 
	truncarFichero.truncate (23) # corta -trunca- el fichero en el tamaño indicado en byte's
	 
with open ("./Escritorio/capitulo7.COPIA","r") as nuevoFichero : # abre y cierra el fichero indicado en modo solo lectura -enlazado como nuevoFichero , objeto fichero-
	print ('contenido del fichero ; capitulo7.COPIA : \n') # presenta la cadena 
	print (nuevoFichero.read(),'\n') # presenta el contenido del fichero

print ('comprobar si el fichero esta en modo escritura con writable : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","a") as ficheroEscritura : ficheroEscritura.writable () \n')

with open ("./Escritorio/capitulo7.COPIA","a") as ficheroEscritura : # abre y cierra el fichero indicado en modo añadir -enlazado como ficheroEscritura , objeto fichero- 
	print ('fichero en modo escritura ',ficheroEscritura.writable (),'\n') # presenta True si es escribible , lo contrario False 

print ('escribir contenido en el fichero con write : \n')

print ('with open ("./Escritorio/capitulo7.COPIA","a") as añadirEscritura : añadirEscritura.write ("\'\'\'control de archivos\'\'\'") \n')

with open ("./Escritorio/capitulo7.COPIA","a") as añadirEscritura : # abre y cierra el fichero indicado en modo añadir -enlazado como añadirEscritura , objeto fichero- 
	añadirEscritura.write ("'''control de archivos'''\n") # escribe la cadena en el fichero del objeto 

with open ("./Escritorio/capitulo7.COPIA","r") as nuevoContenido : # abre y cierra el fichero indicado en modo solo lectura -enlazado como nuevoContenido , objeto fichero-
	print ('contenido del fichero ; capitulo7.COPIA : \n') # presenta la cadena 
	print (nuevoContenido.read()) # presenta el contenido del fichero

print ('escribir una secuencia en el fichero con writelines : \n')

with open ("./Escritorio/capitulo7.py~","r") as leerContenido_py : # abre y cierra el fichero indicado en modo añadir -enlazado como leerContenido_py , objeto fichero- 
	contenidoPY = leerContenido_py.readlines () # lee el contenido del fichero y lo devuelve en una lista  

print ('with open ("./Escritorio/capitulo7.COPIA","a") as añadirContenido : añadirContenido.writelines (contenidoPY [2 : ]) \n')

with open ("./Escritorio/capitulo7.COPIA","a") as añadirContenido : # abre y cierra el fichero indicado en modo añadir -enlazado como añadirContenido , objeto fichero- 
	añadirContenido.writelines (contenidoPY [2 : ]) # escribe la secuencia -lista- en el fichero del objeto  -a partir de la posicion 2 de la lista-

print ('contenido del fichero : \n')

with open ("./Escritorio/capitulo7.COPIA","r") as leerLineas1 : # abre y cierra el fichero indicado en modo solo lectura -enlazado como leerLineas1 , objeto fichero- 
	contenidoFichero1 = leerLineas1.readlines () # asigna la lista devuelta por readlines del objeto fichero

for Linea in contenidoFichero1 : # iterador , bucle for in , pasa los elementos de la lista a linea
	if not Linea : # condicion , si es una cadena vacia -False-
		continue # vuelve a la siguiente linea del iterador
	print (Linea [ : -1]) # presenta la cadena menos el ultimo caracter -salto de linea-
else : # cuando finalice el iterador 
	print ('numero de lineas : ',len (contenidoFichero1),'\n') # presenta la cadena y su valor -numero de lineas-

print ('crear la clase grabarFicheroBINARIO \n')

class grabarFicheroBINARIO (object) : # definicion de la clase
	import os # importa el modulo indicado 
	
	__BORRAR = b'\x01' # asigna byte al atributo privado
	__OKAY = b'\x02' # asigna byte al atributo privado
	
	def __init__ (self,nombreFichero,tamañoGrabacion,auto_limpiar=True) : # definicion del metodo , inicializa la clase con los argumentos indicados
		self.__tamañoGrabacion = tamañoGrabacion + 1 # asigna el valor mas uno al atributo privado
		modo = 'w+b' if not os.path.exists (nombreFichero) else 'r+b' # asigna al atributo segun la condicion ; 'w+b' si no existe el fichero o 'r+b' si existe el fichero
		self.__objetoFichero = open (nombreFichero,modo) # asigna el objeto fichero al atributo privado
		self.auto_limpiar = auto_limpiar # asigna el valor al atributo privado
	
	@property # decorador , funcion property  -modifica el metodo con las propiedades de la funcion property-
	def tamañoGrabacion (self) : # definicion del metodo
		return self.__tamañoGrabacion - 1 # devuelve el valor del atributo privado menos uno
	
	@property # decorador , funcion property  -modifica el metodo con las propiedades de la funcion property-
	def nombre (self) : # definicion del metodo
		return self.__objetoFichero.name # devuelve el nombre del fichero del objeto fichero
	
	def limpiar (self) : # definicion del metodo
		self.__objetoFichero.flush () # limpia el fichero del objeto fichero
		
	def cerrar (self) : # definicion del metodo
		self.__objetoFichero.close () # cierra el fichero del objeto fichero
		
	def __setitem__ (self,indice,grabar) : # definicion del metodo especial -objetoBINARIO [indice] = datos-
		assert isinstance (grabar,(byte,bytearray)),'requiere datos binarios' # regla excepcion , si no se cumple lanza excepcion con mensaje
		assert len (grabar) == self.tamañoGrabacion,("grabara exactamente {0} byte's".format (self.tamañoGrabacion)) # regla excepcion , si no se cumple lanza excepcion con mensaje formateado
		self.__objetoFichero.seek (indice * self.__tamañoGrabacion) # mueve el puntero del fichero a la posicion indicada en byte's
		self.__objetoFichero.write (self.__OKAY) # escribe el byte del valor en el fichero
		self.__objetoFichero.write (grabar) # escribe el dato del argumento
		if self.auto_limpiar : # condicion , si es True
			self.__objetoFichero.flush () # limpia el fichero del objeto fichero
			
	def __getitem__ (self,indice) : # definicion del metodo especial -objetoBINARIO [indice]-
		self.__punteroAindice (indice) # llama al metodo privado
		estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
		if estado != self.__OKAY : # condicion , si el valor es distinto
			return None # devuelve None
		return self.__objetoFichero.read (self.tamañoGrabacion) # devuelve la cadena del tamaño indicado en byte's leido del fichero
	
	def __punteroAindice (self,indice) : # definicion del metodo privado
		if self.auto_limpiar : # condicion , si es True
			self.__objetoFichero.flush () # limpia el fichero del objeto fichero
		self.__objetoFichero.seek (0,os.SEEK_END) # pone el puntero del fichero en la posicion indicada desde el final del archivo 
		fin = self.__objetoFichero.tell () # asigna el fichero cortado por la posicion indicada del puntero 
		offset = indice * self.__tamañoGrabacion # asigna el valor de fuera de rango del fichero
		if offset >= fin : # condicion , si es mayor que el nuevo tamaño del fichero
			raise IndexError ('NO grabado en el indice de la posicion {0}'.format (indice)) # lanza la excepcion indicada con el mensaje de la cadena formateada
		self.__objetoFichero.seek (offset) # mueve el puntero del fichero al valor indicado -posicion byte-
		
	def __delitem__ (self,indice) : # definicion del metodo especial -del objetoBINARIO [indice]-
		self.__punteroAindice (indice) # llama al metodo privado
		estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
		if estado != self.__OKAY : # condicion , si el valor es distinto
			return None # devuelve None # definicion del metodo especial -
		self.__objetoFichero.seek (indice * self.__tamañoGrabacion) # mueve el puntero del fichero a la posicion indicada en byte's
		self.__objetoFichero.write (self.__BORRAR) # escribe el byte del valor en el fichero
		if self.auto_limpiar : # condicion , si es True
			self.__objetoFichero.flush () # limpia el fichero del objeto fichero
			
	def desborrar (self,indice) : # definicion del metodo
		self.__punteroAindice (indice) # llama al metodo privado
		estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
		if estado == self.__BORRAR : # condicion , si el valor es el mismo
			self.__objetoFichero.seek (indice * self.__tamañoGrabacion) # mueve el puntero del fichero a la posicion indicada en byte's
			self.__objetoFichero.write (self.__OKAY) # escribe el byte del valor en el fichero
			if self.auto_limpiar : # condicion , si es True
				self.__objetoFichero.flush () # limpia el fichero del objeto fichero
			return True # devuelve True - 1 - 
		return False # devuelve False - 0 - 
	
	def __len__ (self) : # definicion del metodo especial -len (objetoBINARIO)-
		if self.auto_limpiar : # condicion , si es True
			self.__objetoFichero.flush () # limpia el fichero del objeto fichero
		self.__objetoFichero.seek (0,os.SEEK_END) # pone el puntero del fichero en la posicion indicada desde el final del archivo
		fin = self.__objetoFichero.tell () # asigna el fichero cortado por la posicion indicada del puntero
		return fin // self.__tamañoGrabacion # devuelve el resultado de la division truncada -valor int , entero-
	
	def compactarENlugar (self) : # definicion del metodo
		indice = 0 # asigna el valor de inicio
		longitud = len (self) # valor , longitud del objeto
		while indice < longitud : # bucle while , mientras se cumpla la condicion
			self.__punteroAindice (indice) # llama al metodo privado
			estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
			if estado != self.__OKAY : # condicion , si el valor es distinto
				for siguiente in range (indice + 1,longitud) : # iterador , bucle for in , pasa los elementos de la lista de numeros generada por range a siguiente
					self.__punteroAindice (siguiente) # llama al metodo privado
					estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
					if estado == self.__OKAY : # condicion , si el valor es el mismo
						self [indice] = self [siguiente] # asigna el valor del indice del objeto del iterador
						del self [siguiente] # elimina el valor del indice del objeto del iterador
						break # interrumpe el iterador , bucle for in
			else : # si es lo contrario , coincide
				break # interrumpe el bucle while
			indice += 1 # suma uno al valor actual -asignacion aumentada-
		self.__punteroAindice (0) # llama al metodo privado
		estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
		if estado != self.__OKAY : # condicion , si el valor es distinto
			self.__objetoFichero.truncate (0) # corta el fichero al tamaño indicado -byte- , posicion puntero
		else : # si no es distinto
			limite = None # variable -condicion-
			for indice in range (len(self) - 1,0,-1) : # iterador , bucle for in , pasa los elementos de la lista de numeros generada por range a indice -mayor a menor-
				self.__punteroAindice (indice) # llama al metodo privado
				estado = self.__objetoFichero.read (1) # asigna el primer byte leido del fichero
				if estado != self.__OKAY : # condicion , si el valor es distinto
					limite = indice # asigna el valor -posicion-
				else : # si son iguales
					break # interrumpe el bucle for in
			if limite is not None : # condicion , si el valor NO es None
				self.__objetoFichero.truncate (limite * self.__tamañoGrabacion) # corta el fichero al tamaño indicado -byte- , posicion puntero
		self.__objetoFichero.flush () # limpia el fichero del objeto fichero
		
	def compactar (self,hacerBackup=False) : # definicion del metodo
		ficheroCompactado = self.__objetoFichero.name + '.$$$' # asigna el nombre del fichero del objeto mas la cadena de identificacion
		ficheroBackup = self.__objetoFichero.name + '.bak' # asigna el nombre del fichero del objeto mas la cadena de identificacion
		self.__objetoFichero.flush () # limpia el fichero del objeto fichero
		self.__objetoFichero.seek (0) # mueve el puntero del fichero al primer byte -posicion-
		cabeceraFichero = open (ficheroCompactado,'wb') # crea el fichero en modo escritura binaria
		while True : # bucle continuo while
			datos = self.__objetoFichero.read (self.__tamañoGrabacion) # lee una cadena del tamaño indicado en byte's
			if not datos : # condicion , si esta vacio
				break # interrumpe el bucle continuo while
			if datos [ : 1] == self.__OKAY : # condicion , si el primer byte de la cadena tiene el mismo valor
				cabeceraFichero.write (datos) # escribe el valor  en el fichero que enlaza el objeto
		cabeceraFichero.close () # cierra el fichero del objeto
		self.__objetoFichero.close () # cierra el fichero del objeto
		os.rename (self.__objetoFichero.name,ficheroBackup) # el modulo y su funcion renombran el fichero indicado por el de la variable ; ficheroBackup
		os.rename (ficheroCompactado,self.__objetoFichero.name) # el modulo y su funcion renombran el fichero indicado por la variable ; ficheroCompactado por el nombre del fichero del objeto fichero
		if not hacerBackup : # condicion , si es False
			os.remove (ficheroBackup) # el modulo y su funcion borran el fichero indicado en ficheroBackup
		self.__objetoFichero = open (self.__objetoFichero.name,'r+b') # asigna el objeto fichero -lo abre en modo lectura-escritura binario-
		
print ('crear la clase bicicleta \n')

class bicicleta (object) : # definicion de la clase
	def __init__ (self,identificacion,nombre,cantidad,precio) : # definicion del metodo , inicializa la clase con los argumentos indicados
		assert len (identificacion) > 3,'identificacion bicicleta NO valido "{0}"'.format (identificacion) # regla excepcion , si no se cumple lanza excepcion con mensaje formateado
		self.__identificacion = identificacion # asigna el valor al atributo privado
		self.nombre = nombre # asigna el valor al atributo
		self.cantidad = cantidad # asigna el valor al atributo
		self.precio = precio # asigna el valor al atributo
		
	class stockBicicleta (object) : # definicion de la clase anidada
		import struct # importa el modulo indicado
		_BIKE_STRUCT = struct.Struct ('<8s30sid') # crea una estructura del formato indicado
		def __init__ (self,nombreFichero) : # definicion del metodo , inicializa la clase anidada con los argumentos indicados
			self.__fila = grabarFicheroBINARIO (nombreFichero,_BIKE_STRUCT.size) # asigna el objeto al atributo privado
			self.__identidadDESDEindice = {} # asigna diccionario vacio al atributo privado
			for indice in range (len (self.__fila)) : # iterador , bucle for in , pasa los elementos de la lista de numeros generada por range a indice
				grabar = self.__fila [indice] # asigna el objeto -el valor del indice indicado-
				if grabar is not None : # condicion , si el valor no es None
					bici = __biciDESDEgrabar (grabar) # asigna el metodo privado y su argumento
					self.__identidadDESDEindice [bicicleta.identificacion] = indice # asigna la clave : valor al diccionario
					
		def añadir (self,bici) : # definicion del metodo
			indice = len (self.__fila) # asigna el valor
			self.__fila [indice] = __biciDESDEgrabar (bici) # añade al objeto la clave : valor -metodo privado-
			self.__identidadDESDEindice [bicicleta.identificacion] = indice # asigna la clave : valor al diccionario
			
		def __delitem__ (self,identificacion) : # definicion del metodo especial -del objeto.identificacion-
			del self.__fila [self.__identidadDESDEindice [identificacion]] # borra el valor del objeto
			
		def __getitem__ (self,identificacion) : # definicion del metodo especial -objeto [indice]-
			grabar = self.__fila [self.__identidadDESDEindice [identificacion]] # asigna el valor del objeto
			return None if record is None else __biciDESDEgrabar (grabar) # condicion , si se cumple devuelve None , si no llama al metodo privado
		
		def __cambiarStock (self,identificacion,cantidad) : # definicion del metodo privado
			indice = self.__identidadDESDEindice [identificacion] # asigna el valor de la clave del diccionario
			grabar = self.__fila [indice] # asigna el valor del objeto
			if grabar is None : # condicion , si es None
				return False # devuelve False -0-
			bici = __biciDESDEgrabar (grabar) # asigna el metodo privado y su argumento
			bici.cantidad += cantidad # suma el valor al valor del parametro cantidad del objeto -asignacion aumentada-
			self.__fila [indice] = __grabarDESDEbicicleta (bici) # asigna el metodo privado y su argumento
			return True # devuelve True -1-
		
		incrementarStock = (lambda self,identificacion,cantidad : self.__cambiarStock (identificacion,cantidad)) # definicion metodo lambda -aumenta la cantidad-
		
		decrementarStock = (lambda self,identificacion,cantidad : self.__cambiarStock (identificacion,-cantidad)) # definicion metodo lambda -reduce la cantidad-
		
		def __iter__ (self) : # definicion del metodo especial -iter (objeto)-
			for indice in range (len (self.__fila)) : # iterador , bucle for in , pasa los elementos de la lista de numeros generada por range a indice
				grabar = self.__fila [indice] # asigna el valor del objeto
				if grabar is not None : # condicion , si no es None -no esta vacio-
					yield __biciDESDEgrabar (grabar) # guarda los valores -objetos- en el iterador
					
		def __biciDESDEgrabar (grabar) : # definicion de la funcion
			ID,NOMBRE,CANTIDAD,PRECIO = range (4) # desenpaqueta la lista y la asigna a las variables en el orden puesto
			partes = list (_BIKE_STRUCT.unpack (record)) # desenpaqueta la estructura y la convierte en una lista
			partes [ID] = partes [ID].decode ('utf8').rstrip ('\x00') # asigna separa la cadena en formato utf-8 por la cadena indicada -byte- desde la derecha y devuelve una lista
			partes [NOMBRE] = partes [NOMBRE].decode ('utf8').rstrip ('\x00') # asigna separa la cadena en formato utf-8 por la cadena indicada -byte- desde la derecha y devuelve una lista
			return bicicleta (*partes) # devuelve el objeto con su argumento
		
		def __grabarDESDEbicicleta (grabar) : # definicion de la funcion
			return _BIKE_STRUCT.pack (bicicleta.identificacion.encode ('utf8'),bicicleta.nombre.encode ('utf8'),bicicleta.cantidad,bicicleta.precio) # empaqueta en el formato de struct los argumentos de bicicleta , devuelve el objeto empaquetado
		
















































