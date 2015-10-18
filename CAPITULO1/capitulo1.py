#!/usr/bin/env python3
'''breve intoduccion a la programacion por procedimientos'''

# importar modulo

import sys

print ('VERSION en uso de PYTHON\n')

print (sys.version, '\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

valor = 125.66 # asigna numero con decimales -float-

print (int (valor), '\n') # presenta el valor como numero entero sin decimales con int

cadena = 'esto es una cadena\n' # asigna una cadena con salto de linea

print (cadena) # presenta la cadena

print ('elemento de una cadena ; cadena [0] ',cadena [0], '\n') # presenta el elemento de la posicion indicada de la cadena

print ('subcadena de la cadena ; cadena [0 : 4] ',cadena [0 : 4], '\n') # presenta el tramo entre las posiciones 0 a 4 -4 NO incluido-

print ('convertir un valor en una cadena ; str (valor) ', str (valor), '\n') # presenta el valor convertido en una cadena

valorCadena = '125' # asigna cadena -entero-

print ('convertir la cadena en un valor con decimales ; float (valorCadena) ',float (valorCadena), '\n') # presenta la cadena convertida a un valor con decimales con float

print ('presentar contenidos variables ; valor,cadena,valorCadena ',valor,cadena,valorCadena, '\n') # presenta el contenido de las variables

print ('tipo variable ; type (valor) ',type (valor), '\n') # presenta el tipo de valor de la variable con type

print ('tipo variable ; type (cadena) ',type (cadena), '\n') # presenta el tipo de valor de la variable con type

print ('tipo variable ; type (valorCadena) ',type (valorCadena), '\n') # presenta el tipo de valor de la variable con type

print ('tipo valor ; type (1000) ',type (1000), '\n') # presenta el tipo de valor con type

print ('tipo valor ; type (.10) ',type (.10), '\n') # presenta el tipo de valor con type

print ('tipo valor ; type ("1000") ',type ("1000"), '\n') # presenta el tipo de valor con type

tupla = ('cadena',100, .9, '200') # tupla -valores inmutables , NO se pueden cambiar-

lista = ['cadena',100, .9, '200'] # lista -valores mutables , SE pueden cambiar-

print ('tipo tupla , type (tupla) ', type (tupla), '\n') # presenta el tipo de la referencia

print ('tipo tupla , type (lista) ', type (lista), '\n') # presenta el tipo de la referencia

print ('len () devuelve el numero de elementos de una secuencia ; len (tupla)',len (tupla), '\n' )

print ('len () devuelve el numero de elementos de una secuencia ; len (lista)',len (lista), '\n' )

print ('len () devuelve el numero de elementos de una secuencia ; len (cadena)',len (cadena), '\n' )

print ('len () devuelve el numero de elementos de una secuencia ; len (valorCadena)',len (valorCadena), '\n' )

print ('len () devuelve el numero de elementos de una secuencia ; len ("numero de elementos de esta cadena")',len ("numero de elementos de esta cadena"), '\n' )

print ('añadir elementos a una lista ; lista.append ("penultimo elemento")\n')

lista.append ("penultimo elemento") # añade la cadena al final dde la lista

print ('contenido de lista ', lista, '\n') # presenta el contenido de la lista

print ('añadir elementos a la lista mediante tipos ; list.append (lista,"ultimo elemento")\n')

list.append (lista,"ultimo elemento") # añade el elemento a la lista usando el tipo de dato

print ('contenido de lista ', lista, '\n') # presenta el contenido de la lista

print ('insertar un elemento en la posicion indicada de lista ; lista.insert (1,"uno")\n')

lista.insert (1,"uno") # inserta en la posicion indicada la cadena indicada

print ('contenido de lista ', lista, '\n') # presenta el contenido de la lista

print ('presentar el elemento de la posicion 1 de lista ; lista [1] ',lista [1], '\n') # presenta el valor de la posicion indicada 

print ('eliminar un elemento de la lista con remove ; lista.remove ("cadena")\n')

lista.remove ("cadena") # elimina el elemento indicado de la lista

print ('contenido de lista ', lista, '\n') # presenta el contenido de la lista

print ('presentar el elemento de un posicion indicada en una tupla ; tupla [1] ',tupla [1], '\n') # presenta el elemento de la tupla indicado en la posicion

print ('cambiar el elemento de una posicion de la lista ; lista [1] = "CIEN"\n')

lista [1] = "CIEN" # cambia el elemento de la posicion indicada por el indicado

print ('contenido de lista ', lista, '\n') # presenta el contenido de la lista

Lista = ['cadena',100, .9, '200']  # lista -valores mutables , SE pueden cambiar- 

LISTA = ['cadena',100, .9, '200']  # lista -valores mutables , SE pueden cambiar- 

print ('contenido de Lista ', Lista, '\n') # presenta el contenido de la lista

print ('contenido de LISTA ', LISTA, '\n') # presenta el contenido de la lista

print ('comparar si dos objetos son el mismo ; Lista is LISTA ',Lista is LISTA, '\n') # presenta False al no ser la misma lista

print ('asignar el mismo objeto a LISTA ; LISTA = Lista\n')

LISTA = Lista # asigna el bjeto indicado

print ('comparar si dos objetos son el mismo ; Lista is LISTA ',Lista is LISTA, '\n') # presenta True al ser la misma lista

cualquiera = 'cualquiera' # asigna cadena

nulo = None # asigna valor nulo

print ('contenido de cualquiera ', cualquiera, '\n') # presenta el contenido de la variable

print ('contenido de nulo ', nulo, '\n') # presenta el contenido de la variable

print ('comprobar si el contenido es del objeto -variable- ; cualquiera is "cualquiera" ',cualquiera is "cualquiera", '\n' )  # presenta True al ser el contenido

print ('comprobar si el contenido es del objeto -variable- ; nulo is None ',nulo is None, '\n' )  # presenta True al ser el contenido

print ('comprobar si el contenido es del objeto -variable- ; cualquiera is not None ',cualquiera is not None, '\n' )  # presenta True al NO ser el contenido

print ('comprobar si el contenido es del objeto -variable- ; nulo is not None ',nulo is not None, '\n' )  # presenta False al ser el contenido

CUALQUIERA = "cualquiera" # asigna cadena

print ('contenido de CUALQUIERA ', CUALQUIERA, '\n') # presenta el contenido de la variable

print ('comparar si los dos objetos son los mismo ; cualquiera is CUALQUIERA ',cualquiera is CUALQUIERA, '\n' ) # presenta True al ser el mismo objeto 

cero = 0 # asigna valor entero

uno = 1 # asigna valor entero

seis = 6 # asigna valor entero

print ('contenido de cero ', cero, '\n') # presenta el contenido de la variable

print ('contenido de uno ', uno, '\n') # presenta el contenido de la variable

print ('contenido de seis ', seis, '\n') # presenta el contenido de la variable

print ('cero mayor que uno ; cero > uno ',cero > uno, '\n' )  # presenta False al NO serlo 

print ('seis menor que uno ; seis < uno ',seis < uno, '\n' )  # presenta False al NO serlo

print ('seis menor o igual que uno ; seis <= uno ',seis <= uno, '\n' )  # presenta False al NO serlo

print ('seis mayor o igual que uno ; seis >= uno ',seis >= uno, '\n' )  # presenta True al ser mayor

print ('seis igual que uno ; seis == uno ',seis == uno, '\n' )  # presenta False al NO serlo

print ('seis igual seis ; seis == seis ',seis == seis, '\n' )  # presenta True al ser iguales

print ('comprobar si un elemento pertenece a una secuencia -lista- ; 100 in LISTA ',100 in LISTA, '\n' ) # presenta True al pertenecer a la lista

print ('comprobar si un elemento pertenece a una secuencia -lista- ; 1 in LISTA ',1 in LISTA, '\n' ) # presenta False al NO pertenecer a la lista

print ('comprobar si un elemento pertenece a una secuencia -cadena- ; "a" in cualquiera ',"a" in cualquiera, '\n' ) # presenta True al pertenecer a la cadena

print ('comprobar si un elemento pertenece a una secuencia -cadena- ; "1" in cualquiera ',"1" in cualquiera, '\n' ) # presenta False al NO pertenecer a la cadena

print ('comprobar si un elemento NO pertenece a una secuencia -cadena- ; "a" not in cualquiera ',"a" not in cualquiera, '\n' ) # presenta False al pertenecer a la cadena

print ('comprobar si un elemento pertenece a una secuencia -cadena- ; "1" not in cualquiera ',"1" not in cualquiera, '\n' ) # presenta True al NO pertenecer a la cadena

print ('comprobar si un elemento NO pertenece a una secuencia -lista- ; 100 not in LISTA ',100 not in LISTA, '\n' ) # presenta False al pertenecer a la lista

print ('comprobar si un elemento NO pertenece a una secuencia -lista- ; 1 not in LISTA ',1 not in LISTA, '\n' ) # presenta True al NO pertenecer a la lista

print ('comparacion logica -uso de and- ; cero and uno ',cero and uno, '\n' ) # presenta el valor menor ; 0 -si los dos valores son True-

print ('comparacion logica -uso de and- ; seis and uno ',seis and uno, '\n' ) # presenta el valor menor ; 1 -si los dos valores son True-

print ('comparacion logica -uso de and- ; seis and seis ',seis and seis, '\n' ) # presenta el valor menor ; 6 -si los dos valores son True-

print ('comparacion logica -uso de or- ; cero or uno ',cero or uno, '\n' ) # presenta el valor mayor ; 0 -si uno de los valores es True-

print ('comparacion logica -uso de or- ; seis or uno ',seis or uno, '\n' ) # presenta el valor mayor ; 1 -si uno de los valores es True-

print ('comparacion logica -uso de or- ; seis or seis ',seis or seis, '\n' ) # presenta el valor mayor ; 6 -si uno de los valores es True-

print ('comparacion logica -uso de not- ; not cero ', not cero , '\n' ) # presenta True ; not (negacion) -False tiene valor cero y True tiene valor 1-

print ('comparacion logica -uso de not- ; not (seis and uno) ',not (seis and uno), '\n' ) # presenta False ; not (negacion) -si los dos valores son True-

print ('comparacion logica -uso de not- ; not (seis or uno) ',not (seis or uno), '\n' ) # presenta False ; not (negacion) -si uno de los valores es True-

tuplaVacia = () # asigna tupla vacia

listaVacia = [] # asigna lista vacia

cadenaVacia = "" # asigna cadena vacia

falso = 0 # asigna valor int

verdadero = 1 # asigna valor int 

print ('contenido de tuplaVacia ', tuplaVacia, '\n') # presenta el contenido

print ('contenido de listaVacia ', listaVacia, '\n') # presenta el contenido

print ('contenido de cadenaVacia ', cadenaVacia, '\n') # presenta el contenido

print ('contenido de falso ', falso, '\n') # presenta el contenido

print ('contenido de verdadero ', verdadero, '\n') # presenta el contenido

print ('uso de if -condicion- :\n')

if tuplaVacia : # condicion , verdadero -True-
    print ('NO es una tupla vacia ', tuplaVacia, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES UNA TUPLA VACIA ', tuplaVacia, '\n') # presenta el texto y su valor

if listaVacia : # condicion , verdadero -True-
    print ('NO es una lista vacia ', listaVacia, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES UNA LISTA VACIA ', listaVacia, '\n') # presenta el texto y su valor

if cadenaVacia : # condicion , verdadero -True-
    print ('NO es una cadena vacia ', cadenaVacia, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES UNA CADENA VACIA ', cadenaVacia, '\n') # presenta el texto y su valor

if falso : # condicion , verdadero -True-
    print ('NO es False ', falso, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES False ', falso, '\n') # presenta el texto y su valor

if verdadero : # condicion , verdadero -True-
    print ('ES True ', verdadero, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('NO ES True ', verdadero, '\n') # presenta el texto y su valor

if tupla : # condicion , verdadero -True-
    print ('NO es una tupla vacia ', tupla, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES UNA TUPLA VACIA ', tupla, '\n') # presenta el texto y su valor

if lista : # condicion , verdadero -True-
    print ('NO es una lista vacia ', lista, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES UNA LISTA VACIA ', lista, '\n') # presenta el texto y su valor

if cadena : # condicion , verdadero -True-
    print ('NO es una cadena vacia ', cadena, '\n') # presenta el texto y su valor
else : # falso -False-
    print ('ES UNA CADENA VACIA ', cadena, '\n') # presenta el texto y su valor

if seis == 0 : # condicion , verdadero -True- 
    print ('-version if- el valor de seis es : ', seis, '\n') # presenta el texto y su valor
elif seis == 6 : # 2ª condicion , verdadero -True-
    print ('-version elif- el valor de seis es : ', seis, '\n') # presenta el texto y su valor
else : # si no se cumplen una de las dos condiciones -if,elif- 
    print ('-version else- el valor de seis es : ', seis, '\n') # presenta el texto y su valor    

print ('bucle mientras se cumpla una condicion ; while\n')

indice = 0 # asigna valor int -uso en while-

while True : # bucle while continuo 
    print ('ELEMENTO de lista ',lista [indice], '\n') # presenta el texto y su valor -elemento de la lista-
    indice += 1 # suma uno al valor actual
    if indice == len (lista) : # condicion , si el valor de indice es mayor al numero de elementos de lista
        print ('-- FIN DE LA LISTA --\n') # presenta el texto
        break # interrumpe el bucle  

posicion = 0 # asigna valor int -uso en while-

while posicion <= len (lista) - 1 : # bucle while , condicion ; mientras el valor de posicion sea menor o igual al numero de elementos de la lista restandole uno 
    print ('ELEMENTO de lista ',lista [posicion], '\n') # presenta el texto y su valor -elemento de la lista-
    posicion += 1 # suma uno al valor actual
else : # cuando finalice el bucle 
    print ('-- FIN DE LA LISTA --\n') # presenta el texto

print ('iterar una secuencia mediante for in \n')

for Elemento in LISTA : # iterador , bucle for in , pasa los elementos de la lista a la variable ; Elemento
    print ('elemento de LISTA > ', Elemento, '\n')
else : # cuando finalice el iterador
    print ('-- FIN DE LA LISTA --\n')

for caracter in cadena : # iterador , bucle for in , pasa los caracteres de la cadena a la variable ; caracter
    if caracter == ' ' or caracter == '\n': # condicion , si es un espacio en blanco o un salto de linea
        continue # vuelve al siguiente elemento de la secuencia
    if caracter in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'] : # condicion , si el valor esta en la lista 
        print ('el caracter es una VOCAL > ', caracter, '\n') # presenta el texto y su valor -vocal-
    else : # si no esta en la lista 
        print ('el caracter es una CONSONANTE > ', caracter, '\n') # presenta el texto y su valor -consonante- 
else : # cuando finalice el iterador
    print ('-- FIN DE LA SECUENCIA DE LA CADENA --\n') # presenta el texto

print ('control de excepciones -errores- con try / except\n')

try : # control de excepciones
    9 / 0 # division por cero -lanza excepcion-
except ZeroDivisionError : # tipo de excepcion
    print ('** ERROR DIVISION POR CERO ** no se puede dividir por cero\n') # presenta el texto
    
try : # control de excepciones
    9 / 0 # division por cero -lanza excepcion-
except ZeroDivisionError as Salida : # tipo de excepcion , pasa la salida de la excepcion a Salida
    print ('** ERROR DIVISION POR CERO ** no se puede dividir por cero\n') # presenta el texto
    print (Salida, '\n') # presenta la salida de la excepcion indicada

try : # control de excepciones
    9 / 0 # division por cero -lanza excepcion-
except : # tipo de excepcion general
    print ('** ERROR DIVISION POR CERO ** no se puede dividir por cero\n') # presenta el texto
    
print ('operadores aritmeticos basicos ; + suma , - resta , * multiplicacion , / division\n')

print ('suma\n') # presenta el texto

print ('uno + seis ',uno + seis, '\n' ) # presenta el texto y su valor -suma los valores-

print ('seis += 1\n')

seis += 1 # asignacion aumentada -suma 1 al valor de seis-

print ('seis ', seis, '\n') # presenta el texto y su valor -7 , el valor de la variable mas el asignado mediante las suma-

print ('lista += "suma" ', '\n' )

lista += "suma" # añade los caracteres de la cadena a la lista

print ('lista ', lista, '\n') # presenta el texto y su valor -la lista con los caracteres añadidos de la cadena

print ('lista + ["suma"] ',lista + ["suma"], '\n' ) # presenta el texto y su valor -une las dos listas en una-

print ('cadena [ : -1] + cualquiera ',cadena [ : -1] + cualquiera, '\n' ) # presenta el texto y su valor -une las dos cadenas en una-

print ('resta\n') # presenta el texto

print ('seis - uno ',seis - uno, '\n' ) # presenta el texto y su valor -resta los valores-

print ('seis ', seis, '\n') # presenta el texto y su valor

print ('seis -= 1\n')

seis -= 1 # asignacion aumentada -resta 1 al valor de seis-

print ('seis ', seis, '\n') # presenta el texto y su valor -5 , el valor de la variable mas el asignado mediante las resta-

print ('multiplicacion\n') # presenta el texto

print ('seis * seis ',seis * seis, '\n' ) # presenta el texto y su valor -multiplica los valores-

print ('seis *= 2\n')

seis *= 2 # asignacion aumentada -multiplica 2 al valor de seis-

print ('seis ', seis, '\n') # presenta el texto y su valor -12 , el valor de la variable mas el asignado mediante la multiplicacion-

print ('lista *= 3 ', '\n' )

lista *= 3 # repite la lista tres veces

print ('lista ', lista, '\n') # presenta el texto y su valor -la lista repetida tres veces-

print ('division\n') # presenta el texto

print ('uno / seis ',uno / seis, '\n' ) # presenta el texto y su valor -divide los valores-

print ('seis ', seis, '\n') # presenta el texto y su valor

print ('seis /= 2\n')

seis /= 2 # asignacion aumentada -divide por 2 al valor de seis-

print ('seis ', seis, '\n') # presenta el texto y su valor -3 , el valor de la variable mas el asignado mediante las division-

print ('teclee un numero entero seguido de enter o enter para salir\n') # presenta el texto

total = 0 # asigna valor int

contador = 0 # asigna valor int

while True : # bucle while continuo
    entradaTeclado = input ('ENTERO :') # espera entrada teclado 
    if entradaTeclado : # no es una cadena vacia
        try : # control de excepciones
            numero = int (entradaTeclado) # asigna un numero entero devuelto por int -cambia el formato cadena a digito-
        except ValueError as error : # tipo de excepcion , pasa la salida a error
            print ('tiene que ser un  numero entero\n') # presenta el texto 
            print (error, '\n') # presenta la salida de la excepcion indicada
            continue # vuelve al inicio del bucle while
        total += numero # suma el valor de numero al valor actual de total
        contador += 1 # suma uno al valor actual
    else : # es una cadena vacia
        break # interrumpe el bucle while
        
if contador : # condicion , si es True -NO cero-
    print ('contador =', contador, 'total =', total, 'media =', total / contador, '\n') # presenta los valores finales de contador , total y el resultado de su division
    
print ('entrada numeros enteros desde otro fichero , ejemplo ; capitulo1 < ficheo datos\n') # presenta el texto

Total = 0 # asigna valor int

Contador = 0 # asigna valor int
'''
while True : # bucle while continuo
    EntradaTeclado = input () # espera entrada datos desde fichero externo 
    if EntradaTeclado : # no es una cadena vacia
        try : # control de excepciones
            Numero = int (EntradaTeclado) # asigna un numero entero devuelto por int -cambia el formato cadena a digito-
        except ValueError as error : # tipo de excepcion , pasa la salida a error
            print ('tiene que ser un  numero entero\n') # presenta el texto 
            print (error, '\n') # presenta la salida de la excepcion indicada
            continue # vuelve al inicio del bucle while
        except EOFError :  # tipo de excepcion , error fin de archivo -no contiene mas datos-
            break # interrumpe el bucle while
        Total += Numero # suma el valor de Numero al valor actual de Total
        Contador += 1 # suma uno al valor actual
'''
if Contador : # condicion , si es True -NO cero-
    print ('contador =', Contador, 'total =', Total, 'media =', Total / Contador, '\n') # presenta los valores finales de contador , total y el resultado de su division

print ('entrada numeros enteros desde otro fichero -version bloques try / except anidados- , ejemplo ; capitulo1 < ficheo datos\n') # presenta el texto

Total1 = 0 # asigna valor int

Contador1 = 0 # asigna valor int
'''
while True : # bucle while continuo
    try : # control de excepciones 
        EntradaTeclado1 = input () # espera entrada datos desde fichero externo 
        if EntradaTeclado1 : # no es una cadena vacia
            try : # control de excepciones anidado 
                Numero1 = int (EntradaTeclado1) # asigna un numero entero devuelto por int -cambia el formato cadena a digito-
            except ValueError as error : # tipo de excepcion , pasa la salida a error
                print ('tiene que ser un  numero entero\n') # presenta el texto 
                print (error, '\n') # presenta la salida de la excepcion indicada
                continue # vuelve al inicio del bucle while
        Total1 += Numero1 # suma el valor de Numero1 al valor actual de Total1
        Contador1 += 1 # suma uno al valor actual    
    except EOFError :  # tipo de excepcion , error fin de archivo -no contiene mas datos-
        break # interrumpe el bucle while
'''    
if Contador1 : # condicion , si es True -NO cero-
    print ('contador =', Contador1, 'total =', Total1, 'media =', Total1 / Contador1, '\n') # presenta los valores finales de contador , total y el resultado de su division

print ('crear una funcion con def\n')

def cogerEntero (mensaje) : # definicion de la funcion
    while True : # bucle while continuo
        try : # control de excepciones
            entrada = int (input(mensaje)) # asigna el argumento del parametro a input -mensaje entrada teclado- , int cambia el formato de cadena a digito de la entrada de teclado
            return entrada # devuelve mensaje presentado por la entrada de teclado
        except ValueError as Error : # tipo de excepcion , pasa la salida a Error
            print ('tiene que ser un numero entero\n') # presenta el texto
            print (Error, '\n') # presenta la salida de la excepcion indicada
            break # interrumpe el bucle
            
cogerEntero ('ponga un numero ') # llama y ejecuta la funcion con el argumento indicado

print ('importar modulos mediante import\n')

print ('nombre del programa ejecutado ', sys.argv, '\n') # presenta el nombre del fichero llamado a ejecutar

# importar modulo

import random # importa el modulo indicado

for x in range (5) : # iterador , bucle for in , pasa los elementos de la lista a ; x
    print (random.randint(1, 6), '\n') # presenta un numero entero aleatorio en el rango indicado
else : # cuando finalice el iterador
    print ('-- FIN random --\n') # presenta el texto

for X in range (5) : # iterador , bucle for in , pasa los elementos de la lista a ; X
    print (random.choice(['manzana', 'banana', 'platano', 'pera', 'queso', 'tomate']), '\n') # presenta una cadena aleatoria de las indicadas en la lista
else : # cuando finalice el iterador
    print ('-- FIN random --\n') # presenta el texto

CERO = ['  ***  ', 
        ' *   * ', 
        '*     *', 
        '*     *', 
        '*     *',
        ' *   * ',
        '  ***  '] # lista -numero cero 0-

UNO = ['   *  ', 
       '  **  ', 
       '   *  ', 
       '   *  ', 
       '   *  ',
       '   *  ',
       '  *** '] # lista -numero uno 1-
 
DOS = ['  ***  ', 
       '     **', 
       '     **', 
       ' **    ', 
       '*      ',
       '**     ',
       '  **** '] # lista -numero dos 2-
 
TRES = ['  ***  ',  
        '     **', 
        '      *', 
        '   ****', 
        '      *',
        '     **',
        '  ***  '] # lista -numero tres 3-

CUATRO = ['**    *', 
          '**    *', 
          '**    *', 
          '*******', 
          '     **',
          '     **',
          '     **'] # lista -numero cuatro 4-
 
CINCO = ['****** ',
         '**     ', 
         '**     ', 
         '*****  ', 
         '     **',
         '     **',
         '****** '] # lista -numero cinco 5-

SEIS = ['  **** ',
        '**     ', 
        '**     ', 
        '*****  ', 
        '**   **',
        '**   **',
        '  ***  '] # lista -numero seis 6-

SIETE = ['*******', 
         '*******', 
         '     **', 
         '    ** ', 
         '   **  ',
         '  **   ',
         ' **    '] # lista -numero siete 7-

OCHO = ['  ***  ',
        '*     *', 
        ' *   * ', 
        '  ***  ', 
        ' *   * ',
        '*     *',
        '  ***  '] # lista -numero ocho 8-

NUEVE = [' ***** ', 
         '*     *', 
         '*     *', 
         ' ***** ', 
         '    ** ',
         '   **  ',
         '  **   '] # lista -numero nueve 9-

def numerosGrandes (numero) : # definicion de la funcion
    assert type (numero) == str, 'el argumento de numero tiene que ser un numero entero en formato cadena\n' # regla de excepcion , si no se cumple lanza excepcion
    listaNumeros = [] # lista vacia , se asignan las listas de digitos que integran el parametro numero
    for digito in numero : # iterador , bucle for in , pasa los digitos a ; digito
        if digito == '0' : # condicion , si es igual al valor indicado
            listaNumeros.append (CERO) # añade la lista indicada a listaNumeros
        elif digito == '1' : # condicion , si es igual al valor indicado
            listaNumeros.append (UNO) # añade la lista indicada a listaNumeros
        elif digito == '2' : # condicion , si es igual al valor indicado
            listaNumeros.append (DOS) # añade la lista indicada a listaNumeros
        elif digito == '3' : # condicion , si es igual al valor indicado
            listaNumeros.append (TRES) # añade la lista indicada a listaNumeros
        elif digito == '4' : # condicion , si es igual al valor indicado
            listaNumeros.append (CUATRO) # añade la lista indicada a listaNumeros
        elif digito == '5' : # condicion , si es igual al valor indicado
            listaNumeros.append (CINCO) # añade la lista indicada a listaNumeros
        elif digito == '6' : # condicion , si es igual al valor indicado
            listaNumeros.append (SEIS) # añade la lista indicada a listaNumeros
        elif digito == '7' : # condicion , si es igual al valor indicado
            listaNumeros.append (SIETE) # añade la lista indicada a listaNumeros
        elif digito == '8' : # condicion , si es igual al valor indicado
            listaNumeros.append (OCHO) # añade la lista indicada a listaNumeros
        elif digito == '9' : # condicion , si es igual al valor indicado
            listaNumeros.append (NUEVE) # añade la lista indicada a listaNumeros
    numeroDigitos = range (len(listaNumeros)) # devuelve una lista de numeros con el numero de elementos de la lista -cero al penultimo elemento- 
    for POSICION in range (7) : # iterador , bucle for in , pasa los elementos de la lista a ; POSICION -posicion de la lista-
        for columna in numeroDigitos : # iterador , bucle for in , pasa los elementos de la lista a ; columna -NUMERO-
            if columna == 0 : # condicion , asigna la lista de la posicion 0 -columna- y su indice -POSICION- de listaNumeros
               DIGITOS = listaNumeros [columna] [POSICION] + '  ' # asigna el elemento de sublista y posicion indicada   
            if columna != 0 : # condicion , las siguientes columnas se añaden de listaNumeros
                DIGITOS += listaNumeros [columna] [POSICION] + '  ' # añade las siguientes sublistas y posiciones de listaNumeros
        print (DIGITOS) # presenta los elementos de las sublistas con las misma posicion en una sola linea -cadena-
    else : # cuando finalice el iterador 
        print ('\n') # salto de linea

numerosGrandes ('1015') # llama y ejecuta la funcion con el argumento indicado

numerosGrandes ('0123456789') # llama y ejecuta la funcion con el argumento indicado

def cuadriculaNumerosAleatorios (columnas, lineas, valorMaximo) : # definicion de la funcion
    assert type (columnas) == int, 'columnas debe ser un numero entero\n' # regla de excepcion , si no se cumple lanza excepcion
    assert type (lineas) == int, 'lineas debe ser un numero entero\n' # regla de excepcion , si no se cumple lanza excepcion
    assert type (valorMaximo) == int, 'valorMaximo debe ser un numero entero\n' # regla de excepcion , si no se cumple lanza excepcion
    numerosAleatorios = [] # lista vacia , añade los numeros aleatorios devueltos por random.randint
    lineaAleatorios = '' # cadena vacia , añade los numeros aleatorios en formato cadena
    for linea in range(lineas) : # iterador , bucle for in , pasa los elementos de la lista a ; linea -numero de lineas de numeros aleatorios a presentar-
        contador = 0 # cuenta el numero de columnas añadidas a la linea de numeros aleatorios
        while True : # bucle while continuo
            aleatorio = random.randint(1, valorMaximo) # devuelve un numero entero aleatorio dentro del rango indicado -1 al valor de valorMaximo-
            if aleatorio in numerosAleatorios : # condicion , si el numero aleatorio esta en la lista 
                continue # vuelve al inicio del bucle while -genera otro numero aleatorio-
            else : # si no esta en la lista
                numerosAleatorios.append (aleatorio) # lo añade a la lista de numeros aleatorios
                if not lineaAleatorios : # condicion ,  si la cadena esta vacia 
                    lineaAleatorios = str (aleatorio) + ' ' # asigna el numero aleatorio en formato cadena mas un espacio en blanco
                else : # si la cadena no esta vacia
                    lineaAleatorios += str (aleatorio) + ' ' # añade el siguiente numero aleatorio en formato cadena mas un espacio en blanco
                contador += 1 # suma uno al valor actual de contador 
            if contador == columnas : # condicion , si el valor es igual al de las columnas de la linea de numeros aleatorios 
                print (lineaAleatorios) # presenta una linea de numeros aleatorios -NO REPETIDOS- en formato cadena 
                lineaAleatorios = '' # asigna una cadena vacia de nuevo a lineaAleatorios , para la siguiente linea
                break # interrumpe el bucle while continuo para iterar la siguiente linea de numeros aleatorios
    else : # cuando finalice el iterador
        print ('\n-- FIN CUADRICULA NUMEROS ALEATORIOS --\n') # presenta el texto

cuadriculaNumerosAleatorios (5, 5, 100) # llama y ejecuta la funcion con el argumento indicado

cuadriculaNumerosAleatorios (10, 10, 100) # llama y ejecuta la funcion con el argumento indicado

def numerosGrandes1 (numero) : # definicion de la funcion
    assert type (numero) == str, 'el argumento de numero tiene que ser un numero entero en formato cadena\n' # regla de excepcion , si no se cumple lanza excepcion
    listaNumeros = [] # lista vacia , se asignan las listas de digitos que integran el parametro numero
    for digito in numero : # iterador , bucle for in , pasa los digitos a ; digito
        if digito == '0' : # condicion , si es igual al valor indicado
            listaNumeros.append (CERO) # añade la lista indicada a listaNumeros
        elif digito == '1' : # condicion , si es igual al valor indicado
            listaNumeros.append (UNO) # añade la lista indicada a listaNumeros
        elif digito == '2' : # condicion , si es igual al valor indicado
            listaNumeros.append (DOS) # añade la lista indicada a listaNumeros
        elif digito == '3' : # condicion , si es igual al valor indicado
            listaNumeros.append (TRES) # añade la lista indicada a listaNumeros
        elif digito == '4' : # condicion , si es igual al valor indicado
            listaNumeros.append (CUATRO) # añade la lista indicada a listaNumeros
        elif digito == '5' : # condicion , si es igual al valor indicado
            listaNumeros.append (CINCO) # añade la lista indicada a listaNumeros
        elif digito == '6' : # condicion , si es igual al valor indicado
            listaNumeros.append (SEIS) # añade la lista indicada a listaNumeros
        elif digito == '7' : # condicion , si es igual al valor indicado
            listaNumeros.append (SIETE) # añade la lista indicada a listaNumeros
        elif digito == '8' : # condicion , si es igual al valor indicado
            listaNumeros.append (OCHO) # añade la lista indicada a listaNumeros
        elif digito == '9' : # condicion , si es igual al valor indicado
            listaNumeros.append (NUEVE) # añade la lista indicada a listaNumeros
    numeroDigitos = range (len(listaNumeros)) # devuelve una lista de numeros con el numero de elementos de la lista -cero al penultimo elemento- 
    for POSICION in range (7) : # iterador , bucle for in , pasa los elementos de la lista a ; POSICION -posicion de la lista-
        for columna in numeroDigitos : # iterador , bucle for in , pasa los elementos de la lista a ; columna -NUMERO-
            if numero [columna] == '0' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '0' # asigna el digito en formato cadena
            elif numero [columna] == '1' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '1' # asigna el digito en formato cadena 
            elif numero [columna] == '2' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '2' # asigna el digito en formato cadena
            elif numero [columna] == '3' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '3' # asigna el digito en formato cadena
            elif numero [columna] == '4' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '4' # asigna el digito en formato cadena
            elif numero [columna] == '5' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '5' # asigna el digito en formato cadena
            elif numero [columna] == '6' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '6' # asigna el digito en formato cadena
            elif numero [columna] == '7' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '7' # asigna el digito en formato cadena
            elif numero [columna] == '8' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '8' # asigna el digito en formato cadena    
            elif numero [columna] == '9' : # condicion , si coincide la posicion de la cadena con el digito indicado
                valorColumna = '9' # asigna el digito en formato cadena
            cambiarAsteriscos = '' # asigna una cadena vacia 
            for DIGITO in listaNumeros [columna] [POSICION] : # iterador , bucle for in , pasa los elementos de la cadena a ; DIGITO
                if DIGITO == '*' : # condicion , si la subcadena es un asterisco
                    if not cambiarAsteriscos : # condicion , si la cadena esta vacia
                        cambiarAsteriscos = valorColumna # asigna el valor correspondiente -digito en formato cadena-
                        continue # vuelve al siguiente elemento de la cadena
                    else : # si la cadena NO esta vacia
                        cambiarAsteriscos += valorColumna # añade el valor valor correspondiente -digito en formato cadena- a la cadena
                        continue # vuelve al siguiente elemento de la cadena
                cambiarAsteriscos += DIGITO # añade el valor valor correspondiente -la subcadena de la cadena- a la cadena (no lo cambia al no ser un asterisco) 
            if columna == 0 : # condicion , si es la primera columna -cadena- , asigna la cadena a la variable 
               DIGITOS = cambiarAsteriscos + '  ' # asigna la nueva cadena modificada -los asteriscos cambiados por el digito correspondiente- mas el espacio en blanco   
            if columna != 0 : # condicion , si no es la primera columna -cadena- las siguientes cadenas se añaden consecutivas
                DIGITOS += cambiarAsteriscos + '  ' # añade la nueva cadena modificada -los asteriscos cambiados por el digito correspondiente- mas el espacio en blanco   
        print (DIGITOS) # presenta los elementos de las sublistas con las misma posicion en una sola linea -cadena-
    else : # cuando finalice el iterador 
        print ('\n') # salto de linea

numerosGrandes1 ('1015') # llama y ejecuta la funcion con el argumento indicado

numerosGrandes1 ('0123456789') # llama y ejecuta la funcion con el argumento indicado

def calcular () : # definicion de la funcion 
    listaDEnumeros = [] # lista vacia , se añaden los numeros introducidos
    while True : # bucle while continuo
        entrada_Teclado = input ('introduzca un numero y pulse enter -salir solo enter- ') # espera entrada teclado
        if not entrada_Teclado : # condicion , si es una cadena vacia
            if not listaDEnumeros : # condicion , si la lista esta vacia
                print ('lista vacia', listaDEnumeros, '\n') # presenta la cadena y su valor -lista vacia-
                break # interrumpe el bucle while
            listaOrdenada = sorted (listaDEnumeros) # ordena la lista
            suma = 0 # asigna valor int 
            for x in listaDEnumeros : # iterador , bucle for in , pasa los elementos de la lista a ; x 
                suma += x # suma  el valor de x al valor actual de suma -suma todos los numeros de la lista-
            print ('numeros introducidos : ', listaDEnumeros, '\n') # presenta la cadena y su valor -lista de numeros introducidos-
            print ('cantidad de numeros introducidos : {} , suma total numeros : {} , numero mas bajo : {} , numero mas alto : {} , media : {}\n'.format (len(listaDEnumeros), suma, listaOrdenada[0],listaOrdenada[-1], suma / len(listaDEnumeros))) # presenta la cadena formateada y sus valores
            break # interrumpe el bucle while
        listaDEnumeros.append (int(entrada_Teclado)) # añade los numeros a la lista


calcular () # llama y ejecuta la funcion 

def frasesAleatorias (numeroLineas=5) : # definicion de la funcion 
    if numeroLineas > 10 : # condicion , si es mas del numero indicado
        numeroLineas = 10 # asigna el numero maximo 
    articulos = ['el','la', 'los', 'ella', 'ellos', 'nosotros', 'vosotros', 'yo'] # asigna la lista de articulos
    sujetos = ['hombre', 'hombres', 'mujer', 'mujeres', 'niño', 'niños', 'perro', 'gato'] # asigna la lista de sujetos
    adverbios = ['tranquilo', 'nervioso', 'alto', 'bajo', 'delgado', 'grueso', 'joven', 'viejo'] # asigna la lista de adverbios
    verbos = ['correr', 'parar', 'subir', 'bajar', 'coger', 'dejar', 'hablar', 'callar', 'pensar', 'dormir'] # asigna la lista de verbos
    for bucle in range (numeroLineas) : # iterador , bucle for in , pasa los elementos de la lista a ; bucle -numero de lineas aleatorias-
        articulo = random.choice (articulos) # selecciona una de las cadenas de la lista indicada
        sujeto = random.choice (sujetos) # selecciona una de las cadenas de la lista indicada
        adverbio = random.choice (adverbios) # selecciona una de las cadenas de la lista indicada
        verbo = random.choice (verbos) # selecciona una de las cadenas de la lista indicada
        tipoFrase = random.randint (1, 2) # selecciona uno de los dos numeros
        if tipoFrase == 1 : # condicion , si el numero es el indicado
            print (articulo + ' ' + sujeto + ' ' + verbo + ' ' + adverbio) # presenta una frase completa
        else : # numero 2
            print (articulo + ' ' + sujeto + ' ' + verbo) # presenta una frase sin adverbio
    else : # cuando finalice el iterador
        print ('\n') # salto de linea

frasesAleatorias () # llama y ejecuta la funcion sin argumento

frasesAleatorias (6) # llama y ejecuta la funcion con el argumento indicado

frasesAleatorias (8) # llama y ejecuta la funcion con el argumento indicado 

frasesAleatorias (9) # llama y ejecuta la funcion con el argumento indicado 

frasesAleatorias (10) # llama y ejecuta la funcion con el argumento indicado 

frasesAleatorias (12) # llama y ejecuta la funcion con el argumento indicado 

def calcular1 () : # definicion de la funcion 
    listaDEnumeros = [] # lista vacia , se añaden los numeros introducidos
    while True : # bucle while continuo
        entrada_Teclado = input ('introduzca un numero y pulse enter -salir solo enter- ') # espera entrada teclado
        if not entrada_Teclado : # condicion , si es una cadena vacia
            if not listaDEnumeros : # condicion , si la lista esta vacia
                print ('lista vacia', listaDEnumeros, '\n') # presenta la cadena y su valor -lista vacia-
                break # interrumpe el bucle while
            menor = None # asigna el numero menor
            mayor = None # asigna el numero mayor 
            for bucle in range (len(listaDEnumeros)) : # iterador , bucle for in , pasa los elementos de la lista a ; bucle -numero de veces que ordena la lista-
                for posicion, numero in enumerate (listaDEnumeros) : # iterador , bucle for in , pasa los elementos de la lista a ; numero , enumerate () numera los elementos de la lista
                    posicionSiguiente = posicion + 1 # posicion siguiente
                    if posicionSiguiente == len (listaDEnumeros) : # condicion , si el valor es igual al numero de elementos de la lista
                        break # interrumpe el bucle
                    if numero > listaDEnumeros [posicionSiguiente] : # condicion , si el numero es mayor que el siguiente
                        menor = listaDEnumeros [posicionSiguiente] # asigna el numero menor 
                        mayor = numero # asigna el numero mayor
                        listaDEnumeros [posicion] = menor # asigna el valor menor a la posicion actual de la lista 
                        listaDEnumeros [posicionSiguiente] = mayor # asigna el valor mayor a la posicion siguiente de la lista
            suma = 0 # asigna valor int
            for x in listaDEnumeros : # iterador , bucle for in , pasa los elementos de la lista a ; x 
                suma += x # suma  el valor de x al valor actual de suma -suma todos los numeros de la lista-
            print ('numeros introducidos : ', listaDEnumeros, '\n') # presenta la cadena y su valor -lista de numeros introducidos-
            if len (listaDEnumeros) % 2 == 0 : # condicion , si el numero de elementos es par
                izquierda = listaDEnumeros [ : int(len (listaDEnumeros) / 2)] # asigna la subcadena desde inicio a la posicion indicada -posicion par-
                derecha = listaDEnumeros [int(len (listaDEnumeros) / 2) : ] # asigna la subcadena desde la posicion indicada -posicion par- al final de la lista 
                sumaIzquierda = 0 # asigna la suma total de la subcadena izquierda
                for sumaI in izquierda : # iterador , bucle for in , pasa los elementos de la lista a ; sumaI
                    sumaIzquierda += sumaI # suma el valor indicado al valor actual
                sumaDerecha = 0 # asigna la suma total de la subcadena derecha
                for sumaD in derecha : # iterador , bucle for in , pasa los elementos de la lista a ; sumaD
                    sumaDerecha += sumaD # suma el valor indicado al valor actual
                media = ((sumaIzquierda / len (izquierda)) + (sumaDerecha / len (derecha))) / 2 # asigna el resultado de las medias de las dos subcadenas
            else : # si el numero de elementos es inpar
                media = suma / len(listaDEnumeros) # asigna el valor medio del resultado
            print ('cantidad de numeros introducidos : {} , suma total numeros : {} , numero mas bajo : {} , numero mas alto : {} , media : {}\n'.format (len(listaDEnumeros), suma, listaDEnumeros[0],listaDEnumeros[-1], media)) # presenta la cadena formateada y sus valores
            break # interrumpe el bucle while
        listaDEnumeros.append (int(entrada_Teclado)) # añade los numeros a la lista

calcular1 () # llama y ejecuta la funcion sin argumento












