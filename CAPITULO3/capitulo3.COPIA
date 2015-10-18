#!/usr/bin/env python3
'''colecciones de tipos de datos'''

# importar modulo

import sys

print ('VERSION en uso de PYTHON\n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('crear una lista inmutable -tupla- ; tupla = (1,"33","cadena",.339,3+2j,"ultimo") \n')

tupla = (1,"33","cadena",.339,3+2j,"ultimo") # tupla , lista de elementos inmutables -NO modificable-

print ('tupla ',tupla," tipo ",type (tupla),'\n') # presenta el contenido y el tipo de la lista 

print ('modificar una tupla -uso de list ()- ; convertirTuplaLista = list (tupla) \n')

convertirTuplaLista = list (tupla) # convierte la tupla en una lista

print ('convertirTuplaLista ',convertirTuplaLista," tipo ",type (convertirTuplaLista),'\n') # presenta el contenido y el tipo de la lista

print ('modificar tupla ; tupla [0] = "primero" \n')

try : # control de excepciones
  tupla [0] = "primero" # cambiar el valor del indice indicado por el valor indicado -lanza excepcion-
except TypeError as error : # tipo de excepcion , pasa la salida a error
  print ('es una tupla -lista inmutable- ++ {} ++'.format (error),'\n')
  
print ('modificar convertirTuplaLista ; convertirTuplaLista [0] = "primero" \n')

convertirTuplaLista [0] = "primero" # cambiar el valor del indice indicado por el valor indicado

print ('contenido convertirTuplaLista ',convertirTuplaLista,'\n') # presenta el contenido modificado

print ('convertir la lista mutable en inmutable -uso de tuple ()- ; convertirAtupla = tuple (convertirTuplaLista) \n')

convertirAtupla = tuple (convertirTuplaLista) # convierte la lista en una tupla -lista inmutable-

print ('contenido convertirAtupla ',convertirAtupla,' tipo ',type (convertirAtupla),'\n') # presenta el contenido y el tipo de la lista

print ('modificar convertirAtupla ; convertirAtupla [0] = 1 \n')

try : # control de excepciones
  convertirAtupla [0] = 1 # cambiar el valor del indice indicado por el valor indicado -lanza excepcion-
except TypeError as error : # tipo de excepcion , pasa la salida a error
  print ('es una tupla -lista inmutable- ++ {} ++'.format (error),'\n')

print ('presentar los elementos de la tupla por su indice -tupla [numeroIndice]- \n')

for indice,elemento in enumerate (tupla) : # iterador , bucle for in , pasa los elementos de la tupla a elemento , enumerate numera los elementos de la tupla
  print ('tupla [{0}] >> {1} '.format (indice,elemento),'\n') # presenta la cadena formateada con los valores indicados -indice , elemento-
else : # cuando finaliza el iterador
  print ('** FIN DEL CONTENIDO **\n') # presenta la cadena
  
print ('presentar los elementos de la tupla por su indice negativo , a la inversa -tupla [-numeroIndice]- \n')

for indiceNegativo in range (-1,-7,-1) : # iterador , bucle for in , pasa los numeros de la lista a indiceNegativo 
  print ('tupla [{0}] >> '.format (indiceNegativo),tupla [indiceNegativo],'\n') # presenta la cadena formateada con los valores indicados -indice , elemento-
else : # cuando finaliza el iterador
  print ('** FIN DEL CONTENIDO **\n') # presenta la cadena

print ('contar numero de veces que contiene un elemento en la tupla -tupla.count (elemento)- ; tupla.count ("cadena") ',tupla.count ("cadena"),'\n') # presenta el numero de veces que contiene el elemento indicado

print ('devolver el indice del elemento indicado mas a la izquierda -tupla.index (elemento)- ; tupla.index ("cadena") ',tupla.index ("cadena"),'\n') # presenta el indice del elemento indicado mas a la izquierda

print ('concatenar dos tuplas , unir -tupla1 + tupla2- ; concatenarTuplas = tupla + convertirAtupla \n')

concatenarTuplas = tupla + convertirAtupla # une las dos tuplas en una

print ('contenido concatenarTuplas ',concatenarTuplas,'\n') # presenta las dos tuplas en una 

print ('duplicar una tupla , repetir -tupla * numero- ; duplicarTupla = tupla * 3 \n')

duplicarTupla = tupla * 3 # asigna la tupla repetida tres veces

print ('contenido duplicarTupla ',duplicarTupla,'\n') # presenta la tupla repetida tres veces

print ('crear subtuplas , separar -tupla [inicio : fin]- ; tupla [0 : 3] ',tupla [0 : 3],'\n') # presenta la subtupla del indice 0 al 2  -3 NO incluido-

print ('subtupla tupla [3 : ] ',tupla [3 : ],'\n') # presenta la subtupla del indice 3 al ultimo

print ('pertenencia a una tupla -uso de in- ; tupla [1] in duplicarTupla ',tupla [1] in duplicarTupla,'\n') # presenta True o False si el elemento indicado pertenece a la tupla , devuelve True -pertenece-

print ('NO pertenencia a una tupla -uso de not in- ; tupla not in duplicarTupla ',tupla not in duplicarTupla,'\n') # presenta True o False si el elemento indicado NO pertenece a la tupla , devuelve True -NO pertenece-

print ('asignacion aumentada , concatenar - += - ; tupla += convertirAtupla \n')

tupla += convertirAtupla # concatena la tupla indicada por asignacion aumentada

print ('contenido tupla ',tupla,'\n') # presenta el nuevo contenido de la tupla

print ('asignacion aumentada , repetir - *= - ; tupla *= 2 \n')

tupla *= 2 # repite la tupla el numero de veces indicado por asignacion aumentada

print ('contenido tupla ',tupla,'\n') # presenta el nuevo contenido de la tupla

print ('comparar elementos de tuplas o tuplas , menor que - < - ; tupla < tupla ',tupla < tupla,'\n') # presenta True o False si la primera es menor que la segunda , devuelve False

print ('comparar elementos de tuplas o tuplas , mayor que - > - ; tupla > tupla ',tupla > tupla,'\n') # presenta True o False si la primera es mayor que la segunda , devuelve False

print ('comparar elementos de tuplas o tuplas , iguales - == - ; tupla == tupla ',tupla == tupla,'\n') # presenta True o False si las dos son iguales , devuelve True

print ('comparar elementos de tuplas o tuplas , distintos - != - ; tupla != tupla ',tupla != tupla,'\n') # presenta True o False si la primera es distinta que la segunda , devuelve False

print ('comparar elementos de tuplas o tuplas , menor o igual que - <= - ; tupla <= tupla ',tupla <= tupla,'\n') # presenta True o False si la primera es menor o igual que la segunda , devuelve True

print ('comparar elementos de tuplas o tuplas , mayor o igual que - >= - ; tupla >= tupla ',tupla >= tupla,'\n') # presenta True o False si la primera es mayor o igual que la segunda , devuelve True

print ('crear tuplas con nombre , modulo collections -uso de collections.namedtuple()- ; ventas = collections.namedtuple ("venta","producto identificacionCliente fecha cantidad precio")\n')

# importar modulo

import collections # importa el modulo indicado

ventas = collections.namedtuple ("venta","producto identificacionCliente fecha cantidad precio") # asigna los nombres de las tuplas a la funcion namedtuple del modulo importado -collections-

print ('tuplas con nombre ; VENTAS = ventas (432,921,"14-09-2015",3,7.99) \n')

VENTAS = ventas (432,921,"14-09-2015",3,7.99) # crea una tupla por nombres

print ('llamar a los valores de la tupla por su nombre ; VENTAS.producto ',VENTAS.producto,'\n') # presenta el valor de la tupla asignado al nombre

print ('llamar a los valores de la tupla por su nombre ; VENTAS.identificacionCliente ',VENTAS.identificacionCliente,'\n') # presenta el valor de la tupla asignado al nombre

print ('llamar a los valores de la tupla por su nombre ; VENTAS.fecha ',VENTAS.fecha,'\n') # presenta el valor de la tupla asignado al nombre

print ('llamar a los valores de la tupla por su nombre ; VENTAS.cantidad ',VENTAS.cantidad,'\n') # presenta el valor de la tupla asignado al nombre

print ('llamar a los valores de la tupla por su nombre ; VENTAS.precio ',VENTAS.precio,'\n') # presenta el valor de la tupla asignado al nombre

print ('crear una lista mutable -lista- ; lista = ["primero",1,.66,"segundo",3+2j,"penultimo",tupla,"final"]\n')

lista = ["primero",1,.66,"segundo",3+2j,"penultimo",tupla,"final"] # lista de 8 elementos mutables -lista modificable-

print ('contenido de lista ',lista,'\n') # presenta el contenido de la lista

print ('convertir argumentos en lista -list ()- ; tuplaAlista = list (tupla)\n')

tuplaAlista = list (tupla) # convierte la tupla en lista

print ('contenido de tuplaAlista ',tuplaAlista,'\n') # presenta el contenido de la lista

print ('presentar los elementos de la lista por su indice -lista [numeroIndice]- \n')

for indice,elemento in enumerate (lista) : # iterador , bucle for in , pasa los elementos de la lista a elemento , enumerate numera los elementos de la lista
  print ('lista [{0}] >> {1} '.format (indice,elemento),'\n') # presenta la cadena formateada con los valores indicados -indice , elemento-
else : # cuando finaliza el iterador
  print ('** FIN DEL CONTENIDO **\n') # presenta la cadena
  
print ('presentar los elementos de la lista por su indice negativo , a la inversa -lista [-numeroIndice]- \n')

for indiceNegativo in range (-1,-9,-1) : # iterador , bucle for in , pasa los numeros de la lista a indiceNegativo 
  print ('lista [{0}] >> '.format (indiceNegativo),lista [indiceNegativo],'\n') # presenta la cadena formateada con los valores indicados -indice , elemento-
else : # cuando finaliza el iterador
  print ('** FIN DEL CONTENIDO **\n') # presenta la cadena

print ('concatenar dos listas , unir -tupla1 + tupla2- ; concatenarListas = lista + tuplaAlista \n')

concatenarListas = lista + tuplaAlista # une las dos listas en una

print ('contenido concatenarListas ',concatenarListas,'\n') # presenta las dos listas en una 

print ('duplicar una lista , repetir -lista * numero- ; duplicarLista = lista * 3 \n')

duplicarLista = lista * 3 # asigna la lista repetida tres veces

print ('contenido duplicarLista ',duplicarLista,'\n') # presenta la lista repetida tres veces

print ('crear sublistas , separar -lista [inicio : fin]- ; lista [0 : 3] ',lista [0 : 3],'\n') # presenta la sublista del indice 0 al 2  -3 NO incluido-

print ('sublista lista [3 : ] ',lista [3 : ],'\n') # presenta la sublista del indice 3 al ultimo

print ('pertenencia a una lista -uso de in- ; lista [1] in duplicarLista ',lista [1] in duplicarLista,'\n') # presenta True o False si el elemento indicado pertenece a la lista , devuelve True -pertenece-

print ('NO pertenencia a una lista -uso de not in- ; lista not in duplicarLista ',lista not in duplicarLista,'\n') # presenta True o False si el elemento indicado NO pertenece a la lista , devuelve True -NO pertenece-

print ('asignacion aumentada , concatenar - += - ; lista += tuplaAlista \n')

lista += tuplaAlista # concatena la lista indicada por asignacion aumentada

print ('contenido lista ',lista,'\n') # presenta el nuevo contenido de la lista

print ('asignacion aumentada , repetir - *= - ; lista *= 2 \n')

lista *= 2 # repite la lista el numero de veces indicado por asignacion aumentada

print ('contenido lista ',lista,'\n') # presenta el nuevo contenido de la lista

print ('comparar elementos de listas o listas , menor que - < - ; lista < lista ',lista < lista,'\n') # presenta True o False si la primera es menor que la segunda , devuelve False

print ('comparar elementos de listas o listas , mayor que - > - ; lista > lista ',lista > lista,'\n') # presenta True o False si la primera es mayor que la segunda , devuelve False

print ('comparar elementos de listas o listas , iguales - == - ; lista == lista ',lista == lista,'\n') # presenta True o False si las dos son iguales , devuelve True

print ('comparar elementos de listas o listas , distintos - != - ; lista != lista ',lista != lista,'\n') # presenta True o False si la primera es distinta que la segunda , devuelve False

print ('comparar elementos de listas o listas , menor o igual que - <= - ; lista <= lista ',lista <= lista,'\n') # presenta True o False si la primera es menor o igual que la segunda , devuelve True

print ('comparar elementos de listas o listas , mayor o igual que - >= - ; lista >= lista ',lista >= lista,'\n') # presenta True o False si la primera es mayor o igual que la segunda , devuelve True

print ('numero de elementos de una lista -uso de len ()- ; len (lista) ',len (lista),'\n') # presenta numero de elementos de la lista 

print ('contenido lista [6] ',lista [6],'\n') # presenta el elemento del indice indicado

print ('eliminar un elemento de la la lista -uso de del- ; del lista [6] \n')

del lista [6] # elimina el elemento del indice indicado

print ('contenido lista [6] ',lista [6],'\n') # presenta el elemento del indice indicado

print ('añadir un elemento al final de la lista -append- ; lista.append ("ULTIMO") \n')

lista.append ("ULTIMO") # añade el elemento al final de la lista

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('contar numero de veces que contiene un elemento en la lista -lista.count (elemento)- ; lista.count (tupla) ',lista.count (tupla),'\n') # presenta el numero de veces que contiene el elemento indicado

print ('añadir los elementos de una secuencia a la lista -extend- ; lista.extend (tupla)\n')

lista.extend (tupla) # añade los elementos de la tupla al final de la lista 

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('devolver el indice del elemento indicado mas a la izquierda -lista.index (elemento)- ; lista.index ("ULTIMO") ',lista.index ("ULTIMO"),'\n') # presenta el indice del elemento indicado mas a la izquierda

print ('insertar un elemento en el indice indicado -insert- ; lista.insert (6,"elementoInsertado")\n')

lista.insert (6,"elementoInsertado") # inserta el elemento en el indice indicado

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('eliminar y devolver el ultimo elemento -pop- ; lista.pop () ',lista.pop (),'\n') # presenta el ultimo elemento eliminado 

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('eliminar y devolver el elemento del indice indicado -pop- ; lista.pop (0) ',lista.pop (0),'\n') # presenta el elemento eliminado del indice indicado

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('elimina el elemento indicado mas cercano a la izquierda -remove- ; lista.remove (tupla) \n')

lista.remove (tupla) # elimina el elemento indicado

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('invertir el orden de la lista -reverse- ; lista.reverse () \n') # presenta la lista a la inversa

lista.reverse () # invierte el orden de la lista 

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('lista.count (3+2j) ',lista.count (3+2j),'\n') # presenta el numero de veces que se repite

print ('eliminar 3+2j \n')

while True : # bucle while continuo
  lista.remove (3+2j) # elimina el elemento indicado
  if not lista.count (3+2j) : # condicion , si es False -valor cero-
    print ('no quedan mas elementos\n') # presenta la cadena
    break # interrumpe el bucle while continuo

print ('eliminar float \n')

for eliminarFloat in lista : # iterador , bucle for in , pasa los elementos de la lista a eliminarFloat
  if type (eliminarFloat) == float : # condicion , si es float
    lista.remove (eliminarFloat) # elimina el elemento indicado
else : # cuando finaliza el iterador
  print ('no quedan mas elementos float \n') # presenta la cadena

print ('eliminar int \n')

for eliminarInt in lista : # iterador , bucle for in , pasa los elementos de la lista a eliminarInt
  if type (eliminarInt) == int : # condicion , si es int 
    lista.remove (eliminarInt) # elimina el elemento indicado
else : # cuando finaliza el iterador
  print ('no quedan mas elementos int \n') # presenta la cadena
    
print ('ordenar la lista -sort- ; lista.sort () \n')

lista.sort () # ordena la lista

print ('contenido lista ',lista,'\n') # presenta el contenido

print ('lista por compresion -[x for x in secuencia]- ; años = [año for año in range (1900,2016)] \n')

años = [año for año in range (1900,2016)] # lista por compresion , añade los elementos del iterador a la lista 

print ('contenido años ',años,'\n') # presenta la lista generada por compresion

print ('lista por compresion condicional -[x for x in secuencia if condicion]- ; añosBisiesto = [año for año in range (1900,2016) if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)] \n')

añosBisiesto = [año for año in range (1900,2016) if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)] # lista por compresion condicional , añade los elementos del iterador a la lista , si cumple la condicion indicada

