#!/usr/bin/env python3
'''crear una ventana en formato texto 

- redimensionar





- añadir_linea_horizontal 

- limpiarPantalla

 

\n''' # docstring , documentacion del modulo

# importar modulos

import sys

import subprocess

class ErrorRango (Exception) : # definicion de la clase , hereda de Exception -excepcion propia-
	pass # funcion de relleno -no hace nada-

class ErrorRangoFila (ErrorRango) : # definicion de la clase , hereda de ErrorRango -excepcion propia-
	pass # funcion de relleno -no hace nada-

class ErrorRangoColumna (ErrorRango) : # definicion de la clase , hereda de ErrorRango -excepcion propia-
	pass # funcion de relleno -no hace nada-

_plantillaCadena_assert = ("debe ser un solo caracter '{0}' " "es demasiado largo") # variable privada -asigna cadena formateada-

_filasMaximas = 25  # variable privada -numero de filas-

_columnasMaximas = 80 # variable privada -numero de columnas-

_cuadricula = [] # variable privada , asigna lista vacia

_caracterDEfondo = " " # variable privada , asigna cadena vacia

def limpiarPantalla () : # definicion de la funcion
	subprocess.call ([clear]) # limpiar la pantalla , la funcion call de subprocess llama al comando del sistema ; clear , que limpia la pantalla
	
limpiarPantalla.__doc__ = 'usa el comando clear del sistema GNU/linux para limpiar la pantalla \n' # mensaje docstring para la funcion limpiarPantalla cuando se llama a __doc__

def redimensionar (filasMaximas,columnasMaximas,caracter=None) : # definicion de la funcion
	"""cambia el tamaño de la cuadricula , saca el contenido y cambia el fondo si caracter no es None""" # docstring , documentacion de la funcion
	assert filasMaximas > 0 and columnasMaximas > 0,'demasiado corto\n' # regla de excepcion , si no se cumple lanza excepcion assert y presenta la cadena indicada
	global _filasMaximas,_columnasMaximas,_cuadricula,_caracterDEfondo # usa las variables globales en la funcion como locales
	if caracter is not None : # condicion , si el valor NO es None
		assert len(caracter) == 1,_plantillaCadena_assert.format(caracter) # regla de excepcion , si no se cumple lanza excepcion assert y presenta la cadena indicada -plantilla cadena-
		_caracterDEfondo = caracter # asigna el valor de caracter
		_filasMaximas = filasMaximas # asigna el valor de filasMaximas
		_columnasMaximas = columnasMaximas # asigna el valor de columnasMaximas
		_cuadricula = [[_caracterDEfondo for columna in range (_columnasMaximas)] for fila in range (_filasMaximas)] # genera una lista de listas -las listas son los caracteres de fondo por columna de la cuadricula , ancho de la cuadricula- y el numero de listas , las filas de la cuadricula -altura de la cuadricula-

def añadir_linea_horizontal (fila,columna0,columna1,caracter='-') : # definicion de la funcion
	'''añade linea horizontal a la cuadricula usando el caracter por defecto o el indicado''' # docstring , documentacion de la funcion
	assert len(caracter) == 1,_plantillaCadena_assert.format(caracter) # regla de excepcion , si no se cumple lanza excepcion assert y presenta la cadena indicada -plantilla cadena-
	try : # control de excepciones
		for columna in range (columna0,columna1) : # iterador , bucle for in , pasa la lista de numeros a la variable columna , range devuelve una lista de numeros
			_cuadricula [fila] [columna] = caracter # asigna el caracter a la fila -lista- de la columna -posicion de la lista _cuadricula-
	except IndexError : # tipo de excepcion
		if not 0 <= fila <= _filasMaximas : # condicion , si es mayor que cero , se cumple la condicion -True menor o igual a cero , not niega True , True >> False-
			raise ErrorRangoFila () # lanza excepcion indicada -excepcion propia-
		raise ErrorRangoColumna () # lanza excepcion indicada -excepcion propia-

redimensionar (_filasMaximas,_columnasMaximas) # inicializa el modulo llamando a la funcion con los parametros por defecto

if __name__ == '__main__' : # condicion , si se llama al modulo como script -la variable __name__ de python tiene como valor __main__ en vez del nombre del modulo sin extension-
	import doctest # importa el modulo indicado
	doctest.testmod () # ejecuta el test del modulo
	redimensionar (_filasMaximas,_columnasMaximas) # llama a la funcion con los argumentos indicados


















































