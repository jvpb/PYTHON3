#!/usr/bin/env python3
'''tipo de datos'''

# importar modulo

import sys

print ('VERSION en uso de PYTHON\n')

print (sys.version, '\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('atributos de un objeto , uso de dir ()\n')

print ('atributos de una lista ; dir ([1, 2, 3, 4, 5])\n')

print (dir ([1, 2, 3, 4, 5]), '\n') # presenta los atributos y funciones que se pueden usar en una lista

for _ in range (10) : print (_) # se puede utilizar _ -guion bajo- para evaluar la ultima expresion -elemento de la la lista

# importar modulo

import math # importa el modulo indicado

radio = 1.2 # asigna valor float

viejaArea = 22 # asigna valor entero

pi = math.pi # asigna el valor de pi

epsilon = 0.0000001 # asigna valor float

nuevaArea = pi * radio * radio # asigna el valor de la operacion

if abs (nuevaArea - viejaArea) < epsilon : # condicion , si el valor es menor que el de epsilon
    print ('las areas han convergido\n') # presenta el texto
else : # lo contrario , es mayor que el de epsilon
    print ('las areas NO han convergido\n') # presenta el texto
    
print ('tipo int -convierte a entero- ; int (15.99) ', int (15.99), '\n') # presenta el valor entero sin decimales

print ('tipo bool -devuelve True o False , dependiendo de la asignacion- ; bool (0) ', bool (0), '\n') # presenta False , cero equivale a False

# importar modulo

import fractions # importa el modulo indicado

print ('modulo fractions -devuelve valores racionales con precision ilimitada- ; fractions.Fraction (0.5) ', fractions.Fraction (0.5), '\n') # presenta el valor racional con precision ilimitada

print ('tipo False -equivale a cero- ; bool (0) ', bool (0), '\n') # presenta el valor de False -falso- , cero

print ('tipo True -equivale a uno- ; bool (1) ', bool (1), '\n') # presenta el valor de True -verdadero- , uno

print ('representacion de un valor entero en decimal -base 10- ; 124566 ', 124566, '\n') # presenta el valor en base 10

print ('representacion de un valor entero en binario -base 2- ; 0b11110011010010110 ', 0b11110011010010110, '\n') # presenta el valor en base 2

print ('representacion de un valor entero en octal -base 8- ; 0o363226 ', 0o363226, '\n') # presenta el valor en base 8

print ('representacion de un valor entero en hexadecimal -base 16- ; 0x1e696 ', 0x1e696, '\n') # presenta el valor en base 16

valor1 = 5 # asigna entero -int-

valor2 = 0.53 # asigna entero con decimales -float-

print ('sumar dos valores - + - ; valor1 + valor2 ',valor1 + valor2, '\n' ) # presenta la suma de los dos valores

print ('restar dos valores - - - ; valor1 - valor2 ',valor1 - valor2, '\n' ) # presenta la resta de los dos valores

print ('multiplicar dos valores - * - ; valor1 * valor2 ',valor1 * valor2, '\n' ) # presenta la multiplicacion de los dos valores

print ('division dos valores - / - ; valor1 / valor2 ',valor1 / valor2, '\n' ) # presenta la division de los dos valores

print ('division truncada  dos valores - // - ; valor1 // valor2 ',valor1 // valor2, '\n' ) # presenta la division truncada de los dos valores -sin decimales , si los hubiere-

print ('resto division dos valores - % - ; valor1 % valor2 ',valor1 % valor2, '\n' ) # presenta el resto de la division de los dos valores

print ('elevacion potencia dos valores - ** - ; valor1 ** valor2 ',valor1 ** valor2, '\n' ) # presenta el resultado de valor1 elevado a la potencia de valor2

print ('valor negativo - -valor - ; -valor1 ',-valor1, '\n' ) # presenta el valor de signo negativo

print ('valor positivo - +valor - ; +valor1 ',+valor1, '\n' ) # presenta el valor de signo positivo -todos los numeros sin signo , se consideran positivos + -

print ('valor absoluto - abs - ; abs (valor1) ',abs(valor1), '\n' ) # presenta el valor absoluto del indicado

print ('cociente y resto de una division  - divmod - ; divmod (valor1,valor2) ',divmod(valor1, valor2), '\n' ) # presenta el resultado de la division en una tupla (cociente,resto)

print ('elevacion potencia  - pow - ; pow (valor1,valor2) ',pow (valor1, valor2), '\n' ) # presenta el resultado de valor1 elevado a la potencia de valor2 -igual que **-

print ('elevacion potencia  y resto division - pow (x,y,z) - ; pow (valor1,2,3) ',pow (valor1, 2, 3), '\n' ) # presenta el resultado de valor1 elevado a la potencia de valor2  y el resto de la division por el tercer valor-igual que X ** Y % Z-

print ('redondear un valor float a entero  - round - ; round (3.5) ',round (3.5), '\n' ) # redondea un numero float a entero 

print ('convertir un numero en base 10 a binario - bin - ; bin (96245) ', bin (96245), '\n') # presenta el numero indicado en binario

print ('convertir un numero en base 10 a hexadecimal - hex - ; hex (96245) ', hex (96245), '\n') # presenta el numero indicado en hexadecimal

print ('convertir un numero en base 10 a octal - oct - ; oct (96245) ', oct (96245), '\n') # presenta el numero indicado en octal

print ('convertir un numero float o en formato cadena a entero - int - ; int (96.245) ', int (96.245), '\n') # presenta el numero indicado en entero sin decimales

print ('convertir una cadena en la base indicada (base 10) - int - ; int ("44", 10) ', int ("44", 10), '\n') # presenta la cadena convertida en un numero entero en base indicada -base 10-

print ('operador logico int | - or - ; 0 | 1 ', 0 | 1, '\n') # presenta True - 1 - si uno de ellos coincide (True)

print ('operador logico int ^ - xor - ; 1 ^ 1 ', 1 ^ 1, '\n') # presenta False - 0 - al coincidir los dos (True) -excluyente- 

print ('operador logico int & - and - ; 1 & 1 ', 1 & 1, '\n') # presenta True - 1 - al coincidir los dos (True) 

print ('operador logico int << - mueve bits hacia el primer valor , izquierda - ; 1 << 1 ', 1 << 1, '\n') # mueve los bits del segundo valor al primero -operacion realizada ; 1 * (2 ** 1)-

print ('operador logico int >> - mueve bits hacia el segundo valor , derecha - ; 1 >> 1 ', 1 >> 1, '\n') # mueve los bits del primero valor al segundo -operacion realizada ; 1 // (2 ** 1)-

print ('operador logico int ~ - invierte los bits del valor indicado - ; ~10 ', ~10, '\n') # invierte los bits del valor indicado

print ('operador boleano and ; True and True ', True and True, '\n') # presenta True -los dos valores coinciden-

print ('operador boleano and ; False and True ', False and True, '\n') # presenta False -los dos valores NO coinciden-

print ('operador boleano or ; False or True ', False or True, '\n') # presenta True -uno de los dos valores coinciden-

print ('operador boleano not - negacion , lo contrario- ; not False and True ', not False and True, '\n') # presenta True ; not False es convertido a True -los dos valores coinciden-

print ('numeros en punto flotante ; 12.6 ', 12.6, type (12.6), '\n') # presenta el valor en punto flotante y su tipo

print ('numeros en punto flotante ; 12.e6 ', 12.e6, type (12.e6), '\n') # presenta el valor en punto flotante y su tipo

print ('numeros en punto flotante ; 12.6j ', 12.6j, type (12.6j), '\n') # presenta el valor en punto flotante y su tipo

print ('tipo en punto flotante - float - ; float (12) ', float (12), type (float (12)), '\n') # presenta el valor en punto flotante y su tipo

print ('tipo en punto flotante - complex - ; complex (12.6) ', complex (12.6), type (complex (12.6)), '\n') # presenta el valor en punto flotante y su tipo

# importar modulo

import decimal # importa el modulo indicado

print ('tipo en punto flotante - decimal.Decimal - ; decimal.Decimal (12.69e-9) ', decimal.Decimal (12.69e-9), '\n') # presenta el numero en punto flotante con mayor precision

print ('valor de sys.float_info.epsilon ', sys.float_info.epsilon, '\n')

print ('comparar dos numeros en punto flotante con la exactitud maxima del procesador - sys.float_info.epsilon - ; abs (12.69e-9 - 12.69e-15) ', abs (12.69e-9 - 12.69e-15), '\n')

if abs (12.69e-9 - 12.69e-15) < sys.float_info.epsilon :
    print ('abs (12.69e-9 - 12.69e-15) ', abs (12.69e-9 - 12.69e-15), '\n')
    print ('es menor que sys.float_info.epsilon ', sys.float_info.epsilon, '\n')
else :
    print ('abs (12.69e-9 - 12.69e-15) ', abs (12.69e-9 - 12.69e-15), '\n')
    print ('es igual o mayor que sys.float_info.epsilon ', sys.float_info.epsilon, '\n')    

print ('comprobar si la parte decimal del punto flotante es cero ; 1.0.is_integer () ', 1.0.is_integer (), '\n') # presenta True si la parte decimal es cero

print ('devolver el numero de enteros y de fraciones de un punto flotante - ratio - ; 10.0.as_integer_ratio () ', 10.0.as_integer_ratio (), '\n') # presenta el ratio de enteros y decimales del punto flotante

print ('devolver una cadena con la representacion en hexadecimal de un numero float ; 10.1.hex () ', 10.1.hex (), '\n') # presenta el float en formato cadena hexadecimal

print ('converti una cadena en hexadecimal a base 10 ; float.fromhex ("0x1.4333333333333p+3") ', float.fromhex ("0x1.4333333333333p+3"), '\n') # presenta la conversion de la cadena con formato hexadecimal en punto flotante

print ('modulo math y sus funciones\n')

print ('devolver el arcoseno en radianes del valor indicado - acos - ; math.acos (.12) ',math.acos (.12), '\n' ) # presenta el resultado en radianes del valor indicado

print ('devolver el arcoseno hiperbolico en radianes del valor indicado - acosh - ; math.acosh (12) ',math.acosh (12), '\n' ) # presenta el resultado en radianes del valor indicado

print ('devolver el seno inverso en radianes del valor indicado - asin - ; math.asin (.12) ', math.asin (.12), '\n') # presenta el resultado en radianes del valor indicado

print ('devolver el seno hiperbolico inverso en radianes del valor indicado - asinh - ; math.asinh (12) ',math.asinh (12), '\n' ) # presenta el resultado en radianes del valor indicado

print ('devolver el arco tangente en radianes del valor indicado - atan - ; math.atan (12) ',math.atan (12), '\n' ) # presenta el resultado en radianes del valor indicado

print ('devolver el arco tangente en radianes de los dos  valores indicados - atan2 (x,y) - ; math.atan2 (12,.12) ',math.atan2 (12, .12), '\n' ) # presenta el resultado en radianes de los  valores indicados

print ('devolver el arco tangente hiperbolico en radianes del valor indicado - atanh - ; math.atanh (.12) ',math.atanh (.12), '\n' ) # presenta el resultado en radianes del  valor indicado

print ('devolver el valor int mas pequeño mayor o igual alvalor indicado - ceil - ; math.ceil (.12) ',math.ceil (.12), '\n' ) # presenta el el valor int mas pequeño mayor o igual alvalor indicado

print ('devolver el primer valor indicado con el signo del segundo - copysign - ; math.copysign (-12,+1) ',math.copysign (-12,+1), '\n' ) # presenta el primer valor indicado con el signo del segundo

print ('devolver el coseno en radianes del valor indicado - cos - ; math.cos (.12) ',math.cos (.12), '\n' ) # presenta el resultado en radianes del valor indicado

print ('devolver el coseno hiperbolico en radianes del valor indicado - cosh - ; math.cosh (12) ',math.cosh (12), '\n' ) # presenta el resultado en radianes del valor indicado

print ('convertir los radianes en grados - degrees - ; math.degrees (0.9928086358538663) ',math.degrees (0.9928086358538663), '\n' ) # presenta el resultado de radianes a grados

print ('la constante de e -e - ; math.e ',math.e, '\n' ) # presenta la constante e

print ('devolver la constante de e elevado a la potencia del valor indicado - exp - ; math.exp (2) ',math.exp (2), '\n' ) # presenta la constante e elevado a la potencia del valor indicado

print ('devolver el valor absoluto del valor indicado en formato float - fabs - ; math.fabs (6) ',math.fabs (6), '\n' ) # presenta  el valor absoluto del valor indicado en formato punto flotante -float-

print ('devolver el factorial del valor indicado - factorial - ; math.factorial (33) ', math.factorial (33), '\n') # presenta el factorial del valor indicado

print ('devolver el valor entero mas pequeño o igual al valor indicado - floor - ; math.floor (5.4) ',math.floor (5.4), '\n' ) # presenta el valor entero mas pequeño o igual al valor indicado

print ('devolver el resto de la division en formato float de los valores indicados - fmod - ; math.fmod (8,3) ',math.fmod (8,3), '\n' ) # presenta el resto de la division en formato float  de los valores indicados

print ('devolver mantisa como float y el exponente como int en una tupla - frexp - ; math.frexp (2) ', math.frexp (2), '\n') # presenta una tupla con la mantisa como float y el exponente como int

print ('devolver la suma de los valores del iterador indicado como float - fsum - ; math.fsum (range(10)) ',math.fsum (range(10)), '\n' ) # presenta la suma de todos los numeros de la lista indicada como float

print ('devolver la hypotenusa de los valores indicados - hypot - ; math.hypot (2,3) ',math.hypot (2,3), '\n' ) # presenta la hypotenusa de los valores indicados

print ('devolver True si el valor float indicado es inf - isinf - ; math.isinf (.333) ',math.isinf (333), '\n' ) # presenta True si el valor float es inf 

print ('devolver True si el valor float indicado no es un numero - isnan - ; math.isnan (.33) ',math.isnan (.33), '\n' ) # presenta True si el valor float no es un numero

print ('devolver el valor inverso de math.frexp - ldexp - ; math.ldexp (3,2) ',math.ldexp (3, 2), '\n' ) # presenta el valor inverso de math.frexp

print ('devolver log del valor indicado - log - ; math.log (2) ', math.log (2), '\n') # presenta el valor de log

print ('devolver log base 10 del valor indicado - log10 - ; math.log10 (2) ', math.log10 (2), '\n') # presenta el valor de log10

print ('devolver log del valor indicado mas 1 -log1p - ; math.log1p (.339) ', math.log1p (.339), '\n') # presenta el valor de log1p

print ('devolver el valor float indicado como entero con formato float y fraccion con formato float - modf - ; math.modf (3.339) ', math.modf (3.339), '\n') # presenta el valor float indicado como entero con formato float y fraccion con formato float

print ('constante pi - pi - ; math.pi ', math.pi, '\n') # presenta el valor de pi

print ('devolver la potencia de los valores indicados con formato float - pow - ; math.pow (3,2) ',math.pow (3, 2), '\n' ) # presenta la potencia de los valores indicados con formato float

print ('devolver grados en formato float en radianes - radians - ; math.radians (1.2) ', math.radians (1.2), '\n') # presenta grados en formato float en radianes

print ('devolver el seno del valor indicado en radianes - sin - ; math.sin (2) ',math.sin (2), '\n') # presenta el seno del valor indicado en radianes

print ('devolver el seno hiperbolico del valor indicado en radianes - sinh - ; math.sinh (2) ',math.sinh (2), '\n') # presenta el seno del valor indicado en radianes

print ('devolver la raiz del valor indicado - sqrt - ; math.sqrt (3) ',math.sqrt (3), '\n' ) # presenta la raiz del valor indicado 

print ('devolver la tangente del valor indicado en radianes  - tan - ; math.tan (10) ',math.tan (10), '\n' ) # presenta la tangente del valor indicado en radianes

print ('devolver la tangente hiperbolico del valor indicado en radianes  - tanh - ; math.tanh (10) ',math.tanh (10), '\n') # presenta la tangente hiperbolico del valor indicado en radianes

print ('devolver la parte entera del valor indicado en formato float - trunc - ; math.trunc (2.9) ',math.trunc (2.9), '\n' ) # presenta la parte entera del valor indicado en formato float

print ('numero complejo ; complejo = 39.5+99j \n') 

complejo = 39.5+99j # asigna el numero complejo

print ('atributos del numero complejo - real , imag - ;  parte real : complejo.real {} , parte imaginaria : complejo.imag {} \n'.format (complejo.real,complejo.imag)) # presenta las partes reales e imaginarias con los atributos real e imag

print ('cambiar el signo de la parte imaginaria del numero complejo - conjugate - ; complejo.conjugate () ',complejo.conjugate (), '\n' ) # presenta el numero complejo con el signo cambiado

print ('convertir un valor a complex - complex - ; complex () ', complex (), '\n') # presenta la parte imaginaria

print ('convertir un valor a complex - complex - ; complex (2.9) ', complex (2.9), '\n') # presenta la parte indicada con la parte imaginaria añadida

print ('calcular numeros decimales con alta precision - decimal.Decimal - ; decimal.Decimal (0.993e-3 + 1.369) ',decimal.Decimal (0.993e-3 + 1.369), '\n' ) # presenta el resultado con decimales con alta precision

print ('convertir un valor a cadena - str - ; str (complejo) ',str (complejo), 'tipo : ', type (str (complejo)), '\n' ) # presenta el valor convertido a cadena y su tipo

print ('cadena = "esto es una cadena"\n')

cadena = "esto es una cadena" # asigna la cadena 

print ('contenido de cadena ', cadena, '\n') # presenta la cadena 

print ('uso de triple comillas simples o dobles - \'\'\' \'\'\' , """ """ -\n')

print ('''cadenaMultipleLineas = """esto es una cadena
en multiple lineas
tantas como sean necesarias"""\n''')

cadenaMultipleLineas = """esto es una cadena
en multiple lineas
tantas como sean necesarias""" # asigna una cadena multilinea

print ('contenido de cadenaMultipleLineas \n')

print (cadenaMultipleLineas) # presenta la cadena multilinea

print ('barra invertida - \\\ - ; \\ \n') # presenta la invertida

print ('comilla simple - \\\' - ; \' \n') # presenta la comilla simple

print ('comilla dobles - \\\" - ; \" \n') # presenta la comilla simple

print ('campana ASCII - \\a - ; \a \n') # presenta BEL

print ('tecla retroceso - \\b - ; \b \n') # presenta BS

print ('alimentacion de papel ASCII - \\f - ; \f \n') # presenta FF

print ('salto de linea ASCII - \\n - ; \n') # salto de linea

print ('caracter unicode con el nombre indicado - \\N{nombre ingles} - ; \N{Latin Capital Letter N With Tilde}\n') # presenta la letra Ñ mayuscula

print ('caracter en formato octal - \\ovalor - ;  \n') # presenta el caracter del valor indicado en octal

print ('retorno de carro ASCII - \\r - ; \r ') # retorno de carro ASCII -salto de linea-

print ('tabulador ASCII - \\t - ; \t \n') # mueve el tabulador una posicion

print ('caracter unicode en formato hexadecimal 16 bit - \\uvalor - ; \u00d1 \n') # presenta la letra Ñ mayuscula

print ('caracter unicode en formato hexadecimal 32 bit - \\Uvalor - ; \U000000d1 \n') # presenta la letra Ñ mayuscula

print ('tabulador vertical - \\v - ; \v \n') # mueve el tabulador vertical

print ('caracter en formato hexadecimal 8 bit - \\xvalor - ; \xd1 \n') # presenta la letra Ñ mayuscula

print ('cadena en crudo -sin procesar- , - r - ; r"caracter en formato hexadecimal 8 bit - \\\\xvalor - ; \\xd1" \n')

print (r"caracter en formato hexadecimal 8 bit - \\xvalor - ; \xd1", '\n') # presenta la cadena sin procesar -en crudo-

print ('saber el codigo unicode de un caracter - ord - ; ord ("ñ") ', ord("ñ"),'\n') # presenta el codigo unicode de un caracter

print ('saber el caracter unicode de un codigo - chr - ; chr (241) ',chr (241),'\n') # presenta el  caracter unicode del codigo 

import unicodedata # importa el modulo indicado

print ('normalizar un codigo unicode unico - unicodedata.normalize ("NFKD", "caracter o codigo caracter") - ; unicodedata.normalize ("NFKD", "ñ") ', '\n')

unicodedata.normalize ("NFKD", "ñ") # normaliza el codigo del carcter indicado en unicode

print ('comparar cadenas , menor - < - ; "piña" < "piña" ',"piña" < "piña", '\n' ) # presenta False en la comparacion

print ('comparar cadenas , menor o igual - <= - ; "piña" <= "piña" ',"piña" <= "piña", '\n' ) # presenta True en la comparacion

print ('comparar cadenas , mayor - > - ; "piña" > "piña" ',"piña" > "piña", '\n' ) # presenta False en la comparacion

print ('comparar cadenas , mayor o igual - >= - ; "piña" >= "piña" ',"piña" >= "piña", '\n' ) # presenta True en la comparacion

print ('comparar cadenas , igual - == - ; "piña" == "piña" ',"piña" == "piña", '\n' ) # presenta True en la comparacion

print ('comparar cadenas , NO iguales - != - ; "piña" != "piña" ',"piña" != "piña", '\n' ) # presenta False en la comparacion

print ('contenido de cadena ', cadena, '\n') # presenta el contenido de cadena

print ('seleccionar un caracter de cadena por el indice - variable [indice] - , primer caracter ; cadena [0] ', cadena [0], '\n') # presenta el primer caracter de la cadena 

print ('seleccionar un caracter de cadena por el indice - variable [indice] - , ultimo caracter ; cadena [-1] ', cadena [-1], '\n') # presenta el ultimo caracter de la cadena 

print ('seleccionar un tramo de cadena por el indice - variable [indice : indice] - , desde primer caracter al indicado ; cadena [0 : 5] ', cadena [0 : 5], '\n') # presenta el tramo desde primer caracter de la cadena al indicado

print ('seleccionar un tramo de cadena por el indice - variable [indice : indice] - , desde caracter indicado al final ; cadena [5 : ] ', cadena [5 : ], '\n') # presenta el tramo desde caracter indicado al final de la cadena

print ('seleccionar un tramo de cadena por el indice - variable [indice : indice] - , desde un indice indicado a otro ; cadena [5 : 10] ', cadena [5 : 10], '\n') # presenta el tramo desde caracter indicado a otro de la cadena

print ('seleccionar un tramo de cadena por el indice - variable [indice : indice : pasos] - , desde primer caracter al indicado por pasos ; cadena [0 : : 2] ', cadena [0 : : 2], '\n') # presenta los caracteres coincidentes con los pasos indicados desde primer caracter al ultimo de la cadena

print ('seleccionar toda la cadena por el indice - variable [indice : indice] - , cadena [ : ] ',cadena [ : ], '\n' ) # presenta toda la cadena

print ('añadir una subcadena a la cadena ; cadena [0 : 8] + "otra cadena en " + cadena [8 : ] ',cadena [0 : 8] + "otra cadena en " + cadena [8 : ], '\n' ) # presenta la cadena con la subcadena añadida entre los indices indicados

print ('unir un conjunto de cadenas separados por el caracter indicado - join - ; "*".join (["estas","cadenas","estan","unidas","por","el","caracter","indicado","ASTERISCO"]) ',"*".join (["estas","cadenas","estan","unidas","por","el","caracter","indicado","ASTERISCO"]), '\n' ) # presenta las cadenas unidas por asteriscos

print ('poner el primer caracter de una cadena en mayuscula - capitalize - cadena.capitalize () ',cadena.capitalize (), '\n' ) # presenta la cadena con el primer caracter de la cadena en mayuscula

print ('centrar la cadena en un ancho indicado -opcional caracter de relleno- , - center (ancho,caracter opcinal) - ; cadena.center (30,"-") ','\n\n', cadena.center (30,"-"), '\n' ) # presenta la cadena centrada en el ancho indicado 

print ('devuelve el numero de caracteres en la cadena del caracter indicado - count - ; cadena.count ("a") ',cadena.count ("a"), '\n' ) # presenta la cantidad del caractyer indicado en la cadena

print ('devuelve la cadena en formato del codigo indicado (ascii,utf-8,latin1) - encode - ; cadena.encode ("latin1") ',cadena.encode ("latin1"), '\n' ) # presenta la cadena en formato de texto indicado -latin1-

print ('devuelve True si la cadena termina en la cadena indicada - endswith - ; cadena.endswith ("cadena") ',cadena.endswith ("cadena"), '\n' ) # presenta True si coincide el final de la cadena con la indicada

print ('devuelve la cadena con los tabuladores cambiados al tamaño indicado - expandtabs - ; cadena.expandtabs (10) ',cadena.expandtabs (10), '\n' ) # presenta la cadena con los tabuladores con el tamaño indicado

print ('devuelve la posicion de la cadena indicada en el extremo izquierdo de la cadena  - find - ; cadena.find ("esto") ',cadena.find ("esto"), '\n' ) # presenta la posicion de la cadena indicada en el extremo izquierdo de la cadena

print ('devuelve una cadena formateada con los valores indicados - format - ; "est{} es una cadena{}{}".format ("A"," ","FORMATEADA") ',"est{} es una cadena{}{}".format ("A"," ","FORMATEADA"), '\n' ) # presenta la cadena formateada

print ('devuelve la posicion de la cadena indicada en el extremo izquierdo de la cadena  - index - ; cadena.index ("esto") ',cadena.index ("esto"), '\n' ) # presenta la posicion de la cadena indicada en el extremo izquierdo de la cadena

print ('devuelve True si la cadena no esta vacia y su contenido es alfanumerico (caracteres y numeros) - isalnum - ; "cadena1".isalnum () ',"cadena1".isalnum (), '\n' ) # presenta True si la cadena no esta vacia y su contenido es alfanumerico (caracteres y numeros)

print ('devuelve True si la cadena no esta vacia y su contenido es alfabetico (solo caracteres , no numeros) - isalpha - ; cadena[ : 4] , cadena[ : 4].isalpha () ', cadena[ : 4],cadena[ : 4].isalpha (), '\n' ) # presenta True si la cadena no esta vacia y su contenido es alfabetico

print ('devuelve True si la cadena no esta vacia y su contenido es digito unicode base 10 - isdecimal - ; "102450".isdecimal () ',"102450".isdecimal (), '\n' ) # presenta True si la cadena no esta vacia y su contenido es digito unicode base 10

print ('devuelve True si la cadena no esta vacia y su contenido es digito ASCII - isdigit - ; "102450".isdigit () ',"102450".isdigit (), '\n' ) # presenta True si la cadena no esta vacia y su contenido es digito ASCII 

print (r'devuelve True si la cadena no esta vacia y su contenido contiene identificadores validos - isidentifier - ; "\u00d1".isidentifier () ',"\u00d1".isidentifier (), '\n' ) # presenta True si la cadena no esta vacia y su contenido contiene identificadores validos

print ('devuelve True si la cadena contiene caracteres en minuscula - islower - ; "cadena".islower () ',"cadena".islower (), '\n' ) # presenta True si la cadena contiene algun caracter en minuscula

print ('devuelve True si la cadena no esta vacia y su contenido es digito o fraccion unicode - isnumeric - ; "3356".isnumeric () ',"3356".isnumeric (), '\n' ) # presenta True si la cadena no esta vacia y su contenido es digito o fraccion unicode

print ('devuelve True si la cadena no esta vacia y su contenido es imprimible - isprintable - ; cadena.isprintable () ',cadena.isprintable (), '\n' ) # presenta True si la cadena no esta vacia y su contenido es imprimible

print ('devuelve True si la cadena no esta vacia y su contenido son espacios en blanco - isspace - ; "   ".isspace () ',"   ".isspace (), '\n' ) # presenta True si la cadena no esta vacia y su contenido son espacios en blanco

print ('devuelve True si no es una cadena de titulo vacia - istitle - ; "Titulo".istitle () ',"Titulo".istitle (), '\n' ) # presenta True si no es una cadena de titulo vacia

print ('devuelve True si la cadena contiene caracteres en mayuscula - isupper - ; "TITULO".isupper () ',"TITULO".isupper (), '\n' ) # presenta True si la cadena contiene algun caracter en mayuscula

print ('devuelve una secuencia de cadenas unidas por el caracter indicado - join - ; "-".join (["esta","es","la","cadena","a","unir"]) ',"-".join (["esta","es","la","cadena","a","unir"]), '\n' ) # presenta una secuencia de cadenas unidas por el caracter indicado

print ('devuelve una copia de la cadena alineada a la izquierda del ancho indicado - ljust - ; cadena.ljust (30,"-") ',cadena.ljust (30,"-"), '\n' ) # presenta una copia de la cadena alineada a la izquierda del ancho indicado

print ('devuelve una copia de la cadena en minusculas - lower - ; "TITULO".lower () ',"TITULO".lower (), '\n' ) # presenta una copia de la cadena en minusculas

print ('crea diccionario , translada el diccionario a la cadena - maketrans - ; cadena.maketrans ({1 : "cadena", 2 : "diccionario"}) ', cadena.maketrans ({1 : "cadena", 2 : "diccionario"}), '\n') # presenta el diccionario creado para trasladar a la cadena

print ('devuelve una tupla de tres elementos (la parte izquierda,la parte indicada,la parte derecha) - partition - ; cadena.partition (" es ") ',cadena.partition (" es "), '\n' ) # presenta una tupla de tres elementos (la parte izquierda,la parte indicada,la parte derecha)

print ('devuelve una copia de la cadena con las coincidencias indicadas por el primer valor sustituidas por el segundo valor - replace - ; cadena.replace ("a","*") ',cadena.replace ("a","*"), '\n' ) # presenta una copia de la cadena con las coincidencias indicadas por el primer valor sustituidas por el segundo valor 

print ('devuelve una lista con la cadena separada por el caracter indicado - split - ; cadena.split () ',cadena.split (), '\n' ) # presenta una lista con la cadena separada por sus espacios

print (r'devuelve una lista con la cadena separada por los saltos de linea - splitlines - ; "esta\ncadena\ncontiene\nsaltos\nde linea".splitlines () ', "esta\ncadena\ncontiene\nsaltos\nde linea".splitlines (), '\n') # presenta una lista con la cadena separada por los saltos de linea

print ('devuelve True si la cadena empieza por la cadena indicada - startswith - ; cadena.startswith ("esto") ',cadena.startswith ("esto"), '\n' ) # presenta True si la cadena empieza por la cadena indicada

print ('devuelve una copia de la cadena sin el caracter indicado en principio y final de esta - strip - ; "otro".strip ("o") ',"otro".strip ("o"), '\n' ) # presenta una copia de la cadena sin el caracter indicado en principio y final de esta

print ('devuelve una copia de la cadena cambiando las minusculas en mayusculas y viciversa - swapcase - ; "cadena con MAYUSCULAS y minusculas".swapcase () ', "cadena con MAYUSCULAS y minusculas".swapcase (), '\n') # presenta copia de la cadena cambiando las minusculas en mayusculas y viciversa

print ('devuelve una copia de la cadena cambiando el primer caracter de cada palabra a mayusculas - title - cadena.title () ',cadena.title (), '\n' ) # presenta una copia de la cadena cambiando el primer caracter de cada palabra a mayusculas

print ('trasladar = str.maketrans ("acdefhnoprstuw","אקדיפהנופרסתאו") \n')

trasladar = str.maketrans ('acdefhnoprstuw','אקדיפהנופרסתאו'              ) # genera la tabla de traslado  

print ('trasladar la cadena a la tabla creada ; - translate - ; cadena.translate (trasladar) ', cadena.translate (trasladar), '\n') # presenta la cadena trasladada al hebreo

print ('trasladar la cadena a la tabla creada ; - translate - ; "esta es otra cadena ha trasladar".translate (trasladar) ','\t',  "esta es otra cadena ha trasladar".translate (trasladar), '\n' ) # presenta la cadena trasladada al hebreo

print ('devuelve una copia de la cadena a mayusculas - upper - ; cadena.upper () ',cadena.upper (), '\n' ) # presenta una copia de la cadena a mayusculas

print ('devuelve una copia de la cadena que si es mas corta que el ancho indicado la rellena de ceros - zfill - ; cadena.zfill (30) ',cadena.zfill (30), '\n' ) # presenta una copia de la cadena que si es mas corta que el ancho indicado la rellena de ceros

print ('cadenas formateadas -format - ; "esta {} esta {} con {}".format ("cadena","formateada","format") ',"esta {} esta {} con {}".format ("cadena","formateada","format"), '\n' ) # presenta la cadena formateada con los argumentos indicados en format

print ('cadenas formateadas , uso de indices -format - ; "esta {1} esta {2} con {0}".format ("format","cadena","formateada") ',"esta {1} esta {2} con {0}".format ("format","cadena","formateada"), '\n' ) # presenta la cadena formateada con los indices de los argumentos indicados en format

print ('cadenas formateadas , uso de nombres de campos -format - ; "esta {segundo} esta {tercero} con {primero}".format (primero="format",segundo="cadena",tercero="formateada") ',"esta {segundo} esta {tercero} con {primero}".format (primero="format",segundo="cadena",tercero="formateada"), '\n' ) # presenta la cadena formateada con las variables de los argumentos indicados en format

print ('listaArgumentos = ["format","cadena","formateada"]\n')

listaArgumentos = ["format","cadena","formateada"] # lista argumentos format

print ('cadenas formateadas , uso de nombres de campos -format - ; "esta {0[1]} esta {0[2]} con {0[0]}".format (listaArgumentos) ',"esta {0[1]} esta {0[2]} con {0[0]}".format (listaArgumentos), '\n' ) # presenta la cadena formateada con los indices del argumento indicado en format

print ('diccionarioArgumentos = {"primero" : "format","segundo" : "formateada","tercero" : "cadena"}\n')

diccionarioArgumentos = {"primero" : "format","segundo" : "formateada","tercero" : "cadena"} # diccionario de argumentos

print ('cadenas formateadas , uso de nombres de campos -format - ; "esta {0[tercero]} esta {0[segundo]} con {0[primero]}".format (diccionarioArgumentos) ','esta {0[tercero]} esta {0[segundo]} con {0[primero]}'.format (diccionarioArgumentos), '\n' ) # presenta la cadena formateada con las claves del diccionario del argumento indicado en format

print (r'cadenas formateadas , uso de nombres de campos -format - ; "\nVERSION DE PYTHON  \n {0.version}".format (sys) ',"\nVERSION DE PYTHON  \n {0.version}".format (sys), '\n' ) # presenta la cadena formateada con el atributo del metodo del argumento indicado en format 

print (r'cadenas formateadas , uso de conversores , s cadena , -format - ; \'\t {0!s}\'.format ("אקדיפהנופרסתאו") ',"\t {0!s}".format ("אקדיפהנופרסתאו"               ), '\n') # presenta la cadena formateada convertida a cadena 

print (r'cadenas formateadas , uso de conversores , r representacion , -format - ; \'\t {0!r}\'.format ("אקדיפהנופרסתאו") ',"\t {0!r}".format ("אקדיפהנופרסתאו"               ), '\n') # presenta la cadena formateada convertida a representacion 

print (r'cadenas formateadas , uso de conversores , a representacion ASCII , -format - ; \'\t {0!a}\'.format ("אקדיפהנופרסתאו") ',"\t {0!a}".format ("אקדיפהנופרסתאו"               ), '\n') # presenta la cadena formateada convertida a representacion ASCII 

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo :numero , -format - ; "{0:35}".format ("esta es la cadena a formatear") ',"{0:35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio 

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo alinacion derecha :>numero , -format - ; "{0:>35}".format ("esta es la cadena a formatear") ',"{0:>35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la derecha

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo alineacion central :^numero , -format - ; "{0:^35}".format ("esta es la cadena a formatear") ',"{0:^35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alinacion central

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno alinacion derecha :caracter>numero , -format - ; "{0:*>35}".format ("esta es la cadena a formatear") ',"{0:*>35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la derecha rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno alinacion central :caracter^numero , -format - ; "{0:*^35}".format ("esta es la cadena a formatear") ',"{0:*^35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alinacion central rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno alinacion izquierda :caracter<numero , -format - ; "{0:*<35}".format ("esta es la cadena a formatear") ',"{0:*<35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la izquierda rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo alinacion izquierda :.numero , -format - ; "{0:.35}".format ("esta es la cadena a formatear") ',"{0:.35}".format ("esta es la cadena a formatear"), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la izquierda   

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  :numero=numero , -format - ; "{0:0=35}".format (123456789) ',"{0:0=35}".format (123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , rellenando con el numero indicado

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  :numero=numero , -format - ; "{0:0=35}".format (-123456789) ',"{0:0=35}".format (-123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , rellenando con el numero indicado entre el signo y el numero

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  :numeronumero , -format - ; "{0:035}".format (123456789) ',"{0:035}".format (123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , rellenando con el numero indicado

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  :numeronumero , -format - ; "{0:035}".format (-123456789) ',"{0:035}".format (-123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , rellenando con el numero indicado entre el signo y el numero

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  alinacion derecha :caracter>numero , -format - ; "{0:*>35}".format (123456789) ',"{0:*>35}".format (123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la derecha rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  alinacion central :caracter^numero , -format - ; "{0:*^35}".format (123456789) ',"{0:*^35}".format (123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alinacion central rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  alinacion izquierda :caracter<numero , -format - ; "{0:*<35}".format (123456789) ',"{0:*<35}".format (123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la izquierda rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  alinacion derecha :caracter>numero , -format - ; "{0:*>35}".format (-123456789) ',"{0:*>35}".format (-123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la derecha rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  alinacion central :caracter^numero , -format - ; "{0:*^35}".format (-123456789) ',"{0:*^35}".format (-123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alinacion central rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , ancho minimo con relleno numeros  alinacion izquierda :caracter<numero , -format - ; "{0:*<35}".format (-123456789) ',"{0:*<35}".format (-123456789), '\n' ) # presenta la cadena formateada con un ancho minimo de espacio , alineada a la izquierda rellenando con el caracter indicado  

print ('cadenas formateadas , uso especificaciones de formato , con signo   : , -format - ; "{0:} {1:}".format (123456789,-123456789) ',"{0:} {1:}".format (123456789,-123456789), '\n' ) # presenta la cadena formateada con los numeros indicados

print ('cadenas formateadas , uso especificaciones de formato , con signo , fuerza el signo  :+ , -format - ; "{0:+} {1:+}".format (123456789,-123456789) ',"{0:+} {1:+}".format (123456789,-123456789), '\n' ) # presenta la cadena formateada con los numeros indicados y sus signos 

print ('cadenas formateadas , uso especificaciones de formato , con signo , fuerza el signo negativo  :- , -format - ; "{0:-} {1:-}".format (123456789,-123456789) ',"{0:-} {1:-}".format (123456789,-123456789), '\n' ) # presenta la cadena formateada con los numeros indicados y su signo menos si es necesario 

print ('cadenas formateadas , uso especificaciones de formato , formato binario , :b , -format - ; "{0:b}".format (123456789) ',"{0:b}".format (123456789), '\n' ) # presenta la cadena formateada en binario con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato binario , :#b , -format - ; "{0:#b}".format (123456789) ',"{0:#b}".format (123456789), '\n' ) # presenta la cadena formateada en binario con su identificador con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato octal , :o , -format - ; "{0:o}".format (123456789) ',"{0:o}".format (123456789), '\n' ) # presenta la cadena formateada en octal con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato octal , :#o , -format - ; "{0:#o}".format (123456789) ',"{0:#o}".format (123456789), '\n' ) # presenta la cadena formateada en octal con su identificador con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato hexadecimal , :x , -format - ; "{0:x}".format (123456789) ',"{0:x}".format (123456789), '\n' ) # presenta la cadena formateada en hexadecimal con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato hexadecimal , :#x , -format - ; "{0:#x}".format (123456789) ',"{0:#x}".format (123456789), '\n' ) # presenta la cadena formateada en hexadecimal con su identificador con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato hexadecimal en mayusculas , :X , -format - ; "{0:X}".format (123456789) ',"{0:X}".format (123456789), '\n' ) # presenta la cadena formateada en hexadecimal con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato hexadecimal en mayusculas , :#X , -format - ; "{0:#X}".format (123456789) ',"{0:#X}".format (123456789), '\n' ) # presenta la cadena formateada en hexadecimal con su identificador con los numeros indicados 

print ('cadenas formateadas , uso especificaciones de formato , formato numerico entero -int- (representacion idioma), :n , -format - ; "{0:n} {1:n} {2:n}".format (123456789,-123456789,123456.789) ',"{0:n} {1:n} {2:n}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato numero entero idioma usado  

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante -float- , :f , -format - ; "{0:f} {1:f} {2:f}".format (123456789,-123456789,123456.789) ',"{0:f} {1:f} {2:f}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float  

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante , numero de decimales -float- , :.numerof , -format - ; "{0:.10f} {1:.10f} {2:.10f}".format (123456789,-123456789,123456.789) ',"{0:.10f} {1:.10f} {2:.10f}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float con el numero de decimales indicados despues del punto 

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante , exponencial -float- , :e , -format - ; "{0:e} {1:e} {2:.25e}".format (123456789,-123456789,123456.789) ',"{0:e} {1:e} {2:.25e}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float con el numero exponencial 

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante , exponencial en mayuscula -float- , :E , -format - ; "{0:E} {1:E} {2:.25E}".format (123456789,-123456789,123456.789) ',"{0:E} {1:E} {2:.25E}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float con el numero exponencial 

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante , punto flotante generico -float- , :g , -format - ; "{0:g} {1:g} {2:.25g}".format (123456789,-123456789,123456.789) ',"{0:g} {1:g} {2:.25g}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float generico 

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante , punto flotante generico mayuscula -float- , :G , -format - ; "{0:G} {1:G} {2:.25G}".format (123456789,-123456789,123456.789) ',"{0:G} {1:G} {2:.25G}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float generico mayuscula 

print ('cadenas formateadas , uso especificaciones de formato , formato numerico punto flotante , multiplicar por 100 y presenta el resultado seguido del simbolo % -float- , :% , -format - ; "{0:%} {1:%} {2:.25%}".format (123456789,-123456789,123456.789) ',"{0:%} {1:%} {2:.25%}".format (123456789,-123456789,123456.789), '\n' ) # presenta la cadena formateada en el formato float multiplicado por 100 seguido del simbolo %

def codigo_utf8 (caracter=None) : # definicion de la funcion con argumento por defecto -None-
  assert caracter == None or type (caracter) == str,'el argumento tiene que ser una cadena de un caracter\n' # regla de excepcion , si no se cumple lanza excepcion con la cadena indicada
  print ('DECIMAL   HEXADECIMAL   CARACTER  {0:^40}'.format ('NOMBRE')) # presenta la cadena formateada con la cadena indicada centrada en un ancho de 40 espacios
  print ('------    ----------    --------  {0:-<40}'.format ("")) # presenta la cadena formateada con la cadena indicada alineada a la izquierda en un ancho de 40 espacios -rellenandos por simbolo guion-
  codigo = ord (" ") # asigna codigo ordinal unicode de la cadena indicada -espacio-
  if caracter == None : # condicion , si el valor del argumento es None
    fin = sys.maxunicode # asigna el valor maximo unicode de la cadena que ejecuta el script python
  else : # si NO es None
    fin = ord (caracter) # asigna el valor unicode 
  while codigo < fin + 1 : # bucle while , mientras se cumpla la condicion -valor de codigo menor que fin-
    CARACTER = chr (codigo) # asigna el caracter del codigo indicado
    nombre = unicodedata.name (CARACTER,'*** DESCONOCIDO ***') # asigna el nombre del caracter , devuelve la cadena indicada si no lo encuentra 
    if caracter is None or caracter in nombre.lower () : # condicion , si el valor es None o el de caracter en minusculas
      print ('{0:7}  {0:5X}  {0:^3c}  {1}'.format (codigo,nombre.title())) # presenta la cadena formateada con el valor de codigo en primera posicion con un ancho de 7 espacios , la segunda posicion en codigo hexadecimal con un ancho de 5 espacios , la tercera posicion la cadena de caracter unicode centrada con un espacio de 3 espacios -del valor de codigo- , cuarta posicion el nombre del caracter en formato titulo 
    codigo += 1 # suma uno al valor actual de codigo
  print ('\n') # salto de linea

print ('codigo_utf8 ()\n')

try : # control de excepciones
  codigo_utf8 () # llama y ejecuta la funcion sin argumento indicado -valor por defecto None-
except : # tipo de excepcion general
  print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n') # presenta la cadena 

print ('codigo_utf8 ("m")\n')  

codigo_utf8 ('m') # llama y ejecuta la funcion con el argumento indicado

try :
  print ('codificar caracteres al formato indicado -encode- ; "esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -ascii-".encode ("ascii") \n')
  print ("esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -ascii-".encode ("ascii"),'\n') # presenta la cadena indicada codificada en el codigo indicado -ascii-
except UnicodeEncodeError as Salida :
  print ('caracteres ñ y Ñ fuera de rango ascii : *** {} ***\n'.format (Salida)) # presenta la cadena y la salida de la excepcion indicada
  
print ('codificar caracteres al formato indicado -encode- ; "esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -latin1-".encode ("latin1") ',"esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -latin1-".encode ("latin1"),'\n') # presenta la cadena indicada codificada en el codigo indicado -latin1-

print ('codificar caracteres al formato indicado -encode- ; "esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -cp850-".encode ("cp850") ',"esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -cp850-".encode ("cp850"),'\n') # presenta la cadena indicada codificada en el codigo indicado -cp850-

print ('codificar caracteres al formato indicado -encode- ; "esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -utf16-".encode ("utf16") ',"esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -utf16-".encode ("utf16"),'\n') # presenta la cadena indicada codificada en el codigo indicado -utf16-

print ('codificar caracteres al formato indicado -encode- ; "esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -utf32-".encode ("utf32") ',"esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -utf32-".encode ("utf32"),'\n') # presenta la cadena indicada codificada en el codigo indicado -utf32-

print ('codificar caracteres al formato indicado -encode- ; "esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -utf8-".encode ("utf8") ',"esta es la cadena a codificar en el codigo indicado (ñ , Ñ) -utf8-".encode ("utf8"),'\n') # presenta la cadena indicada codificada en el codigo indicado -utf8-

print (r'decodificar una cadena en bytes al formato indicado -decode- ; b"esta es la cadena a decodificar en el codigo indicado (\xf1 , \xd1) -latin1-".decode ("latin1") ',b"esta es la cadena a decodificar en el codigo indicado (\xf1 , \xd1) -latin1-".decode ("latin1"),'\n') # presenta la cadena en bytes codificada a utf8 -unicode- 

print (r'decodificar una cadena en bytes al formato indicado -decode- ;  b"esta es la cadena a decodificar en el codigo indicado (\xa4 , \xa5) -cp850-".decode ("cp850") ',b"esta es la cadena a decodificar en el codigo indicado (\xa4 , \xa5) -cp850-".decode ("cp850"),'\n') # presenta la cadena en bytes codificada a cp850 

print (r'decodificar una cadena en bytes al formato indicado -decode- ;  b"\xff\xfee\x00s\x00t\x00a\x00 \x00e\x00s\x00 \x00l\x00a\x00 \x00c\x00a\x00d\x00e\x00n\x00a\x00 \x00a\x00 \x00c\x00o\x00d\x00i\x00f\x00i\x00c\x00a\x00r\x00 \x00e\x00n\x00 \x00e\x00l\x00 \x00c\x00o\x00d\x00i\x00g\x00o\x00 \x00i\x00n\x00d\x00i\x00c\x00a\x00d\x00o\x00 \x00(\x00\xf1\x00 \x00,\x00 \x00\xd1\x00)\x00 \x00-\x00u\x00t\x00f\x001\x006\x00-\x00".decode ("utf16") ',b"\xff\xfee\x00s\x00t\x00a\x00 \x00e\x00s\x00 \x00l\x00a\x00 \x00c\x00a\x00d\x00e\x00n\x00a\x00 \x00a\x00 \x00c\x00o\x00d\x00i\x00f\x00i\x00c\x00a\x00r\x00 \x00e\x00n\x00 \x00e\x00l\x00 \x00c\x00o\x00d\x00i\x00g\x00o\x00 \x00i\x00n\x00d\x00i\x00c\x00a\x00d\x00o\x00 \x00(\x00\xf1\x00 \x00,\x00 \x00\xd1\x00)\x00 \x00-\x00u\x00t\x00f\x001\x006\x00-\x00".decode ("utf16"),'\n') # presenta la cadena en bytes codificada a utf16 

print (r'decodificar una cadena en bytes al formato indicado -decode- ;  b"\xff\xfe\x00\x00e\x00\x00\x00s\x00\x00\x00t\x00\x00\x00a\x00\x00\x00 \x00\x00\x00e\x00\x00\x00s\x00\x00\x00 \x00\x00\x00l\x00\x00\x00a\x00\x00\x00 \x00\x00\x00c\x00\x00\x00a\x00\x00\x00d\x00\x00\x00e\x00\x00\x00n\x00\x00\x00a\x00\x00\x00 \x00\x00\x00a\x00\x00\x00 \x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00i\x00\x00\x00f\x00\x00\x00i\x00\x00\x00c\x00\x00\x00a\x00\x00\x00r\x00\x00\x00 \x00\x00\x00e\x00\x00\x00n\x00\x00\x00 \x00\x00\x00e\x00\x00\x00l\x00\x00\x00 \x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00i\x00\x00\x00g\x00\x00\x00o\x00\x00\x00 \x00\x00\x00i\x00\x00\x00n\x00\x00\x00d\x00\x00\x00i\x00\x00\x00c\x00\x00\x00a\x00\x00\x00d\x00\x00\x00o\x00\x00\x00 \x00\x00\x00(\x00\x00\x00\xf1\x00\x00\x00 \x00\x00\x00,\x00\x00\x00 \x00\x00\x00\xd1\x00\x00\x00)\x00\x00\x00 \x00\x00\x00-\x00\x00\x00u\x00\x00\x00t\x00\x00\x00f\x00\x00\x003\x00\x00\x002\x00\x00\x00-\x00\x00\x00".decode ("utf32") ',b"\xff\xfe\x00\x00e\x00\x00\x00s\x00\x00\x00t\x00\x00\x00a\x00\x00\x00 \x00\x00\x00e\x00\x00\x00s\x00\x00\x00 \x00\x00\x00l\x00\x00\x00a\x00\x00\x00 \x00\x00\x00c\x00\x00\x00a\x00\x00\x00d\x00\x00\x00e\x00\x00\x00n\x00\x00\x00a\x00\x00\x00 \x00\x00\x00a\x00\x00\x00 \x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00i\x00\x00\x00f\x00\x00\x00i\x00\x00\x00c\x00\x00\x00a\x00\x00\x00r\x00\x00\x00 \x00\x00\x00e\x00\x00\x00n\x00\x00\x00 \x00\x00\x00e\x00\x00\x00l\x00\x00\x00 \x00\x00\x00c\x00\x00\x00o\x00\x00\x00d\x00\x00\x00i\x00\x00\x00g\x00\x00\x00o\x00\x00\x00 \x00\x00\x00i\x00\x00\x00n\x00\x00\x00d\x00\x00\x00i\x00\x00\x00c\x00\x00\x00a\x00\x00\x00d\x00\x00\x00o\x00\x00\x00 \x00\x00\x00(\x00\x00\x00\xf1\x00\x00\x00 \x00\x00\x00,\x00\x00\x00 \x00\x00\x00\xd1\x00\x00\x00)\x00\x00\x00 \x00\x00\x00-\x00\x00\x00u\x00\x00\x00t\x00\x00\x00f\x00\x00\x003\x00\x00\x002\x00\x00\x00-\x00\x00\x00".decode ("utf32"),'\n') # presenta la cadena en bytes codificada a utf32 

print (r'decodificar una cadena en bytes al formato indicado -decode- ;  b"esta es la cadena a codificar en el codigo indicado (\xc3\xb1 , \xc3\x91) -utf8-".decode ("utf8") ',b"esta es la cadena a codificar en el codigo indicado (\xc3\xb1 , \xc3\x91) -utf8-".decode ("utf8"),'\n') # presenta la cadena en bytes codificada a utf8 

print ('funcion ecuacionCuadrada () \n')

def ecuacionCuadrada () : # definicion de la funcion
  # importar modulos
  import cmath # importa el modulo indicado
  import math # importa el modulo indicado
  import sys # importa el modulo indicado
  print ('ax\N{SUPERSCRIPT TWO} + bx + c = 0\n') # presenta el algoritmo de calculo
  for factor in range (3) : # iterador , bucle for in , pasa los numeros a factor
    cogerFloat = None # asigna el valor indicado
    permitirCero = True # asigna el valor indicado
    permitir_cero = input ('permitir cero ? si/no -salir pulsar enter- ') # espera entrada teclado
    if not permitir_cero : # condicion , si es una cadena vacia
      print ('\n') # salto de linea
      return # sale de la funcion -devuelve None-
    if permitir_cero in ['no','NO','n','N'] : # condicion , si es una de las cadenas 
      permitirCero = False # cambia el valor , asignando False
    while cogerFloat is None : # bucle while , mientras se cumpla la condicion -bucle hasta que cogerFloat sea un valor mayor que epsilon-
      try : # control de excepciones
        cogerFloat = float (input('introduzca un numero y pulse enter ')) # espera entrada teclado
        if not permitirCero and abs (cogerFloat) < sys.float_info.epsilon : # condicion , si permitirCero es False -valor 0- y el valor devuelto por abs de cogerFloat es menor que el valor de epsilon
          print ('cero NO esta permitido\n') # presenta el mensaje
          cogerFloat = None # se asigna None
      except ValueError as Error : # tipo de excepcion , pasa la salida a Error
        print ('debe ser un numero -** {} **-\n'.format(Error)) # presenta la cadena formateada con la salida de Error
    if factor == 0 : # condicion , si es la primera iteracion -valor 0-
      a = cogerFloat # asigna numero cogerFloat 
      print ('factor a : ',a,'\n') # presenta el valor asignado a a
    elif factor == 1 : # condicion , si es la segunda iteracion -valor 1-
      b = cogerFloat # asigna numero cogerFloat
      print ('factor b : ',b,'\n') # presenta el valor asignado a b     
    elif factor == 2 : # condicion , si es la tercera iteracion -valor 2-
      c = cogerFloat # asigna numero cogerFloat
      print ('factor c : ',c,'\n') # presenta el valor asignado a c     
  print ('{}x\N{SUPERSCRIPT TWO} + {}x + {} = 0\n'.format (a,b,c)) # presenta el algoritmo de calculo formateado con los valores asignados
  x1 = None # asigna el valor indicado
  x2 = None # asigna el valor indicado
  descriminar = (b ** 2) - (4 * a * c) # asigna el resultado de la operacion matematica
  if descriminar == 0 : # condicion , si el resultado es cero
    x1 = -(b / (2 * a)) # asigna el resultado de la operacion matematica
  else : # si no es igual a cero
    if descriminar > 0 : # condicion , si es mayor que cero
      raiz = math.sqrt (descriminar) # asigna el resultado de la raiz del valor de descriminar
    else : # si es menor de cero
      raiz = cmath.sqrt (descriminar) # asigna el resultado de la raiz del valor de descriminar
    x1 = (-b + raiz) / (2 * a) # asigna el resultado de la operacion matematica
    x2 = (-b - raiz) / (2 * a) # asigna el resultado de la operacion matematica
  ecuacion = ('{0}x\N{SUPERSCRIPT TWO} + {1}x + {2} = 0' ' \N{RIGHTWARDS ARROW}  x = {3}').format (a,b,c,x1) # asigna una cadena formateada con los valores indicados
  if x2 is not None : # condicion , si el valor no es cero
    ecuacion += '  O  x = {0}'.format (x2) # añade la cadena formateada con el valor indicado a la cadena de ecuacion
  print (ecuacion,'\n') # presenta la ecuacion con sus valores y resultados

ecuacionCuadrada () # llama y ejecuta la funcion sin argumento  

print ('funcion conversorCSVaHTML () \n')

def conversorCSVaHTML () : # definicion de la funcion
  with open ('./Escritorio/elementosHTML.csv','r') as csv : # abre el fichero indicado , lo lee y lo cierra -enlazado como csv-
    contenidoCSV = csv.readlines () # almacena el contenido del fichero en una lista 
  anchoMaximo = 100 # ancho maximo en caracteres por celda html 
  print ("<table border='1'>") # presenta la cadena de inicio de la tabla html
  contador = 0 # contador iterador
  for linea in contenidoCSV : # iterador , bucle for in , pasa los lineas del fichero csv a linea
    linea # linea de datos csv del fichero
    if contador == 0 : # condicion , si es el valor indicado
      color = "lightgreen" # color de la tabla html -verde luminoso-
    elif contador % 2 : # condicion , si el valor es 1 -True-
      color = "white" # color de la tabla html -blanco-
    else : # cualquier otro numero
      color = "lightyellow" # color de la tabla html -amarillo luminoso-
    print ("<tr bgcolor='{0}'>".format(color)) # presenta la cadena formateada con el valor indicado -color de fondo de la tabla html-
    campos = [] # lista vacia -añadir los campos de la linea html-
    campo = "" # cadena vacia
    for caracter in linea : # iterador , bucle for in , pasa los caracteres de la linea del fichero csv a caracter 
      if caracter in "\"'" : # condicion , si el caracter esta en la cadena indicada -es una comilla doble o simple-
        continue # vuelve al siguiente caracter de la linea
      elif caracter == ',' or caracter == '\n' : # condicion , si el caracter esta en la cadena indicada -coma o salto de linea- , fin de un campo html
        campos.append (campo) # añade el valor actual de campo a la lista -cadena o numero-
        campo = "" # vuelve a asignar el valor por defecto -cadena vacia-
      else : # si no es una comilla simple o doble o una coma o salto de linea
        campo += caracter # añade el caracter 
    for Campo in campos : # iterador , bucle for in , pasa los campos html -cadenas o numeros- de la lista a Campo
      if not Campo : # condicion , si la cadena esta vacia -False-
        print ("<td></td>") # presenta la cadena html
      else : # si no es una cadena vacia
        numero = Campo.replace (",","") # si hay una coma en la cadena , reemplaza la coma por una cadena vacia
        try : # control de excepciones
          numeroFlotante = float (numero) # convierte el entero a punto flotante
          print ("<td aling='right'>{0:d}</td>".format(round(numeroFlotante))) # presenta la cadena formateada html con el valor float redondeado a entero
        except ValueError : # tipo de excepcion -valor erroneo-
          Campo = Campo.title () # convierte la cadena a titulo -cadena con el primer caracter en mayusculas-
          Campo = Campo.replace (" Y "," y ") # reemplaza la primera cadena indicada por la segunda
          Campo = Campo.replace ("&","&amp;") # reemplaza la primera cadena indicada por la segunda
          Campo = Campo.replace ("<","&lt;") # reemplaza la primera cadena indicada por la segunda
          Campo = Campo.replace (">","&gt;") # reemplaza la primera cadena indicada por la segunda
          if len (Campo) <= anchoMaximo : # condicion , si el tamaño de la cadena es inferior o igual al valor de anchoMaximo
            print ("<td>{0}</td>".format(Campo)) # presenta la cadena formateada html con el valor de Campo -cadena en formato html-
          else : # si es mayor al valor de anchoMaximo
            print ("<td>{0:.{1}} ...</td>".format(Campo,anchoMaximo)) # presenta la cadena formateada html con el valor de Campo -cadena en formato html- al ancho indicado en anchoMaximo
    print ("</tr>") # presenta la cadena en formato html -fin <tr>-
    contador += 1 # suma uno al valor actual de contador 
  print ("</table>") # presenta la cadena en formato html -fin <table>- , tabla  

conversorCSVaHTML () # llama y ejecuta la funcion sin argumento 



















































