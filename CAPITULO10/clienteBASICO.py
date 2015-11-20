#!/usr/bin/env python3
'''cliente basico'''

# importar modulos

import socket # importa el modulo indicado

class crearSOCKET (object) : # definicion de la clase 
	def __enter__ (self) : # definicion metodo especial 
		self.conectar = socket.socket (socket.AF_INET,socket.SOCK_STREAM) # crea el objeto socket con los protocolos indicados -protocolo IPv4 y protocolo TCP-
		self.conectar.connect (('localhost',50007)) # conecta en la ip de localhost en el puerto 9653
		return self.conectar # devuelve el objeto socket -la conexion al servidor-
		
	def __exit__ (self,*ignorar) : # definicion metodo especial
		self.conectar.close () # cierra el socket -enviando los datos-

try : # control de excepciones
	with crearSOCKET () as conexion : # abre y cierra el puerto del servidor en la IP por defecto indicado en la clase ; crearSOCKET , enlazado como conexion
		entrada = bytes (input ('ENVIAR >>> '),'utf8') # entrada de teclado
		print ('\n') # salto de linea
		conexion.sendall (entrada) # envia los datos al socket -servidor-
		recibirdatos = conexion.recv (1024) # recibe datos desde el socket -tamaño bloque de bytes indicado-
	print ('RECIBIDO >>> ',recibirdatos.decode ('utf8'),'n') # presenta los datos recibidos del servidor -convertido de binario a utf-8-
except socket.error as error : # tipo de excepcion , pasa la salida a error
	print ('{0} : esta el SERVIDOR funcionando ?\n'.format (error)) # presenta la cadena formateada con el error de salida
	sys.exit (1) # sale del script que se esta ejecutando con codigo de error ; 1