print ('contenido añosBisiesto ',añosBisiesto,'\n') # presenta la lista generada por compresion condicional

print ('crear conjuntos mutables -lista de elementos no repetidos , uso de set ()- ; conjuntoMutable = set (añosBisiesto) \n')

conjuntoMutable = set (añosBisiesto) # conjunto de elementos unicos -no repetidos-

print ('tipo conjuntoMutable ',type (conjuntoMutable),' contenido ',conjuntoMutable,'\n') # presenta tipo y contenido

print ('numero de elementos de set -uso de len ()- ; len (conjuntoMutable) ',len (conjuntoMutable),'\n') # presenta el numero de elementos del conjunto mutable

print ('pertenencia en set -uso de in- ; añosBisiesto [0] in conjuntoMutable ',añosBisiesto [0] in conjuntoMutable,'\n') # presenta True o False , si el elemento indicado pertenece al conjunto

print ('añadir un elemento a conjuntoMutable -uso de add- ; conjuntoMutable.add ("FINAL") \n')

conjuntoMutable.add ("FINAL") # añade el elemento al conjunto mutable , siempre que no este

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido de set ()

print ('crear conjuntos inmutables -lista NO modificable de elementos no repetidos , uso de frozenset ()- ; conjuntoInmutable = frozenset (años) \n')

