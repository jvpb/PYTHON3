#!/usr/bin/env python3
'''servidor basico'''

# importar modulos

import socket # importa el modulo indicado

servidor = socket.socket (socket.AF_INET,socket.SOCK_STREAM) # crea el objeto socket con los protocolos indicados -protocolo IPv4 y protocolo TCP-

servidor.bind (('',50007)) # conecta con el socket

servidor.listen (1) # numero de conexiones en cola -una ; 1-

conexion,direccion = servidor.accept () # acepta la conexion -devuelve una tupla de dos elementos (objetoSocketnuevo,(IP,PUERTO))-

print ('CONECTADO A : ',direccion [0],' - PUERTO : ',direccion [1],'\n') # presenta la cadena con los valores indicados ; IP , PUERTO

while True : # bucle while mientras se cumpla la condicion
	datos = conexion.recv (1024) # recibe datos desde el socket -tamaño bloque de bytes indicado-
	if not datos : # condicion , si no hay datos -False-
		break # interrumpe el bucle while
	conexion.sendall (datos) # envia los datos recibidos al socket ; datos 

conexion.close () # cierra el socket -enviando los datos-


