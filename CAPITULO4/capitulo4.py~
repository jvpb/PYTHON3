#!/usr/bin/env python3
'''estructuras de control y funciones'''

# importar modulo

import sys

print ('VERSION en uso de PYTHON\n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('uso de condiciones multiples -if elif else- \n')

listaPares = [] # lista vacia -añade numeros pares-

listaInpares = [] # lista vacia -añade numeros inpares-

for numero in range (11) : # iterador , bucle for in , pasa los numeros de la lista generada por range a numero
  if numero % 2 == 0 : # condicion , si el resto de la division es cero -numero par-
	   listaPares.append (numero) # añade el numero par a la lista
	   print ('{0} : es un numero par\n'.format(numero)) # presenta la cadena formateada con su valor -numero par-
  elif numero % 2 == 1 : # condicion , si el resto de la division es uno -numero inpar-
	  listaInpares.append (numero) # añade el numero inpar a la lista	  
	  print ('{0} : es un numero inpar\n'.format(numero)) # presenta la cadena formateada con su valor -numero inpar-
else :  # cuando finalice el iterador
  print ('{0} numeros pares : {1} \n'.format(len(listaPares),listaPares)) # presenta la cadena formateada con su valor -cantidad de numeros pares   y lista de numeros pares-
  print ('{0} numeros inpares : {1} \n'.format(len(listaInpares),listaInpares)) # presenta la cadena formateada con su valor -cantidad de numeros inpares   y lista de numeros inpares- 
  
print ('expresion condicional simple ;  sentencia1  if expresionBoleana else sentencia2 \n')

verdadero = 1 # asigna valor booleano -True-

falso = 0 # asigna valor booleano -False-

print ('>>>>> VERDADERO -True-\n') if verdadero else print ('>>>>> FALSO -False-\n')  # si la expresion booleana es verdadera , ejecuta la primera sentencia y si NO la segunda -ultima sentencia-

print ('>>>>> VERDADERO -True-\n') if falso else print ('>>>>> FALSO -False-\n')  # si la expresion booleana es verdadera , ejecuta la primera sentencia y si NO la segunda -ultima sentencia-

print ('bucle condicional while -while condicion- ; while contador <  20 \n')

contador = 0 # contador de bucles while

while contador < 20 : # bucle condicional while , mientras se cumpla la condicion -valor menor  a 20-
	contador += 1 # suma uno al valor actual del contador
else : # si finaliza el bucle while
	print ('** FIN DEL BUCLE while , contador =  ',contador,' **\n') # presenta la cadena y su valor 

print ('bucle iterador for in  -for valor in secuencia- ;  for valor in range (21) \n')

for valor in range (21) : # iterador , bucle for in , pasa los elementos de la lista devuelta por range a valor
   print (valor) # presenta los numeros de la lista
else : # cunado finalice el iterador
   print ('\n\n --- FIN DE LA SECUENCIA ---\n' ) # presenta el texto

print ('control de excepciones (con tipo de excepcion) -try / except / else / finally- ;  valorError = "ERROR"  \n')

valorError = "ERROR" # asigna la cadena 

try : # control de excepciones
	print ('int (valorError)\n') # presenta la cadena
	int (valorError) # lanza excepcion ValueError -el valor NO es un numero en formato cadena-
except ValueError as error : # tipo de error , pasa la salida a error
	print ('este es el mensaje lanzado por except al producirse un error del tipo indicado ; ValueError - {} -\n'.format(error)) # presenta el texto formateado y su valor -salida de error-
else  :  # si no se produce ninguna excepcion
	print ('si no se produce ninguna excepcion -error- , else presenta este mensaje\n') # presenta el texto
finally : # ejecuta el codigo de su bloque aun que no se produzca una excepcion
	print ('este es el mensaje que envia finally se produzca o NO , una excepcion\n') # presenta el texto 

print ('control de excepciones (con tipo de excepcion)  -try / except / else / finally- ;  valorSINerror = 10  \n')

valorSINerror = 10 # asigna un entero 

try : # control de excepciones
	print ('int (valorSINerror)\n') # presenta la cadena
	int (valorSINerror) # lanza excepcion ValueError -el valor NO es un numero en formato cadena-
except ValueError as error : # tipo de error , pasa la salida a error
	print ('este es el mensaje lanzado por except al producirse un error del tipo indicado ; ValueError - {} -\n'.format(error)) # presenta el texto formateado y su valor -salida de error-
else  :  # si no se produce ninguna excepcion
	print ('si no se produce ninguna excepcion -error- , else presenta este mensaje\n') # presenta el texto
finally : # ejecuta el codigo de su bloque aun que no se produzca una excepcion
	print ('este es el mensaje que envia finally se produzca o NO , una excepcion\n') # presenta el texto 

print ('control de excepciones (SIN tipo de excepcion) -try / except / else / finally- ;  valorError = "ERROR"  \n')

try : # control de excepciones
	print ('int (valorError)\n') # presenta la cadena
	int (valorError) # lanza excepcion ValueError -el valor NO es un numero en formato cadena-
except  : # tipo de excepcion general
	print ('este es el mensaje lanzado por except al producirse una excepcion de tipo general , tipo NO indicado \n') # presenta el texto 
else  :  # si no se produce ninguna excepcion
	print ('si no se produce ninguna excepcion -error- , else presenta este mensaje\n') # presenta el texto
finally : # ejecuta el codigo de su bloque aun que no se produzca una excepcion
	print ('este es el mensaje que envia finally se produzca o NO , una excepcion\n') # presenta el texto 

print ('control de excepciones (SIN tipo de excepcion) -try / finally- ;  valorSINerror = 10  \n')

try : # control de excepciones
	print ('int (valorSINerror)\n') # presenta la cadena
	int (valorSINerror) # lanza excepcion ValueError -el valor NO es un numero en formato cadena-
finally : # ejecuta el codigo de su bloque aun que no se produzca una excepcion
	print ('este es el mensaje que envia finally se produzca o NO , una excepcion\n') # presenta el texto 

print ('si se produce una excepcion ; primero captura la excepcion  , ejecuta finally y luego presenta la excepcion\n') 

print ('generar una excepcion con mensaje propio -raise tipo de excepcion ("texto")- ;  raise ValueError ("este es el texto que presenta la excepcion ValueError lanzada por raise") \n')

try : # control de excepciones
	raise  ValueError ("este es el texto que presenta la excepcion ValueError lanzada por raise\n") # lanza la excepcion indicada con el mensaje del texto
except ValueError as Salida : # tipo de error , pasa la salida a Salida
	print (Salida) # presenta el texto indicado en raise

print ('generar una excepcion general , SIN tipo de excepcion -raise- ;  raise \n')

try : # control de excepciones
	raise   # lanza una excepcion general
except : # tipo de excepcion general 
	print ("este es el texto que presenta la excepcion general lanzada por raise\n") # presenta el texto 

print ('crear nuestro tipo de excepcion con una clase que hereda de BaseException -class nombreExcepcion (BaseException)- ;  class ERROR (BaseException) : \n')

class ERROR ( BaseException) : # definicion de una clase , hereda de la clase padre BaseException
	Error = """++++++++		++++++++		++++++++		++++++++		++++++++
++                      ++    ++                ++    ++                ++    ++                ++    ++
++                      ++    ++                ++    ++                ++    ++                ++    ++
++++++++                ++++++++                ++++++++                ++    ++                ++++++++
++                      ++++                    ++++                    ++    ++                ++++
++                      ++  ++                  ++  ++                  ++    ++                ++  ++
++                      ++   ++                 ++   ++                 ++    ++                ++   ++
++++++++                ++    ++                ++    ++                ++++++++                ++    ++\n""" # asigna la cadena multilinea al atributo

error = ERROR.Error # instancia la clase y su atributo perteneciente a BaseException -clase padre de las excepciones-

try : # control de excepciones
	raise ERROR # lanza el error propio creado -pertenece a BaseException-
except BaseException : # tipo de error
	print (error) # presenta el mensaje del atributo que enlaza la clase creada , perteneciente a BaseException

print ('crear una funcion   sin argumento  -def nombreFuncion ()- ; def funcionSINargumento () \n')

def funcionSINargumento () : # definicion de la funcion
	print ('esta es la funcion llamada ; funcionSINargumento \n') # codigo que ejecuta la funcion al llamarla
	
funcionSINargumento () # llama a la funcion y ejecuta el codigo

print ('crear una funcion  con argumento  -def nombreFuncion (argumento)- ; def funcionCONargumento (argumento) \n')

def funcionCONargumento (argumento) :# definicion de la funcion
	print ('esta es la funcion llamada ; funcionCONargumento \n') # codigo que ejecuta la funcion al llamarla
	print ('este es el argumento puesto en la funcion →→→ {} ←←←\n'.format(argumento)) # codigo que ejecuta la funcion al llamarla

print ("funcionCONargumento ('cadena 0123456789')\n")

funcionCONargumento ('cadena 0123456789') # llama a la funcion y ejecuta el codigo

print ('devolver un valor y salir de la funcion , devolver None  -return- ; return  O  return None \n')

def funcion_return_None () : # definicion de la funcion
	return # devuelve el valor indicado -None- y sale de la funcion
	print ('esta es la funcion llamada ; funcion_return_None \n') # codigo que NO ejecuta la funcion al llamarla

print (funcion_return_None (),'\n') # llama a la funcion y ejecuta el codigo , presenta el valor devuelto por return ; None

print ('devolver un valor y salir de la funcion   -return valor- ; return argumento \n')

def funcion_return_valor (argumento) : # definicion de la funcion
	return argumento # devuelve el valor indicado -argumento- y sale de la funcion
	print ('esta es la funcion llamada ; funcion_return_valor \n') # codigo que NO ejecuta la funcion al llamarla

print (funcion_return_valor ('este es el argumento devuelto'),'\n') # llama a la funcion y ejecuta el codigo , presenta el valor devuelto por return 

print ('funcion con argumento por defecto -def nombreFuncion (argumento=valorPORdefecto)- ; def funcionCONargumentoPORdefecto (argumento="este es el argumento por defecto") \n')

def funcionCONargumentoPORdefecto (argumento="este es el argumento por defecto") : # definicion de la funcion
	return argumento # devuelve el valor indicado -argumento- y sale de la funcion

print ('funcionCONargumentoPORdefecto ("argumento puesto") \n')

print (funcionCONargumentoPORdefecto ("argumento puesto"),'\n') # llama a la funcion y ejecuta el codigo , presenta el argumento puesto

print ('funcionCONargumentoPORdefecto () \n')

print (funcionCONargumentoPORdefecto (),'\n') # llama a la funcion y ejecuta el codigo , presenta el argumento por defecto

print ('cambiar el orden de los argumentos de la funcion ; def funcionCONargumentos (texto,anchoTexto=7,indicador="+...") \n')

def funcionCONargumentos (texto,anchoTexto=7,indicador="+...") :  # definicion de la funcion
	if len (texto) > anchoTexto : # condicion , si el texto tiene mas caracteres que el valor indicado en anchoTexto - 7 por defecto-
		TEXTO = texto [ : len (texto) - anchoTexto] + indicador # devuelve el texto recortado hasta la posicion indicada mas la cadena por defecto de indicador
	else : # si no es mayor que anchoTexto
		TEXTO = texto # asigna la cadena sin cambios 
	return TEXTO # devuelve la nueva cadena y sale de la funcion

print ('funcion con los argumentos en su orden ; funcionCONargumentos ("ESTE ES EL ARGUMENTO PUESTO") \n')

print (funcionCONargumentos ("ESTE ES EL ARGUMENTO PUESTO"),'\n') # llama a la funcion y ejecuta el codigo ,  con el argumento en su orden y sus valores por defecto

print ('funcion con los argumentos cambiados en su orden ; funcionCONargumentos (anchoTexto=7,texto="ESTE ES EL ARGUMENTO PUESTO",indicador="+...") \n')

print (funcionCONargumentos (anchoTexto=7,texto="ESTE ES EL ARGUMENTO PUESTO",indicador="+..."),'\n') # llama a la funcion y ejecuta el codigo ,  con el argumento desordenado  y sus valores por defecto

print ('funcion SIN los argumentos por defecto ,  cambiados en su orden ; funcionCONargumentos (indicador="+&&&&",anchoTexto=10,texto="ESTE ES EL ARGUMENTO PUESTO") \n')

print (funcionCONargumentos (indicador="+&&&&",anchoTexto=10,texto="ESTE ES EL ARGUMENTO PUESTO"),'\n') # llama a la funcion y ejecuta el codigo ,  con el argumento desordenado  y sus valores cambiados

print ('documentar una funcion    -docstring-  ; informacion sobre la funcion , que se pone antes del bloque de codigo \n')

def funcionCONdocumentacion () :  # definicion de la funcion
	'''esta es la cadena de documentacion -docstring-  que informa sobre la funcion y sus caracteristicas'''  # docstring , documentacion de la funcion
	pass # funcion de relleno , no hace nada

print ('devolver la documentacion de una funcion  -nombreFuncion.__doc__- ;  funcionCONdocumentacion.__doc__ \n')

print (funcionCONdocumentacion.__doc__ ,'\n') # presenta la documentacion -docstring- de la funcion

print ('funcion con argumento en formato lista  -def nombreFuncion (*argumentoLista)- ;  def funcionCONargumentoLISTA (*argumentoLista) \n')

def funcionCONargumentoLISTA (*argumentoLista) :  # definicion de la funcion
	'''funcion que procesa la lista del argumento'''  # docstring , documentacion de la funcion
	print ('tipo de argumento ',type (argumentoLista),'\n') # presenta la cadena y su valor , tipo del argumento
	print ('numero de elementos del argumento ',len (argumentoLista),'\n') # presenta la cadena y su valor , numero de elementos
	print ('contenido del argumento ',argumentoLista,'\n') # presenta la cadena y su valor , lista de argumentos
	for numero,argumento in enumerate (argumentoLista) : # iterador , bucle for in , pasa los elementos de la lista a argumento y los numeros a numero , enumerate numera los elementos de la lista
		print ('argumento Nº  {0}  :   {1}   TIPO {2} \n'.format(numero,argumento,type(argumento).__name__)) # presenta la cadena formateada y sus  valores -numero , argumento lista y tipo de argumento-
	else : # cuando finalice el iterador
		print (' FIN DEL CONTENIDO DEL ARGUMENTO LISTA \n') # presenta la cadena
		
print ('documentacion de la funcion funcionCONargumentoLISTA ; funcionCONargumentoLISTA.__doc__  ',funcionCONargumentoLISTA.__doc__,'\n') # presenta la documentacion -docstring- de la funcion

print ('funcionCONargumentoLISTA ("primero","UNO","123","lista",10,["33",.6,"final"],55,"ultimo") \n')

funcionCONargumentoLISTA ("primero","UNO","123","lista",10,["33",.6,"final"],55,"ultimo") # llama y ejecuta la funcion con el argumento indicado como lista

print ('funcion con argumento en formato diccionario  -def nombreFuncion (**argumentoDiccionario)- ;  def funcionCONargumentoDICCIONARIO (**argumentoDiccionario) \n')

def funcionCONargumentoDICCIONARIO (**argumentoDiccionario) :  # definicion de la funcion
	'''funcion que procesa el diccionario del argumento'''  # docstring , documentacion de la funcion
	print ('tipo de argumento ',type (argumentoDiccionario),'\n') # presenta la cadena y su valor , tipo del argumento
	print ('numero de elementos del argumento ',len (argumentoDiccionario),'\n') # presenta la cadena y su valor , numero de elementos
	print ('contenido del argumento ',argumentoDiccionario,'\n') # presenta la cadena y su valor , diccionario de argumentos
	print ('nombre de los argumentos ',argumentoDiccionario.keys(),'\n') # presenta la cadena y su valor , claves del diccionario
	print ('valores de los argumentos ',argumentoDiccionario.values(),'\n') # presenta la cadena y su valor , valores del diccionario
	for numero,tupla in enumerate(argumentoDiccionario.items()) : # iterador , bucle for in , pasa los argumentos a argumento y sus valores a valor , items devuelve una lista de tuplas (clave,valor) del diccionario , enumerate numera las tuplas
		print ('argumento Nº  {0}  :     nombre argumento :  {1[0]:<10}   valor :  {1[1]!s:<10} \n'.format(numero,tupla)) # presenta la cadena formateada y sus  valores -numero y tupla (argumento,valor)-
	else : # cuando finalice el iterador
		print (' FIN DEL CONTENIDO DEL ARGUMENTO DICCIONARIO \n') # presenta la cadena

print ('documentacion de la funcion funcionCONargumentoDICCIONARIO ; funcionCONargumentoDICCIONARIO.__doc__  ',funcionCONargumentoDICCIONARIO.__doc__,'\n') # presenta la documentacion -docstring- de la funcion

print ('funcionCONargumentoDICCIONARIO (primero=1,cadena="UNO",numero="123",cadena1="lista",entero=10,lista=["33",.6,"final"],penultimo=55,final="ultimo") \n')

funcionCONargumentoDICCIONARIO (primero=1,cadena="UNO",numero="123",cadena1="lista",entero=10,lista=["33",.6,"final"],penultimo=55,final="ultimo") # llama y ejecuta la funcion con el argumento indicado como diccionario

INGLES = {0 : 'ZERO',1 : 'ONE',2 : 'TWO',3 : 'THREE',4 : 'FOUR',5 : 'FIVE',6 : 'SIX',7 : 'SEVEN',8 : 'EIGHT',9 : 'NINE'} # diccionario -global-

FRANCES = {0 : 'ZERO',1 : 'UN',2 : 'DEUX',3 : 'TROIS',4 : 'QUATRE',5 : 'CINQ',6 : 'SIX',7 : 'SEPT',8 : 'HUIT',9 : 'NEUF'} # diccionario -global-

ESPAÑOL = {0 : 'CERO',1 : 'UNO',2 : 'DOS',3 : 'TRES',4 : 'CUATRO',5 : 'CINCO',6 : 'SEIS',7 : 'SIETE',8 : 'OCHO',9 : 'NUEVE'} # diccionario -global-

LENGUAJE = 'español'  # variable -global-

def conversionDigitos (numero) :   # definicion de la funcion
	if LENGUAJE == 'ingles'  : # condicion , si coincide uno de los valores de LENGUAJE  -variable global-
		diccionarioIdioma = INGLES # asigna diccionario global
	elif LENGUAJE == 'español'  : # condicion , si coincide uno de los valores de LENGUAJE  -variable global-
		diccionarioIdioma = ESPAÑOL  # asigna diccionario global
	elif  LENGUAJE == 'frances'  : # condicion , si coincide uno de los valores de LENGUAJE  -variable global-
		diccionarioIdioma = FRANCES  # asigna diccionario global
	for digito in numero : # iterador , bucle for in , pasa los caracteres de la cadena  a digito 
		print (diccionarioIdioma [int(digito)],end=' ') # presenta los valores de las claves en la misma linea separados por un espacio
	else :  # cuando finalice el iterador
		print ('\n\nFIN DE LA CONVERSION\n') # salto de linea y texto

print ("LENGUAJE = 'español'\n")

print ('conversionDigitos ("321568")\n') 

conversionDigitos ("321568") # llama y ejecuta la funcion con el argumento indicado -numero en formato cadena-

print ("LENGUAJE = 'ingles'\n")

LENGUAJE = 'ingles'   # variable -global-

print ('conversionDigitos ("321568")\n') 

conversionDigitos ("321568") # llama y ejecuta la funcion con el argumento indicado -numero en formato cadena-

print ("LENGUAJE = 'frances'\n")

LENGUAJE = 'frances'   # variable -global-

print ('conversionDigitos ("321568")\n') 

conversionDigitos ("321568") # llama y ejecuta la funcion con el argumento indicado -numero en formato cadena-

print ('funcion ANONIMA  , lambda  -lambda parametro : expresion-  ; funcionANONIMA = lambda numero :  \'{0} ** 2 =  {1}\'.format (numero,numero ** 2) \n')

funcionANONIMA = lambda numero : '{0} ** 2 =  {1}'.format (numero,numero ** 2) # asigna la funcion ANONIMA -lambda-

print ('[funcionANONIMA (numero) for numero in range (10)]  \n')

print ([funcionANONIMA (numero) for numero in range (10)],'\n') # presenta el resultado de la funcion lambda de una lista comprimida 

print ('reglas de excepcion para funciones -assert expresion,"mensaje de excepcion"- ;  assert type (numero) == str,"EL ARGUMENTO TIENE QUE SER UN NUMERO EN FORMATO CADENA" \n')

print ('conversionDigitos1 (numero) ; version de conversionDigitos con regla assert \n')

def conversionDigitos1 (numero) :   # definicion de la funcion
	'''convierte una cifra en en formato cadena a sus numeros en caracteres , contiene una regla de excepcion ; assert''' # docstring , informacion de la funcion
	assert type (numero) == str,"EL ARGUMENTO TIENE QUE SER UN NUMERO EN FORMATO CADENA"  # regla de excepcion , si no se cumple la expresion lanza el mensaje de excepcion -el argumento tiene que ser en formato cadena-
	if LENGUAJE == 'ingles'  : # condicion , si coincide uno de los valores de LENGUAJE  -variable global-
		diccionarioIdioma = INGLES # asigna diccionario global
	elif LENGUAJE == 'español'  : # condicion , si coincide uno de los valores de LENGUAJE  -variable global-
		diccionarioIdioma = ESPAÑOL  # asigna diccionario global
	elif  LENGUAJE == 'frances'  : # condicion , si coincide uno de los valores de LENGUAJE  -variable global-
		diccionarioIdioma = FRANCES  # asigna diccionario global
	for digito in numero : # iterador , bucle for in , pasa los caracteres de la cadena  a digito 
		print (diccionarioIdioma [int(digito)],end=' ') # presenta los valores de las claves en la misma linea separados por un espacio
	else :  # cuando finalice el iterador
		print ('\n\nFIN DE LA CONVERSION\n') # salto de linea y texto

print ('documentacion de la funcion conversionDigitos1 ; conversionDigitos1.__doc__ ',conversionDigitos1.__doc__,'\n') # presenta la documentacion de la funcion

print ('conversionDigitos1 ("321568")\n') 

conversionDigitos1 ("321568") # llama y ejecuta la funcion con el argumento indicado -numero en formato cadena- , no lanza la excepcion , cumple la regla assert

print ('conversionDigitos1 (321568)\n') 

try : # control de excepciones
	conversionDigitos1 (321568) # llama y ejecuta la funcion con el argumento indicado -numero en formato cadena- , lanza la excepcion , NO cumple la regla assert
except AssertionError as errorAssert : # tipo de excepcion , pasa la salida a errorAssert
	print ('**** {0} ****\n'.format(errorAssert)) # presenta la cadena formateada con la salida de error

# importar modulos

import datetime  # modulo para procesar fechas y horas en formatos personalizados

import xml.sax.saxutils # procesa cadenas y las convierte al formato HTML con caracteres especiales

# plantillas para usar en fromato HTML

plantillaCOPYRIGHT = 'copyright  (c)   {0}  {1} . all rights reserved.' # plantilla html

plantillaSTYLESHEET = ('<link rel="stylesheet"  type="text/css" '  'media="all"  href="{0}"  />\n') # plantilla html

plantillaHTML = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML  1.0 Strict//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html  xmlns="http://www.w3.org/1999/xhtml"  lang="en"  xml : lang="en">


<head>
<title>{titulo}</title>
<!-- {copyright} -->
<meta name="description"  content="{descripcion}" />
<meta name="keywords"  content="{keywords}"  />
<meta name="content-type"  content="text/html;  charset=utf-8"  />
{stylesheet}
</head>


<body>

</body>
</html>
"""  # cadena multilinea  ,  plantilla html

# crear excepcion personalizada

class cancelacionError (Exception) : pass # definicion de la clase , hereda de Exception , pass funcion de relleno -no hace nada-

def informacionPublica (informacion) : # definicion de la funcion
	nombre = cogerCadena ('escriba su nombre (PARA COPYRIGHT) ','nombre',informacion ['nombre']) # devuelve la cadena escrita en la entrada de teclado para el parametro indicado o su valor por defecto -nombre del autor-
	if not nombre : # condicion , si es una cadena vacia o None
		raise cancelacionError () # lanza excepcion propia indicada con raise
	año = cogerCadena ('escriba año COPYRIGHT','año',informacion ['año'],2000,datetime.date.today().year + 1) # devuelve la cadena escrita en la entrada de teclado para el parametro indicado o su valor por defecto -año-   ,True 
	if año == 0 : # condicion , si el valor es cero
		raise cancelacionError () # lanza excepcion propia indicada con raise
	nombreFichero = cogerCadena ('esciba nombre del fichero','nombreFichero',informacion['nombreFichero']) # devuelve la cadena escrita en la entrada de teclado para el parametro indicado o su valor por defecto -nombre del fichero-
	if not nombreFichero : # condicion , si es una cadena vacia o None
		raise cancelacionError () # lanza excepcion propia indicada con raise
	if not nombreFichero.endswith (('.htm','.html')) : # condicion , si la cadena escrita no termina en una de las dos cadenas 
		nombreFichero += '.html'  # añade la cadena al final del nombre del fichero escrito
	titulo = cogerCadena ('escriba el titulo de la plantilla html','titulo',informacion ['titulo']) # devuelve la cadena escrita en la entrada de teclado para el parametro indicado o su valor por defecto -titulo plantilla html-
	if not titulo :# condicion , si es una cadena vacia o None
		raise cancelacionError () # lanza excepcion propia indicada con raise
	descripcion = cogerCadena ('escriba una descripcion de la pagina html','descripcion',informacion ['descripcion']) # devuelve la cadena escrita en la entrada de teclado para el parametro indicado o su valor por defecto -descripcion pagina html-
	if not descripcion :# condicion , si es una cadena vacia o None
		raise cancelacionError () # lanza excepcion propia indicada con raise
	informacion.update (nombre=nombre,año=año,nombreFichero=nombreFichero,titulo=titulo,descripcion=descripcion) # actualiza el diccionario con los valores indicados 
	
def crearEsqueletoHTML (año,nombre,titulo,descripcion,keywords,stylesheet,nombreFichero) : # definicion de la funcion
	copyright = plantillaCOPYRIGHT.format (año,xml.sax.saxutils.escape(nombre)) # devuelve la plantilla formateada con los valores indicados -año y nombreen formato escape html-
	titulo = xml.sax.saxutils.escape(titulo) # devuelve el valor en formato html
	descripcion = xml.sax.saxutils.escape(descripcion) # devuelve el valor en formato html
	if  keywords : # condicion , si keywords no es una cadena vacia o None 
		keywords = ','.join ([xml.sax.saxutils.escape(clave) for clave in keywords])  #   devuelve una cadena con las claves separadas por comas 
	else : # si es una cadena vacia o None
		keywords = ' ' # asigna una cadena vacia
	if stylesheet : # condicion , si stylesheet no es una cadena vacia o None
		stylesheet = plantillaSTYLESHEET.format (stylesheet) # devuelve una plantilla formateada con los valores de stylesheet
	else : # lo contario una cadena vacia
		 stylesheet = ' '   # asigna una cadena vacia
	html = plantillaHTML.format (titulo=titulo,copyright=copyright,descripcion=descripcion,keywords=keywords,stylesheet=stylesheet) # devuelve la plantilla formateada con los valores indicados 
	ficheroHTML = None # uso para open ()
	try : # control de excepciones
		ficheroHTML = open ('./Escritorio/' + nombreFichero,'w') # crea el fichero con el nombre indicado en modo escritura
		ficheroHTML.write (html) # escribe la plantilla html en el fichero
	except EnvironmentError as salidaError : # tipo de excepcion , pasa la salida a salidaError
		print ('** ERROR ** -- {} --\n'.format (salidaError)) # presenta la salida formateada
	else : # si no se produce ninguna excepcion
		print ('salvando plantilla html : {} \n'.format(nombreFichero)) # presenta la cadena formateada y su valor  -nombre del fichero-
	finally : # se produzca una excepcion o no , ejecuta la sentencia
		if ficheroHTML is not None : # condicion , si no contiene None -su primer valor-
			ficheroHTML.close () # cierra el fichero que enlaza el objeto
			
def cogerCadena (mensaje,nombre='cadena',default=None,caracteresMinimos=0,caracteresMaximos=80) :  # definicion de la funcion
	mensaje += ' :   '  if default is None else '  [{0}] :   '.format (default) # condicion , añade a la cadena de mensaje la primera cadena si el valor es None o el valor formateado si NO es None
	while True : # bucle while continuo
		try : # control de excepciones 
			entradaTeclado = input (mensaje) # espera entrada de teclado -presenta la cadena de mensaje-
			if not entradaTeclado : # condicion , si es una cadena vacia
				return default # devuelve el valor indicado y sale de la funcion
			if caracteresMinimos == 0 : # condicion , si el valor es el indicado
				return ' ' # devuelve una cadena vacia y sale de la funcion
			else : # si es distinto a cero
				raise ValueError ('{0} no puede estar vacio \n'.format (nombre)) # lanza la excepcion indicada y presenta el mensaje de la cadena formateada
			if not (caracteresMinimos <= len (entradaTeclado) <= caracteresMaximos) : # condicion , si la entrada no esta entre los valores indicados -minimo y maximo-
				raise ValueError ('{0} tiene que tener entre {1} y {2} caracteres \n'.format (nombre,caracteresMinimos,caracteresMaximos)) # lanza la excepcion indicada y presenta el mensaje de la cadena formateada
			return entradaTeclado # devuelve la entrada de teclado y sale de la funcion
		except ValueError as ERROR : # tipo de excepcion , pasa la salida a ERROR
			print ('+++ ERROR +++ -{0} - \n'.format (ERROR)) # presenta la cadena formateada con la salida de ERROR
			
def principal () : # definicion de la funcion
	informacion = dict (nombre=None,año=datetime.date.today().year,nombreFichero=None,titulo=None,descripcion=None,keywords=None,stylesheet=None) # devuelve un diccionario con los parametros y sus valores como clave : valor
	while True : # bucle while continuo
		try : # control de excepciones
			print ("\nCREAR ESQUELETO HTML\n") # presenta la cadena
			informacionPublica (informacion) # llama a la funcion con el argumento indicado -diccionario-
			crearEsqueletoHTML (**informacion) # llama a la funcion con el argumento indicado -diccionario- 
		except cancelacionError : # tipo de excepcion
			print ("CANCELADO") # presenta el texto
		if (cogerCadena ("\nCREAR OTRO (s/n) ?",default="s").lower () not in {"s","si"}) : # condicion , si la cadena devuelta en minusculas por la funcion NO esta en el diccionario
			break # interrumpe el bucle while continuo

principal () # llama y ejecuta la funcion sin argumentos






