conjuntoInmutable = frozenset (años) # conjunto de elementos NO modificable unicos -no repetidos-

print ('tipo conjuntoInmutable ',type (conjuntoInmutable),' contenido ',conjuntoInmutable,'\n') # presenta tipo y contenido

print ('numero de elementos de frozenset -uso de len ()- ; len (conjuntoInmutable) ',len (conjuntoInmutable),'\n') # presenta el numero de elementos del conjunto inmmutable

print ('pertenencia en frozenset -uso de in- ; años [0] in conjuntoInmutable ',años [0] in conjuntoInmutable,'\n') # presenta True o False , si el elemento indicado pertenece al conjunto

print ('añadir un elemento a conjuntoInmutable -uso de add- ; conjuntoInmutable.add ("FINAL") \n')

try : # control de excepciones
  conjuntoInmutable.add ("FINAL") # añade el elemento al conjunto inmmutable , siempre que no este -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
  print ('CONJUNTO INMUTABLE , NO SE PUEDE AÑADIR *** {} *** \n'.format (error)) # presenta la cadena formateada con la salida de error
  
print ('contenido de conjuntoInmutable ',conjuntoInmutable,'\n') # presenta el contenido de set ()

print ('comparar elementos de conjuntos o conjuntos , menor que - < - ; conjuntoMutable < conjuntoMutable ',conjuntoMutable < conjuntoMutable,'\n') # presenta True o False si la primera es menor que la segunda , devuelve False

print ('comparar elementos de conjuntos o conjuntos , mayor que - > - ; conjuntoMutable > conjuntoMutable ',conjuntoMutable > conjuntoMutable,'\n') # presenta True o False si la primera es mayor que la segunda , devuelve False

print ('comparar elementos de conjuntos o conjuntos , iguales - == - ; conjuntoMutable == conjuntoMutable ',conjuntoMutable == conjuntoMutable,'\n') # presenta True o False si las dos son iguales , devuelve True

print ('comparar elementos de conjuntos o conjuntos , distintos - != - ; conjuntoMutable != conjuntoMutable ',conjuntoMutable != conjuntoMutable,'\n') # presenta True o False si la primera es distinta que la segunda , devuelve False

print ('comparar elementos de conjuntos o conjuntos , menor o igual que - <= - ; conjuntoMutable <= conjuntoMutable ',conjuntoMutable <= conjuntoMutable,'\n') # presenta True o False si la primera es menor o igual que la segunda , devuelve True

print ('comparar elementos de conjuntos o conjuntos , mayor o igual que - >= - ; conjuntoMutable >= conjuntoMutable ',conjuntoMutable >= conjuntoMutable,'\n') # presenta True o False si la primera es mayor o igual que la segunda , devuelve True

print ('operador de union de conjuntos - | - ; conjuntoMutable | conjuntoInmutable ',conjuntoMutable | conjuntoInmutable,'\n') # presenta la union de los elementos NO repetidos

print ('operador de interseccion de conjuntos - & - ; conjuntoMutable & conjuntoInmutable ',conjuntoMutable & conjuntoInmutable,'\n') # presenta los elementos que estan en ambos conjuntos

print ('operador de diferencia de conjuntos - - - ; conjuntoMutable - conjuntoInmutable ',conjuntoMutable - conjuntoInmutable,'\n') # presenta los elementos que NO estan en el segundo conjunto

print ('operador de diferencia simetrica de conjuntos - ^ - ; conjuntoMutable ^ conjuntoInmutable ',conjuntoMutable ^ conjuntoInmutable,'\n') # presenta los elementos que NO estan en el otro conjunto

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido de set ()

print ('añadir un elemento o secuencia a set -add- ; conjuntoMutable.add ("LISTA") \n')

conjuntoMutable.add ("LISTA") # añade la lista al conjunto set

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido de set ()

print ('devolver una copia simple del conjunto -copy- ; copiaSet = conjuntoMutable.copy () \n') # presenta una copia simple de set o frozenset

copiaSet = conjuntoMutable.copy () # presenta una copia simple del conjunto

print ('contenido de copiaSet ',copiaSet,'\n') # presenta el contenido de set ()

print ('eliminar todos los elementos del conjunto -clear- copiaSet.clear () \n')

copiaSet.clear () # elimina todos los elementos del conjunto

print ('contenido de copiaSet ',copiaSet,'\n') # presenta el contenido de set ()

