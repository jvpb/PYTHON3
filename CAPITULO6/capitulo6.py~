#!/usr/bin/env python3
'''programacion orientada a objetos'''

import sys

print ('VERSION en uso de PYTHON \n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('tupla de 3 elementos ; circulo = (11,60,8) \n')

circulo = (11,60,8) # tupla de 3 elementos

print ('circulo ',circulo,'tipo ',type (circulo).__name__,'\n') # presenta el valor y su tipo

print ('desempaquetar la tupla ; valor1,valor2,valor3 = circulo \n')

valor1,valor2,valor3 = circulo # desempaqueta la tupla en las variables asignadas

print ('valor1 ',valor1,'valor2 ',valor2,'valor3 ',valor3,'\n') # presenta los valores desempaquetados de la tupla

print ('crear una tupla nombrada ; import collections \n')

import collections # importa el modulo indicado

print ('asignar tupla nombrada ; Circulo = collections.namedtuple ("Circulo","x y radio") \n')

Circulo = collections.namedtuple ("Circulo","x y radio") # asigna la tupla nombrada

print ('añadir los valores a la tupla nombrada ; CIRCULO = Circulo (13,84,9) \n')

CIRCULO = Circulo (13,84,9) # añade los valores a la tupla nombrada

print ('CIRCULO ',CIRCULO,'tipo ',type (CIRCULO).__name__,'\n') # presenta el valor y su tipo

print ('modificar una tupla nombrada con namedtuple._replace de collections ; CIRCULO = CIRCULO._replace (radio=12) \n')

CIRCULO = CIRCULO._replace (radio=12) # reemplaza el valor de radio de la tupla nombrada

print ('CIRCULO ',CIRCULO,'tipo ',type (CIRCULO).__name__,'\n') # presenta el valor y su tipo

print ('cadena = "esto es una cadena" \n')

cadena = "esto es una cadena" # cadena -tipo string , str-

print ('cambiar la cadena a mayusculas con el metodo upper ; cadena.upper () ',cadena.upper (),'\n') # presenta la cadena en mayusculas

print ('concatenar la cadena con + ; cadena + cadena.upper () ',cadena + cadena.upper (),'\n') # presenta las cadenas unidas en una

print ('longitud de la cadena con len ; len (cadena) ',len (cadena),'\n') # presenta la longitud de la cadena

print ('uso de los metodos especiales __add__ y __len__ en una clase ; class longitudConcatenacion (object) : \n')

class longitudConcatenacion (object) : # definicion de la clase
	def __init__ (self,cadena) : # metodo , inicializa la clase con los parametros indicados
		self.cadena = cadena # asigna el valor de cadena

	def __add__ (self,otraCadena) : # metodo especial - + - , permite la concatenacion 
		return self.cadena + otraCadena # devuelve la concatenacion de los dos argumentos

	def __len__ (self) : # metodo especial - len () - , permite el uso de len ()
		return len (self.cadena) # devuelve la longitud del argumento

print ('instanciar la clase ; objeto = longitudConcatenacion (cadena.upper()) \n')

objeto = longitudConcatenacion (cadena.upper()) # instancia la clase y su argumento

print ('concatenar ; objeto + cadena ',objeto + cadena,'\n') 

print ('longitud ; len (objeto) ',len (objeto),'\n')

print ('crear un objeto numero complejo ; numeroComplejo = complex (10,5) \n')

numeroComplejo = complex (10,5) # asigna un numero complejo mediante la funcion complex

print ('numeroComplejo ',numeroComplejo,'\n') # presenta el numero complejo devuelto por complex

print ('numero real de numeroComplejo ; numeroComplejo.real ',numeroComplejo.real,'\n') # presenta el numero real del complejo

print ('numero imaginario de numeroComplejo ; numeroComplejo.imag ',numeroComplejo.imag,'\n') # presenta el numero imaginario del complejo

print ('crear una clase propia ; class clasePROPIA (object) : \n')

class clasePROPIA (object) : # definicion de la clase
	def __init__ (self,argumento=None) : # metodo , inicializa la clase con los parametros indicados , argumento con valor por defecto
		self.argumento = argumento # asigna el valor de argumento
		
	atributo = 'este es el atributo de la clase ; clasePROPIA' # atributo de la clase
	
	def metodo1 (self) : # definicion del metodo de la clase
		return self.argumento # devuelve el argumento puesto en el objeto
	
	def metodo2 (self,otroArgumento) : # definicion del metodo de la clase , argumento propio
		return otroArgumento # devuelve el argumento propio del metodo
	
print ('instanciar clase con valores por defecto ; valorPorDefecto = clasePROPIA () \n')

valorPorDefecto = clasePROPIA () # instancia la clase con valores por defecto

print ('llamando al atributo del objeto ; valorPorDefecto.atributo ',valorPorDefecto.atributo,'\n') # presenta el valor del atributo

print ('llamando a un metodo del objeto ; valorPorDefecto.metodo1 () ',valorPorDefecto.metodo1 (),'\n') # presenta el valor por defecto devuelto por el metodo

print ('instanciar clase con valor indicado ; valorindicado = clasePROPIA (cadena) \n')

valorindicado = clasePROPIA (cadena) # instancia la clase con valores por defecto

print ('llamando al atributo del objeto ; valorindicado.atributo ',valorindicado.atributo,'\n') # presenta el valor del atributo

print ('llamando a un metodo del objeto ; valorindicado.metodo1 () ',valorindicado.metodo1 (),'\n') # presenta el valor indicado en el objeto 

print ('llamando a un metodo del objeto ; valorindicado.metodo2 (cadena.upper ()) ',valorindicado.metodo2 (cadena.upper ()),'\n') # presenta el valor indicado en el objeto

print ('crear una clase propia con herencia ; class claseCONherencia (clasePROPIA) : \n')

class claseCONherencia (clasePROPIA) : # definicion de la clase con herencia -hereda de clasePROPIA-
	'''clase que hereda los atributos y metodos de clasePROPIA''' # docstring , informacion de la clase
	
print ('documentacion de la clase ; claseCONherencia.__doc__ ',claseCONherencia.__doc__,'\n') # presenta la documentacion de la clase

print ('instanciar la clase con herencia ; conHerencia = claseCONherencia (cadena.upper ()) \n')

conHerencia = claseCONherencia (cadena.upper ()) # objeto con herencia de clasePROPIA

print ('llamando al atributo del objeto ; conHerencia.atributo ',conHerencia.atributo,'\n') # presenta el valor del atributo

print ('llamando a un metodo del objeto ; conHerencia.metodo1 () ',conHerencia.metodo1 (),'\n') # presenta el valor indicado en el objeto 

print ('llamando a un metodo del objeto ; conHerencia.metodo2 (cadena) ',conHerencia.metodo2 (cadena),'\n') # presenta el valor indicado en el objeto

print ('crear la clase punto ; class punto (object) : \n')

class punto (object) : # definicion de la clase
	def __init__ (self,x=0,y=0) : # metodo , inicializa la clase con los parametros indicados , argumento con valor por defecto
		self.x = x  # asigna el valor de x
		self.y = y  # asigna el valor de y
	
	def distanciaDESDEorigen (self) : # definicion del metodo
		import math # importa el modulo indicado
		return math.hypot (self.x,self.y) # devuelve la hypotenusa de los valores indicados -x,y-
	
	def __eq__ (self,otro) : # metodo especial -==- , comparacion igual a 
		return self.x == otro.x and self.y == otro.y # devuelve True si los valores son iguales , lo contrario False
	
	def __repr__ (self) : # metodo especial , devuelve una cadena que se puede ejecutar o reproducir por la funcion eval ()
		return 'punto ({0.x!r},{0.y!r})'.format (self) # devuelve una llamada a la clase punto con los valores indicados
	
	def __str__ (self) : # metodo especial , devuelve una cadena que se puede leer
		return '({0.x!r},{0.y!r})'.format (self) # devuelve una cadena para lectura en formato humano

print ('instanciar la clase punto ; Punto = punto () \n')

Punto = punto () # crea el objeto con los valores por defecto

print ('crear una segunda instancia la clase punto ; PUNTO = punto (3,4) \n')

PUNTO = punto (3,4) # crea el objeto con los valores indicados

print ('usar la funcion repr en los objetos Punto y PUNTO : \n')

print ('repr (Punto) ',repr (Punto),'\n') # presenta la salida del metodo especial __repr__

print ('repr (PUNTO) ',repr (PUNTO),'\n') # presenta la salida del metodo especial __repr__

print ('usar la funcion str en los objetos Punto y PUNTO : \n')

print ('str (Punto) ',str (Punto),'\n') # presenta la salida del metodo especial __str__

print ('str (PUNTO) ',str (PUNTO),'\n') # presenta la salida del metodo especial __str__

print ('uso del metodo distanciaDESDEorigen del objeto PUNTO ; PUNTO.distanciaDESDEorigen () ',PUNTO.distanciaDESDEorigen (),'\n') # presenta el resultado de math.hypot

print ('cambiar el valor de x del objeto PUNTO ; PUNTO.x = -33 \n')

PUNTO.x = -33 # cambia el valor de x del objeto

print ('evaluar repr (PUNTO) con eval ; eval (repr (PUNTO)).distanciaDESDEorigen () ',eval (repr (PUNTO)).distanciaDESDEorigen (),'\n') # presenta la salida del metodo especial __repr__ evaluada por eval ()

print ('str (PUNTO) ',str (PUNTO),'\n') # presenta la salida del metodo especial __str__

print ('PUNTO.distanciaDESDEorigen () ',PUNTO.distanciaDESDEorigen (),'\n') # presenta la salida del metodo del objeto

print ('comparar los objetos Punto y PUNTO por igualdad - == - ; Punto == PUNTO ',Punto == PUNTO,'\n') # presenta True si los dos objetos son iguales , lo contrario False

print ('comparar los objetos Punto y PUNTO por desigualdad - != - ; Punto != PUNTO ',Punto != PUNTO,'\n') # presenta True si los dos objetos NO son iguales , lo contrario False 

print ('crear clase con metodos especiales ; class metodosEspecialesCOMPARACION (object) : \n')

class metodosEspecialesCOMPARACION (object) : # definicion de la clase
	def __init__ (self,numero) : # metodo , inicializa la clase con los parametros indicados
		self.numero = numero # asigna el valor del parametro
		
	def __lt__ (self,otroNumero) : # metodo especial - < - , comparacion menor que
		return self.numero < otroNumero # devuelve True si self.numero es menor que otroNumero , lo contrario False
	
	def __le__ (self,otroNumero) : # metodo especial - <= - , comparacion menor o igual que
		return self.numero <= otroNumero # devuelve True si self.numero es menor o igual que otroNumero , lo contrario False
	
	def __eq__ (self,otroNumero) : # metodo especial - == - , comparacion igual que
		return self.numero == otroNumero # devuelve True si self.numero es igual que otroNumero , lo contrario False
	
	def __ne__ (self,otroNumero) : # metodo especial - != - , comparacion NO igual que
		return self.numero != otroNumero # devuelve True si self.numero NO es igual que otroNumero , lo contrario False
	
	def __ge__ (self,otroNumero) : # metodo especial - >= - , comparacion mayor o igual que
		return self.numero >= otroNumero # devuelve True si self.numero es mayor o igual que otroNumero , lo contrario False
	
	def __gt__ (self,otroNumero) : # metodo especial - > - , comparacion mayor que
		return self.numero > otroNumero # devuelve True si self.numero es mayor que otroNumero , lo contrario False

print ('instanciar la clase metodosEspecialesCOMPARACION ; COMPARAR = metodosEspecialesCOMPARACION (50) \n')

COMPARAR = metodosEspecialesCOMPARACION (50) # crea el objeto de la clase con el valor indicado

print ('comparaciones : \n')

print ('menor que : \n')

print ('COMPARAR < 100 ',COMPARAR < 100,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR < 10 ',COMPARAR < 10,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('menor o igual que : \n')

print ('COMPARAR <= 100 ',COMPARAR <= 100,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR <= 10 ',COMPARAR <= 10,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR <= 50 ',COMPARAR <= 50,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('igual que : \n')

print ('COMPARAR == 100 ',COMPARAR == 100,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR == 10 ',COMPARAR == 10,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR == 50 ',COMPARAR == 50,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('NO igual que : \n')

print ('COMPARAR != 100 ',COMPARAR != 100,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR != 10 ',COMPARAR != 10,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR != 50 ',COMPARAR != 50,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('mayor o igual que : \n')

print ('COMPARAR >= 100 ',COMPARAR >= 100,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR >= 10 ',COMPARAR >= 10,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR >= 50 ',COMPARAR >= 50,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('mayor que : \n')

print ('COMPARAR > 100 ',COMPARAR > 100,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR > 10 ',COMPARAR > 10,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('COMPARAR > 50 ',COMPARAR > 50,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('crear la clase circuloHerencia que hereda de punto ; class circuloHerencia (punto) : \n')

class circuloHerencia (punto) : # definicion de la clase con herencia , hereda de punto
	def __init__ (self,radio,x=0,y=0) : # metodo , inicializa la clase con los parametros con los valores por defecto
		super ().__init__ (x,y) # inicializa el metodo indicado de la clase base -punto-
		self.radio = radio # asigna el valor del parametro

	def distanciaBordeDesdeOrigen (self) : # definicion del metodo
		return abs (self.distanciaDESDEorigen () - self.radio) # devuelve el resultado devuelto por la funcion abs
	
	def area (self) : # definicion del metodo
		import math # importa el modulo indicado
		return math.pi * (self.radio ** 2) # devuelve el resultado de la operacion
	
	def circunferencia (self) : # definicion del metodo
		import math # importa el modulo indicado
		return 2 * math.pi * self.radio # devuelve el resultado de la operacion
	
	def __eq__ (self,otro) : # metodo especial - == - , comparacion igual que
		return self.radio == otro.radio and super ().__eq__ (otro) # devuelve True si self.radio es igual que otro.radio y los valores -x,y- del metodo especial base __eq__ son iguales , lo contrario False
	
	def __repr__ (self) : # metodo especial -repr- , devuelve una cadena que se puede evaluar por eval
		return 'circuloHerencia ({0.radio!r},{0.x!r},{0.y!r})'.format (self) # devuelve una cadena que se puede evaluar por eval
	
	def __str__ (self) : # metodo especial -str- , devuelve una cadena que puede ser evaluada
		return repr (self) # devuelve la salida de repr -cadena que puede ser evaluada-
	
print ('instanciar clase con herencia circuloHerencia ; circuloRadio = circuloHerencia (6,33,10) \n')

circuloRadio = circuloHerencia (6,33,10) # crea un objeto de la clase con los valores indicados

print ('uso de metodo distanciaDESDEorigen heredado de punto ; circuloRadio.distanciaDESDEorigen () ',circuloRadio.distanciaDESDEorigen (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo distanciaBordeDesdeOrigen del objeto ; circuloRadio.distanciaBordeDesdeOrigen () ',circuloRadio.distanciaBordeDesdeOrigen (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo area del objeto ; circuloRadio.area () ',circuloRadio.area (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo circunferencia del objeto ; circuloRadio.circunferencia () ',circuloRadio.circunferencia (),'\n') # presenta el resultado devuelto por el metodo

print ('crear nuevo objeto ; circuloRadio1 = circuloHerencia (6,3,10) \n')

circuloRadio1 = circuloHerencia (6,3,10) # crea un objeto de la clase con los valores indicados

print ('uso de metodo distanciaDESDEorigen heredado de punto ; circuloRadio1.distanciaDESDEorigen () ',circuloRadio1.distanciaDESDEorigen (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo distanciaBordeDesdeOrigen del objeto ; circuloRadio1.distanciaBordeDesdeOrigen () ',circuloRadio1.distanciaBordeDesdeOrigen (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo area del objeto ; circuloRadio1.area () ',circuloRadio1.area (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo circunferencia del objeto ; circuloRadio1.circunferencia () ',circuloRadio1.circunferencia (),'\n') # presenta el resultado devuelto por el metodo

print ('igualdad de circuloRadio y circuloRadio1 ; circuloRadio == circuloRadio1 ',circuloRadio == circuloRadio1,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('NO igualdad de circuloRadio y circuloRadio1 ; circuloRadio != circuloRadio1 ',circuloRadio != circuloRadio1,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('uso de repr en el objeto ; repr (circuloRadio) ',repr (circuloRadio),'\n') # presenta una cadena que se puede evaluar con eval

print ('uso de repr en el objeto ; repr (circuloRadio1) ',repr (circuloRadio1),'\n') # presenta una cadena que se puede evaluar con eval

print ('evaluar repr (circuloRadio) con eval ; eval (repr (circuloRadio)).distanciaDESDEorigen () ',eval (repr (circuloRadio)).distanciaDESDEorigen (),'\n') # presenta la salida del metodo especial __repr__ evaluada por eval ()

print ('evaluar repr (circuloRadio1) con eval ; eval (repr (circuloRadio1)).distanciaDESDEorigen () ',eval (repr (circuloRadio1)).distanciaDESDEorigen (),'\n') # presenta la salida del metodo especial __repr__ evaluada por eval ()

print ('uso de str en el objeto ; str (circuloRadio) ',str (circuloRadio),'\n') # presenta una cadena legible para humanos

print ('uso de str en el objeto ; str (circuloRadio1) ',str (circuloRadio1),'\n') # presenta una cadena legible para humanos

print ('crear clase con herencia con decoradores ; class claseDecoradores (punto) : \n')

class claseDecoradores (punto) : # definicion de la clase con herencia , hereda de punto
	def __init__ (self,radio,x=0,y=0) : # metodo , inicializa la clase con los parametros con los valores por defecto
		super ().__init__ (x,y) # inicializa el metodo indicado de la clase base -punto-
		self.radio = radio # asigna el valor del parametro

	@property # decorador funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def distanciaBordeDesdeOrigen (self) : # definicion del metodo
		return abs (self.distanciaDESDEorigen () - self.radio) # devuelve el resultado devuelto por la funcion abs
	
	@property # decorador funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def area (self) : # definicion del metodo
		import math # importa el modulo indicado
		return math.pi * (self.radio ** 2) # devuelve el resultado de la operacion
	
	@property # decorador funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def circunferencia (self) : # definicion del metodo
		import math # importa el modulo indicado
		return 2 * math.pi * self.radio # devuelve el resultado de la operacion
	
	@property # decorador funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def radio (self) : # definicion del metodo
		return self.__radio # devuelve el valor del atributo privado
	
	@radio.setter # decorador funcion radio -modifica el metodo inferior con las propiedades de la funcion radio-
	def radio (self,radio) : # definicion del metodo
		assert radio > 0,'radio tiene que ser un valor que no sea ni cero , ni un valor negativo' # regla de excepcion , si no se cumple lanza excepcion y devuelve la cadena indicada
		self.__radio = radio # asigna el valor de radio al atributo privado
	
	def __eq__ (self,otro) : # metodo especial - == - , comparacion igual que
		return self.radio == otro.radio and super ().__eq__ (otro) # devuelve True si self.radio es igual que otro.radio y los valores -x,y- del metodo especial base __eq__ son iguales , lo contrario False
	
	def __repr__ (self) : # metodo especial -repr- , devuelve una cadena que se puede evaluar por eval
		return 'circuloHerencia ({0.radio!r},{0.x!r},{0.y!r})'.format (self) # devuelve una cadena que se puede evaluar por eval
	
	def __str__ (self) : # metodo especial -str- , devuelve una cadena que puede ser evaluada
		return repr (self) # devuelve la salida de repr -cadena que puede ser evaluada-

print ('instanciar clase con decoradores y herencia claseDecoradores ; circuloRadioDECORADORES = claseDecoradores (6,33,10) \n')

circuloRadioDECORADORES = claseDecoradores (6,33,10) # crea un objeto de la clase con los valores indicados

print ('uso de metodo distanciaDESDEorigen heredado de punto ; circuloRadioDECORADORES.distanciaDESDEorigen () ',circuloRadioDECORADORES.distanciaDESDEorigen (),'\n') # presenta el resultado devuelto por el metodo

print ('uso de metodo distanciaBordeDesdeOrigen del objeto ; circuloRadioDECORADORES.distanciaBordeDesdeOrigen ',circuloRadioDECORADORES.distanciaBordeDesdeOrigen,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de metodo area del objeto ; circuloRadioDECORADORES.area ',circuloRadioDECORADORES.area,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de metodo circunferencia del objeto ; circuloRadioDECORADORES.circunferencia ',circuloRadioDECORADORES.circunferencia,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de atributo radio del objeto ; circuloRadioDECORADORES.radio ',circuloRadioDECORADORES.radio,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('crear nuevo objeto ; circuloRadioDECORADORES1 = claseDecoradores (6,3,10) \n')

circuloRadioDECORADORES1 = claseDecoradores (6,3,10) # crea un objeto de la clase con los valores indicados

print ('uso de metodo distanciaDESDEorigen heredado de punto ; circuloRadioDECORADORES1.distanciaDESDEorigen () ',circuloRadioDECORADORES1.distanciaDESDEorigen (),'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de metodo distanciaBordeDesdeOrigen del objeto ; circuloRadioDECORADORES1.distanciaBordeDesdeOrigen ',circuloRadioDECORADORES1.distanciaBordeDesdeOrigen,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de metodo area del objeto ; circuloRadioDECORADORES1.area ',circuloRadioDECORADORES1.area,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de metodo circunferencia del objeto ; circuloRadioDECORADORES1.circunferencia ',circuloRadioDECORADORES1.circunferencia,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('uso de atributo radio del objeto ; circuloRadioDECORADORES1.radio ',circuloRadioDECORADORES1.radio,'\n') # presenta el resultado devuelto por el metodo como atributo

print ('igualdad de circuloRadioDECORADORES y circuloRadioDECORADORES1 ; circuloRadioDECORADORES == circuloRadioDECORADORES1 ',circuloRadioDECORADORES == circuloRadioDECORADORES1,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('NO igualdad de circuloRadioDECORADORES y circuloRadioDECORADORES1 ; circuloRadioDECORADORES != circuloRadioDECORADORES1 ',circuloRadioDECORADORES != circuloRadioDECORADORES1,'\n') # presenta True si los valores coinciden con la comparacion , lo contrario False

print ('uso de repr en el objeto ; repr (circuloRadioDECORADORES) ',repr (circuloRadioDECORADORES),'\n') # presenta una cadena que se puede evaluar con eval

print ('uso de repr en el objeto ; repr (circuloRadioDECORADORES1) ',repr (circuloRadioDECORADORES1),'\n') # presenta una cadena que se puede evaluar con eval

print ('evaluar repr (circuloRadioDECORADORES) con eval ; eval (repr (circuloRadioDECORADORES)).distanciaDESDEorigen () ',eval (repr (circuloRadioDECORADORES)).distanciaDESDEorigen (),'\n') # presenta la salida del metodo especial __repr__ evaluada por eval ()

print ('evaluar repr (circuloRadioDECORADORES1) con eval ; eval (repr (circuloRadioDECORADORES1)).distanciaDESDEorigen () ',eval (repr (circuloRadioDECORADORES1)).distanciaDESDEorigen (),'\n') # presenta la salida del metodo especial __repr__ evaluada por eval ()

print ('uso de str en el objeto ; str (circuloRadioDECORADORES) ',str (circuloRadioDECORADORES),'\n') # presenta una cadena legible para humanos

print ('uso de str en el objeto ; str (circuloRadioDECORADORES1) ',str (circuloRadioDECORADORES1),'\n') # presenta una cadena legible para humanos

print ('crear clase con metodos especiales fundamentales ; class metodosEspecialesFundamentales (object) : \n')

class metodosEspecialesFundamentales (object) : # definicion de la clase
	def __init__ (self,numero) : # metodo , inicializa la clase con los parametros indicados
		self.numero = numero # asigna el valor del parametro

	def __bool__ (self) : # metodo especial - bool - , devuelve un valor verdadero del objeto
		return self.numero > 0 # devuelve True si es mayor que cero

	def __format__ (self,format_spec) : # metodo especial - format - , devuelve una cadena formateada
		return format (self.numero,format_spec) # devuelve el valor en una cadena formateada
	
	def __hash__ (self) : # metodo especial - hash - , devuelve un valor que se puede usar como clave diccionario o guardarlo en conjunto
		return hash (id (self)) # devuelve el identificador del valor pasado
	
	def __repr__ (self) : # metodo especial -repr- , devuelve una cadena que se puede evaluar por eval
		return 'metodosEspecialesFundamentales ({0.numero!r})'.format (self) # devuelve una cadena que se puede evaluar por eval
	
	def __str__ (self) : # metodo especial , devuelve una cadena que se puede leer
		return 'valor : {0.numero!r}'.format (self) # devuelve una cadena para lectura en formato humano

print ('instanciar la clase metodosEspecialesFundamentales ; FUNDAMENTALES = metodosEspecialesFundamentales (101) \n')

FUNDAMENTALES = metodosEspecialesFundamentales (101) # crea el objeto de la clase con el valor indicado

print ('uso de bool en el objeto ; bool (FUNDAMENTALES) ; ',bool (FUNDAMENTALES),'\n') # presenta el valor devuelto por bool - True -

print (r'uso de format en el objeto ; "{0}\n".format (FUNDAMENTALES) ',"{0}\n".format (FUNDAMENTALES)) # presenta el valor devuelto por el objeto -numero-

print ('uso de hash en el objeto ; hash (FUNDAMENTALES) ',hash (FUNDAMENTALES),'\n') # presenta el valor devuelto por el hash -identificador-

print ('uso de repr en el objeto ; repr (FUNDAMENTALES) ',repr (FUNDAMENTALES),'\n') # presenta una cadena que se puede evaluar por eval

print ('uso de eval con repr ; eval (repr (FUNDAMENTALES)).numero ',eval (repr (FUNDAMENTALES)).numero,'\n') # presenta el valor puesto en el objeto

print ('uso de str en el objeto ; str (FUNDAMENTALES) ',str (FUNDAMENTALES),'\n') # presenta el valor del objeto en una cadena

print ('crear clase con metodos especiales numericos y bit  ; class metodosEspecialesNumericosBit (object) : \n')

class metodosEspecialesNumericosBit (object) : # definicion de la clase
	def __init__ (self,numero) : # metodo , inicializa la clase con los parametros indicados
		self.numero = numero # asigna el valor del parametro
		
	def __abs__ (self) : # metodo especial - abs - , devuelve el valor de abs 
		return abs (self.numero) # devuelve el resultado del valor
	
	def __float__ (self) : # metodo especial - float - , devuelve el valor en punto flotante
		return float (self.numero) # devuelve el numero en punto flotante
	
	def __index__ (self) : # metodo especial - bin oct hex - , devuelve el valor en binario , octal y hexadecimal
		return self.numero # devuelve una cadena con los valores en binario , octal y hexadecimal
	
	def __complex__ (self) : # metodo especial - complex - , devuelve el valor en formato complex
		return complex (self.numero) # devuelve el valor en formato complex
	
	def __int__ (self) : # metodo especial - int - , devuelve el valor entero sin decimales 
		return int (self.numero) # devuelve el valor entero sin decimales
	
	def __round__ (self,digitos) : # metodo especial - round - , devuelve el valor int de un float redondeado en numero de digitos
		return round (self.numero,digitos) # devuelve el valor int de un float redondeado en numero de digitos
	
	def __pos__ (self) : # metodo especial - signo positivo - , devuelve el valor con signo positivo 
		return +self.numero # devuelve el valor con signo positivo
	
	def __neg__ (self) : # metodo especial - signo negativo - , devuelve el valor con signo negativo
		return -self.numero # devuelve el valor con signo negativo
	
	def __add__ (self,otroNumero) : # metodo especial - + - , suma los valores
		return self.numero + otroNumero # devuelve la suma de los dos valores
	
	def __sub__ (self,otroNumero) : # metodo especial - - - , resta los valores
		return self.numero - otroNumero # devuelve la resta de los dos valores 
	
	def __iadd__ (self,otroNumero) : # metodo especial - += - , suma incremental
		return self.numero + otroNumero # devuelve la suma de los dos valores
	
	def __isub__ (self,otroNumero) : # metodo especial - -= - , resta incremental
		return self.numero - otroNumero # devuelve la resta de los dos valores
	
	def __radd__ (self,otroNumero) : # metodo especial - + - , suma los valores ; otroNumero + self.numero
		return otroNumero + self.numero  # devuelve la suma de los dos valores
	
	def __rsub__ (self,otroNumero) : # metodo especial - - - , resta los valores ; otroNumero - self.numero
		return otroNumero - self.numero  # devuelve la resta de los dos valores
	
	def __mul__ (self,otroNumero) : # metodo especial - * - , multiplica los valores 
		return self.numero * otroNumero # devuelve la multiplicacion de los dos valores
	
	def __mod__ (self,otroNumero) : # metodo especial - % - , resto del resultado de la division
		return self.numero % otroNumero # devuelve el resto de la division de los dos valores
	
	def __imul__ (self,otroNumero) : # metodo especial - *= - , multiplicacion incremental
		return self.numero * otroNumero # devuelve la multiplicacion de los dos valores
	
	def __imod__ (self,otroNumero) : # metodo especial - %= - , resto del resultado de la division incremental
		return self.numero % otroNumero # devuelve el resto de la division de los dos valores
	
	def __rmul__ (self,otroNumero) : # metodo especial - * - , multiplica los valores ; otroNumero * self.numero 
		return otroNumero * self.numero # devuelve la multiplicacion de los dos valores
	
	def __rmod__ (self,otroNumero) : # metodo especial - % - , resto del resultado de la division ; otroNumero % self.numero
		return otroNumero % self.numero # devuelve el resto de la division de los dos valores
	
	def __floordiv__ (self,otroNumero) : # metodo especial - // - , division truncada -resultado sin decimales-
		return self.numero // otroNumero # devuelve la division truncada de los dos valores -resultado sin decimales-
	
	def __truediv__ (self,otroNumero) : # metodo especial - / - , division 
		return self.numero / otroNumero # devuelve la division de los dos valores 
	
	def __ifloordiv__ (self,otroNumero) : # metodo especial - //= - , division truncada incremental -resultado sin decimales-
		return self.numero // otroNumero # devuelve la division truncada de los dos valores -resultado sin decimales-
	
	def __itruediv__ (self,otroNumero) : # metodo especial - /= - , division incremental
		return self.numero / otroNumero # devuelve la division de los dos valores 

	def __rfloordiv__ (self,otroNumero) : # metodo especial - // - , division truncada -resultado sin decimales- ; otroNumero // self.numero
		return otroNumero // self.numero # devuelve la division truncada de los dos valores -resultado sin decimales-

	def __rtruediv__ (self,otroNumero) : # metodo especial - / - , division ; otroNumero / self.numero 
		return otroNumero / self.numero # devuelve la division de los dos valores
	
	def __divmod__ (self,otroNumero) : # metodo especial - divmod - , resto del resultado de la division
		return divmod (self.numero,otroNumero) # devuelve el resultado de la funcion - % -

	def __rdivmod__ (self,otroNumero) : # metodo especial - divmod - , resto del resultado de la division ; otroNumero % self.numero
		return divmod (otroNumero,self.numero) # devuelve el resultado de la funcion - % - ; otroNumero % self.numero
	
	def __pow__ (self,otroNumero) : # metodo especial - ** - , potencia de 
		return self.numero ** otroNumero # devuelve el resultado de numero elevado a la potencia de otroNumero
	
	def __and__ (self,otroNumero) : # metodo especial - & - , comparacion , los dos valores iguales
		return self.numero & otroNumero # devuelve el valor and binario
	
	def __ipow__ (self,otroNumero) : # metodo especial - **= - , potencia de  incremental
		return self.numero ** otroNumero # devuelve el resultado de numero elevado a la potencia de otroNumero
	
	def __iand__ (self,otroNumero) : # metodo especial - &= - , comparacion , los dos valores iguales
		return self.numero & otroNumero # devuelve el valor and binario

	def __rpow__ (self,otroNumero) : # metodo especial - ** - , potencia de  ; otroNumero ** self.numero
		return otroNumero ** self.numero # devuelve el resultado de otroNumero elevado a la potencia de numero
	
	def __rand__ (self,otroNumero) : # metodo especial - & - , comparacion , los dos valores iguales ; otroNumero & self.numero
		return otroNumero & self.numero # devuelve el valor and binario
	
	def __xor__ (self,otroNumero) : # metodo especial - ^ - , comparacion , or exclusivo 
		return self.numero ^ otroNumero # devuelve el valor exclusivo binario

	def __or__ (self,otroNumero) : # metodo especial - | - , comparacion , or 
		return self.numero | otroNumero # devuelve el valor or binario

	def __ixor__ (self,otroNumero) : # metodo especial - ^= - , comparacion , or exclusivo 
		return self.numero ^ otroNumero # devuelve el valor exclusivo binario

	def __ior__ (self,otroNumero) : # metodo especial - |= - , comparacion , or 
		return self.numero | otroNumero # devuelve el valor or binario

	def __rxor__ (self,otroNumero) : # metodo especial - ^ - , comparacion , or exclusivo 
		return otroNumero ^ self.numero # devuelve el valor exclusivo binario

	def __ror__ (self,otroNumero) : # metodo especial - | - , comparacion , or 
		return otroNumero | self.numero # devuelve el valor or binario
	
	def __lshift__ (self,otroNumero) : # metodo especial - << - , mover bit a la izquierda
		return self.numero << otroNumero # mueve los bits a la izquierda

	def __rshift__ (self,otroNumero) : # metodo especial - >> - , mover bit a la derecha
		return self.numero >> otroNumero # mueve los bits a la derecha

	def __ilshift__ (self,otroNumero) : # metodo especial - <<= - , mover bit a la izquierda
		return self.numero << otroNumero # mueve los bits a la izquierda

	def __irshift__ (self,otroNumero) : # metodo especial - >>= - , mover bit a la derecha
		return self.numero >> otroNumero # mueve los bits a la derecha

	def __rlshift__ (self,otroNumero) : # metodo especial - << - , mover bit a la izquierda ; otroNumero << self.numero
		return  ; otroNumero << self.numero # mueve los bits a la izquierda

	def __rrshift__ (self,otroNumero) : # metodo especial - >> - , mover bit a la derecha ; otroNumero >> self.numero
		return  ; otroNumero >> self.numero # mueve los bits a la derecha
	
	def __invert__ (self) : # metodo especial - ~ - , invierte el valor binario
		return ~ self.numero # presenta el valor  que representa el valor binario invertido del valor self.numero
	
print ('instanciar la clase metodosEspecialesNumericosBit ; numerosBit = metodosEspecialesNumericosBit (101) \n')

numerosBit = metodosEspecialesNumericosBit (101) # crea el objeto de la clase con el valor indicado

print ('uso de abs en el objeto ; abs (numerosBit) ; ',abs (numerosBit),'\n') # presenta el valor devuelto por abs 

print ('uso de float en el objeto ; float (numerosBit) ; ',float (numerosBit),'\n') # presenta el valor devuelto por float

print ('uso de bin en el objeto ; bin (numerosBit) ; ',bin (numerosBit),'\n') # presenta el valor devuelto por index -binario-

print ('uso de oct en el objeto ; oct (numerosBit) ; ',oct (numerosBit),'\n') # presenta el valor devuelto por index -octal-

print ('uso de hex en el objeto ; hex (numerosBit) ; ',hex (numerosBit),'\n') # presenta el valor devuelto por index -hexadecimal-

print ('uso de complex en el objeto ; complex (numerosBit) ; ',complex (numerosBit),'\n') # presenta el valor devuelto por complex

print ('uso de int en el objeto ; int (numerosBit) ; ',int (numerosBit),'\n') # presenta el valor devuelto por int

print ('uso de round en el objeto ; round (numerosBit,3) ; ',round (numerosBit,3),'\n') # presenta el valor devuelto por round

print ('uso de + en el objeto ; +numerosBit ; ',+numerosBit,'\n') # presenta el valor devuelto por pos

print ('uso de - en el objeto ; -numerosBit ; ',-numerosBit,'\n') # presenta el valor devuelto por neg 

print ('uso de + en el objeto ; numerosBit + .101 ; ',numerosBit + .101,'\n') # presenta el valor devuelto por la suma

print ('uso de - en el objeto ; numerosBit - .101 ; ',numerosBit - .101,'\n') # presenta el valor devuelto por la resta

print ('uso de += en el objeto ; numerosBit += .101 ; \n') 

numerosBit += .101 # suma incremental , suma el valor al del objeto

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por la suma incremental

print ('uso de -= en el objeto ; numerosBit -= .101 ; \n') 

numerosBit -= .101 # resta incremental , resta el valor al del objeto

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por la resta incremental

print ('uso de + en el objeto -valores invertidos- ;  .101 + numerosBit  ; ',.101 + numerosBit,'\n') # presenta el valor devuelto por la suma invertida

print ('uso de - en el objeto -valores invertidos-  ; .101 - numerosBit ; ',.101 - numerosBit,'\n') # presenta el valor devuelto por la resta invertida

print ('uso de * en el objeto ; numerosBit * .101 ; ',numerosBit * .101,'\n') # presenta el valor devuelto por la multiplicacion

print ('uso de % en el objeto ; numerosBit % .101 ; ',numerosBit % .101,'\n') # presenta el valor devuelto por el resto de la division

print ('uso de *= en el objeto ; numerosBit *= 101 ; \n') 

numerosBit *= 101 # multiplicacion incremental , añade el valor al del objeto

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por la multiplicacion incremental

print ('uso de %= en el objeto ; numerosBit %= 10 ; \n') 

numerosBit %= 10 # resto de la division incremental , añade el valor al del objeto

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por el resto de la division incremental

print ('uso de * en el objeto -valores invertidos- ;  .101 * numerosBit  ; ',.101 * numerosBit,'\n') # presenta el valor devuelto por la multiplicacion invertida

print ('uso de % en el objeto -valores invertidos-  ; .101 % numerosBit ; ',.101 % numerosBit,'\n') # presenta el valor devuelto por el resto de la division de la division invertida

print ('uso de // en el objeto ; numerosBit // .101 ; ',numerosBit // .101,'\n') # presenta el valor devuelto por la division truncada -resultado sin decimales-

print ('uso de / en el objeto ; numerosBit / .101 ; ',numerosBit / .101,'\n') # presenta el valor devuelto por la division

print ('uso de //= en el objeto ; numerosBit //= .101 ; \n') 

numerosBit //= .101 # division truncada incremental , añade el valor al del objeto -resultado sin decimales-

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por la division truncada incremental

print ('uso de /= en el objeto ; numerosBit /= .101 ; \n') 

numerosBit /= .101 # division incremental , añade el valor al del objeto

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por la division incremental

print ('uso de // en el objeto -valores invertidos- ;  .101 // numerosBit  ; ',.101 // numerosBit,'\n') # presenta el valor devuelto por la division truncada invertida

print ('uso de / en el objeto -valores invertidos-  ; .101 / numerosBit ; ',.101 / numerosBit,'\n') # presenta el valor devuelto por la division invertida

print ('uso de divmod en el objeto ; divmod (numerosBit,10) ; ',divmod (numerosBit,10),'\n') # presenta el valor devuelto por divmod -resultado division , resto division)

print ('uso de divmod en el objeto ; divmod (10,numerosBit) -valores invertidos-  ; ',divmod (10,numerosBit),'\n') # presenta el valor devuelto por divmod -valores invertidos- , -resultado division , resto division)

print ('uso de ** en el objeto ; numerosBit ** .101 ; ',numerosBit ** .101,'\n') # presenta el valor devuelto por la potencia

print ('uso de & en el objeto ; int (numerosBit) & 101 ; ',int (numerosBit) & 101,'\n') # presenta el valor devuelto por and binario

print ('uso de **= en el objeto ; numerosBit **= 1.-1 ; \n') 

numerosBit **= 1.-1 # potencia incremental , añade el valor al del objeto 

print ('numerosBit ',numerosBit,'\n') # presenta el valor devuelto por la potencia incremental

print ('nueva instancia de la clase metodosEspecialesNumericosBit ; numerosBit1 = metodosEspecialesNumericosBit (101) \n')

numerosBit1 = metodosEspecialesNumericosBit (101) # crea el nuevo objeto de la clase con el valor indicado

print ('uso de &= en el objeto ; numerosBit1 &= 101 ; \n') 

numerosBit1 &= 101 # and binario incremental , añade el valor al del objeto

print ('numerosBit1 ',numerosBit1,'\n') # presenta el valor devuelto por and binario incremental

print ('uso de ** en el objeto -valores invertidos- ;  .101 ** numerosBit  ; ',.101 ** numerosBit,'\n') # presenta el valor devuelto por la potencia -valores invertidos-

print ('uso de & en el objeto -valores invertidos-  ; 101 & numerosBit1 ; ',101 & numerosBit1,'\n') # presenta el valor devuelto por and binario

print ('uso de ^ en el objeto ; 101 ^ numerosBit1 ; ',101 ^ numerosBit1,'\n') # presenta el valor devuelto por xor binario

print ('uso de | en el objeto ; 101 | numerosBit1 ; ',101 | numerosBit1,'\n') # presenta el valor devuelto por or binario

print ('uso de ^= en el objeto ; numerosBit1 ^= 101 ; \n') 

numerosBit1 ^= 101 # xor binario incremental , añade el valor al del objeto

print ('numerosBit1 ',numerosBit1,'\n') # presenta el valor devuelto por xor binario incremental

print ('uso de |= en el objeto ; numerosBit1 |= 101 ; \n') 

numerosBit1 |= 101 # or binario incremental , añade el valor al del objeto

print ('numerosBit1 ',numerosBit1,'\n') # presenta el valor devuelto por or binario incremental

print ('uso de ^ en el objeto -valores invertidos- ;  101 ^ numerosBit  ; ',101 ^ numerosBit1,'\n') # presenta el valor devuelto por xor binario -valores invertidos-

print ('uso de | en el objeto -valores invertidos-  ; 101 | numerosBit1 ; ',101 | numerosBit1,'\n') # presenta el valor devuelto por or binario -valores invertidos-

print ('uso de << en el objeto ; numerosBit1 << 1 ; ',numerosBit1 << 1,'\n') # presenta el valor devuelto por mover 1 bit a la izquierda 

print ('uso de >> en el objeto ; numerosBit1 >> 1 ; ',numerosBit1 >> 1,'\n') # presenta el valor devuelto por mover 1 bit a la derecha

print ('uso de <<= en el objeto ; numerosBit1 <<= 101 ; \n') 

numerosBit1 <<= 101 # mover 101 bit a la izquierda incremental , añade el valor al del objeto

print ('numerosBit1 ',numerosBit1,'\n') # presenta el valor devuelto por mover 101 bit a la izquierda incremental

print ('uso de >>= en el objeto ; numerosBit1 >>= 101 ; \n') 

numerosBit1 >>= 101 # mover 10 bit a la derecha incremental , añade el valor al del objeto

print ('numerosBit1 ',numerosBit1,'\n') # presenta el valor devuelto por mover 101 bit a la derecha incremental

print ('uso de << en el objeto -valores invertidos-  ; 101 << numerosBit1 ; ',101 << numerosBit1,'\n') # presenta el valor devuelto por mover el valor del objeto en bit  a la izquierda

print ('uso de >> en el objeto -valores invertidos-  ; 101 >> numerosBit1 ; ',101 >> numerosBit1,'\n') # presenta el valor devuelto por mover el valor del objeto en bit  a la derecha

print ('uso de ~ en el objeto ; ~numerosBit1 ; ',~numerosBit1,'\n') # presenta el valor invertido

print ('crear la clase logicaDIFUSA (object) : \n')

class logicaDIFUSA (object) : # definicion de la clase
	def __init__ (self,valor=0.0) : # metodo , inicializa la clase con los parametros indicados
		self.__valor = valor if 0.0 <= valor <= 1.0 else 0.0 # asigna el valor del parametro al atributo privado
		
	def __invert__ (self) : # metodo especial - ~ - , invierte el valor binario
		return logicaDIFUSA (1.0 - self.__valor) # devuelve el resultado de la operacion
	
	def __and__ (self,otro) : # metodo especial - & and binario- , comparacion
		return logicaDIFUSA (min (self.__valor,otro.__valor)) # devuelve el valor minimo de los dos objetos comparados
	
	def __iand__ (self,otro) :  # metodo especial -&= and binario incremental- , comparacion
		self.__valor = min (self.__valor,otro.__valor) # asigna el valor minimo de los dos objetos comparados al atributo privado
		return self # devuelve el objeto con el nuevo valor
	
	def __or__ (self,otro) :  # metodo especial - | or binario- , comparacion
		return logicaDIFUSA (max (self.__valor,otro.__valor)) # devuelve el valor maximo de los dos objetos comparados
	
	def __ior__ (self,otro) : # metodo especial - |= or binario incremental- , comparacion
		self.__valor = max (self.__valor,otro.__valor) # asigna el valor maximo de los dos objetos comparados al atributo privado
		return self # devuelve el objeto con el nuevo valor
	
	def __repr__ (self) : # metodo especial -repr- , devuelve una cadena que se puede evaluar por eval
		return ('{0} ({1})'.format (self.__class__.__name__,self.__valor)) # devuelve una cadena formateada con el nombre de la clase y el valor del atributo privado
	
	def __str__ (self) : # metodo especial , devuelve una cadena que se puede leer
		return str (self.__valor) # devuelve el valor del atributo privado en formato cadena
	
	def __bool__ (self) : # metodo especial - bool - , comparacion devuelve True o False
		return self.__valor > 0.5 # devuelve True si el valor del atributo privado es mayor al indicado , lo contrario False
	
	def __int__ (self) : # metodo especial -int- , devuelve el valor entero
		return round (self.__valor) # devuelve el valor redondeado a entero mas cercano al valor del atributo privado
	
	def __float__ (self) : # metodo especial -float- , devuelve el valor en punto flotante
		return self.__valor # devuelve el valor del atributo privado
	
	def __lt__ (self,otro) : # metodo especial -<- , comparacion 
		return self.__valor < otro.__valor # devuelve True si el valor del atributo privado es mayor al del otro objeto , lo contrario False
	
	def __eq__ (self,otro) : # metodo especial -==- , comparacion
		return self.__valor == otro.__valor # devuelve True si el valor del atributo privado es igual al del otro objeto , lo contrario False
	
	def __le__ (self,otro) : # metodo especial -<=- , comparacion
		return self.__valor <= otro.__valor # devuelve True si el valor del atributo privado es menor o igual al del otro objeto , lo contrario False
	
	def __hash__ (self) : # metodo especial -hash- ,  devuelve un valor que se puede usar como clave diccionario o guardarlo en conjunto
		return hash (id (self)) # devuelve el identificador del objeto pasado
	
	def __format__(self,format_spec) : # metodo especial -format- , devuelve una cadena formateada
		return format (self.__valor,format_spec) # devuelve el valor del atributo privado en el formato indicado
	
	@staticmethod # decorador  funcion staticmethod -modifica el metodo inferior con las propiedades de la funcion staticmethod-
	def conjuncion (*DIFUSAS) : # definicion del metodo , para comparar los valores de multiples objetos de logicaDIFUSA
		return logicaDIFUSA (min ([float (x) for x in DIFUSAS])) # devuelve el valor minimo de la lista de valores en punto flotante
	
	@staticmethod # decorador  funcion staticmethod -modifica el metodo inferior con las propiedades de la funcion staticmethod-
	def disjuncion (*DIFUSAS) : # definicion del metodo , para comparar los valores de multiples objetos de logicaDIFUSA
		return logicaDIFUSA (max ([float (x) for x in DIFUSAS])) # devuelve el valor maximo de la lista de valores en punto flotante
	
print ('instanciar la clase logicaDIFUSA : \n')

print ('FUZZY = logicaDIFUSA () \n')

FUZZY = logicaDIFUSA () # crea el objeto con el valor por defecto

print ('FUZZY1 = logicaDIFUSA (0.256) \n')

FUZZY1 = logicaDIFUSA (0.256) # crea el objeto con el valor indicado

print ('FUZZY2 = logicaDIFUSA (0.568) \n')

FUZZY2 = logicaDIFUSA (0.568) # crea el objeto con el valor indicado

print ('FUZZY3 = logicaDIFUSA (0.721) \n')

FUZZY3 = logicaDIFUSA (0.721) # crea el objeto con el valor indicado

print ('FUZZY4 = logicaDIFUSA (1.0) \n')

FUZZY4 = logicaDIFUSA (1.0) # crea el objeto con el valor indicado

print ('~FUZZY ',~FUZZY,'\n') # presenta el valor inverso

print ('~FUZZY1 ',~FUZZY1,'\n') # presenta el valor inverso

print ('~FUZZY2 ',~FUZZY2,'\n') # presenta el valor inverso

print ('~FUZZY3 ',~FUZZY3,'\n') # presenta el valor inverso

print ('~FUZZY4 ',~FUZZY4,'\n') # presenta el valor inverso

print ('FUZZY & FUZZY1 ',FUZZY & FUZZY1,'\n') # presenta el valor minimo 

print ('FUZZY1 & FUZZY2 ',FUZZY1 & FUZZY2,'\n') # presenta el valor minimo

print ('FUZZY2 & FUZZY3',FUZZY2 & FUZZY3,'\n') # presenta el valor minimo

print ('FUZZY3 & FUZZY4',FUZZY3 & FUZZY4,'\n') # presenta el valor minimo

print ('FUZZY4 & FUZZY',FUZZY4 & FUZZY,'\n') # presenta el valor minimo

print ('FUZZY &= FUZZY1 \n') 

FUZZY &= FUZZY1 # asigna el valor minimo al objeto

print ('FUZZY ',FUZZY,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY1 &= FUZZY2 \n') 

FUZZY1 &= FUZZY2 # asigna el valor minimo al objeto

print ('FUZZY1 ',FUZZY1,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY2 &= FUZZY3 \n')

FUZZY2 &= FUZZY3 # asigna el valor minimo al objeto

print ('FUZZY2 ',FUZZY2,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY3 &= FUZZY4 \n')

FUZZY3 &= FUZZY4 # asigna el valor minimo al objeto

print ('FUZZY3 ',FUZZY3,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY4 &= FUZZY \n')

FUZZY4 &= FUZZY # asigna el valor minimo al objeto

print ('FUZZY4 ',FUZZY4,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY | FUZZY1 ',FUZZY | FUZZY1,'\n') # presenta el valor maximo 

print ('FUZZY1 | FUZZY2 ',FUZZY1 | FUZZY2,'\n') # presenta el valor maximo

print ('FUZZY2 | FUZZY3',FUZZY2 | FUZZY3,'\n') # presenta el valor maximo

print ('FUZZY3 | FUZZY4',FUZZY3 | FUZZY4,'\n') # presenta el valor maximo

print ('FUZZY4 | FUZZY',FUZZY4 | FUZZY,'\n') # presenta el valor maximo

print ('FUZZY |= FUZZY1 \n') 

FUZZY |= FUZZY1 # asigna el valor maximo al objeto

print ('FUZZY ',FUZZY,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY1 |= FUZZY2 \n') 

FUZZY1 |= FUZZY2 # asigna el valor maximo al objeto

print ('FUZZY1 ',FUZZY1,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY2 |= FUZZY3 \n')

FUZZY2 |= FUZZY3 # asigna el valor maximo al objeto

print ('FUZZY2 ',FUZZY2,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY3 |= FUZZY4 \n')

FUZZY3 |= FUZZY4 # asigna el valor maximo al objeto

print ('FUZZY3 ',FUZZY3,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY4 |= FUZZY \n')

FUZZY4 |= FUZZY # asigna el valor maximo al objeto

print ('FUZZY4 ',FUZZY4,'\n') # presenta el objeto con el valor maximo asignado

print ('repr (FUZZY) ',repr (FUZZY),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY)) ',eval (repr (FUZZY)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY1) ',repr (FUZZY1),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY1)) ',eval (repr (FUZZY1)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY2) ',repr (FUZZY2),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY2)) ',eval (repr (FUZZY2)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY3) ',repr (FUZZY3),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY3)) ',eval (repr (FUZZY3)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY4) ',repr (FUZZY4),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY4)) ',eval (repr (FUZZY4)),'\n') # presenta el valor de la cadena evaluada

print ('str (FUZZY) ',str (FUZZY),'\n') # presenta el valor en formato cadena

print ('str (FUZZY1) ',str (FUZZY1),'\n') # presenta el valor en formato cadena

print ('str (FUZZY2) ',str (FUZZY2),'\n') # presenta el valor en formato cadena

print ('str (FUZZY3) ',str (FUZZY3),'\n') # presenta el valor en formato cadena

print ('str (FUZZY4) ',str (FUZZY4),'\n') # presenta el valor en formato cadena

print ('bool (FUZZY) ',bool (FUZZY),'\n') # presenta True o False dependiendo del valor comparado con el de bool 

print ('bool (FUZZY1) ',bool (FUZZY1),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('bool (FUZZY2) ',bool (FUZZY2),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('bool (FUZZY3) ',bool (FUZZY3),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('bool (FUZZY4) ',bool (FUZZY4),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('int (FUZZY) ',int (FUZZY),'\n') # presenta el valor redondeado  en formato entero , sin decimales

print ('int (FUZZY1) ',int (FUZZY1),'\n') # presenta el valor redondeado en formato entero , sin decimales

print ('int (FUZZY2) ',int (FUZZY2),'\n') # presenta el valor redondeado  en formato entero , sin decimales

print ('int (FUZZY3) ',int (FUZZY3),'\n') # presenta el valor redondeado  en formato entero , sin decimales

print ('int (FUZZY4) ',int (FUZZY4),'\n') # presenta el valor  redondeado en formato entero , sin decimales

print ('float (FUZZY) ',float (FUZZY),'\n') # presenta el valor del objeto

print ('float (FUZZY1) ',float (FUZZY1),'\n') # presenta el valor del objeto

print ('float (FUZZY2) ',float (FUZZY2),'\n') # presenta el valor del objeto

print ('float (FUZZY3) ',float (FUZZY3),'\n') # presenta el valor del objeto

print ('float (FUZZY4) ',float (FUZZY4),'\n') # presenta el valor del objeto

print ('FUZZY < FUZZY1 ',FUZZY < FUZZY1,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY1 < FUZZY2 ',FUZZY1 < FUZZY2,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY2 < FUZZY3',FUZZY2 < FUZZY3,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY3 < FUZZY4',FUZZY3 < FUZZY4,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY4 < FUZZY',FUZZY4 < FUZZY,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY <= FUZZY1 ',FUZZY <= FUZZY1,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY1 <= FUZZY2 ',FUZZY1 <= FUZZY2,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY2 <= FUZZY3',FUZZY2 <= FUZZY3,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY3 <= FUZZY4',FUZZY3 <= FUZZY4,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY4 <= FUZZY',FUZZY4 <= FUZZY,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY == FUZZY1 ',FUZZY == FUZZY1,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY1 == FUZZY2 ',FUZZY1 == FUZZY2,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY2 == FUZZY3',FUZZY2 == FUZZY3,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY3 == FUZZY4',FUZZY3 == FUZZY4,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY4 == FUZZY',FUZZY4 == FUZZY,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('hash (FUZZY) ',hash (FUZZY),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto

print ('hash (FUZZY1) ',hash (FUZZY1),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto

print ('hash (FUZZY2) ',hash (FUZZY2),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto

print ('hash (FUZZY3) ',hash (FUZZY3),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto

print ('hash (FUZZY4) ',hash (FUZZY4),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto

print ('"{0}".format (FUZZY) ',"{0}".format (FUZZY),'\n') # presenta la cadena formateada y su valor 

print ('"{0}".format (FUZZY1) ',"{0}".format (FUZZY1),'\n') # presenta la cadena formateada y su valor

print ('"{0}".format (FUZZY2) ',"{0}".format (FUZZY2),'\n') # presenta la cadena formateada y su valor

print ('"{0}".format (FUZZY3) ',"{0}".format (FUZZY3),'\n') # presenta la cadena formateada y su valor

print ('"{0}".format (FUZZY4) ',"{0}".format (FUZZY4),'\n') # presenta la cadena formateada y su valor

print ('FUZZY.__format__ ("^20") ',FUZZY.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY1.__format__ ("^20") ',FUZZY1.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY2.__format__ ("^20") ',FUZZY2.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY3.__format__ ("^20") ',FUZZY3.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY4.__format__ ("^20") ',FUZZY4.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY.conjuncion (FUZZY1,FUZZY2,FUZZY3,FUZZY4) ',FUZZY.conjuncion (FUZZY1,FUZZY2,FUZZY3,FUZZY4),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('FUZZY1.conjuncion (FUZZY,FUZZY2,FUZZY3,FUZZY4) ',FUZZY1.conjuncion (FUZZY,FUZZY1,FUZZY3,FUZZY4),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('FUZZY2.conjuncion (FUZZY,FUZZY1,FUZZY3,FUZZY4) ',FUZZY2.conjuncion (FUZZY,FUZZY1,FUZZY3,FUZZY4),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('FUZZY3.conjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY4) ',FUZZY3.conjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY4),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('FUZZY4.conjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY3) ',FUZZY4.conjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY3),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('FUZZY.disjuncion (FUZZY1,FUZZY2,FUZZY3,FUZZY4) ',FUZZY.disjuncion (FUZZY1,FUZZY2,FUZZY3,FUZZY4),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('FUZZY1.disjuncion (FUZZY,FUZZY2,FUZZY3,FUZZY4) ',FUZZY1.disjuncion (FUZZY,FUZZY1,FUZZY3,FUZZY4),'\n') # presenta el valor maximo , comparando la lista de objetos

print ('FUZZY2.disjuncion (FUZZY,FUZZY1,FUZZY3,FUZZY4) ',FUZZY2.disjuncion (FUZZY,FUZZY1,FUZZY3,FUZZY4),'\n') # presenta el valor maximo , comparando la lista de objetos

print ('FUZZY3.disjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY4) ',FUZZY3.disjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY4),'\n') # presenta el valor maximo , comparando la lista de objetos

print ('FUZZY4.disjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY3) ',FUZZY4.disjuncion (FUZZY,FUZZY1,FUZZY2,FUZZY3),'\n') # presenta el valor maximo , comparando la lista de objetos

print ('funciones conjuncion (*DIFUSAS) y disjuncion (*DIFUSAS) \n')

def conjuncion (*DIFUSAS) : # definicion del metodo , para comparar los valores de multiples objetos de logicaDIFUSA
	return logicaDIFUSAalternativa (min (DIFUSAS)) # devuelve el valor minimo de la lista de valores en punto flotante

def disjuncion (*DIFUSAS) : # definicion del metodo , para comparar los valores de multiples objetos de logicaDIFUSA
	return logicaDIFUSAalternativa (max (DIFUSAS)) # devuelve el valor maximo de la lista de valores en punto flotante

print ('crear la clase logicaDIFUSAalternativa con herencia de float ; class logicaDIFUSAalternativa (float) : \n')

class logicaDIFUSAalternativa (float) : # definicion de la clase -hereda de float
	def __new__ (cls,valor=0.0) : # metodo especial -de clase- , creacion del objeto sin inicializar
		
		return super().__new__ (cls,valor if 0.0 <= valor <= 1.0 else 0.0) # inicializa el objeto con los valores de la clase padre -dentro de los valores indicados , 0.0 al 1.0-
	
	def __invert__ (self) : # metodo especial - ~ - , invierte el valor binario
		return logicaDIFUSAalternativa (1.0 - float (self)) # devuelve el resultado de la operacion

	def __and__ (self,otro) : # metodo especial - & and binario- , comparacion
		return logicaDIFUSAalternativa (min (self,otro)) # devuelve el valor minimo de los dos objetos comparados
	
	def __iand__ (self,otro) :  # metodo especial -&= and binario incremental- , comparacion
		return logicaDIFUSAalternativa (min (self,otro)) # devuelve el valor minimo de los dos objetos comparados
	
	def __or__ (self,otro) :  # metodo especial - | or binario- , comparacion
		return logicaDIFUSAalternativa (max (self,otro)) # devuelve el valor maximo de los dos objetos comparados
	
	def __ior__ (self,otro) : # metodo especial - |= or binario incremental- , comparacion
		return logicaDIFUSAalternativa (max (self,otro)) # devuelve el valor maximo de los dos objetos comparados
	
	def __repr__ (self) : # metodo especial -repr- , devuelve una cadena que se puede evaluar por eval
		return ('{0} ({1})'.format (self.__class__.__name__,super ().__repr__ ())) # devuelve una cadena formateada con el nombre de la clase y el valor float en formato cadena
	
	def __bool__ (self) : # metodo especial - bool - , comparacion devuelve True o False
		return self > 0.5 # devuelve True si el valor del atributo  es mayor al indicado , lo contrario False
	
	def __int__ (self) : # metodo especial -int- , devuelve el valor entero
		return round (self) # devuelve el valor redondeado a entero mas cercano al valor del atributo 

	def __add__ (self,otro) : # metodo especial - & and binario- , comparacion
		raise NotImplementedError () # lanza la excepcion indicada
	
	def __iadd__ (self,otro) :  # metodo especial -&= and binario incremental- , comparacion
		raise NotImplementedError () # lanza la excepcion indicada

	def __radd__ (self,otro) : # metodo especial - & and binario- , comparacion -valores invertidos-
		raise NotImplementedError () # lanza la excepcion indicada

	@staticmethod # decorador  funcion staticmethod -modifica el metodo inferior con las propiedades de la funcion staticmethod-
	def __and__ (self,otro) : # metodo especial - & and binario- , comparacion
		raise TypeError ('tipo de operacion NO soportado para + : ' '"{0}" and "{1}"'.format (self.__class__.__name__,otro.__class__.__name__)) # lanza la excepcion indicada con el mensaje de la cadena formateada
	
	def __neg__ (self) : # metodo especial - signo negativo - , devuelve el valor con signo negativo
		raise TypeError ('tipo de operacion NO soportado para unitarios - : "{0}" '.format (self.__class__.__name__)) # lanza la excepcion indicada con el mensaje de la cadena formateada
	
	def __eq__ (self,otro) : # metodo especial -==- , comparacion
		return NotImplemented # lanza la excepcion indicada
	
	##############################################################################################################
	# generador metodo especial unitario :
	
	for nombre,operador in (('__neg__','-'),('__index__','index()')) : # iterador , bucle for in , pasa las tuplas y las desempaqueta asignandolas a las variables nombre y operador
		mensaje = ("tipo operador mal para unitario {0} : '{{self}}'".format (operador)) # cadena formateada con el valor del operador
		exec ('def {0} (self) : raise TypeError ("{1}".format(self=self.__class__.__name__))'.format (nombre,mensaje)) # exec ejecuta la sentencia en formato cadena formateada

	##############################################################################################################
	# generador metodos numericos y binarios
	
	tuplaOperadores = (('__xor__','^'),('__ixor__','^='),('__add__','+'),('__iadd__','+='),('__radd__','+'),('__sub__','-'),('__isub__','-='),('__rsub__','-'),('__mul__','*'),('__imul__','*='),('__rmul__','*'),('__pow__','**'),('__ipow__','**='),('__rpow__','**'),('__floordiv__','//'),('__ifloordiv__','//='),('__rfloordiv__','//'),('__truediv__','/'),('__itruediv__','/='),('__rtruediv__','/'),('__divmod__','divmod()'),('__rdivmod__','divmod()'),('__mod__','%'),('__imod__','%='),('__rmod__','%'),('__lshift__','<<'),('__ilshift__','<<='),('__rlshift__','<<'),('__rshift__','>>'),('__irshift__','>>='),('__rrshift__','>>')) # tupla con tuplas de dos elementos compuesto del nombre del metodo y su operador
	
	for nombreOperador,OPERADOR in tuplaOperadores : # iterador , bucle for in , pasa las tuplas y las desempaqueta asignandolas a las variables nombreOperador y OPERADOR
		MENSAJE = ("tipo operador mal para  {0} : '{{self}}' {{join}} {{args}}".format (OPERADOR)) # cadena formateada con el valor del operador
		exec ('def {0} (self,*args) : \n'
				'\ttypes = [arg.__class__.__name__ for arg in args]\n'
				'\traise TypeError ("{1}".format(self=self.__class__.__name__,join=(" y" if len (args) == 1 else ","),args=", ".join (types)))'.format (nombreOperador,MENSAJE)) # exec ejecuta las sentencias en formato cadena formateada

print ('instanciar la clase logicaDIFUSAalternativa : \n')

print ('FUZZYalternativo = logicaDIFUSAalternativa () \n')

FUZZYalternativo = logicaDIFUSAalternativa () # crea el objeto con el valor por defecto

print ('FUZZY1alternativo = logicaDIFUSAalternativa (0.256) \n')

FUZZY1alternativo = logicaDIFUSAalternativa (0.256) # crea el objeto con el valor indicado

print ('FUZZY2alternativo = logicaDIFUSAalternativa (0.568) \n')

FUZZY2alternativo = logicaDIFUSAalternativa (0.568) # crea el objeto con el valor indicado

print ('FUZZY3alternativo = logicaDIFUSAalternativa (0.721) \n')

FUZZY3alternativo = logicaDIFUSAalternativa (0.721) # crea el objeto con el valor indicado

print ('FUZZY4alternativo = logicaDIFUSAalternativa (1.0) \n')

FUZZY4alternativo = logicaDIFUSAalternativa (1.0) # crea el objeto con el valor indicado

print ('~FUZZYalternativo ',~FUZZYalternativo,'\n') # presenta el valor inverso

print ('~FUZZY1alternativo ',~FUZZY1alternativo,'\n') # presenta el valor inverso

print ('~FUZZY2alternativo ',~FUZZY2alternativo,'\n') # presenta el valor inverso

print ('~FUZZY3alternativo ',~FUZZY3alternativo,'\n') # presenta el valor inverso

print ('~FUZZY4alternativo ',~FUZZY4alternativo,'\n') # presenta el valor inverso

print ('FUZZYalternativo and FUZZY1alternativo ',FUZZYalternativo and FUZZY1alternativo,'\n') # presenta el valor minimo 

print ('FUZZY1alternativo and FUZZY2alternativo ',FUZZY1alternativo and FUZZY2alternativo,'\n') # presenta el valor minimo

print ('FUZZY2alternativo and FUZZY3alternativo ',FUZZY2alternativo and FUZZY3alternativo,'\n') # presenta el valor minimo

print ('FUZZY3alternativo and FUZZY4alternativo ',FUZZY3alternativo and FUZZY4alternativo,'\n') # presenta el valor minimo

print ('FUZZY4alternativo and FUZZYalternativo ',FUZZY4alternativo and FUZZYalternativo,'\n') # presenta el valor minimo

print ('FUZZYalternativo &= FUZZY1alternativo \n') 

FUZZYalternativo &= FUZZY1alternativo # asigna el valor minimo al objeto

print ('FUZZYalternativo ',FUZZYalternativo,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY1alternativo &= FUZZY2alternativo \n') 

FUZZY1alternativo &= FUZZY2alternativo # asigna el valor minimo al objeto

print ('FUZZY1alternativo ',FUZZY1alternativo,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY2alternativo &= FUZZY3alternativo \n')

FUZZY2alternativo &= FUZZY3alternativo # asigna el valor minimo al objeto

print ('FUZZY2alternativo ',FUZZY2alternativo,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY3alternativo &= FUZZY4alternativo \n')

FUZZY3alternativo &= FUZZY4alternativo # asigna el valor minimo al objeto

print ('FUZZY3alternativo ',FUZZY3alternativo,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZY4alternativo &= FUZZYalternativo \n')

FUZZY4alternativo &= FUZZYalternativo # asigna el valor minimo al objeto

print ('FUZZY4alternativo ',FUZZY4alternativo,'\n') # presenta el objeto con el valor minimo asignado

print ('FUZZYalternativo | FUZZY1alternativo ',FUZZYalternativo | FUZZY1alternativo,'\n') # presenta el valor maximo 

print ('FUZZY1alternativo | FUZZY2alternativo ',FUZZY1alternativo | FUZZY2alternativo,'\n') # presenta el valor maximo

print ('FUZZY2alternativo | FUZZY3alternativo',FUZZY2alternativo | FUZZY3alternativo,'\n') # presenta el valor maximo

print ('FUZZY3alternativo | FUZZY4alternativo',FUZZY3alternativo | FUZZY4alternativo,'\n') # presenta el valor maximo

print ('FUZZY4alternativo | FUZZYalternativo',FUZZY4alternativo | FUZZYalternativo,'\n') # presenta el valor maximo

print ('FUZZYalternativo |= FUZZY1alternativo \n') 

FUZZYalternativo |= FUZZY1alternativo # asigna el valor maximo al objeto

print ('FUZZYalternativo ',FUZZYalternativo,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY1alternativo |= FUZZY2alternativo \n') 

FUZZY1alternativo |= FUZZY2alternativo # asigna el valor maximo al objeto

print ('FUZZY1alternativo ',FUZZY1alternativo,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY2alternativo |= FUZZY3alternativo \n')

FUZZY2alternativo |= FUZZY3alternativo # asigna el valor maximo al objeto

print ('FUZZY2alternativo ',FUZZY2alternativo,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY3alternativo |= FUZZY4alternativo \n')

FUZZY3alternativo |= FUZZY4alternativo # asigna el valor maximo al objeto

print ('FUZZY3alternativo ',FUZZY3alternativo,'\n') # presenta el objeto con el valor maximo asignado

print ('FUZZY4alternativo |= FUZZYalternativo \n')

FUZZY4alternativo |= FUZZYalternativo # asigna el valor maximo al objeto

print ('FUZZY4alternativo ',FUZZY4alternativo,'\n') # presenta el objeto con el valor maximo asignado

print ('repr (FUZZYalternativo) ',repr (FUZZYalternativo),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZYalternativo)) ',eval (repr (FUZZYalternativo)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY1alternativo) ',repr (FUZZY1alternativo),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY1alternativo)) ',eval (repr (FUZZY1alternativo)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY2alternativo) ',repr (FUZZY2alternativo),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY2alternativo)) ',eval (repr (FUZZY2alternativo)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY3alternativo) ',repr (FUZZY3alternativo),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY3alternativo)) ',eval (repr (FUZZY3alternativo)),'\n') # presenta el valor de la cadena evaluada

print ('repr (FUZZY4alternativo) ',repr (FUZZY4alternativo),'\n') # presenta una cadena que puede evaluar eval 

print ('eval (repr (FUZZY4alternativo)) ',eval (repr (FUZZY4alternativo)),'\n') # presenta el valor de la cadena evaluada

print ('str (FUZZYalternativo) ',str (FUZZYalternativo),'\n') # presenta el valor en formato cadena

print ('str (FUZZY1alternativo) ',str (FUZZY1alternativo),'\n') # presenta el valor en formato cadena

print ('str (FUZZY2alternativo) ',str (FUZZY2alternativo),'\n') # presenta el valor en formato cadena

print ('str (FUZZY3alternativo) ',str (FUZZY3alternativo),'\n') # presenta el valor en formato cadena

print ('str (FUZZY4alternativo) ',str (FUZZY4alternativo),'\n') # presenta el valor en formato cadena

print ('bool (FUZZYalternativo) ',bool (FUZZYalternativo),'\n') # presenta True o False dependiendo del valor comparado con el de bool 

print ('bool (FUZZY1alternativo) ',bool (FUZZY1alternativo),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('bool (FUZZY2alternativo) ',bool (FUZZY2alternativo),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('bool (FUZZY3alternativo) ',bool (FUZZY3alternativo),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('bool (FUZZY4alternativo) ',bool (FUZZY4alternativo),'\n') # presenta True o False dependiendo del valor comparado con el de bool

print ('int (FUZZYalternativo) ',int (FUZZYalternativo),'\n') # presenta el valor redondeado  en formato entero , sin decimales

print ('int (FUZZY1alternativo) ',int (FUZZY1alternativo),'\n') # presenta el valor redondeado en formato entero , sin decimales

print ('int (FUZZY2alternativo) ',int (FUZZY2alternativo),'\n') # presenta el valor redondeado  en formato entero , sin decimales

print ('int (FUZZY3alternativo) ',int (FUZZY3alternativo),'\n') # presenta el valor redondeado  en formato entero , sin decimales

print ('int (FUZZY4alternativo) ',int (FUZZY4alternativo),'\n') # presenta el valor  redondeado en formato entero , sin decimales

print ('float (FUZZYalternativo) ',float (FUZZYalternativo),'\n') # presenta el valor del objeto

print ('float (FUZZY1alternativo) ',float (FUZZY1alternativo),'\n') # presenta el valor del objeto

print ('float (FUZZY2alternativo) ',float (FUZZY2alternativo),'\n') # presenta el valor del objeto

print ('float (FUZZY3alternativo) ',float (FUZZY3alternativo),'\n') # presenta el valor del objeto

print ('float (FUZZY4alternativo) ',float (FUZZY4alternativo),'\n') # presenta el valor del objeto

print ('FUZZYalternativo < FUZZY1alternativo ',FUZZYalternativo < FUZZY1alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY1alternativo < FUZZY2alternativo ',FUZZY1alternativo < FUZZY2alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY2alternativo < FUZZY3alternativo',FUZZY2alternativo < FUZZY3alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY3alternativo < FUZZY4alternativo',FUZZY3alternativo < FUZZY4alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY4alternativo < FUZZYalternativo',FUZZY4alternativo < FUZZYalternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZYalternativo <= FUZZY1alternativo ',FUZZYalternativo <= FUZZY1alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY1alternativo <= FUZZY2alternativo ',FUZZY1alternativo <= FUZZY2alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY2alternativo <= FUZZY3alternativo',FUZZY2alternativo <= FUZZY3alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY3alternativo <= FUZZY4alternativo',FUZZY3alternativo <= FUZZY4alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY4alternativo <= FUZZYalternativo',FUZZY4alternativo <= FUZZYalternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZYalternativo == FUZZY1alternativo ',FUZZYalternativo == FUZZY1alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY1alternativo == FUZZY2alternativo ',FUZZY1alternativo == FUZZY2alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY2alternativo == FUZZY3alternativo',FUZZY2alternativo == FUZZY3alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY3alternativo == FUZZY4alternativo',FUZZY3alternativo == FUZZY4alternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

print ('FUZZY4alternativo == FUZZYalternativo',FUZZY4alternativo == FUZZYalternativo,'\n') # presenta True si coincide la comparacion , lo contrario False 

try : # control de excepcion
	print ('hash (FUZZYalternativo) \n')
	print (hash (FUZZYalternativo),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('hash (FUZZY1alternativo) \n')
	print (hash (FUZZY1alternativo),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('hash (FUZZY2alternativo) \n')
	print (hash (FUZZY2alternativo),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('hash (FUZZY3alternativo) \n')
	print (hash (FUZZY3alternativo),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('hash (FUZZY4alternativo) \n')
	print (hash (FUZZY4alternativo),'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

print ('"{0}".format (FUZZYalternativo) ',"{0}".format (FUZZYalternativo),'\n') # presenta la cadena formateada y su valor 

print ('"{0}".format (FUZZY1alternativo) ',"{0}".format (FUZZY1alternativo),'\n') # presenta la cadena formateada y su valor

print ('"{0}".format (FUZZY2alternativo) ',"{0}".format (FUZZY2alternativo),'\n') # presenta la cadena formateada y su valor

print ('"{0}".format (FUZZY3alternativo) ',"{0}".format (FUZZY3alternativo),'\n') # presenta la cadena formateada y su valor

print ('"{0}".format (FUZZY4alternativo) ',"{0}".format (FUZZY4alternativo),'\n') # presenta la cadena formateada y su valor

print ('FUZZYalternativo.__format__ ("^20") ',FUZZYalternativo.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY1alternativo.__format__ ("^20") ',FUZZY1alternativo.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY2alternativo.__format__ ("^20") ',FUZZY2alternativo.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY3alternativo.__format__ ("^20") ',FUZZY3alternativo.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('FUZZY4alternativo.__format__ ("^20") ',FUZZY4alternativo.__format__ ("^20"),'\n') # presenta la cadena formateada en el formato especificado

print ('conjuncion (FUZZYalternativo,FUZZY1alternativo,FUZZY2alternativo,FUZZY3alternativo,FUZZY4alternativo) ',conjuncion (FUZZYalternativo,FUZZY1alternativo,FUZZY2alternativo,FUZZY3alternativo,FUZZY4alternativo),'\n') # presenta el valor minimo , comparando la lista de objetos

print ('disjuncion (FUZZYalternativo,FUZZY1alternativo,FUZZY2alternativo,FUZZY3alternativo,FUZZY4alternativo) ',disjuncion (FUZZYalternativo,FUZZY1alternativo,FUZZY2alternativo,FUZZY3alternativo,FUZZY4alternativo),'\n') # presenta el valor minimo , comparando la lista de objetos

try : # control de excepcion
	print ('FUZZYalternativo + FUZZY1alternativo \n')
	print (FUZZYalternativo + FUZZY1alternativo,'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('FUZZYalternativo - FUZZY1alternativo \n')
	print (FUZZYalternativo - FUZZY1alternativo,'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('FUZZYalternativo / FUZZY1alternativo \n')
	print (FUZZYalternativo / FUZZY1alternativo,'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('FUZZYalternativo // FUZZY1alternativo \n')
	print (FUZZYalternativo // FUZZY1alternativo,'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('FUZZYalternativo * FUZZY1alternativo \n')
	print (FUZZYalternativo * FUZZY1alternativo,'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

try : # control de excepcion
	print ('FUZZYalternativo ** FUZZY1alternativo \n')
	print (FUZZYalternativo ** FUZZY1alternativo,'\n') # presenta el valor hash del identificador -direccion de memoria- del objeto -lanza excepcion , metodo no permitido en la clase-
except TypeError as ERROR : # tipo de excepcion , pasa la salida a ERROR
	print ('METODO NO PERMITIDO POR LA CLASE\n') # presenta la cadena
	print ('--- {0} ---\n'.format (ERROR)) # presenta la salida de error en una cadena formateada

print ('crear clase con metodos especiales coleccion ; class metodosEspecialesColeccion (object) : \n')

class metodosEspecialesColeccion (object) : # definicion de la clase
	def __init__ (self,*tupla) : # definicion del metodo , inicializa los parametros de la clase 
		self.tupla = tupla # asigna el valor al atributo

	def __contains__ (self,elemento) : # definicion del metodo especial -elemento in objeto- , devuelve True si el elemento esta en el objeto
		return elemento in self.tupla # devuelve True si el elemento esta en el atributo , lo contrario False

	def __delitem__ (self,posicion) : # definicion del metodo especial -del objeto [posicion]- , elimina el elemento de la posicion indicada
		convertirAlista = list (self.tupla) # convierte la tupla en una lista -modificable-
		del convertirAlista [posicion] # elimina el elemento de la posicion indicada
		self.tupla = tuple (convertirAlista) # convierte la lista en tupla -no modificable- y la asigna
	
	def __getitem__ (self,posicion) : # definicion del metodo especial -objeto [posicion]- , devuelve el elemento de la posicion indicada
		return self.tupla [posicion] # devuelve el elemento de la posicion indicada
	
	def __iter__ (self) : # definicion del metodo especial -for x in objeto- , itera , bucle for in 
		return iter (self.tupla)  # devuelve un iterador con los elementos de la iteracion del objeto
	
	def __len__ (self) : # definicion del metodo especial -len (objeto)- , devuelve el numero de elementos del objeto
		return len (self.tupla) # devuelve el numero de elementos del objeto
	
	def __reversed__ (self) : # definicion del metodo especial -reversed (objeto)- , devuelve un iterador con la secuencia invertida
		return reversed (self.tupla) #  devuelve una lista con los elementos de la iteracion del objeto invertidos
	
	def __setitem__ (self,posicion,valor) : # definicion del metodo especial -objeto [posicion] = valor- , añade en la posicion el valor indicado al objeto
		convertirAlista = list (self.tupla) # convierte la tupla en una lista -modificable-
		convertirAlista [posicion] = valor # añade en la posicion el valor indicado al objeto
		self.tupla = tuple (convertirAlista) # convierte la lista en tupla -no modificable- y la asigna

	def Tupla (self) : # metodo propio 
		return self.tupla # devuelve la tupla del objeto
	

print ('instanciar la clase metodosEspecialesColeccion ; metodosColeccion = metodosEspecialesColeccion ("a",0,1,2,3,4,"cinco","penultimo",.01,"ultimo") \n')

metodosColeccion = metodosEspecialesColeccion ("a",0,1,2,3,4,"cinco","penultimo",.01,"ultimo") # crear un  objeto con los argumentos indicados

print ('pertenencia de un valor en el objeto metodosColeccion ; 1 in metodosColeccion \n')

print (1 in metodosColeccion,'\n') # devuelve True si el valor pertenece al objeto , lo contrario False

print ('eliminar un elemento de la posicion indicada ; del metodosColeccion [2] \n')

del metodosColeccion [2] # elimina el valor de la posicion indicada en el objeto

print ('devolver el elemento de la posicion indicada ; metodosColeccion [2] ',metodosColeccion [2],'\n') # presenta el valor de la posicion indicada del objeto

print ('iterar el objeto ; for elemento in metodosColeccion \n')

for elemento in metodosColeccion : # iterador , bucle for in , itera el objeto
	print (elemento,end=' - ') # presenta el valor de la variable -todas en la misma linea-
else : # cunado finalice el iterador
	print ('\n') # salto de linea
	print ('+++ fin de la iteracion +++\n') # presenta la cadena

print ('numero de elementos del objeto ; len (metodosColeccion) ',len (metodosColeccion),'\n') # presenta el numero de elementos del objeto

print ('iterar el objeto invertido ; for elemento in reversed (metodosColeccion) \n')

for elemento in reversed (metodosColeccion) : # iterador , bucle for in , itera el objeto -invierte el contenido del objeto-
	print (elemento,end=' - ') # presenta el valor de la variable -todas en la misma linea-
else : # cunado finalice el iterador
	print ('\n') # salto de linea
	print ('+++ fin de la iteracion +++\n') # presenta la cadena

print ('añadir un valor al objeto ; metodosColeccion [-1] = "valor añadido" \n')

metodosColeccion [-1] = "valor añadido" # añade el valor al objeto

print (metodosColeccion.Tupla(),'\n') # presenta el contenido del objeto

print ('importar el modulo pickle \n')

import pickle # importa el modulo indicado

print ('crear las clases propias de excepcion ; \n')

print ('class errorImagen (Exception) : pass \n')

class errorImagen (Exception) : # definicion de la clase , hereda de Exception
	pass # funcion de relleno -no hace nada-

print ('class errorCoordinacion (errorImagen) : pass \n')

class errorCoordinacion (errorImagen) : # definicion de la clase , hereda de errorImagen
	pass # funcion de relleno -no hace nada-

print ('class errorCarga (errorImagen) : pass \n')

class errorCarga (errorImagen) : # definicion de la clase , hereda de errorImagen
	pass # funcion de relleno -no hace nada-

print ('class errorGuardar (errorImagen) : pass \n')

class errorGuardar (errorImagen) : # definicion de la clase , hereda de errorImagen
	pass # funcion de relleno -no hace nada-

print ('class errorExportar (errorImagen) : pass \n')

class errorExportar (errorImagen) : # definicion de la clase , hereda de errorImagen
	pass # funcion de relleno -no hace nada-

print ('class errorNOfichero (errorImagen) : pass \n')

class errorNOfichero (errorImagen) : # definicion de la clase , hereda de errorImagen
	pass # funcion de relleno -no hace nada-

print ('crear la clase imagen ; class imagen (object) : \n')

class imagen (object) : # definicion de la clase
	def __init__ (self,ancho,alto,nombreFichero='',fondo='#FFFFFF') : # definicion del metodo , inicializa los parametros de la clase
		self.nombreFichero = nombreFichero # asigna el valor al atributo
		self.__fondo = fondo # asigna el valor al atributo privado
		self.__datos = {} # asigna el valor al atributo privado -diccionario coordenadas-
		self.__ancho = ancho # asigna el valor al atributo privado
		self.__alto = alto # asigna el valor al atributo privado
		self.__colores = {self.__fondo} # asigna el valor al atributo privado -atributo privado-
	
	@property # decorador , funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def fondo (self) : #  definicion del metodo 
		return self.__fondo # devuelve el valor del atributo privado
	
	@property # decorador , funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def ancho (self) : #  definicion del metodo 
		return self.__ancho # devuelve el valor del atributo privado
	
	@property # decorador , funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def alto (self) : #  definicion del metodo 
		return self.__alto # devuelve el valor del atributo privado
	
	@property # decorador , funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def colores (self) : #  definicion del metodo 
		return set (self.__colores) # devuelve el valor del atributo privado en formato set -contenedor de elementos no repetidos-
	
	def __getitem__ (self,coordenadas) : # metodo especial , devuelve el elemento de la posicion o clave indicada
		assert len (coordenadas) == 2,'tiene que ser una tupla de dos elementos -numeros-' # regla de excepcion , si no se cumple lanza excepcion con el mensaje indicado
		if (not (0 <= coordenadas [0] < self.ancho) or not (0 <= coordenadas [1] < self.alto)) : # condicion , si se cumple una de las condiciones
			raise errorCoordinacion (str (coordenadas)) # lanza la excepcion propia indicada presentando las coordenadas erroneas -excepcion propia-
		return self.__datos.get (tuple (coordenadas),self.__fondo) # devuelve los valores de las coordenadas y atributo privado __fondo

	def __setitem__ (self,coordenadas,color) : # metodo especial , comprueba las coordenadas y color y las añade al objeto
		assert len (coordenadas) == 2,'coordenadas tiene que ser una tupla de dos elementos -numeros-' # regla de excepcion , si no se cumple lanza excepcion con el mensaje indicado
		if (not (0 <= coordenadas [0] < self.ancho) or not (0 <= coordenadas [1] < self.alto)) : # condicion , si se cumple una de las condiciones
			raise errorCoordinacion (str (coordenadas)) # lanza la excepcion indicada con las coordenadas que fallan en formato texto  -excepcion propia-
		if color == self.__fondo : # condicion , si coinciden los valores
			self.__datos.pop (tuple (coordenadas),None) # elimina las coordenadas del diccionario
		else : # si no coinciden con el color del fondo
			self.__datos [tuple (coordenadas)] = color # añade al diccionario las coordenadas como clave y el color como valor
			self.__colores.add (color) # añade el color al diccionario como valor de la clave
			
	def __delitem__ (self,coordenadas) : # metodo especial , eliminar el color de unas coordenadas
		assert len (coordenadas) == 2,'coordenadas tiene que ser una tupla de dos elementos -numeros-' # regla de excepcion , si no se cumple lanza excepcion con el mensaje indicado
		if (not (0 <= coordenadas [0] < self.ancho) or not (0 <= coordenadas [1] < self.alto)) : # condicion , si se cumple una de las condiciones
			raise errorCoordinacion (str (coordenadas)) # lanza la excepcion indicada con las coordenadas que fallan en formato texto -excepcion propia-
		self.__datos.pop (tuple (coordenadas),None) # elimina las coordenadas del diccionario y su valor -color-
		
	def guardar (self,nombreFichero=None) : # definicion del metodo , argumento por defecto
		if nombreFichero is not None : # condicion , si nombreFichero es distinto al argumento por defecto -None-
			self.nombreFichero = nombreFichero # asigna el valor al atributo -nombre del fichero-
		if not self.nombreFichero : # condicion , si el valor no es True -contiene una cadena vacia-
			raise errorNOfichero () # lanza excepcion propia
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones 
			datosAserializar = [self.ancho,self.alto,self.__fondo,self.__datos] # lista de datos a serializar
			cabeceraFichero = open ('./Escritorio/{0}'.format (self.nombreFichero),'wb') # objeto fichero , abre el fichero en la ruta indicada en modo escritura binaria -wb-
			pickle.dump (datosAserializar,cabeceraFichero,pickle.HIGHEST_PROTOCOL) # añade los datos serializados al objeto fichero indicado con el protocolo pickle indicado
		except (EnvironmentError,pickle.picklingError) as error : # tipo de excepcion -dos excepciones- , pasa la salida a error
			raise errorGuardar (str (error)) # lanza excepcion propia con el mensaje de salida de error
		finally : # lanze o no una excepcion -ejecuta siempre el codigo-
			if cabeceraFichero is not None : # condicion , si no es el valor por defecto -None-
				cabeceraFichero.close () # cierra el fichero del objeto
			
	def cargar (self,nombreFichero=None) : # definicion del metodo , argumento por defecto
		if nombreFichero is not None : # condicion , si nombreFichero es distinto al argumento por defecto -None-
			self.nombreFichero = nombreFichero # asigna el valor al atributo -nombre del fichero-
		if not self.nombreFichero : # condicion , si el valor no es True -contiene una cadena vacia-
			raise errorNOfichero () # lanza excepcion propia
		cabeceraFichero = None # asigna el valor al objeto fichero
		try : # control de excepciones 
			cabeceraFichero = open ('./Escritorio/{0}'.format (self.nombreFichero),'rb') # objeto fichero , abre el fichero en la ruta indicada en modo solo lectura binaria -rb-
			cargaDatosSerializados = pickle.load (cabeceraFichero) # carga los datos serializados del objeto fichero
			(self.__ancho,self.__alto,self.__fondo,self.__datos) = cargaDatosSerializados # desempaqueta los datos serializados y los asigna a los atributos correspondientes
			self.__colores = (set (self.__datos.values ()) | {self.__fondo}) # asigna los colores del diccionario o el color por defecto si el diccionario esta vacio 
		except (EnvironmentError,pickle.picklingError) as error : # tipo de excepcion -dos excepciones- , pasa la salida a error
			raise errorCarga (str (error)) # lanza excepcion propia con el mensaje de salida de error
		finally : # lanze o no una excepcion -ejecuta siempre el codigo-
			if cabeceraFichero is not None : # condicion , si no es el valor por defecto -None-
				cabeceraFichero.close () # cierra el fichero del objeto
	
print ('crear imagen : \n')

colorBorde = '#FF0000' # color rojo

colorCuadrado = '#0000FF' # color azul

ancho = 240 # ancho en pixels

alto = 60 # alto en pixels

mediaX = ancho // 2 # asigna el resultado de la division -valor entero-

mediaY = alto // 2 # asigna el resultado de la division -valor entero-

print ('crear objeto imagen ; IMAGEN = imagen (ancho,alto,"ojoCuadrado.img") \n')

IMAGEN = imagen (ancho,alto,"ojoCuadrado.img") # objeto imagen

print ('añadir pixels -x,y- y color al objeto \n')

for x in range (ancho) : # iterador , pasa la lista de numeros a x -numero de pixels-
	for y in range (alto) : # iterador , pasa la lista de numeros a y -numero de pixels- 
		if x < 5 or x >= ancho - 5 or y < 5 or y >= ancho - 5 : # condicion , si se cumple una de las condiciones
			IMAGEN [x,y] = colorBorde # añade las coordenadas y color al objeto -color del borde-
		elif mediaX - 20 < x < mediaX + 20 and mediaY - 20 < y < mediaY + 20 : # condicion , si se cumplen las dos condiciones
			IMAGEN [x,y] = colorCuadrado # añade las coordenadas y color al objeto -color del cuadrado-

print ('salvar imagen creada con el metodo guardar ; IMAGEN.guardar () \n')

IMAGEN.guardar () # guarda el objeto y  sus valores con el nombre del fichero indicado 

print ('cargar un fichero serializado ; cargarImagen = imagen (None,None,"ojoCuadrado.img") \n')

cargarImagen = imagen (None,None,"ojoCuadrado.img") # crea el objeto

print ('cargar fichero ; cargarImagen.cargar () \n')

cargarImagen.cargar () # carga el fichero indicado en el objeto

print ('crear la clase listaOrdenada ; class listaOrdenada (object) : \n')

class listaOrdenada (object) : # definicion de la clase
	def __init__ (self,secuencia=None,clave=None) : # definicion del metodo , inicializa los parametros de la clase -argumentos por defecto-
		__identidad = lambda x : x # funcion lambda -funcion sin nombre-
		self.__clave = clave or __identidad # asigna el valor -si no es None-  o la funcion al atributo privado
		assert hasattr (self.__clave,'__call__') # regla excepcion , si no se cumple lanza excepcion -si __call__ no es un metodo del valor del atributo devuelve False-
		if secuencia is None : # condicion , si el valor es el por defecto -None-
			self.__lista = [] # asigna una lista vacia al atributo privado
		elif (isinstance (secuencia,listaOrdenada) and secuencia.clave == self.__clave) : # condicion , si las dos condiciones se cumplen -pertenencia a la instancia y valor igual-
			self.__lista = secuencia.__lista [ : ] # asigna la lista entera al atributo privado
		else : # si no cumple ambas condiciones
			self.__lista = sorted (list (secuencia),key=self.__clave) # asigna la lista ordenada en funcion de la clave
			
	@property # decorador , funcion property -modifica el metodo inferior con las propiedades de la funcion property-
	def clave (self) : # definicion del metodo 
		return self.__clave # devuelve el valor del atributo privado
	
	def añadir (self,valor) : # definicion del metodo  , añade un elemento a la lista del objeto
		indice = self.__bisectIzquierda (valor) # asigna el resultado del metodo privado con el valor indicado
		if indice == len (self.__lista) : # condicion , si es la ultima posicion de la lista privada
			self.__lista.append (valor) # añade el valor al final de la lista -atributo privado-
		else : # si no es la ultima posicion de la lista 
			self.__lista.insert (indice,valor) # inserta en la posicion indicada el valor en la lista privada
			
	def __bisectIzquierda (self,valor) : # definicion del metodo privado
		clave = self.__clave (valor) # asigna el valor del resultado del atributo privado
		izquierda,derecha = 0,len (self.__lista) # asignacion multiple -izquierda = 0 , derecha = len (self.__lista)-
		while izquierda < derecha : # bucle while , mientras se cumpla la condicion -valor izquierda menor que derecha-
			media = (izquierda + derecha) // 2 # asigna el resultado de la suma de los dos valores dividido entre dos -resultado ; valor truncado sin decimales , entero (int)-
			if self.__clave (self.__lista [media]) < clave : # condicion , si el valor del atributo privado es menor que el de clave
				izquierda = media + 1 # asigna el valor de media mas uno -cuando el valor sea igual o mayor a derecha , se detiene el bucle while-
			else : # si no es menor , lo contrario -mayor o igual-
				derecha = media # asigna el valor de media
		return izquierda # devuelve el resultado del valor izquierda
	
	def eliminar (self,valor) : # definicion del metodo 
		'''-elimina el primer valor repetido encontrado-''' # docstring -documentacion del metodo-
		indice = self.__bisectIzquierda (valor) # asigna el resultado del metodo privado con el valor indicado
		if indice < len (self.__lista) and self.__lista [indice] == valor : # condicion , si la posicion indicada no es la ultima y el valor coincide con la posicion
			del self.__lista [indice] # elimina el valor del indice indicado -posicion-
		else : # si no es el valor o posicion
			raise ValueError ('{0}.eliminar ({1}) : {1} no esta en la lista'.format (self.__class__.__name__,valor)) # lanza la excepcion indicada con la cadena formateada -nombre de la clase y valor-
		
	def eliminarTodos (self,valor) : # definicion del metodo 
		'''-elimina todos los valores repetidos encontrados-''' # docstring -documentacion del metodo-
		contador = 0 # contador valor inicio ; cero
		indice = self.__bisectIzquierda (valor) # asigna el resultado del metodo privado con el valor indicado
		while (indice < len (self.__lista) and self.__lista [indice] == valor) : # bucle while , mientras se cumpla la condicion -si la posicion indicada no es la ultima y el valor coincide con la posicion-
			del self.__lista [indice] # elimina el valor del indice indicado -posicion-
			contador += 1 # asignacion aumentada -suma uno al valor actual-
		return contador # devuelve el numero de elementos repetidos eliminados
	
	def contador (self,valor) : # definicion del metodo 
		'''-devuelve el numero de veces que se repite el valor en la lista-''' # docstring -documentacion del metodo-
		CONTADOR = 0 # contador valor inicio ; cero
		indice = self.__bisectIzquierda (valor) # asigna el resultado del metodo privado con el valor indicado
		while (indice < len (self.__lista) and self.__lista [indice] == valor) : # bucle while , mientras se cumpla la condicion -si la posicion indicada no es la ultima y el valor coincide con la posicion-
			indice += 1 # asignacion aumentada -suma uno al valor actual- , -cuando el valor sea igual o mayor al valor de len (self.__lista) , se detiene el bucle while-
			CONTADOR += 1 # asignacion aumentada -suma uno al valor actual-
		return CONTADOR # devuelve el numero de veces que se repite el valor
	
	def indice (self,valor) : # definicion del metodo
		'''devuelve el indice en el que esta el valor indicado''' # docstring -documentacion del metodo-
		indice = self.__bisectIzquierda (valor) # asigna el resultado del metodo privado con el valor indicado
		if indice < len (self.__lista) and self.__lista [indice] == valor : # condicion , si la posicion indicada no es la ultima y el valor coincide con la posicion
			return indice # devuelve el indice en el que esta el valor indicado
		else : # si no es el valor o posicion
			raise ValueError ('{0}.indice ({1}) : {1} no esta en la lista'.format (self.__class__.__name__,valor)) # lanza la excepcion indicada con la cadena formateada -nombre de la clase y valor-
		
	def __delitem__ (self,indice) : # metodo especial - del objeto [indice]- , elimina un elemento de la lista del objeto
		del self.__lista [indice] # elimina el valor del indice indicado
		
	def __getitem__ (self,indice) : # metodo especial -objeto [indice]- , devuelve el valor del indice indicado del objeto
		return self.__lista [indice] # devuelve el valor del indice indicado
	
	def __setitem__ (self,indice,valor) : # metodo especial -objeto [indice] = valor- , cambia en el indice indicado el valor -lanza excepcion-
		raise TypeError ('use añadir (valor)  para añadir un valor al objeto -NO SE ADMITE : objeto [indice] = valor-') # lanza la excepcion indicada con la cadena
	
	def __iter__ (self) : # metodo especial -iter ()- , devuelve un iterador
		return iter (self.__lista) # devuelve un iterador del atributo privado
	
	def __reversed__ (self) : # metodo especial -reversed (objeto)- , devuelve la lista del atributo privado invertida
		return reversed (self.__lista) # devuelve la lista del atributo privado invertida
	
	def __contains__ (self,valor) : # metodo especial -valor in objeto- , pertenencia in
		indice = self.__bisectIzquierda (valor) # asigna el resultado del metodo privado con el valor indicado
		return (indice < len (self.__lista) and self.__lista [indice] == valor) # devuelve True si se cumplen las dos condiciones , lo contrario False
	
	def limpiar (self) : # definicion del metodo
		'''asigna una lista vacia al atributo privado''' # docstring -documentacion del metodo-
		self.__lista = [] #  asigna una lista vacia al atributo privado
		
	def pop (self,indice=-1) : # definicion del metodo , con valor por defecto
		'''uso de la funcion pop () para eliminar el ultimo elemento o el indicado por el indice''' # docstring -documentacion del metodo-
		return self.__lista.pop (indice) # devuelve el elemento eliminado , uso de la funcion pop () para eliminar un elemento del atributo privado
	
	def __len__ (self) : # metodo especial -len (objeto)- , devuelve el numero de elementos del objeto
		return len (self.__lista) # devuelve el numero de elementos del atributo privado
	
	def __str__ (self) : # metodo especial -str ()- , devuelve la lista en formato cadena
		return str (self.__lista) # devuelve el valor del atributo privado en formato cadena
	
	def copia (self) : # definicion del metodo
		'''devuelve una copia identica al del objeto''' # docstring -documentacion del metodo-
		return listaOrdenada (self,self.__clave) # devuelve una copia identica al del objeto
	
print ('instanciar la clase listaOrdenada ; ordenarLISTA = listaOrdenada ([33,3,14,1,4,2,2,.3,6,10,1,5,33,7,9,9,0]) \n')

ordenarLISTA = listaOrdenada ([33,3,14,1,4,2,2,.3,6,10,1,5,33,7,9,9,0]) # crea el objeto con el argumento indicado

print ('añadir un valor al objeto ; ordenarLISTA.añadir (100) \n')

ordenarLISTA.añadir (100) # añade el valor al objeto

print ('presentar lista en formato cadena ; str (ordenarLISTA) ',str (ordenarLISTA),'\n') # presenta la lista en formato cadena

print ('eliminar el primer elemento repetido encontrado del valor indicado ; ordenarLISTA.eliminar (1) \n')

ordenarLISTA.eliminar (1) # elimina el primer elemento repetido encontrado del valor indicado

print ('lista del objeto ; str (ordenarLISTA) ',str (ordenarLISTA),'\n') # presenta la lista en formato cadena

print ('presenta el numero total de los elementos repetidos encontrados del valor indicado ; ordenarLISTA.eliminarTodos (9) ',ordenarLISTA.eliminarTodos (9),'\n') # presenta el numero total de los elementos eliminados repetidos encontrados del valor indicado

print ('lista del objeto ; str (ordenarLISTA) ',str (ordenarLISTA),'\n') # presenta la lista en formato cadena 

print ('eliminar el primer elemento repetido encontrado del valor indicado ; ordenarLISTA.eliminar (9) \n')

try : # control de excepciones
	ordenarLISTA.eliminar (9) # elimina el primer elemento repetido encontrado del valor indicado
except ValueError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : ',error,'\n') # presenta la salida del error

print ('devolver el numero de veces que se repite el valor indicado en el objeto ; ordenarLISTA.contador (33) ',ordenarLISTA.contador (33),'\n') # presenta el numero de veces que se repite el valor indicado en el objeto

print ('devolver el indice -posicion- en que se encuentra el valor indicado en el objeto ; ordenarLISTA.indice (33) ',ordenarLISTA.indice (33),'\n') # presenta el indice -posicion- en que se encuentra el valor indicado en el objeto 

print ('devolver el indice -posicion- en que se encuentra el valor indicado en el objeto ; ordenarLISTA.indice (9) \n') # presenta el indice -posicion- en que se encuentra el valor indicado en el objeto 

try : # control de excepciones
	ordenarLISTA.indice (9) #  presenta el indice -posicion- en que se encuentra el valor indicado en el objeto 
except ValueError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : ',error,'\n') # presenta la salida del error

print ('devolver el valor de la posicion -indice- indicado del objeto ; ordenarLISTA [12] ',ordenarLISTA [12],'\n') # presenta el valor de la posicion -indice- indicado del objeto

print ('eliminar el valor del indice indicado del objeto ; del ordenarLISTA [0] \n') 

del ordenarLISTA [0] # elimina el valor del indice indicado del objeto

print ('lista del objeto ; str (ordenarLISTA) ',str (ordenarLISTA),'\n') # presenta la lista en formato cadena

print ('cambiar el valor del indice indicado del objeto ; ordenarLISTA [0] = 1000 \n')

try : # control de excepciones
	ordenarLISTA [0] = 1000 #  cambia el valor del indice indicado del objeto 
except TypeError as error : # tipo de excepcion , pasa la salida a error
	print ('ERROR : ',error,'\n') # presenta la salida del error

print ('devolver un iterador del objeto ; for Elemento in ordenarLISTA : \n',)

for Elemento in ordenarLISTA : # iterador , bucle for in , pasa los elementos del iterador a Elemento
	print (Elemento,end=' ') # presenta los valores en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('devolver el contenido del objeto en orden invertido ; reversed (ordenarLISTA) \n')

for EL in reversed (ordenarLISTA) : # iterador , bucle for in , pasa los elementos de la lista invertida a EL
	print (EL,end=' ') # presenta los valores en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('pertenencia de un valor al objeto ; 14 in ordenarLISTA ',14 in ordenarLISTA,'\n') # presenta True si pertenece al objeto , lo contario False

print ('eliminar el valor del indice indicado y devolver el valor eliminado -el ultimo por defecto- ; ordenarLISTA.pop () ',ordenarLISTA.pop (),'\n') # elimina el ultimo elemento por defecto y lo presenta

print ('lista del objeto ; str (ordenarLISTA) ',str (ordenarLISTA),'\n') # presenta la lista en formato cadena

print ('numero de elementos del objeto ; len (ordenarLISTA) ',len (ordenarLISTA),'\n') # presenta el numero de elementos del objeto

print ('devolver una copia superficial del objeto ; ordenarLISTA.copia () ',ordenarLISTA.copia (),'\n') # presenta una copia superficial del objeto

print ('limpiar el objeto -eliminar el contenido- ; ordenarLISTA.limpiar () \n')

ordenarLISTA.limpiar () # eliminar el contenido del objeto

print ('lista del objeto ; str (ordenarLISTA) ',str (ordenarLISTA),'\n') # presenta la lista en formato cadena

print ('crear clase diccionarioOrdenado con herencia de dict ; class diccionarioOrdenado (dict) : \n')

class diccionarioOrdenado (dict) : # definicion de la clase , hereda de la clase padre dict
	def __init__ (self,diccionario=None,clave=None,**kwargs) : # definicion del metodo , inicializa los parametros de la clase -argumentos por defecto-
		diccionario = diccionario or {} # asigna un diccionario No vacio o un diccionario vacio si el valor es None
		super().__init__ (diccionario) # inicializa la clase padre con el valor de diccionario
		if kwargs : # condicion , si es True -no esta vacio-
			super().update (kwargs) # actualiza el argumento de la clase padre
		self.__claves = listaOrdenada (super().keys (),clave) # ordena las claves del diccionario inicializados en la clase padre dict
		
	def actualizar (self,diccionario=None,**kwargs) : # definicion del metodo -argumentos por defecto-
		if diccionario is None : # condicion , si coincide -None-
			pass # funcion de relleno , no hace nada
		elif isinstance (diccionario,dict) : # condicion , si diccionario pertenece a la instancia de dict -devuelve True-
			super().update (diccionario) # actualiza el argumento de la clase padre
		else : # si no pertenece a la instancia de dict -False-
			for CLAVE,VALOR in diccionario.items () : # iterador , bucle for in , pasa los elementos ; la clave a CLAVE y el valor a VALOR
				super().__setitem__ (CLAVE,VALOR) # añade la clave : valor a la clase padre dict
		if kwargs : # condicion , si no esta vacio -True-
			super().update (kwargs) # actualiza el argumento de la clase padre 
		self.__claves = listaOrdenada (super().keys (),self.__claves.clave) # ordena las claves del diccionario inicializados en la clase padre dict -comparando con las claves del objeto-
		
	@classmethod # decorador , funcion classmethod -modifica el metodo inferior con las propiedades de la funcion classmethod-
	def desdeClaves (clase,iterable,valor=None,clave=None) : # definicion del metodo -argumentos por defecto-
		return clase ({klave : valor for klave in iterable},clave) # devuelve una clase con el diccionario generado por compresion
	
	def __setitem__ (self,clave,valor) : # metodo especial -objeto [clave] = valor- , añade al diccionario la clave : valor -si no esta en el objeto-
		if clave not in self : # condicion , si la clave NO esta en el diccionario del objeto
			self.__claves.añadir (clave) # añade la clave a la lista de claves
		return super().__setitem__ (clave,valor) # devuelve el valor clave : valor a añadir al metodo especial de la clase padre
	
	def __delitem__ (self,clave) : # metodo especial -del objeto [clave]- , elimina la clave : valor del objeto
		try : # control de excepciones
			self.__claves.eliminar (clave) # elimina la clave de la lista 
		except ValueError : # tipo de excepcion
			raise KeyError (clave) # lanza la excepcion indicada con la clave del error
		return super().__delitem__ (clave) # devuelve la llamada al metodo especial con la clave de la clase padre
	
	def valorPorDefecto (self,clave,valor=None) : # definicion del metodo -valor por defecto-
		if clave not in self : # condicion , si la clave NO esta en el diccionario del objeto
			self.__claves.añadir (clave) # añade la clave a la lista de claves
		return super().setdefault (clave,valor) # devuelve el valor de la clave por defecto con la llamada al metodo de la clase padre
	
	def eliminarClave (self,clave,*argumentos) : # definicion del metodo
		if clave not in self : # condicion , si la clave NO esta en el diccionario del objeto
			if len (argumentos) == 0 : # condicion , si esta vacio
				raise KeyError (clave) # lanza la excepcion indicada con la clave del error
			return argumentos [0] # devuelve el valor del indice -posicion- indicado de la lista
		self.__claves.eliminar (clave) # elimina la clave de la lista de claves
		return super().pop (clave,argumentos) # elimina y devuelve la clave : valor eliminada
	
	def eliminar (self) :  # definicion del metodo
		elemento = super().popitem () # asigna el metodo de la clase padre
		self.__claves.eliminar (elemento [0]) # eliminar de la lista de claves la clave del indice -posicion- indicado
		return elemento # devuelve el elemento eliminado
	
	def limpiar (self) :   # definicion del metodo
		super().clear () # llama al metodo de la clase padre
		self.__claves.limpiar () # asigna una lista vacia -sin claves-
		
	def valores (self) : # definicion del metodo
		for clave in self.__claves : # iterador , bucle for in , pasa los elementos de la lista -claves- a la variable clave
			yield self [clave] # guarda en un iterador -yield- los valores de las claves
			
	def elementos (self) : # definicion del metodo
		for clave in self.__claves : # iterador , bucle for in , pasa los elementos de la lista -claves- a la variable clave
			yield (clave,self [clave]) # guarda en un iterador -yield- el par (clave,valor)
			
	def __iter__ (self) : # metodo especial -iter ()- , devuelve un iterador
		return iter (self.__claves) # devuelve la lista de claves como iterador
	
	claves = __iter__ # asigna al atributo  el metodo especial
	
	def __repr__ (self) : # metodo especial -repr- , devuelve una cadena que se puede evaluar por eval
		return object.__repr__ (self) # devuelve el objeto en formato cadena evaluable por eval ()
	
	def __str__ (self) : # metodo especial -str- , devuelve una cadena
		return str ({(",").join (["{0!r} : {1!r}".format (C,V) for C,V in self.elementos ()])}) # devuelve un diccionario creado por compresion en formato cadena
	
	def copia (self) : # definicion del metodo
		diccionario = diccionarioOrdenado () # asigna la llamada a la clase , un diccionario vacio
		super (diccionarioOrdenado,diccionario).update (self) # actualiza el diccionario de la clase padre con los valores del objeto
		diccionario.__claves = self.__claves.copia () # asigna a la lista de claves del objeto una copia superficial de la lista de claves
		return diccionario # devuelve la copia superficial de la lista de claves del diccionario
	
	def valorDE (self,indice) : # definicion del metodo
		return self [self.__claves [indice]] # devuelve el valor del indice -posicion- indicado de la lista de claves del objeto
	
	def añadirValorIndice (self,indice,valor) : # definicion del metodo
		self [self.__claves [indice]] = valor # añade el valor en el indice -posicion- indicado de la lista de claves del objeto
		
print ('diccionarioDesordenado = {33 : "treintatres",5 : "cinco",10 : "diez",7 : "siete",4 : "cuatro",2 : "dos",0 : "cero",3 : "tres",1 : "uno"} \n')

diccionarioDesordenado = {33 : "treintatres",5 : "cinco",10 : "diez",7 : "siete",4 : "cuatro",2 : "dos",0 : "cero",3 : "tres",1 : "uno"} # diccionario desordenado 

print ('diccionarioDesordenado2 = {6 : "seis",9 : "nueve",8 : "ocho",11 : "once",-1 : "menosuno"} \n')

diccionarioDesordenado2 = {6 : "seis",9 : "nueve",8 : "ocho",11 : "once",-1 : "menosuno"} # diccionario desordenado 

print ('instanciar la clase diccionarioDesordenado ; ordenarDiccionario = diccionarioOrdenado (diccionarioDesordenado) \n')

ordenarDiccionario = diccionarioOrdenado (diccionarioDesordenado) # instancia la clase con el argumento indicado

print ('actualizar el objeto con otro diccionario ; ordenarDiccionario.actualizar (diccionarioDesordenado2) \n')

ordenarDiccionario.actualizar (diccionarioDesordenado2) # actualiza el diccionario del objeto con el indicado

print ('devolvert una clase con el diccionario generado por la secuencia ; nuevoObjeto = ordenarDiccionario.desdeClaves ([36,31,22,15,100,20]) \n')

nuevoObjeto = ordenarDiccionario.desdeClaves ([36,31,22,15,100,20]) # devuelve una clase diccionarioOrdenado con la secuencia convertida en diccionario

print ('convertir en iterador nuevoObjeto e iterar ; for elemento in iter (nuevoObjeto) : \n')

for elemento in iter (nuevoObjeto) : # iterador , bucle for in , pasa las claves a elemento
	print ('clave : ',elemento,end=' - ') # presenta las claves en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('añadir clave : valor al objeto ; ordenarDiccionario [50] = "cincuenta" \n')

ordenarDiccionario [50] = "cincuenta" # añade la clave : valor al objeto

print ('eliminar una clave del objeto ; del ordenarDiccionario [50] \n')

del ordenarDiccionario [50] # eliminar una clave del objeto

print ('añadir una clave con valor por defecto al objeto ; ordenarDiccionario.valorPorDefecto (50) ',ordenarDiccionario.valorPorDefecto (50),'\n') # añade la clave indicada al objeto con un valor por defecto -None-

print ('eliminar la clave del objeto ; ordenarDiccionario.eliminarClave (50) ',ordenarDiccionario.eliminarClave (50),'\n') # elimina la clave indicada del objeto y lo presenta 

print ('eliminar una clave psuo-aleatoria del objeto ; ordenarDiccionario.eliminar () ',ordenarDiccionario.eliminar (),'\n') # elimina una clave psuo-aleatoria y lo presenta

print ('valores del diccionario del objeto ; for valores in ordenarDiccionario.valores () \n') 

for valores in ordenarDiccionario.valores () : # iterador , bucle for in , pasa las valores del diccionario a valores
	print (valores,end=' - ') # presenta los valores de las claves en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('par (clave,valor) del objeto ; for par in ordenarDiccionario.elementos () : \n')

for par in ordenarDiccionario.elementos () : # iterador , bucle for in , pasa los pares del diccionario a par
	print (par,end=' - ') # presenta los pares (clave,valor) del diccionario en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('convertir en iterador el objeto ; for klave in iter (ordenarDiccionario) : \n')

for klave in iter (ordenarDiccionario) : # iterador , bucle for in , pasa las claves de la lista del objeto
	print (klave,end=' - ') # presenta las claves del diccionario en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('uso del atributo especial claves como iterador ; for Clave in ordenarDiccionario.claves() : \n') 

for Clave in ordenarDiccionario.claves() : # iterador , bucle for in , pasa las claves de la lista del objeto
	print (Clave,end=' - ') # presenta las claves del diccionario en una sola linea
else : # cuando finalice el iterador
	print ('\n') # salto de linea

print ('uso de repr , devuelve una cadena que puede ser evaluada por eval ; repr (ordenarDiccionario) \n') 

print (repr (ordenarDiccionario),'\n') # presenta la clase en formato cadena

print ('ordenarDiccionario \n')

print (ordenarDiccionario,'\n') # presenta el diccionario del objeto en formato cadena

print ('copia superficial del diccionario del objeto ; ordenarDiccionario.copia () \n')

print (ordenarDiccionario.copia (),'\n') # presenta una copia superficial del diccionario del objeto

print ('valor de un indice -posicion- ; ordenarDiccionario.valorDE (2) ',ordenarDiccionario.valorDE (2),'\n') # presenta el valor del indice indicado

print ('añadir un valor al diccionario del objeto por el indice -posicion- ; ordenarDiccionario.añadirValorIndice (-1,1000) \n')

ordenarDiccionario.añadirValorIndice (-1,1000) # añade un valor al diccionario del objeto por el indice -posicion-

print (ordenarDiccionario,'\n') # presenta el diccionario del objeto en formato cadena

print ('limpiar el diccionario del objeto -diccionario vacio- ; ordenarDiccionario.limpiar () \n')

ordenarDiccionario.limpiar () # limpia el diccionario del objeto -diccionario vacio-

print ('ordenarDiccionario ',ordenarDiccionario,'\n') # presenta el diccionario del objeto en formato cadena













