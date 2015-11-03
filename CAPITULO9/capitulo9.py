#!/usr/bin/env python3
'''procesos y distribucion'''

# importar modulo

import sys # importa el modulo indicado

print ('VERSION en uso de PYTHON \n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('crear funcion multiprocesos ; def MULTIPROCESOS (*listaComandos) : \n')

def MULTIPROCESOS (*listaComandos) : # definicion de la funcion
	import subprocess # importa el modulo indicado
	listaDEsubprocesos = [] # asigna lista vacia
	for comandos in listaComandos : # iterador , bucle for in , pasa los comandos de la tupla a comandos
		listaDEsubprocesos.append (subprocess.Popen (comandos.split ())) # añade el subproceso a la lista -split separa los argumentos y devuelve una lista con ellos-
	for numeroSubproceso,subproceso in enumerate (listaDEsubprocesos,start=1) : # iterador , bucle for in , pasa los subprocesos de la lista a subproceso y el numero a numeroSubproceso -enumerate ; numera los elementos de la lista , comienza en 1-
		subproceso # ejecuta el subproceso
		subproceso.wait () # espera a que se ejecute el proceso
	else : # cuando finalice el iterador
		print ('\n*** FIN DE LA EJECUCION DE MULTIPROCESOS : procesos ejecutados ; {0} \n'.format (numeroSubproceso)) # presenta la cadena formateada -numero de procesos- 

print ("llamar a la funcion MULTIPROCESOS ; MULTIPROCESOS ('cat Escritorio/capitulo9.txt','ls','ls -l','ls -l Escritorio/capitulo9.txt','ls -l Documentos')\n")

MULTIPROCESOS ('cat Escritorio/capitulo9.txt','ls','ls -l','ls -l Escritorio/capitulo9.txt','ls -l Documentos') # llama a la funcion con los argumentos indicados -comandos shell bash- , ejecutando en procesos independientes

print ('crear funcion procesos ; def PROCESOS (*listaComandos) : \n')

def PROCESOS (*listaComandos) : # definicion de la funcion
	import subprocess # importa el modulo indicado
	listaDEsubprocesos = [] # asigna lista vacia
	for comandos in listaComandos : # iterador , bucle for in , pasa los comandos de la tupla a comandos
		listaDEsubprocesos.append (subprocess.call (comandos.split ())) # añade el subproceso a la lista -split separa los argumentos y devuelve una lista con ellos-
	for numeroSubproceso,subproceso in enumerate (listaDEsubprocesos,start=1) : # iterador , bucle for in , pasa los subprocesos de la lista a subproceso y el numero a numeroSubproceso -enumerate ; numera los elementos de la lista , comienza en 1-
		subproceso # ejecuta el subproceso
	else : # cuando finalice el iterador
		print ('\n*** FIN DE LA EJECUCION DE MULTIPROCESOS : procesos ejecutados ; {0} \n'.format (numeroSubproceso)) # presenta la cadena formateada -numero de procesos- 

print ("llamar a la funcion PROCESOS ; PROCESOS ('cat Escritorio/capitulo9.txt','ls','ls -l','ls -l Escritorio/capitulo9.txt','ls -l Documentos')\n")

PROCESOS ('cat Escritorio/capitulo9.txt','ls','ls -l','ls -l Escritorio/capitulo9.txt','ls -l Documentos') # llama a la funcion con los argumentos indicados -comandos shell bash- , ejecutando en procesos independientes

print ('funcion que ejecuta el thread -hilo- por defecto ; run : def run () : \n')

def run () : # definicion de la funcion -ejecutado por Thread-
	PROCESOS ('ls -l','ls -l Documentos') # llama a la funcion con los argumentos indicados -comandos shell bash- , ejecutando en procesos independientes
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL HILO -THREAD- A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('uso de thread -hilos- como procesos -funcion- ; def hilos () : \n')

def hilos () : # definicion de la funcion
	import threading # importa el modulo indicado
	HILO = threading.Thread (run ()) # crea el objeto hilo -thread- con el objeto a ejecutar
	HILO.start () # ejecuta el hilo -la funcion run ; por defecto-
	HILO.join () # bloquea el hilo -thread- asta que finalice -funcion run ()-
	
print ('ejecutar el thread -hilo- ; hilos () \n')

hilos () # ejecuta el thread -hilo , procesos en funcion run ()-

print ('funciones a ejecutar como multihilos ; run , THREAD2 , THREAD3 , THREAD4 y THREAD5 \n')

def THREAD2 () : # definicion de la funcion -ejecutado por Thread-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL HILO - THREAD2 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

def THREAD3 () : # definicion de la funcion -ejecutado por Thread-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL HILO - THREAD3 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

def THREAD4 () : # definicion de la funcion -ejecutado por Thread-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL HILO - THREAD4 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

def THREAD5 () : # definicion de la funcion -ejecutado por Thread-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL HILO - THREAD5 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('uso de multithread -multihilos- como procesos -funcion- ; def multiHilos () : \n')

def multiHilos () : # definicion de la funcion
	import threading # importa el modulo indicado
	colaHilos = [run (),THREAD2 (),THREAD3 (),THREAD4 (),THREAD5 ()] # lista de funciones a ejecutar como hilos
	for numeroHilo,hilo in enumerate (colaHilos,start=1) : # iterador , bucle for in , pasa las funciones al objeto hilo -enumerate numera los elementos de la lista , empieza en 1-
		HILO = threading.Thread (hilo) # crea el objeto hilo -thread- con el objeto a ejecutar
		HILO.start () # ejecuta el hilo -la funcion indicada en el objeto-
		HILO.join () # bloquea el hilo -thread- asta que finalice -la funcion indicada en el objeto-
	else : # cuando finalice el iterador
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
		print ('****** TODOS LOS HILOS - THREAD - HAN SIDO EJECUTADOS : TOTAL {0} ******\n'.format (numeroHilo)) # presenta la cadena formateada y  su valor -numero de hilos ejecutados-
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('ejecutar el multithread -multihilos- ; multiHilos () \n')

multiHilos () # ejecuta el multithread -multihilos , procesos en funciones run , THREAD2 , THREAD3 , THREAD4 y THREAD5-

print ('importar modulo threading de modo global para herencia de la clase procesarHilo (threading.Thread) : \n')

import threading # importa el modulo indicado de forma global

print ('crear clase con herencia de threading.Thread ; class procesarHilo (threading.Thread) : \n')

class procesarHilo (threading.Thread) : # definicion de la clase -hereda threading.Thread-
	def run (self) : # definicion del metodo standard -ejecuta por defecto al ser llamado por start-
		PROCESOS ('ls -l Documentos') # llama a la funcion con los argumentos indicados -comandos shell bash- , ejecutando en procesos independientes
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
		print ('****** EL HILO -THREAD- A SIDO EJECUTADO ******\n') # presenta la cadena 
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('uso de thread -hilos- como procesos -funcion- ; def ejecutarHilo () : \n')

def ejecutarHilo () : # definicion de la funcion 
	HILO = procesarHilo () # instancia y crea el objeto Thread -hereda threading.Thread-
	HILO.start () # inicia el objeto Thread -ejecuta el metodo run () por defecto de la clase que enlaza el objeto
	HILO.join () # bloquea el hilo hasta que finaliza 

print ('ejecutar el thread -hilo- ; ejecutarHilo () \n')

ejecutarHilo () # llama y ejecuta la funcion que ejecuta la clase con herencia 

print ('crear clase con herencia de threading.Thread ; class procesarMultiHilos (threading.Thread) : \n')

class procesarMultiHilos (threading.Thread) : # definicion de la clase -hereda threading.Thread-
	def __init__ (self,proceso) : # definicion del metodo , inicializa la clase con los argumentos indicados
		super ().__init__ () # llama e inicializa los argumentos de la clase padre -threading.Thread-
		self.proceso = proceso # asigna el valor al atributo
	
	def run (self) : # definicion del metodo standard -ejecuta por defecto al ser llamado por start-
		self.proceso # llama y ejecuta el proceso

print ('uso de multithread -multihilos- como procesos -funcion- ; def MultiHilos (*listaProcesos) : \n')

def MultiHilos (*listaProcesos) : # definicion de la funcion
	#colaHilos = [run (),THREAD2 (),THREAD3 (),THREAD4 (),THREAD5 ()] # lista de funciones a ejecutar como hilos
	for numeroHilo,hilo in enumerate (listaProcesos,start=1) : # iterador , bucle for in , pasa las funciones al objeto hilo -enumerate numera los elementos de la lista , empieza en 1-
		HILO = procesarMultiHilos (hilo) # crea el objeto hilo -thread- con el objeto a ejecutar en la clase con herencia en threading.Thread
		HILO.start () # ejecuta el hilo -la funcion indicada en el objeto-
		HILO.join () # bloquea el hilo -thread- asta que finalice -la funcion indicada en el objeto-
	else : # cuando finalice el iterador
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
		print ('****** TODOS LOS HILOS - THREAD - HAN SIDO EJECUTADOS : TOTAL {0} ******\n'.format (numeroHilo)) # presenta la cadena formateada y  su valor -numero de hilos ejecutados-
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('ejecutar el multithread -multihilos- ; MultiHilos (run (),THREAD2 (),THREAD3 (),THREAD4 (),THREAD5 ()) \n')

MultiHilos (run (),THREAD2 (),THREAD3 (),THREAD4 (),THREAD5 ()) # ejecuta el multithread -multihilos , procesos en funciones run , THREAD2 , THREAD3 , THREAD4 y THREAD5-

print ('modulo multiprocessing ; API similar a threading para procesos : import multiprocessing \n')

import multiprocessing # importa el modulo indicado

print ('crear funcion procesos en paralelo  ; def procesosPARALELOS (*PROCESOS) : \n')

def procesosPARALELOS (*PROCESOS) : # definicion de la funcion
	for numeroProceso,proceso in enumerate (PROCESOS,start=1) : # iterador , bucle for in , pasa las funciones al objeto hilo -enumerate numera los elementos de la lista , empieza en 1-
		iniciar = multiprocessing.Process (proceso) # instancia y crea el objeto Process que ejecuta el proceso indicado
		iniciar.start () # inicia el proceso indicado en el objeto
		iniciar.join () # bloquea el proceso hasta que finaliza su ejecucion -ningun otro proceso puede ejecutarlo hasta que finalice-
	else : # cuando finalice el iterador
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
		print ('****** TODOS LOS PROCESOS - PROCESS - HAN SIDO EJECUTADOS : TOTAL {0} ******\n'.format (numeroProceso)) # presenta la cadena formateada y  su valor -numero de procesos ejecutados-
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('funciones a ejecutar como procesos ; PROCESO2 , PROCESO3 , PROCESO4 y PROCESO5 \n')

def PROCESO2 () : # definicion de la funcion -ejecutado por Process-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL PROCESO - PROCESO2 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

def PROCESO3 () : # definicion de la funcion -ejecutado por Process-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL PROCESO - PROCESO3 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

def PROCESO4 () : # definicion de la funcion -ejecutado por Process-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL PROCESO - PROCESO4 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

def PROCESO5 () : # definicion de la funcion -ejecutado por Process-
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
	print ('****** EL PROCESO - PROCESO5 - A SIDO EJECUTADO ******\n') # presenta la cadena 
	print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('ejecutar la funcion ; procesosPARALELOS (PROCESOS ("ls -l"),PROCESO2 (),PROCESO3 (),PROCESO4 (),PROCESO5 ()) \n')

procesosPARALELOS (PROCESOS ("ls -l"),PROCESO2 (),PROCESO3 (),PROCESO4 (),PROCESO5 ()) # ejecuta la funcion con los argumentos indicados -como procesos independientes-

print ('crear clase con herencia de multiprocessing.Process ; class procesarMultiPROCESOS (multiprocessing.Process) : \n')

class procesarMultiPROCESOS (multiprocessing.Process) : # definicion de la clase -hereda multiprocessing.Process-
	def __init__ (self,proceso) : # definicion del metodo , inicializa la clase con los argumentos indicados
		super ().__init__ () # llama e inicializa los argumentos de la clase padre -multiprocessing.Process-
		self.proceso = proceso # asigna el valor al atributo
	
	def run (self) : # definicion del metodo standard -ejecuta por defecto al ser llamado por start-
		self.proceso # llama y ejecuta el proceso

print ('crear funcion multiPROCESOS ; def multiPROCESOS (*procesos) : \n')

def multiPROCESOS (*procesos) : # definicion de la funcion -ejecuta la clase procesarMultiPROCESOS con herencia de multiprocessing.Process-
	for numeroProceso,proceso in enumerate (procesos,start=1) : # iterador , bucle for in , pasa las funciones al objeto hilo -enumerate numera los elementos de la lista , empieza en 1-
		iniciarPROCESOS = procesarMultiPROCESOS (proceso) # instancia y crea el objeto Process - procesarMultiPROCESOS - que ejecuta el proceso indicado
		iniciarPROCESOS.start () # inicia el proceso indicado en el objeto -ejecuta el metodo standard run () de la clase procesarMultiPROCESOS-
		iniciarPROCESOS.join () # bloquea el proceso hasta que finaliza su ejecucion -ningun otro proceso puede ejecutarlo hasta que finalice-
	else : # cuando finalice el iterador
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
		print ('****** TODOS LOS PROCESOS - PROCESS - HAN SIDO EJECUTADOS : TOTAL {0} ******\n'.format (numeroProceso)) # presenta la cadena formateada y  su valor -numero de procesos ejecutados-
		print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('ejecutar la funcion ; multiPROCESOS (PROCESOS ("ls -l","ls -l Documentos"),PROCESO2 (),PROCESO3 (),PROCESO4 (),PROCESO5 ()) \n')

multiPROCESOS (PROCESOS ("ls -l","ls -l Documentos"),PROCESO2 (),PROCESO3 (),PROCESO4 (),PROCESO5 ()) # ejecuta la funcion con los argumentos indicados -como procesos independientes , llamando a procesarMultiPROCESOS-



































