print ('operador de diferencia de conjuntos -difference- ; conjuntoMutable.difference (conjuntoInmutable) ',conjuntoMutable.difference (conjuntoInmutable),'\n') # presenta los elementos que NO estan en el segundo conjunto

print ('eliminar un elemento del conjunto -discard- ; conjuntoMutable.discard (1920) \n')

conjuntoMutable.discard (1920) # elimina el elemento indicado del conjunto

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido 

print ('devuelve un conjunto con los elementos que se encuentren en ambos conjuntos -intersection- conjuntoMutable.intersection (conjuntoInmutable) \n')

print (conjuntoMutable.intersection (conjuntoInmutable),'\n') # presenta un conjunto con los elementos que se encuentren en ambos conjuntos

print ('añadir al primer conjunto la interseccion del segundo conjunto -intersection_update- ; conjuntoMutable.intersection_update (conjuntoInmutable) \n')

conjuntoMutable.intersection_update (conjuntoInmutable) # añade al primer conjunto la interseccion del segundo conjunto

print ('contenido conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido

print ('devuelve True si ambos conjuntos no tienen elementos comunes -isdisjoint- ; conjuntoMutable.isdisjoint (conjuntoInmutable) ',conjuntoMutable.isdisjoint (conjuntoInmutable),'\n') # presenta True si ambos conjuntos no tienen elementos comunes

print ('devuelve True si el primer conjunto es igual o un subconjunto del segundo conjunto -issubset- ; conjuntoMutable.issubset (conjuntoInmutable) ',conjuntoMutable.issubset (conjuntoInmutable),'\n') # presenta True si el primer conjunto es igual o un subconjunto del segundo conjunto

print ('devuelve True si el primer conjunto es igual o un superconjunto del segundo conjunto -issuperset- ; ',conjuntoMutable.issuperset (conjuntoInmutable),'\n') # presenta True si el primer conjunto es igual o un superconjunto del segundo conjunto

print ('elimina y devuelve un elemento aleatorio del conjunto -pop- ; conjuntoMutable.pop () ',conjuntoMutable.pop (),'\n')

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido 

print ('eliminar un elemento del conjunto -remove- ; conjuntoMutable.remove (2012) \n')

conjuntoMutable.remove (2012) # elimina el elemento indicado del conjunto

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido 

print ('devuelve un conjunto que contenga los elementos del primer conjunto y los del segundo que no esten en el primero -symmetric_difference- ; conjuntoMutable.symmetric_difference (conjuntoInmutable) \n')

print (conjuntoMutable.symmetric_difference (conjuntoInmutable)) # presenta un conjunto con los elementos del primer conjunto y del segundo que no esten en el primero

print ('añadir al primer conjunto los elementos del segundo que no esten en el primero -symmetric_difference_update- ; conjuntoMutable.symmetric_difference_update (conjuntoInmutable) \n')

conjuntoMutable.symmetric_difference_update (conjuntoInmutable) # añade al primer conjunto los elementos del segundo que no esten en el primero 

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido 

print ('devuelve un conjunto que contenga el primer conjunto mas los elementos del segundo conjunto que no se encuentren en el primero -union- ; conjuntoMutable.union (conjuntoInmutable) \n')

print (conjuntoMutable.union (conjuntoInmutable),'\n') # presenta un conjunto que contenga el primer conjunto mas los elementos del segundo conjunto que no se encuentren en el primero

print ('añade al primer conjunto los elementos del segundo conjunto que no se encuentren en el primero -update- ; conjuntoMutable.update (conjuntoInmutable) \n')

conjuntoMutable.update (conjuntoInmutable) # añade al primer conjunto los elementos del segundo conjunto que no se encuentren en el primero

print ('contenido de conjuntoMutable ',conjuntoMutable,'\n') # presenta el contenido 

print ('conjunto por compresion -{valor for valor in iterador}- ; conjuntoPORcompresion = {SET for SET in range (101)} \n')

conjuntoPORcompresion = {SET for SET in range (101)} # asigna un conjunto por compresion -lista de numeros-

print ('contenido de conjuntoPORcompresion ',conjuntoPORcompresion,' tipo ',type (conjuntoPORcompresion),'\n') # presenta el contenido y tipo

print ('conjunto por compresion condicional -{valor for valor in iterador if condicion}- ; conjuntoPORcompresionCondicional = {SET for SET in range (101) if SET % 2 == 0} \n')

conjuntoPORcompresionCondicional = {SET for SET in range (101) if SET % 2 == 0} # asigna un conjunto por compresion condicional -lista de numeros pares-

print ('contenido de conjuntoPORcompresionCondicional ',conjuntoPORcompresionCondicional,' tipo ',type (conjuntoPORcompresionCondicional),'\n') # presenta el contenido y tipo

print ('conjuntos fijos (conjuntos inmutables) -frozenset- ; conjuntoFijo = conjuntoInmutable \n')

conjuntoFijo = conjuntoInmutable # asigna el conjunto inmutable

print ('contenido conjuntoFijo ',conjuntoFijo,'\n') # presenta el contenido 

print ('añadir un elemento al conjunto inmutable ; conjuntoFijo.add ("ELEMENTO_AÑADIDO") \n')

try : # control de excepciones
  conjuntoFijo.add ("ELEMENTO_AÑADIDO") # añade el elemento al conjunto inmmutable , siempre que no este -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
  print ('CONJUNTO FIJO -INMUTABLE- , NO SE PUEDE AÑADIR *** {} *** \n'.format (error)) # presenta la cadena formateada con la salida de error

print ('conjunto fijo por compresion condicional ; conjuntoFijoCondicional = frozenset (SET for SET in range (101) if SET % 2 == 0) \n')

conjuntoFijoCondicional = frozenset (SET for SET in range (101) if SET % 2 == 0) # asigna un conjunto por compresion condicional -lista de numeros pares-

print ('contenido conjuntoFijoCondicional ',conjuntoFijoCondicional,'\n') # presenta el contenido 

print ('añadir un elemento al conjunto inmutable ; conjuntoFijoCondicional.add ("ELEMENTO_AÑADIDO") \n')

try : # control de excepciones
  conjuntoFijoCondicional.add ("ELEMENTO_AÑADIDO") # añade el elemento al conjunto inmmutable , siempre que no este -lanza excepcion-
except AttributeError as error : # tipo de excepcion , pasa la salida a error
  print ('CONJUNTO FIJO -INMUTABLE- , NO SE PUEDE AÑADIR *** {} *** \n'.format (error)) # presenta la cadena formateada con la salida de error

print ('tipo de agrupacion dict -dict (clave=valor)- ; tipoDict = dict (valor1=1,valor2=2,valor3=3,valor4=4,valor5=5) \n')

tipoDict = dict (valor1=1,valor2=2,valor3=3,valor4=4,valor5=5) # asigna tipo dict -diccionario-

print ('contenido tipoDict ',tipoDict,' tipo ',type (tipoDict),'\n') # presenta el contenido y tipo

print ('numero de elementos de tipoDict ; len (tipoDict) ',len (tipoDict),'\n') # presenta el numero de elementos

print ('pertenencia de los elementos de dict ; clave in diccionario \n')

for clave in tipoDict : # iterador , bucle for in , pasa las claves del diccionario a clave
  print ('{} in tipoDict '.format(clave),clave in tipoDict,'\n') # presenta True si la clave pertenece al contenido del tipo dict
else : # cuando finaliza el iterador
  print ('** fin del contenido ** \n') # presenta el texto

print ('tipo de agrupacion collections.defaultdict -collections.defaultdict ()- ; tipoDefaultdict = collections.defaultdict (int) \n')

tipoDefaultdict = collections.defaultdict (int) # asigna tipo defaultdict -diccionario con el tipo de valor por defecto indicado , numeros enteros int-

print ('ITERADOR = "PYTHON" \n')

ITERADOR = "PYTHON" # asigna cadena

print ('añadir la cadena a defaultdict \n')

for caracter in ITERADOR : # iterador , bucle for in , pasa los caracteres de la cadena a caracter
  print ('tipoDefaultdict [{}] += 1 \n'.format(caracter)) # presenta la cadena formateada -clave ; caracter-
  tipoDefaultdict [caracter] += 1 # añade la clave (caracter) ; valor (numero int) , suma uno al valor actual de la clave
  
print ('contenido tipoDefaultdict ',tipoDefaultdict,' tipo ',type (tipoDefaultdict),'\n') # presenta el contenido y tipo

print ('crear un diccionario ; Diccionario = {1 : 2,"tres" : 3,"cuatro" : "cinco","lista" : lista,"tupla" : tupla,"diccionario" : tipoDefaultdict} \n')

Diccionario = {1 : 2,"tres" : 3,"cuatro" : "cinco","lista" : lista,"tupla" : tupla,"diccionario" : tipoDefaultdict} # asigna diccionario

print ('iterar diccionario ; Diccionario \n')

for Clave in Diccionario : # iterador , bucle for in , pasa las claves del diccionario a Clave
  print ('Diccionario [{}] '.format(Clave),Diccionario [Clave],'\n') # presenta la cadena formateada y su valor -clave , valor-
else : # cuando finaliza el iterador
  print ('** fin del contenido ** \n') # presenta el texto

print ('copia superficial de un diccionario -copy- ; copiaDiccionario = Diccionario.copy () \n')

copiaDiccionario = Diccionario.copy () # crea una copia superficial del diccionario

print ('contenido de copiaDiccionario ',copiaDiccionario,'\n') # presenta el contenido

print ('eliminar todos los elementos de un diccionario -clear- ; copiaDiccionario.clear () \n')

copiaDiccionario.clear () # elimina los elementos del diccionario

print ('contenido de copiaDiccionario ',copiaDiccionario,'\n') # presenta el contenido

print ('devolver un diccionario con la secuencia indicada -fromkeys- ; copiaDiccionario.fromkeys ("secuencia",True) \n')

print (copiaDiccionario.fromkeys ("secuencia",True),'\n') # presenta el diccionario creado con la secuencia de la cadena y la lista -NO lo asigna al diccionario-

print ('contenido de copiaDiccionario ',copiaDiccionario,'\n') # presenta el contenido

print ('devolver el valor de la clave indicada -get- ; Diccionario.get (1) ',Diccionario.get (1),'\n') # presenta el valor de la clave indicada

print ('devolver la clave o el valor si estan en el diccionario -get- ; Diccionario.get (2,3) ',Diccionario.get (2,3),'\n') # presenta el valor de la clave indicada

print ('devolver un par clave,valor de todos los elementos del diccionario -items- ; Diccionario.items () \n')

print (Diccionario.items (),'\n') # presenta una lista con pares clave,valor de todos los elementos del diccionario

print ('devolver las claves del diccionario -keys- ; Diccionario.keys () ',Diccionario.keys (),'\n') # presenta las claves del diccionario

print ('devolver el valor de la clave indicada y eliminarla -pop- ; Diccionario.pop (1) ',Diccionario.pop (1),'\n') # presenta el valor de la clave indicada y lo elimina

print ('devolver el valor de la clave indicada -get- ; Diccionario.get (1) ',Diccionario.get (1),'\n') # presenta el valor de la clave indicada

print ('devolver el valor de la clave indicada y eliminarla o el valor indicado -pop- ; Diccionario.pop (1,3) ',Diccionario.pop (1,3),'\n') # presenta el valor de la clave indicada y lo elimina , si no esta la clave , presenta el valor indicado si esta

print ('devolver el valor de la clave indicada -get- ; Diccionario.get ("tres") ',Diccionario.get ("tres"),'\n') # presenta el valor de la clave indicada

print ('devolver un par clave,valor aleatorio del diccionario y eliminarlo -popitem- ; Diccionario.popitem () ',Diccionario.popitem (),'\n') # presenta un par clave,valor aleatorio del diccionario y eliminarlo

print ('añadir una clave y su valor -opcional- al diccionario -setdefault- Diccionario.setdefault ("clave") \n')

Diccionario.setdefault ("clave") # añade la clave y valor None al diccionario

print ('contenido Diccionario ',Diccionario,'\n') # presenta el diccionario

print ('añadir la secuencia de pares clave,valor al diccionario -update- ; Diccionario.update ([("seis",6),("siete",7),("ocho",8),("nueve",9),("cero",0)]) \n')

Diccionario.update ([("seis",6),("siete",7),("ocho",8),("nueve",9),("cero",0)]) # añade la secuencia de pares clave,valor al diccionario

print ('contenido Diccionario ',Diccionario,'\n') # presenta el diccionario

print ('devolver los valores de las claves del diccionario -values- ; Diccionario.values () \n')

for valores in Diccionario.values () : # iterador , bucle for in , pasa los valores del diccionario a valores
  print ('valor ',valores,'\n') # presenta el valor del diccionario
else : # cuando finaliza el iterador
  print ('** fin del contenido ** \n') # presenta el texto

print ('leer un fichero de texto , modo r -open- ; open ("./Escritorio/capitulo3.py~","r") \n')

with open ("./Escritorio/capitulo3.py~","r") as leer : # abre y cierra el fichero indicado en modo lectura enlazado como leer
  contenidoLectura = leer.readlines () # devuelve una lista con las lineas del contenido del fichero enlazado
  print ('contenido del fichero ; capitulo3.py~ - {} lineas - \n'.format(len(contenidoLectura))) # presenta el texto formateado con el numero total de lineas
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
  for numeroLinea,lineaLeida in enumerate (contenidoLectura) : # iterador , bucle for in , pasa las lineas de la lista a lineaLeida , enumerate numera las lineas de la lista
    print ('linea {} → '.format(numeroLinea),lineaLeida) # presenta el numero de linea y la linea 
  else : # cuando finaliza el iterador
    print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
    print ('+++ FIN DEL CONTENIDO * {} lineas * +++\n'.format(len(contenidoLectura))) # presenta el texto formateado con el numero total de lineas
    
print ('crear y escribir en un fichero de texto , modo w -open- ; open ("./Escritorio/capitulo3.COPIA","w") \n')

with open ("./Escritorio/capitulo3.COPIA","w") as escribir : # abre y cierra el fichero indicado en modo escritura enlazado como escribir -si existe ; elimina el contenido , si no lo crea-
  print ('crear y escribir en el fichero ; capitulo3.COPIA - {} lineas - \n'.format(len(contenidoLectura))) # presenta el texto formateado con el numero total de lineas
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
  print ('ESCRIBIENDO EL CONTENIDO \n') # presenta el texto
  escribir.writelines (contenidoLectura) # escribe en el fichero enlazado el contenido de la secuencia -lista con el contenido del fichero que enlaza capitulo3.py~ -
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
  print ('+++ FIN DEL CONTENIDO * {} lineas * +++\n'.format(len(contenidoLectura))) # presenta el texto formateado con el numero total de lineas

print ('leer fichero de texto creado , modo r -open- ; open ("./Escritorio/capitulo3.COPIA","r") \n')

for numeroLineaCopia,lineaCopia in enumerate (open ("./Escritorio/capitulo3.COPIA","r")) : # iterador , bucle for in , itera el contenido del fichero indicado a lineaCopia , enumerate numera las lineas iteradas
  print ('linea {} → '.format(numeroLineaCopia),lineaCopia) # presenta el numero de linea y la linea
else : # cuando finaliza el iterador
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
  print ('+++ FIN DEL CONTENIDO  * {} lineas * +++\n'.format(numeroLineaCopia)) # presenta el texto formateado con el numero total de lineas

print ('crear diccionario por compresion -{clave : valor for clave,valor in iterador}- ; diccionarioPorCompresion = {clave : valor for clave,valor in enumerate (open ("./Escritorio/capitulo3.COPIA","r"))} \n')

diccionarioPorCompresion = {clave : valor for clave,valor in enumerate (open ("./Escritorio/capitulo3.COPIA","r"))} # crea un diccionario por compresion con el numero de linea como clave y el contenido del fichero en valor

print ('iterar el diccionario por compresion ; diccionarioPorCompresion \n')

for CLAVE in diccionarioPorCompresion : # iterador , bucle for in , itera el contenido del diccionario a CLAVE 
  print ('diccionarioPorCompresion [{}] '.format(CLAVE),diccionarioPorCompresion [CLAVE],'\n') # presenta el texto formateado con la clave del diccionario y su valor
else : # cuando finaliza el iterador
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
  print ('+++ FIN DEL CONTENIDO  * {} lineas * +++\n'.format(len(diccionarioPorCompresion))) # presenta el texto formateado con el numero total de lineas

print ('crear diccionario por compresion condicional -{clave : valor for clave,valor in iterador if condicion}- ; diccionarioPorCompresionCondicional = {clave : valor for clave,valor in enumerate (open ("./Escritorio/capitulo3.COPIA","r")) if valor != "\\n"} \n')

diccionarioPorCompresionCondicional = {clave : valor for clave,valor in enumerate (open ("./Escritorio/capitulo3.COPIA","r")) if valor != "\n"} # crea un diccionario por compresion con el numero de linea como clave y el contenido del fichero en valor , con la condicion de que la linea sea distinta a un salto de linea

print ('iterar el diccionario por compresion condicional ; diccionarioPorCompresionCondicional \n')

for CLAVEcondicional in diccionarioPorCompresionCondicional : # iterador , bucle for in , itera el contenido del diccionario a CLAVEcondicional 
  print ('diccionarioPorCompresionCondicional [{}] '.format(CLAVEcondicional),diccionarioPorCompresionCondicional [CLAVEcondicional],'\n') # presenta el texto formateado con la clave del diccionario y su valor
else : # cuando finaliza el iterador
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena
  print ('+++ FIN DEL CONTENIDO  * {} lineas * +++\n'.format(len(diccionarioPorCompresionCondicional))) # presenta el texto formateado con el numero total de lineas

print ("numero de lineas diccionarioPorCompresion : {0} lineas , numero de lineas diccionarioPorCompresionCondicional : {1} lineas , diferencia : {2} lineas de salto \n".format(len(diccionarioPorCompresion),len(diccionarioPorCompresionCondicional),len(diccionarioPorCompresion) - len(diccionarioPorCompresionCondicional))) # presenta el texto formateado con los valores indicados , numeros de lineas y diferencia

print ('diccionarios por defecto -collections.defaultdict ()- ; diccionarioPorDefecto = collections.defaultdict (str) \n')

diccionarioPorDefecto = collections.defaultdict (str) # asigna tipo defaultdict -diccionario con el tipo de valor por defecto indicado , cadena str -string-

print ('Iterador = "PYTHON" \n')

Iterador = "PYTHON" # asigna cadena

print ('añadir la cadena a defaultdict \n')

for Caracter in Iterador : # iterador , bucle for in , pasa los caracteres de la cadena a Caracter
  print ('diccionarioPorDefecto [{}] += "VALOR POR DEFECTO \n" \n'.format(Caracter)) # presenta la cadena formateada -clave ; Caracter-
  diccionarioPorDefecto [Caracter] += "VALOR POR DEFECTO\n" # añade la clave (Caracter) ; valor (cadena) , añade la cadena a la clave CAracter 
  
print ('contenido diccionarioPorDefecto ',diccionarioPorDefecto,' tipo ',type (diccionarioPorDefecto),'\n') # presenta el contenido y tipo

print ('añadir solo la clave al diccionario -con valor por defecto- ; diccionarioPorDefecto ["M"] \n')

diccionarioPorDefecto ["M"] # añade la clave con un valor por defecto

print ('contenido diccionarioPorDefecto \n') # presenta el contenido

for ClavE in diccionarioPorDefecto : # iterador , bucle for in , pasa las claves del diccionario a ClavE
  print ('diccionarioPorDefecto [{}] '.format(ClavE),diccionarioPorDefecto[ClavE]) # presenta la clave y su valor 
else : # cuando finaliza el iterador 
  print ('--- FIN DEL CONTENIDO --- {} elementos \n'.format(len(diccionarioPorDefecto))) # presenta el texto formateado con el numero total de elementos

print ('concatenar dos secuencias del mismo tipo -uso de + - ; Iterador + "cadena" ',Iterador + "cadena",'\n') # presenta la concatenacion de dos secuencias del mismo tipo

print ('concatenar una secuencia repetida -uso de * - ; Iterador * 3 ',Iterador * 3,'\n') # presenta la secuencia repetida un numero de veces

print ('pertenencia a una secuencia -uso de in- ; elemento in secuencia \n')

for elemento in Iterador : # iterador , bucle for in , pasa los elementos de la secuencia a elemento
  print ('{} in Iterador '.format(elemento),elemento in Iterador,'\n') # presenta True si el elemento pertenece -esta- en la secuencia
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('devuelve True si todos los elementos de una secuencia son True -uso all- ; all (Iterador) ',all (Iterador),'\n') # presenta True si todos los elementos de una secuencia son True

print ('NO pertenencia a una secuencia -uso de not in- ; elemento in secuencia \n')

for elemento in Iterador : # iterador , bucle for in , pasa los elementos de la secuencia a elemento
  print ('{} not in Iterador '.format(elemento),elemento not in Iterador,'\n') # presenta True si el elemento NO pertenece -esta- en la secuencia
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('devuelve True si alguno de los elementos de una secuencia es True -uso any- ; any (Iterador) ',any (Iterador),'\n') # presenta True si alguno de los elementos de una secuencia es True

print ('numerar los elementos de una secuencia -uso enumerate- ; enumerate (Iterador) \n')

for numero,elemento in enumerate (Iterador) : # iterador , bucle for in , pasa los elementos de la secuencia a elemento y los numeros de enumerate a numero
  print ('numero : {} - elemento : {} \n'.format(numero,elemento)) # presenta la cadena formateada con sus valores -numero y elemento-
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('devolver el numero de elementos de una secuencia -uso len- ; len (Iterador) ',len (Iterador),'\n') # presenta el numero de elementos de una secuencia

print ('devolver el elemento mas grande de una secuencia -uso max- ; max ([0,1,2,3,4,5,6,7,8,9]) ',max ([0,1,2,3,4,5,6,7,8,9]),'\n') # presenta el elemento mas grande de una secuencia
       
print ('devolver el elemento mas pequeño de una secuencia -uso min- ; min ([0,1,2,3,4,5,6,7,8,9]) ',min ([0,1,2,3,4,5,6,7,8,9]),'\n') # presenta el elemento mas pequeño de una secuencia

print ('devolver una secuencia de numeros -uso range- ; range (10) ',[x for x in range (10)],'\n') # presenta una secuencia de numeros , lista por compresion -del 0 al penultimo del indicado , 9-

print ('devolver una secuencia de numeros , con salto indicado -uso range (numeroInicio,numeroFinal,paso)- ; range (0,10,2) ',[x for x in range (0,10,2)],'\n') # presenta una secuencia de numeros , lista por compresion -del 0 al penultimo del indicado , 8 , cada dos numeros-

print ('devolver una secuencia a la inversa de la indicada , al reves -uso reversed- ; reversed ([0,1,2,3,4,5,6,7,8,9]) ',[x for x in reversed ([0,1,2,3,4,5,6,7,8,9])],'\n') # presenta una secuencia invertida de numeros , lista por compresion -del 9 al 0-

print ('devolver una secuencia ordenada -uso sorted- ; sorted ([9,.66,7,-8,5,66,33,6,2,8,1,3]) ',sorted ([9,.66,7,-8,5,66,33,6,2,8,1,3]),'\n') # presenta una secuencia ordenada

print ('devolver la suma total de los valores de una secuencia -uso sum- ; sum ([0,1,2,3,4,5,6,7,8,9]) ',sum ([0,1,2,3,4,5,6,7,8,9]),'\n') # presenta la suma total de los valores de una secuencia

print ('devolver tuplas con elementos de cada secuencia indicada -uso zip- ; zip ([0,1,2,3,4,5,6,7,8,9],["CERO","UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"]) \n')

print ([x for x in zip ([0,1,2,3,4,5,6,7,8,9],["CERO","UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"])],'\n') # presenta una secuencia de tuplas (iterador1,iterador2) usando los iteradores indicados , lista por compresion


print ('devolver un iterador de una secuencia -uso iter- ; iteradorCadena = iter ("0123456789") \n')

iteradorCadena = iter ("0123456789") # devuelve un iterador de la secuencia indicada

print ('iterar iteradorCadena -uso next- next (iteradorCadena) \n')

suma = 0 # valor inicial a sumar

while True : # bucle while continuo
  try : # control de excepciones
    numeroEntero = int (next (iteradorCadena)) # coge el siguiente elemento del iterador -int , lo convierte en entero-
  except StopIteration : # tipo de excepcion
    print ('NO HAY MAS ELEMENTOS  \n') # presenta la cadena
    break # interrumpe el bucle while continuo
  print ('numeroEntero ',numeroEntero,'\n') # presenta el elemento iterador convertido a numero entero
  print('{} + {} = '.format(suma,numeroEntero)) # presenta la cadena formateada
  suma += numeroEntero # suma el valor del elemento al valor actual de suma
  print ('resultado → ',suma,'\n') # presenta la suma de los valores
  
print ('copia de una secuencia por asignacion -uso de = - ; copiaSecuencia = Iterador \n')

copiaSecuencia = Iterador # copia la secuencia por asignacion

print ('Iterador : {} - copiaSecuencia : {} \n'.format(Iterador,copiaSecuencia)) # presenta la cadena formateada con el contenido de los iteradores

print ('iterar las dos secuencias ; zip (Iterador,copiaSecuencia) \n')

for par in zip (Iterador,copiaSecuencia) : # iterador , bucle for in , pasa los elementos de la secuencia a par , zip devuelve una secuencia de tuplas (iterador1,iterador2) usando los iteradores indicados
  print (par,'\n') # presenta la tupla con un elemento de cada iterador
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('copia de un diccionario -uso de copy- ; Diccionario.copy () \n')

print ('iterar las dos secuencias ; zip (sorted(Diccionario),sorted(Diccionario.copy()) \n')

for parClaves in zip (sorted(Diccionario),sorted(Diccionario.copy())) : # iterador , bucle for in , pasa los elementos de la secuencia a parClaves , zip devuelve una secuencia de tuplas (iterador1,iterador2) usando los iteradores indicados , sorted ordena las claves
  print (parClaves,'\n') # presenta la tupla con un elemento de cada iterador
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('copia de set -uso de copy- ; conjuntoMutable.copy() \n')

print ('iterar las dos secuencias ; zip (conjuntoMutable,conjuntoMutable.copy()) \n')

for parSet in zip (conjuntoMutable,conjuntoMutable.copy()) : # iterador , bucle for in , pasa los elementos de la secuencia a parSet , zip devuelve una secuencia de tuplas (iterador1,iterador2) usando los iteradores indicados 
  print (parSet,'\n') # presenta la tupla con un elemento de cada iterador
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('importar modulo copy ; import copy \n')

import copy # importa el modulo indicado 

print ('hacer una copia con copy del modulo copy -copy.copy- ; copy.copy (lista) \n')

print ('iterar las dos secuencias ; zip (lista,copy.copy(lista)) \n')

for parLista in zip (lista,copy.copy(lista)) : # iterador , bucle for in , pasa los elementos de la secuencia a parLista , zip devuelve una secuencia de tuplas (iterador1,iterador2) usando los iteradores indicados 
  print (parLista,'\n') # presenta la tupla con un elemento de cada iterador
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('contenido de lista \n')

print (lista,'\n') # presenta el contenido 

print ('hacer una copia profunda con deepcopy del modulo copy -copy.deepcopy- ; copiaProfunda = copy.deepcopy (lista) \n')

copiaProfunda = copy.deepcopy (lista) # copia profunda de la secuencia indicada

print ('modificar lista \n')

for indice in range (len(lista)) : # iterador , bucle for in , pasa los elementos de la lista de numeros a indice , len devuelve el numero de elementos de la secuencia
  print ('lista [{0}] = {0} \n'.format(indice)) # presenta la cadena formateada con el valor indicado -numeros del 0 al 9-
  lista [indice] = indice # asigna el valor actual al indice indicado -modifica lista-
else : # cuando finaliza el iterador 
  print ('** FIN DE LA MODIFICACION DE lista **\n') # presenta el texto 

print ('iterar las dos secuencias ; zip (lista,copiaProfunda) \n')

for parLista1 in zip (lista,copiaProfunda) : # iterador , bucle for in , pasa los elementos de la secuencia a parLista1 , zip devuelve una secuencia de tuplas (iterador1,iterador2) usando los iteradores indicados 
  if parLista1 [0] != parLista1 [1] : # condicion , si no coinciden los dos elementos de la tupla
    print ('** PAR MODIFICADO ** ',parLista1,'\n') # presenta la cadena y el par modificado
    continue # vuelve al siguiente elemento del iterador
  print (parLista1,'\n') # presenta la tupla con un elemento de cada iterador
else : # cuando finaliza el iterador 
  print ('** FIN DE LA SECUENCIA **\n') # presenta el texto 

print ('contenido de lista \n')

print (lista,'\n') # presenta el contenido 

def generadorNOMBRESusuarios (nombreFichero) : # definicion de la funcion
  nombresUsuarios = set () # asigna conjunto -lista sin elementos repetidos-
  usuarios = {} # asigna diccionario vacio
  for lineaFichero in open (nombreFichero,'r') : # iterador , bucle for in , pasa el contenido del fichero a lineaFichero -linea a linea-
    linea = lineaFichero.rstrip () # devuelve una copia de la cadena con los espacios en blanco del final eliminados
    if linea : # condicion , si la linea no esta vacia -True-
      elementosLinea = linea.split (':') # separa la cadena por el caracter indicado y devuelve una lista con los elementos separados
      nombreUsuario = ((elementosLinea [1] + elementosLinea [2] + elementosLinea [3]).replace('-','').replace("'",'')) # reemplaza los caracteres indicados por un espacio en blanco -guion y comilla simple-
      nombreUsuario = nombreOriginal = nombreUsuario [: 8].lower () # convierte la subcadena a minusculas -8 caracteres-
      contador = 1 # contador
      while nombreUsuario in nombresUsuarios : # bucle while , mientras se cumpla la condicion -nombre de usuario en conjunto -set- nombresUsuarios- , cuenta el numero de usuarios con el mismo nombre y le asigna un numero
        nombreUsuario = "{0} {1}".format (nombreOriginal,contador) # asigna la cadena formateada con los valores indicados -nombre usuario y numero-
        contador += 1 # suma uno al valor actual del contador
      nombresUsuarios.add (nombreUsuario) # añade la cadena nombre de usuario numero al conjunto set 
      usuario = (nombreUsuario,elementosLinea [1],elementosLinea [2],elementosLinea [3],elementosLinea [0]) # tupla de elementos
      usuarios [(elementosLinea [3].lower(),elementosLinea [1].lower(),elementosLinea [0])] = usuario # asigna el nombre , ultimo apellido e id al diccionario de la tupla usuario -clave tupla en minusculas-
  anchoNombre = 32 # maximo numero de caracteres
  anchoNombreUsuario = 9 # maximo numero de caracteres
  print ('{0:<32} {1:^6} {2:9}'.format('NOMBRE','ID','NOMBRE_USUARIO',anchoNombre,anchoNombreUsuario)) # presenta la cadena formateada con los valores indicados -cadenas y ancho de espacio-
  print ('{0:-<32} {0:-<6} {0:9}'.format('',anchoNombre,anchoNombreUsuario))
  for clave in sorted(usuarios) : # iterador , bucle for in , pasa las claves del diccionario a clave
    usuario = usuarios [clave] # asigna el valor de la clave del diccionario
    inicial = '' # cadena vacia
    if usuario [2] : # condicion , si no es una cadena vacia -True-
      inicial = ' ' + usuario [2] [0] # añade el primer caracter de la cadena  
    nombre = '{0[3]} , {0[1]} {1}'.format (usuario,inicial) # cadena formateada con los valores indicados -nombre e inicial del usuario- 
    print ('{0:.<32} ({1[4]:4}) {1[0]:32}\n'.format(nombre,usuario,anchoNombre,anchoNombreUsuario)) # presenta la cadena formateada con los valores indicados -nombre del usuario , ID , usuario- 

print ('llamar a la funcion generadorNOMBRESusuarios ; generadorNOMBRESusuarios (\'./Escritorio/USUARIOS.txt\')\n')

generadorNOMBRESusuarios ('./Escritorio/USUARIOS.txt') # llama y ejecuta la funcion con el argumento indicado -ruta y nombre del fichero-

def estadisticaNumeros (nombreFichero) : # definicion de la funcion
  import math # importa el modulo indicado
  numeros = [] # asigna lista vacia
  fecruencias = collections.defaultdict (int) # devuelve un diccionario con el valor por defecto int -numero entero-
  for lineaNumero,linea in enumerate (open(nombreFichero),start=1) : # iterador , bucle for in , pasa las lineas del fichero a linea y los numeros a lineaNumero , enumerate numera las lineas del fichero , empieza en 1
    for numero in linea.split () :  # iterador , bucle for in , pasa los numeros de la lista a numero , split devuelve una lista con los numeros de la linea separada por sus espacios en blanco
      try : # control de excpciones
        NUMERO = float (numero) # convierte los numeros a punto flotante
        numeros.append (NUMERO) # añade el valor a la lista 
        fecruencias [NUMERO] += 1 # si la clave se encuentra en el diccionario le suma uno al valor actual y si no esta ; 1
      except ValueError as error : # tipo de excepcion , pasa la salida a error
         print ('FICHERO {0} : LINEA {1} : NUMERO {2} : ERROR {3}\n'.format(nombreFichero,lineaNumero,numero,error)) # presenta la cadena formateada y sus valores -nombre fichero , numero linea fichero , numero , error-
  if numeros : # condicion , si la lista no esta vacia -True-
    PROMEDIO = sum (numeros) / len (numeros) # suma todos los numeros de la lista y lo divide entre el numero de elementos de la lista
    fecruenciaAlta = max (fecruencias.values()) # devuelve el valor mas alto de la lista de valores del diccionario
    MODO = [Numero for Numero,frecuencia in fecruencias.items() if math.fabs (frecuencia - fecruenciaAlta) <= sys.float_info.epsilon] # lista por compresion condicional , items devuelve tuplas (clave,valor) , clave asignada a Numero y valor a frecuencia , si se cumple la condicion se añade a la lista -si el valor devuelto por math.fabs es menor o igual a la constante epsilon-
    if not (1 <= len (MODO) <= 3) : # condicion , si MODO NO tiene tres o mas elementos
      MODO = None # asigna valor None
    else : # si tiene 3 o mas elementos
      MODO.sort () # ordena la lista
    numeros = sorted (numeros) # ordena la lista
    media = len (numeros) // 2 # devuelve el resultado de la division truncada -numero entero-
    MEDIANA = numeros [media] # asigna el valor del indice indicado de la lista
    if len (numeros) % 2 == 0 : # condicion , si el numero de elementos es un numero par 
      MEDIANA = (MEDIANA + numeros [media - 1]) / 2 # asigna el resultado de la suma del valor actual mas el valor del indice indicado de la lista divido entre dos
    total = 0 # uso calculo variacion
    for NumerO in numeros : # iterador , bucle for in , pasa los numeros de la lista a NumerO
      total += ((NumerO - PROMEDIO) ** 2) # suma al valor actual el resultado de la operacion
    variacion = total / (len (numeros) - 1) # asigna el resultado de la operacion
    STD_DEV = math.sqrt (variacion) # asigna el resultado de la raiz del valor indicado
    contador = len (numeros) # contador , valor numero de elementos de la lista
    numeroReal = '9.2f' # valor formato cadena
    if MODO is None : # condicion , si el valor de MODO es None
      modoLinea = '' # asigna una cadena vacia
    elif len (MODO) == 1 : # condicion , si MODO contiene un elemento
      modoLinea = 'MODO = {0:{1}}\n'.format (MODO[0],numeroReal) # asigna la cadena formateada , el valor del indice y el formato
    else : # si tiene mas de un elemento
      modoLinea = ('MODO = [' + ', '.join (['{0:.2f}}'.format (modo) for modo in MODO]) + ']\n') # asigna la cadena formateada , convierte al formato indicado los valores de la lista MODO
    print ("""\
      CONTADOR = {0:6}
      PROMEDIO = {1:{5}}
      MEDIANA =  {2:{5}}
      {3}\
      STD_DEV =  {4:{5}}\n""".format(contador,PROMEDIO,MEDIANA,modoLinea,STD_DEV,numeroReal)) # presenta la cadena formateada con los valores indicados en el formato indicado
  else : # si la lista esta vacia  
    print ('NO SE ENCONTRARON NUMEROS\n') # presenta el texto

print ('llamar a la funcion estadisticaNumeros ; estadisticaNumeros (\'./Escritorio/numerosPROCESOS.txt\')\n')

estadisticaNumeros ('./Escritorio/numerosPROCESOS.txt') # llama y ejecuta la funcion con el argumento indicado -ruta y nombre del fichero-

















































