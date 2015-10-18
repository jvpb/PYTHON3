#!/usr/bin/env python3
'''este modulo contiene funciones que manipulan cadenas

- emparejado >> devuelve True -verdadero- si los simbolos estan emparejados () [] {} <>

- simplificarTexto >> devuelve la cadena  con multiples espacios seguidos en cadenas con un solo de espacio o los caracteres indicados eliminados

- acortadorTexto >> acorta el texto al tamaño indicado

\n''' # docstring , documentacion del modulo

# importar modulo

import string # importa el modulo indicado

def simplificarTexto (texto,espacioENblanco=string.whitespace,borrar="  ") : # definicion de la funcion
	resultado = [ ] # asigna lista vacia 
	palabra = "" # asigna cadena vacia
	for caracter in texto : # iterador , bucle for in , pasa los caracteres de la cadena a la variable ; caracter
		if caracter in borrar : # condicion , si el valor coincide con el de borrar
			continue # vuelve al siguiente caracter de la cadena 
		elif caracter in espacioENblanco :  # condicion , si el valor coincide con un espacio en blanco
			if palabra : # condicion , si no es una cadena vacia 
				resultado.append (palabra) # añade la palabra a la lista
				palabra = "" # asigna cadena vacia
		else : # si no es un espacio en blanco 
			palabra += caracter # añade el caracter al valor actual -cadena-
	if palabra : # condicion , si no es una cadena vacia  -ultima palabra de la cadena-
		resultado.append (palabra) # añade la palabra a la lista
	return " ".join (resultado) # devuelve la lista de palabras en una cadena separadas por un espacio

def emparejado (texto,parentesis='() [] {} <>') :  # definicion de la funcion
	contador  = { } # asigna un diccionario
	izquierdaAderecha = { }  # asigna un diccionario
	for izquierda,derecha in zip (parentesis [ : : 2],parentesis [1 : : 2]) : # iterador , bucle for in , pasa las tuplas de dos elementos  con los valores indicados a izquierda -elemento 0- y derecha -elemento 1- , zip devuelve una lista de tuplas con los elementos indicados -(parentisis izquierdo,parentesis derecho)-
		assert izquierda != derecha,'los parentesis no estan emparejados , son iguales : {0}\n'.format (izquierda)    # regla excepcion , si no se cumple lanza excepcion con el mensaje indicado
		contador [izquierda] = 0 # añade el simbolo izquierdo al diccionario , cuenta el numero de veces que aparece el simbolo izquierdo del par -diccionario-
		izquierdaAderecha [derecha] = izquierda # añade al simbolo derecho el simbolo izquierdo del par -diccionario-
	for caracter in texto :  # iterador , bucle for in , pasa los caracteres de la cadena a la variable ; caracter
		if caracter in contador : # condicion , si el valor de caracter esta en el diccionario contador -simbolo izquierdo del par-
			contador [caracter] += 1 # suma uno al valor de caracter -simbolo izquierdo del par-
		elif caracter in izquierdaAderecha : # condicion , si el valor de caracter esta en el diccionario -simbolo derecho del par-
			izquierda = izquierdaAderecha [caracter] # asigna el simbolo izquierdo del par 
			if contador [izquierda] == 0 : # condicion , si el valor es cero -solo hay un simbolo izquierdo del par-
				return False  # devuelve 
			contador [izquierda] -= 1 # resta uno al valor actual del simbolo izquierdo 
	return not any (contador.values ()) # si any devuelve False , la condicion es verdadero , devuelve True -not niega el valor por defecto (NO ES VERDADERO)-  any devuelve True si cualquier elemento del iterador NO es cero o NO estavacio -si los valores son cero , NO hay ningun simbolo  izquierdo suelto- 

def acortadorTexto (texto,tamaño) :   # definicion de la funcion
	puntos = '...' # cadena final añadir a la subcadena
	cadenaAcortada = texto [ : tamaño - 3]  + puntos  # asigna la subcadena con la cadena añadida , de la cadena desde la posicion inicial al indicado -0 al valor indicado menos 2-
	return cadenaAcortada # devuelve la cadena acortada

if __name__ == '__main__' : # condicion , si se llama al modulo como script -si el valor de la variable name de python es __main__  indica que se ejecuta como un script  , si no su valor seria solo el nombre del modulo sin la extension .py-
	import doctest # importa el modulo indicado
	doctest.testmod ()  # test del modulo -analiza las funciones del modulo y sus cadenas de descripcion (docstring) , intenta ejecutar todas las funciones que encuentre-
	print ("simplificarTexto ('este        es           el texto a    simplicar') ",simplificarTexto ('este        es           el texto a    simplicar'),'\n') # presenta la cadena , llama a la funcion con el argumento indicado y presenta el resultado
	print ("emparejado ('(este)       [es]          { el texto a}    <simplicar>') ",emparejado ('(este)       [es]          { el texto a}    <simplicar>'),'\n') # presenta la cadena , llama a la funcion con el argumento indicado y presenta el resultado 
	print ("acortadorTexto ('este es el texto a ACORTAR',14) ",acortadorTexto ('este es el texto a ACORTAR',14),'\n') # presenta la cadena , llama a la funcion con el argumento indicado y presenta el resultado
	print ('*** FIN DEL TEST DEL MODULO ***\n')







































