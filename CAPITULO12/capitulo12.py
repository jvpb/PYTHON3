#!/usr/bin/env python3
'''expresiones regulares'''

# importar modulo

import sys # importa el modulo indicado

print ('VERSION en uso de PYTHON \n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('uso de abreviaciones de registros de expresiones regulares : \n')

cadena = 'aeiou , bcdfghklmnp , abcdefghlmnopwz , 0123456789 , a5d8g7b1c6 , AEIOU  BCDFGLMNP 5AB7FX8MN9 AeioU AbcdefgL ,cdaBklmOpkl,correo@servidor.net , z*x=n' # cadena 

print ('contenido de listaDEcadenas : \n')

print (cadena,'\n') # presenta la cadena

print ('importar modulo de expresiones regulares ; import re \n')

import re # importa el modulo indicado

print ('uso de la expresion regular abreviada : \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".",cadena) \n')

print (re.findall (".",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d",cadena) \n')

print (re.findall ("\d",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D",cadena) \n')

print (re.findall ("\D",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s",cadena) \n')

print (re.findall ("\s",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S",cadena) \n')

print (re.findall ("\S",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w",cadena) \n')

print (re.findall ("\w",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W",cadena) \n')

print (re.findall ("\W",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('cuantificadores : concordancia en el numero de elementos indicados en la expresion regular \n')

print ('con 0 o 1 coincidencia -cualquiera- de la expresion indicada : simbolo abreviado ; ? -interrogante- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".?",cadena) \n')

print (re.findall (".?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d?",cadena) \n')

print (re.findall ("\d?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D?",cadena) \n')

print (re.findall ("\D?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s?",cadena) \n')

print (re.findall ("\s?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S?",cadena) \n')

print (re.findall ("\S?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w?",cadena) \n')

print (re.findall ("\w?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W?",cadena) \n')

print (re.findall ("\W?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('con 0 o 1 coincidencia -no cualquiera- de la expresion indicada : simbolo abreviado ; ?? -doble interrogante- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".??",cadena) \n')

print (re.findall (".??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d??",cadena) \n')

print (re.findall ("\d??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D??",cadena) \n')

print (re.findall ("\D??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s??",cadena) \n')

print (re.findall ("\s??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S??",cadena) \n')

print (re.findall ("\S??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w??",cadena) \n')

print (re.findall ("\w??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W??",cadena) \n')

print (re.findall ("\W??",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('por lo menos con 1 coincidencia -cualquiera- de la expresion indicada : simbolo abreviado ; + -simbolo mas- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".+",cadena) \n')

print (re.findall (".+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d+",cadena) \n')

print (re.findall ("\d+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D+",cadena) \n')

print (re.findall ("\D+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s+",cadena) \n')

print (re.findall ("\s+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S+",cadena) \n')

print (re.findall ("\S+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w+",cadena) \n')

print (re.findall ("\w+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W+",cadena) \n')

print (re.findall ("\W+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('por lo menos con 1 coincidencia -no cualquiera- de la expresion indicada : simbolo abreviado ; +? -simbolo mas e interrogante- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".+?",cadena) \n')

print (re.findall (".+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d+?",cadena) \n')

print (re.findall ("\d+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D+?",cadena) \n')

print (re.findall ("\D+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s+?",cadena) \n')

print (re.findall ("\s+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S+?",cadena) \n')

print (re.findall ("\S+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w+?",cadena) \n')

print (re.findall ("\w+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W+?",cadena) \n')

print (re.findall ("\W+?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('cualquier cantidad de coincidencias -cualquiera- de la expresion indicada : simbolo abreviado ; * -asterisco- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".*",cadena) \n')

print (re.findall (".*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d*",cadena) \n')

print (re.findall ("\d*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D*",cadena) \n')

print (re.findall ("\D*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s*",cadena) \n')

print (re.findall ("\s*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S*",cadena) \n')

print (re.findall ("\S*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w*",cadena) \n')

print (re.findall ("\w*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W*",cadena) \n')

print (re.findall ("\W*",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('cualquier cantidad de coincidencias -no cualquiera- de la expresion indicada : simbolo abreviado ; *? -asterisco e interrogante- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".*?",cadena) \n')

print (re.findall (".*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d*?",cadena) \n')

print (re.findall ("\d*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D*?",cadena) \n')

print (re.findall ("\D*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s*?",cadena) \n')

print (re.findall ("\s*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S*?",cadena) \n')

print (re.findall ("\S*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w*?",cadena) \n')

print (re.findall ("\w*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W*?",cadena) \n')

print (re.findall ("\W*?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('numero de coincidencias no usando los simbolos abreviados ; "expresionRegular{numeroMINIMO,numeroMAXIMO}" \n')

print ('la cantidad indicada de coincidencias de la expresion indicada ; {numero} -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{2}",cadena) \n')

print (re.findall (".{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{2}",cadena) \n')

print (re.findall ("\d{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{2}",cadena) \n')

print (re.findall ("\D{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{2}",cadena) \n')

print (re.findall ("\s{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{2}",cadena) \n')

print (re.findall ("\S{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{2}",cadena) \n')

print (re.findall ("\w{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{2}",cadena) \n')

print (re.findall ("\W{2}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('la cantidad indicada de coincidencias de la expresion indicada -cualquiera- ; {numeroMINIMO,} -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{2,}",cadena) \n')

print (re.findall (".{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{2,}",cadena) \n')

print (re.findall ("\d{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{2,}",cadena) \n')

print (re.findall ("\D{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{2,}",cadena) \n')

print (re.findall ("\s{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{2,}",cadena) \n')

print (re.findall ("\S{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{2,}",cadena) \n')

print (re.findall ("\w{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{2,}",cadena) \n')

print (re.findall ("\W{2,}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('la cantidad indicada de coincidencias de la expresion indicada -no cualquiera-  ; {numeroMINIMO,}? -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{2,}?",cadena) \n')

print (re.findall (".{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{2,}?",cadena) \n')

print (re.findall ("\d{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{2,}?",cadena) \n')

print (re.findall ("\D{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{2,}?",cadena) \n')

print (re.findall ("\s{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{2,}?",cadena) \n')

print (re.findall ("\S{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{2,}?",cadena) \n')

print (re.findall ("\w{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{2,}?",cadena) \n')

print (re.findall ("\W{2,}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('la cantidad indicada de coincidencias de la expresion indicada -cualquiera- ; {,numeroMAXIMO} -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{,8}",cadena) \n')

print (re.findall (".{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{,8}",cadena) \n')

print (re.findall ("\d{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{,8}",cadena) \n')

print (re.findall ("\D{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{,8}",cadena) \n')

print (re.findall ("\s{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{,8}",cadena) \n')

print (re.findall ("\S{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{,8}",cadena) \n')

print (re.findall ("\w{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{,8}",cadena) \n')

print (re.findall ("\W{,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('la cantidad indicada de coincidencias de la expresion indicada -no cualquiera-  ; {,numeroMAXIMO}? -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{,8}?",cadena) \n')

print (re.findall (".{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{,8}?",cadena) \n')

print (re.findall ("\d{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{,8}?",cadena) \n')

print (re.findall ("\D{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{,8}?",cadena) \n')

print (re.findall ("\s{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{,8}?",cadena) \n')

print (re.findall ("\S{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{,8}?",cadena) \n')

print (re.findall ("\w{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{,8}?",cadena) \n')

print (re.findall ("\W{,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('la cantidad indicada de coincidencias de la expresion indicada -cualquiera- ; {numeroMINIMO,numeroMAXIMO} -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{2,8}",cadena) \n')

print (re.findall (".{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{2,8}",cadena) \n')

print (re.findall ("\d{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{2,8}",cadena) \n')

print (re.findall ("\D{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{2,8}",cadena) \n')

print (re.findall ("\s{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{2,8}",cadena) \n')

print (re.findall ("\S{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{2,8}",cadena) \n')

print (re.findall ("\w{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{2,8}",cadena) \n')

print (re.findall ("\W{2,8}",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('la cantidad indicada de coincidencias de la expresion indicada -no cualquiera-  ; {numeroMINIMO,numeroMAXIMO}? -simbolo llaves- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".{2,8}?",cadena) \n')

print (re.findall (".{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d{2,8}?",cadena) \n')

print (re.findall ("\d{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D{2,8}?",cadena) \n')

print (re.findall ("\D{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s{2,8}?",cadena) \n')

print (re.findall ("\s{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S{2,8}?",cadena) \n')

print (re.findall ("\S{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w{2,8}?",cadena) \n')

print (re.findall ("\w{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W{2,8}?",cadena) \n')

print (re.findall ("\W{2,8}?",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencias usando agrupaciones -()- y alternacion -|- en expresiones regulares -() parentesis y | barra vertical- \n')

print ('coincidencias usando agrupaciones -()- ; re.findall ("([a-z]+@\D..+\.\D{3})",cadena) \n')

print (re.findall ("([a-z]+@\D..+\.\D{3})",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencias usando agrupaciones -()- y alternaciones ; re.findall ("([a-z]+@\D+\.)(com|org|net)",cadena) \n')

print (re.findall ("([a-z]+@\D+\.)(com|org|net)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('re.search ("([a-z]+@\D+\.)(com|org|net)",cadena) \n') 

print (re.search ("([a-z]+@\D+\.)(com|org|net)",cadena),'\n') # presenta el objeto con las coincidencias indicadas en la expresion regular abreviada

print ('re.search ("([a-z]+@\D+\.)(com|org|net)",cadena).group () \n')

print (re.search ("([a-z]+@\D+\.)(com|org|net)",cadena).group (),'\n') # presenta la coincidencia del grupo y alternancia indicada en la expresion regular abreviada

print ('coincidencias usando afirmaciones y marcadores en expresiones regulares \n')

print ('uso de afirmaciones en expresiones regulares \n')

print ('coincidencia al inicio de la linea  ; -^- acento circunflejo \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("^.",cadena) \n')

print (re.findall ("^.",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("^\d",cadena) \n')

print (re.findall ("^\d",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("^\D",cadena) \n')

print (re.findall ("^\D",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("^\s",cadena) \n')

print (re.findall ("^\s",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("^\S",cadena) \n')

print (re.findall ("^\S",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("^\w",cadena) \n')

print (re.findall ("^\w",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("^\W",cadena) \n')

print (re.findall ("^\W",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia al final de la linea  ; -$- simbolo dolar \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".$",cadena) \n')

print (re.findall (".$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d$",cadena) \n')

print (re.findall ("\d$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D$",cadena) \n')

print (re.findall ("\D$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s$",cadena) \n')

print (re.findall ("\s$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S$",cadena) \n')

print (re.findall ("\S$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w$",cadena) \n')

print (re.findall ("\w$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W$",cadena) \n')

print (re.findall ("\W$",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia al inicio de la palabra o linea ; -\A- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("\A.+",cadena) \n')

print (re.findall ("\A.+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\A\d+",cadena) \n')

print (re.findall ("\A\d+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\A\D+",cadena) \n')

print (re.findall ("\A\D+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\A\s+",cadena) \n')

print (re.findall ("\A\s+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\A\S+",cadena) \n')

print (re.findall ("\A\S+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\A\w+",cadena) \n')

print (re.findall ("\A\w+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\A\W+",cadena) \n')

print (re.findall ("\A\W+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia al limite de la palabra  ; -\\b- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".\\b",cadena) \n')

print (re.findall (".\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d\\b",cadena) \n')

print (re.findall ("\d\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D\\b",cadena) \n')

print (re.findall ("\D\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s\\b",cadena) \n')

print (re.findall ("\s\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S\\b",cadena) \n')

print (re.findall ("\S\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w\\b",cadena) \n')

print (re.findall ("\w\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W\\b",cadena) \n')

print (re.findall ("\W\\b",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia un limite que no sea palabra  ; -\B- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".\B",cadena) \n')

print (re.findall (".\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d\B",cadena) \n')

print (re.findall ("\d\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D\B",cadena) \n')

print (re.findall ("\D\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s\B",cadena) \n')

print (re.findall ("\s\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S\B",cadena) \n')

print (re.findall ("\S\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w\B",cadena) \n')

print (re.findall ("\w\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W\B",cadena) \n')

print (re.findall ("\W\B",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia al final de la palabra o linea ; -\Z- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall (".+\Z",cadena) \n')

print (re.findall (".+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("\d+\Z",cadena) \n')

print (re.findall ("\d+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("\D+\Z",cadena) \n')

print (re.findall ("\D+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("\s+\Z",cadena) \n')

print (re.findall ("\s+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("\S+\Z",cadena) \n')

print (re.findall ("\S+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("\w+\Z",cadena) \n')

print (re.findall ("\w+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("\W+\Z",cadena) \n')

print (re.findall ("\W+\Z",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia si la expresion concuerda con la afirmacion -no avanza sobre ella- ; -(?=expresion)- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?=.+)",cadena) \n')

print (re.findall ("(?=.+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?=\d+)",cadena) \n')

print (re.findall ("(?=\d+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?=\D+)",cadena) \n')

print (re.findall ("(?=\D+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?=\s+)",cadena) \n')

print (re.findall ("(?=\s+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?=\S+)",cadena) \n')

print (re.findall ("(?=\S+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?=\w+)",cadena) \n')

print (re.findall ("(?=\w+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?=\W+)",cadena) \n')

print (re.findall ("(?=\W+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia si la expresion NO concuerda con la afirmacion -no avanza sobre ella- ; -(?!expresion)- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?!.+)",cadena) \n')

print (re.findall ("(?!.+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?!\d+)",cadena) \n')

print (re.findall ("(?!\d+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?!\D+)",cadena) \n')

print (re.findall ("(?!\D+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?!\s+)",cadena) \n')

print (re.findall ("(?!\s+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?!\S+)",cadena) \n')

print (re.findall ("(?!\S+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?!\w+)",cadena) \n')

print (re.findall ("(?!\w+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?!\W+)",cadena) \n')

print (re.findall ("(?!\W+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia si la expresion concuerda inmediatamente antes de la afirmacion ; -(?<=expresion)- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?<=.)",cadena) \n')

print (re.findall ("(?<=.)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?<=\d)",cadena) \n')

print (re.findall ("(?<=\d)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?<=\D)",cadena) \n')

print (re.findall ("(?<=\D)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?<=\s)",cadena) \n')

print (re.findall ("(?<=\s)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?<=\S)",cadena) \n')

print (re.findall ("(?<=\S)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?<=\w)",cadena) \n')

print (re.findall ("(?<=\w)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?<=\W)",cadena) \n')

print (re.findall ("(?<=\W)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('coincidencia si la expresion NO concuerda inmediatamente antes de la afirmacion ; -(?!=expresion)- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?!=.+)",cadena) \n')

print (re.findall ("(?!=.+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?!=\d+)",cadena) \n')

print (re.findall ("(?!=\d+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?!=\D+)",cadena) \n')

print (re.findall ("(?!=\D+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?!=\s+)",cadena) \n')

print (re.findall ("(?!=\s+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?!=\S+)",cadena) \n')

print (re.findall ("(?!=\S+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?!=\w+)",cadena) \n')

print (re.findall ("(?!=\w+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?!=\W+)",cadena) \n')

print (re.findall ("(?!=\W+)",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('uso de marcadores en expresiones regulares \n')

print ('marcador formato ASCII -re.A o re.ASCII- ; -(?a)expresion- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?a).+",cadena) \n')

print (re.findall ("(?a).+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?a)\d+",cadena) \n')

print (re.findall ("(?a)\d+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?a)\D+",cadena) \n')

print (re.findall ("(?a)\D+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?a)\s+",cadena) \n')

print (re.findall ("(?a)\s+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?a)\S+",cadena) \n')

print (re.findall ("(?a)\S+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?a)\w+",cadena) \n')

print (re.findall ("(?a)\w+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?a)\W+",cadena) \n')

print (re.findall ("(?a)\W+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('marcador coincidencia sin tener en cuenta las mayusculas -re.I o re.IGNORECASE- ; -(?i)expresion- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?i).+",cadena) \n')

print (re.findall ("(?i).+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?i)\d+",cadena) \n')

print (re.findall ("(?i)\d+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?i)\D+",cadena) \n')

print (re.findall ("(?i)\D+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?i)\s+",cadena) \n')

print (re.findall ("(?i)\s+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?i)\S+",cadena) \n')

print (re.findall ("(?i)\S+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?i)\w+",cadena) \n')

print (re.findall ("(?i)\w+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?i)\W+",cadena) \n')

print (re.findall ("(?i)\W+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('marcador que . -punto- coincida en cada caracter incluyendo las lineas nuevas -\\n-  -re.S o re.DOTALL- ; -(?s)expresion- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?s).+",cadena) \n')

print (re.findall ("(?s).+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?s)\d+",cadena) \n')

print (re.findall ("(?s)\d+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?s)\D+",cadena) \n')

print (re.findall ("(?s)\D+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?s)\s+",cadena) \n')

print (re.findall ("(?s)\s+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?s)\S+",cadena) \n')

print (re.findall ("(?s)\S+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?s)\w+",cadena) \n')

print (re.findall ("(?s)\w+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?s)\W+",cadena) \n')

print (re.findall ("(?s)\W+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('marcador permitir la inclusion de comentarios y espacios en blanco -re.X o re.VERBOSE- ; -(?x)expresion   # COMENTARIO- \n')

print ('concordancia con cualquier caracter menos salto de linea ; . -punto- \n')

print ('re.findall ("(?x).+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x).+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un digito -numero- unicode ; \d  \n')

print ('re.findall ("(?x)\d+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x)\d+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un digito -numero- unicode ; \D  \n')

print ('re.findall ("(?x)\D+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x)\D+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un espacio en blanco unicode ; \s  \n')

print ('re.findall ("(?x)\s+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x)\s+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un valor que no sea un espacio en blanco unicode ; \S  \n')

print ('re.findall ("(?x)\S+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x)\S+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter alfanumerico unicode ; \w  \n')

print ('re.findall ("(?x)\w+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x)\w+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('concordancia con un caracter no alfanumerico unicode ; \W  \n')

print ('re.findall ("(?x)\W+  # COMENTARIO",cadena) \n')

print (re.findall ("(?x)\W+  # COMENTARIO",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('funciones del modulo re : \n')

print ('funcion escape -re.escape- ; devuelve la cadena con todos los caracteres que no son alfanumericos de barra invertida escapados \n')

print ('re.escape (cadena) \n')

print (re.escape (cadena),'\n') # presenta la cadena con todos los caracteres que no son alfanumericos de barra invertida escapados

print ('funcion findall -re.findall- devuelve todas las coincidencias indicadas en la expresion regular encontradas en toda la cadena \n')

print ('re.findall ("\d+",cadena) \n')

print (re.findall ("\d+",cadena),'\n') # presenta una lista con las coincidencias indicadas en la expresion regular abreviada

print ('funcion finditer -re.finditer- devuelve un objeto iterador con las coincidencias indicadas en la expresion regular encontradas en toda la cadena \n')

print ('iterador_finditer = re.finditer ("\d+",cadena) \n')

iterador_finditer = re.finditer ("\d+",cadena) # devuelve un objeto iterador con las coincidencias indicadas en la expresion regular encontradas en toda la cadena 

print ('iterador_finditer ',iterador_finditer,'\n') # presenta el objeto iterador devuelto

print ('iterar el objeto iterador devuelto por iterador_finditer ; for numero,coincidencia in enumerate (iterador_finditer,start=1) : \n')

for numero,coincidencia in enumerate (iterador_finditer,start=1) : # iterador , bucle for in , pasa los elmentos del objeto iterador a coincidencia y los numeros a numero -enumerate numera los elementos del iterador , empiexa en 1-
	print ('COINCIDENCIA Nº {0} - {1} \n'.format (numero,coincidencia.group ())) # presenta una cadena formateada y  sus valores  -numero y elemento coincidente con el metodo group ()-
else : # cuando finalice el iterador
	print ('--- FIN DE LA LISTA DE COINCIDENCIAS ---\n') # presenta la cadena

print ('funcion match -re.match- devuelve un objeto con la coincidencia indicada en la expresion regular encontrada al comienzo de la cadena \n')

print ('coincidencia_inicioCadena = re.match ("[a-zA-Z]+",cadena) \n')

coincidencia_inicioCadena = re.match ("[a-zA-Z]+",cadena) # devuelve un objeto con las coincidencias indicadas en la expresion regular encontradas al comienzo de la cadena

print ('coincidencia_inicioCadena ',coincidencia_inicioCadena,'\n') # presenta el objeto devuelto

print ('presentar la coincidencia del objeto con group ; coincidencia_inicioCadena.group () ',coincidencia_inicioCadena.group (),'\n') # presenta la coincidencia devuelta

print ('funcion search -re.search- devuelve un objeto con la primera coincidencia indicada en la expresion regular encontrada en alguna parte de la cadena \n')

print ('coincidenciaCadena = re.search ("\d+",cadena) \n')

coincidenciaCadena = re.search ("\d+",cadena) # devuelve un objeto con la primera coincidencia indicada en la expresion regular encontrada en alguna parte de la cadena

print ('coincidenciaCadena ',coincidenciaCadena,'\n') # presenta el objeto devuelto

print ('presentar la coincidencia del objeto con group ; coincidenciaCadena.group () ',coincidenciaCadena.group (),'\n') # presenta la coincidencia devuelta

print ('funcion split -re.split- devuelve una lista de cadenas separadas por la expresion regular coincidente \n')

print ('re.split ("\d+",cadena) \n')

print (re.split ("\d+",cadena),'\n') # presenta la lista de la cadena separada por las coincidencias de la expresion regular

print ('funcion sub -re.sub- devuelve una copia de la cadena con cada coincidencia de la expresion regular cambiada por el valor indicado \n')

print ('re.sub ("\d+","?",cadena) \n')

print (re.sub ("\d+","?",cadena),'\n') # presenta una copia de la cadena con cada coincidencia de la expresion regular cambiada por el valor indicado

print ('funcion subn -re.subn- devuelve una tupla 2 elementos con una copia de la cadena con cada coincidencia de la expresion regular cambiada por el valor indicado y el numero de sustituciones realizadas \n')

print ('re.subn ("\d+","?",cadena) \n')

print (re.subn ("\d+","?",cadena),'\n') # presenta una tupla 2 elementos con una copia de la cadena con cada coincidencia de la expresion regular cambiada por el valor indicado y el numero de sustituciones realizadas

print ('funcion compile -re.compile- devuelve una expresion regular compilada para usar con los metodos de este objeto \n')

print ('EXPRESION_REGULAR = re.compile ("\d+") \n')

EXPRESION_REGULAR = re.compile ("\d+") # compila expresion regular

print ('EXPRESION_REGULAR ',EXPRESION_REGULAR,'\n') # presenta la expresion regular compilada

print ('metodos para re.compile : \n')

print ('metodo findall -igual que la funcion- ; EXPRESION_REGULAR.findall (cadena) ',EXPRESION_REGULAR.findall (cadena),'\n') # presenta el resultado del metodo sobre la expresion regular compilada

print ('metodo finditer -igual que la funcion- ; iterador_finditer_compilado = EXPRESION_REGULAR.finditer (cadena) \n')

iterador_finditer_compilado = EXPRESION_REGULAR.finditer (cadena) # devuelve un objeto iterador con las coincidencias indicadas en la expresion regular encontradas en toda la cadena 

print ('iterador_finditer_compilado ',iterador_finditer_compilado,'\n') # presenta el objeto iterador devuelto

print ('iterar el objeto iterador devuelto por iterador_finditer_compilado ; for Numero,Coincidencia in enumerate (iterador_finditer_compilado,start=1) : \n')

for Numero,Coincidencia in enumerate (iterador_finditer_compilado,start=1) : # iterador , bucle for in , pasa los elmentos del objeto iterador a Coincidencia y los numeros a Numero -enumerate numera los elementos del iterador , empiexa en 1-
	print ('COINCIDENCIA Nº {0} - {1} \n'.format (Numero,Coincidencia.group ())) # presenta una cadena formateada y  sus valores  -numero y elemento coincidente con el metodo group ()-
else : # cuando finalice el iterador
	print ('--- FIN DE LA LISTA DE COINCIDENCIAS ---\n') # presenta la cadena

print ('metodo flags ; devuelve los marcadores -opcional- que se indicaron en el compilador de la expresion regular \n')

print ('EXPRESION_REGULAR.flags ',EXPRESION_REGULAR.flags,'\n') # presenta los marcadores que se indicaron en el compilador 

print ('metodo groupindex ; devuelve un diccionario cuyas claves son los nombres de grupo de captura y los valores los numeros del grupo \n')

print ('EXPRESION_REGULAR.groupindex ',EXPRESION_REGULAR.groupindex,'\n') # presenta un diccionario cuyas claves son los nombres de grupo de captura y los valores los numeros del grupo

print ('metodo match -igual que la funcion- ; coincidencia_inicio_cadena = EXPRESION_REGULAR.match (cadena) \n')

coincidencia_inicio_cadena = EXPRESION_REGULAR.match (cadena) # devuelve un objeto con las coincidencias indicadas en la expresion regular encontradas al comienzo de la cadena

print ('coincidencia_inicio_cadena ',coincidencia_inicio_cadena,'\n') # presenta el objeto devuelto

print ('metodo pattern ; devuelve la cadena compila \n')

print ('EXPRESION_REGULAR.pattern ',EXPRESION_REGULAR.pattern,'\n')

print ('metodo search -igual que la funcion- ; coincidencia_cadena = EXPRESION_REGULAR.search (cadena) \n')

coincidencia_cadena = EXPRESION_REGULAR.search (cadena) # devuelve un objeto con las coincidencias indicadas en la expresion regular encontradas al comienzo de la cadena

print ('coincidencia_cadena ',coincidencia_cadena,'\n') # presenta el objeto devuelto

print ('coincidencia_cadena.group () ',coincidencia_cadena.group (),'\n') # presenta la subcadena coincidente

print ('metodo split -igual que la funcion- ; EXPRESION_REGULAR.split (cadena) \n')

print (EXPRESION_REGULAR.split (cadena),'\n') # presenta una lista de cadenas separadas por la coincidencia de la expresion regular compilada

print ('metodo sub -igual que la funcion- ; EXPRESION_REGULAR.sub ("←↓→",cadena) \n')

print (EXPRESION_REGULAR.sub ("←↓→",cadena),'\n') # presenta una copia de la cadena con las coincidencias sustituidas por la cadena indicada

print ('metodo subn -igual que la funcion- ; EXPRESION_REGULAR.subn ("←↓→",cadena) \n')

print (EXPRESION_REGULAR.subn ("←↓→",cadena),'\n') # presenta una tupla de dos con una copia de la cadena con las coincidencias sustituidas por la cadena indicada y el numero de sustituciones

print ('atributos y metodos de los objetos de coincidencia ; finditer , match y search \n')

ITERADOR_finditer = re.finditer ("\d+",cadena) # devuelve un objeto iterador con las coincidencias indicadas en la expresion regular encontradas en toda la cadena 

COINCIDENCIA_inicioCadena = re.match ("[a-zA-Z]+",cadena) # devuelve un objeto con las coincidencias indicadas en la expresion regular encontradas al comienzo de la cadena

COINCIDENCIACadena = re.search ("\d+",cadena) # devuelve un objeto con la primera coincidencia indicada en la expresion regular encontrada en alguna parte de la cadena

print ('ITERADOR_finditer = re.finditer ("\d+",cadena) \n')

print ('COINCIDENCIA_inicioCadena = re.match ("[a-zA-Z]+",cadena) \n')

print ('COINCIDENCIACadena = re.search ("\d+",cadena) \n')

print ('metodo end ; devuelve la posicion final -indice- de la coincidencia en el texto para el grupo indicado o el grupo 0 -toda la cadena coincidente- \n')

print ('COINCIDENCIA_inicioCadena.end () ',COINCIDENCIA_inicioCadena.end (),'\n') # presenta la posicion final -indice- de la coincidencia en el texto

print ('COINCIDENCIACadena.end () ',COINCIDENCIACadena.end (),'\n') # presenta la posicion final -indice- de la coincidencia en el texto

print ('for numeroOBJETO,objeto in enumerate (ITERADOR_finditer,start=1) : \n')

for numeroOBJETO,objeto in enumerate (ITERADOR_finditer,start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.end () : {1} \n'.format (numeroOBJETO,objeto.end ())) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena
	
print ('atributo endpos ; la posicion del final del texto \n')

print ('COINCIDENCIA_inicioCadena.endpos ',COINCIDENCIA_inicioCadena.endpos,'\n') # presenta la posicion del final del texto

print ('COINCIDENCIACadena.endpos ',COINCIDENCIACadena.endpos,'\n') # presenta la posicion del final del texto

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.endpos : {1} \n'.format (numeroOBJETO,objeto.endpos)) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('metodo expand ; devuelve la cadena indicada con los marcadores de captura sustituidos por las coincidencias correspondientes \n')

print ('COINCIDENCIA_inicioCadena.expand (cadena) \n')

print (COINCIDENCIA_inicioCadena.expand (cadena),'\n') # presenta la cadena indicada con los marcadores de captura sustituidos por las coincidencias correspondientes

print ('COINCIDENCIACadena.expand (cadena) \n')

print (COINCIDENCIACadena.expand (cadena),'\n') # presenta la cadena indicada con los marcadores de captura sustituidos por las coincidencias correspondientes

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.expand (cadena) : \n\n{1} \n'.format (numeroOBJETO,objeto.expand (cadena))) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('metodo group ; devuelve la coincidencia con la cadena de la expresion regular \n')

print ('COINCIDENCIA_inicioCadena.group () ',COINCIDENCIA_inicioCadena.group (),'\n') # presenta la coincidencia con la cadena de la expresion regular

print ('COINCIDENCIACadena.group () ',COINCIDENCIACadena.group (),'\n') # presenta la coincidencia con la cadena de la expresion regular

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.group () : {1} \n'.format (numeroOBJETO,objeto.group ())) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('metodo groupdict ; devuelve un diccionario con el grupo de captura como clave y la coincidencia como valor \n')

print ('COINCIDENCIA_inicioCadena.groupdict () ',COINCIDENCIA_inicioCadena.groupdict (),'\n') # presenta un diccionario con el grupo de captura como clave y la coincidencia como valor

print ('COINCIDENCIACadena.groupdict () ',COINCIDENCIACadena.groupdict (),'\n') # presenta un diccionario con el grupo de captura como clave y la coincidencia como valor

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.groupdict () : {1} \n'.format (numeroOBJETO,objeto.groupdict ())) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('metodo groups ; devuelve una tupla con todos los grupos de captura \n')

print ('COINCIDENCIA_inicioCadena.groups () ',COINCIDENCIA_inicioCadena.groups (),'\n') # presenta una tupla con todos los grupos de captura

print ('COINCIDENCIACadena.groups () ',COINCIDENCIACadena.groups (),'\n') # presenta una tupla con todos los grupos de captura

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.groups () : {1} \n'.format (numeroOBJETO,objeto.groups ())) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('atributo lastgroup ; devuelve el nombre del ultimo grupo de captura que coincidio o None -si no contiene grupos- \n')

print ('COINCIDENCIA_inicioCadena.lastgroup ',COINCIDENCIA_inicioCadena.lastgroup,'\n') # presenta el nombre del ultimo grupo de captura que coincidio o None 

print ('COINCIDENCIACadena.lastgroup ',COINCIDENCIACadena.lastgroup,'\n') # presenta el nombre del ultimo grupo de captura que coincidio o None 

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.lastgroup : {1} \n'.format (numeroOBJETO,objeto.lastgroup)) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('atributo lastindex ; devuelve el numero del ultimo grupo de captura que coincidio o None -si no contiene grupos- \n')

print ('COINCIDENCIA_inicioCadena.lastindex ',COINCIDENCIA_inicioCadena.lastindex,'\n') # presenta el numero del ultimo grupo de captura que coincidio o None 

print ('COINCIDENCIACadena.lastindex ',COINCIDENCIACadena.lastindex,'\n') # presenta el numero del ultimo grupo de captura que coincidio o None 

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.lastindex : {1} \n'.format (numeroOBJETO,objeto.lastindex)) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('atributo pos ; devuelve la posicion inicial desde la que comienza a buscar en la cadena \n')

print ('COINCIDENCIA_inicioCadena.pos ',COINCIDENCIA_inicioCadena.pos,'\n') # presenta la posicion inicial desde la que comienza a buscar en la cadena 

print ('COINCIDENCIACadena.pos ',COINCIDENCIACadena.pos,'\n') # presenta la posicion inicial desde la que comienza a buscar en la cadena 

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.pos : {1} \n'.format (numeroOBJETO,objeto.pos)) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('atributo re ; devuelve la expresion regular que produjo el objeto coincidente \n')

print ('COINCIDENCIA_inicioCadena.re ',COINCIDENCIA_inicioCadena.re,'\n') # presenta la expresion regular que produjo el objeto coincidente 

print ('COINCIDENCIACadena.re ',COINCIDENCIACadena.re,'\n') # presenta la expresion regular que produjo el objeto coincidente 

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.re : {1} \n'.format (numeroOBJETO,objeto.re)) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('metodo span ; devuelve la posicion de inicio y de fin de la coincidencia en la cadena \n')

print ('COINCIDENCIA_inicioCadena.span () ',COINCIDENCIA_inicioCadena.span (),'\n') # presenta la posicion de inicio y de fin de la coincidencia en la cadena 

print ('COINCIDENCIACadena.span () ',COINCIDENCIACadena.span (),'\n') # presenta la posicion de inicio y de fin de la coincidencia en la cadena 

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.span () : {1} \n'.format (numeroOBJETO,objeto.span ())) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('metodo start ; devuelve la posicion de inicio de la coincidencia en la cadena \n')

print ('COINCIDENCIA_inicioCadena.start () ',COINCIDENCIA_inicioCadena.start (),'\n') # presenta la posicion de inicio de la coincidencia en la cadena 

print ('COINCIDENCIACadena.start () ',COINCIDENCIACadena.start (),'\n') # presenta la posicion de inicio de la coincidencia en la cadena 

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.start () : {1} \n'.format (numeroOBJETO,objeto.start ())) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena

print ('atribuito string ; devuelve la cadena analizada por la expresion regular \n')

print ('COINCIDENCIA_inicioCadena.string \n') 

print (COINCIDENCIA_inicioCadena.string,'\n') # presenta la cadena analizada por la expresion regular

print ('COINCIDENCIACadena.string \n') 

print (COINCIDENCIACadena.string,'\n') # presenta la cadena analizada por la expresion regular

print ('for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : \n')

for numeroOBJETO,objeto in enumerate (re.finditer ("\d+",cadena),start=1) : # iterador , bucle for in , pasa los numeros a numeroOBJETO y los objetos de coincidencia del iterador a objeto -enumerate numera los elementos del objeto , empezando en 1-
	print ('Nº {0} - objeto.string : \n\n{1} \n'.format (numeroOBJETO,objeto.string)) # presenta la cadena formateada y sus valores -numero y coincidencia-
else : # cuando finalice el iterador 
	print (' fin del objeto iterador : ITERADOR_finditer \n') # presenta la cadena














