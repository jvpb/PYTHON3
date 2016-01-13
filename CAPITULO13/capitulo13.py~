#!/usr/bin/env python3
'''introduccion a la programacion GUI -uso del modulo PyQt5-'''

# importar modulo

import sys # importa el modulo indicado

print ('VERSION en uso de PYTHON \n')

print (sys.version,'\n')

print ('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

print ('importar modulo lenguaje GUI QT5 para crear ventanas -modulo QtWidgets-  ; import PyQt5.QtWidgets \n')

import PyQt5.QtWidgets # importa el modulo indicado del lenguaje QT5 -paquete PyQt5-

print ('importar modulo lenguaje GUI QT5 para graficos -modulo QtGui- ; import PyQt5.QtGui \n')

import PyQt5.QtGui # importa el modulo indicado del lenguaje QT5 -paquete PyQt5-

print ('importar modulo lenguaje GUI QT5 para nucleo QT -modulo QtCore- ; import PyQt5.QtCore \n')

import PyQt5.QtCore # importa el modulo indicado del lenguaje QT5 -paquete PyQt5-

print ('crear la clase InterfazGraficaUsuario ; class InterfazGraficaUsuario (object) : \n')

class InterfazGraficaUsuario (object) : # definicion de la clase
	def ventanaBASICA (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana
		ventana.resize (250,150) # tamaño de la ventana al crearse en pixels -ancho,alto-
		ventana.move (300,300) # mueve la ventana a las coordenadas en pixels de la pantalla
		ventana.setWindowTitle ('ventanaBASICA') # titulo de la ventana en la parte superior 
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto-
		
	def ventanaBASICAconICONO (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana
		ventana.setGeometry (300,300,400,220) # los dos primeros valores mueve la ventana a las coordenadas en pixels de la pantalla (move (300,300)) y los dos segundos valores el tamaño de la ventana al crearse en pixels -ancho,alto- (resize (300,220))
		ventana.setWindowTitle ('ventanaBASICAconICONO') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
		
	def ventanaBASICA_ICONO_textoInformativo (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana
		ventana.setGeometry (300,300,400,220) # los dos primeros valores mueve la ventana a las coordenadas en pixels de la pantalla (move (300,300)) y los dos segundos valores el tamaño de la ventana al crearse en pixels -ancho,alto- (resize (300,220))
		ventana.setWindowTitle ('ventanaBASICA_ICONO_textoInformativo') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
		
	def ventanaBOTON (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana
		ventana.setGeometry (300,300,400,220) # los dos primeros valores mueve la ventana a las coordenadas en pixels de la pantalla (move (300,300)) y los dos segundos valores el tamaño de la ventana al crearse en pixels -ancho,alto- (resize (300,220))
		ventana.setWindowTitle ('ventanaBOTON') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR',ventana) # crea el objeto boton -con un icono , texto en el boton y llama al constructor de ventanas y sus datos-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.resize (botonSALIR.sizeHint ()) # tamaño del boton al crearse en pixels -ancho,alto- , metodo tamaño automatico ajustado al texto e icono
		botonSALIR.move (50,50) # mueve el boton a las coordenadas en pixels de la ventana interior
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
		
	def ventanaBOTON_CENTRADA (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = PyQt5.QtWidgets.QWidget ().frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaBOTON_CENTRADA') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR',ventana) # crea el objeto boton -con un icono , texto en el boton y llama al constructor de ventanas y sus datos-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.resize (botonSALIR.sizeHint ()) # tamaño del boton al crearse en pixels -ancho,alto- , metodo tamaño automatico ajustado al texto e icono
		botonSALIR.move (50,50) # mueve el boton a las coordenadas en pixels de la ventana interior
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaCENTRADA_barraESTADO (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QMainWindow () # crea el objeto constructor de ventana principal
		ventana.statusBar ().showMessage ('PREPARADO - pulse boton SALIR para cerrar la ventana') # crea la barra de estado con el mensaje indicado en la cadena
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = PyQt5.QtWidgets.QWidget ().frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaCENTRADA_barraESTADO') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR',ventana) # crea el objeto boton -con un icono , texto en el boton y llama al constructor de ventanas y sus datos-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.resize (botonSALIR.sizeHint ()) # tamaño del boton al crearse en pixels -ancho,alto- , metodo tamaño automatico ajustado al texto e icono
		botonSALIR.move (50,50) # mueve el boton a las coordenadas en pixels de la ventana interior
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaBarraESTADO_barraMENU (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QMainWindow () # crea el objeto constructor de ventana principal
		accionSALIR = PyQt5.QtWidgets.QAction (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'&Salir',ventana) # crea el objeto accion con un icono y texto indicativo
		accionSALIR.setShortcut ('Ctrl+S') # crea accion corta teclado -salir-
		accionSALIR.setStatusTip ('SALIDA APLICACION') # crea texto informativo accion que se presenta en la barra de estado
		accionSALIR.triggered.connect (PyQt5.QtWidgets.qApp.quit) # envia la señal para salir de la aplicacion -ventana- 
		ventana.statusBar () # crea la barra de estado con el mensaje indicado en setStatusTip 
		barraMENU = ventana.menuBar () # crea la barra de menu 
		menuFICHERO = barraMENU.addMenu ('&Fichero') # añade a la barra menu el texto
		menuFICHERO.addAction (accionSALIR) # añade a la barra menu la accion a ejecutar -accionSALIR-
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = PyQt5.QtWidgets.QWidget ().frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaBarraESTADO_barraMENU') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR',ventana) # crea el objeto boton -con un icono , texto en el boton y llama al constructor de ventanas y sus datos-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.resize (botonSALIR.sizeHint ()) # tamaño del boton al crearse en pixels -ancho,alto- , metodo tamaño automatico ajustado al texto e icono
		botonSALIR.move (125,110) # mueve el boton a las coordenadas en pixels de la ventana interior
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaBarraESTADO_MENU_barraICONOS_EDITORtexto (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QMainWindow () # crea el objeto constructor de ventana principal
		textoEDITADO = PyQt5.QtWidgets.QTextEdit () # crea el objeto editor  de texto para la ventana
		ventana.setCentralWidget (textoEDITADO) # crea y ocupa todo el espacio central , ajusta el texto a la izquierda de la ventana
		accionSALIR = PyQt5.QtWidgets.QAction (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'&Salir',ventana) # crea el objeto accion con un icono y texto indicativo
		accionSALIR.setShortcut ('Ctrl+S') # crea accion corta teclado -salir-
		accionSALIR.setStatusTip ('SALIDA APLICACION') # crea texto informativo accion que se presenta en la barra de estado
		accionSALIR.triggered.connect (PyQt5.QtWidgets.qApp.quit) # envia la señal para salir de la aplicacion -ventana- 
		ventana.statusBar () # crea la barra de estado con el mensaje indicado en setStatusTip 
		barraMENU = ventana.menuBar () # crea la barra de menu 
		menuFICHERO = barraMENU.addMenu ('&Fichero') # añade a la barra menu el texto
		menuFICHERO.addAction (accionSALIR) # añade a la barra menu la accion a ejecutar -accionSALIR-
		ventana.toolbar = ventana.addToolBar ('Salir') # crea la barra de iconos y le añade el texto informativo
		ventana.toolbar.addAction (accionSALIR) # añade a la barra de iconos la accion a ejecutar -accionSALIR- 
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = PyQt5.QtWidgets.QWidget ().frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaBarraESTADO_MENU_barraICONOS') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR',ventana) # crea el objeto boton -con un icono , texto en el boton y llama al constructor de ventanas y sus datos-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.resize (botonSALIR.sizeHint ()) # tamaño del boton al crearse en pixels -ancho,alto- , metodo tamaño automatico ajustado al texto e icono
		botonSALIR.move (305,190) # mueve el boton a las coordenadas en pixels de la ventana interior
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaETIQUETA (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QMainWindow () # crea el objeto constructor de ventana principal
		textoEDITADO = PyQt5.QtWidgets.QTextEdit () # crea el objeto editor  de texto  para la ventana
		ventana.setCentralWidget (textoEDITADO) # crea y ocupa todo el espacio central , ajusta el texto a la izquierda de la ventana
		etiqueta = PyQt5.QtWidgets.QLabel ('ETIQUETA',ventana) # crea el objeto etiqueta con la cadena indicada
		etiqueta.move(7,195) # mueve la etiqueta a las coordenadas en pixels del interior de la ventana
		accionSALIR = PyQt5.QtWidgets.QAction (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'&Salir',ventana) # crea el objeto accion con un icono y texto indicativo
		accionSALIR.setShortcut ('Ctrl+S') # crea accion corta teclado -salir-
		accionSALIR.setStatusTip ('SALIDA APLICACION') # crea texto informativo accion que se presenta en la barra de estado
		accionSALIR.triggered.connect (PyQt5.QtWidgets.qApp.quit) # envia la señal para salir de la aplicacion -ventana- 
		ventana.statusBar () # crea la barra de estado con el mensaje indicado en setStatusTip 
		barraMENU = ventana.menuBar () # crea la barra de menu 
		menuFICHERO = barraMENU.addMenu ('&Fichero') # añade a la barra menu el texto
		menuFICHERO.addAction (accionSALIR) # añade a la barra menu la accion a ejecutar -accionSALIR-
		ventana.toolbar = ventana.addToolBar ('Salir') # crea la barra de iconos y le añade el texto informativo
		ventana.toolbar.addAction (accionSALIR) # añade a la barra de iconos la accion a ejecutar -accionSALIR- 
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = PyQt5.QtWidgets.QWidget ().frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaETIQUETA') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR',ventana) # crea el objeto boton -con un icono , texto en el boton y llama al constructor de ventanas y sus datos-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.resize (botonSALIR.sizeHint ()) # tamaño del boton al crearse en pixels -ancho,alto- , metodo tamaño automatico ajustado al texto e icono
		botonSALIR.move (305,190) # mueve el boton a las coordenadas en pixels de la ventana interior
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaETIQUETA_BOTONES (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana 
		etiqueta = PyQt5.QtWidgets.QLabel ('ETIQUETA',ventana) # crea el objeto etiqueta con la cadena indicada
		etiqueta.move(7,195) # mueve la etiqueta a las coordenadas en pixels del interior de la ventana
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR') # crea el objeto boton -con un icono , texto en el boton-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		botonCANCELAR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CANCELAR') # crea el objeto boton -con un icono , texto en el boton-
		botonCANCELAR.setToolTip ('ESTE ES EL BOTON PARA <b>CANCELAR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		crearBotonesHORIZONTAL = PyQt5.QtWidgets.QHBoxLayout () # objeto creador boton posicion horizontal
		crearBotonesHORIZONTAL.addStretch (1) # añadir espacio entre botones -horizontal-
		crearBotonesHORIZONTAL.addWidget (botonCANCELAR) # añade el boton indicado
		crearBotonesHORIZONTAL.addWidget (botonSALIR) # añade el boton indicado
		crearBotonesVERTICAL = PyQt5.QtWidgets.QVBoxLayout () # objeto creador boton posicion vertical 
		crearBotonesVERTICAL.addStretch (1) # añadir espacio entre botones y ventana -vertical-
		crearBotonesVERTICAL.addLayout (crearBotonesHORIZONTAL) # añade los botones indicados a la ventana en la parte derecha
		ventana.setLayout (crearBotonesVERTICAL) # crea los botones
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = ventana.frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaETIQUETA_BOTONES') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaCUADRICULA_BOTONES (self) :  # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana 
		etiqueta = PyQt5.QtWidgets.QLabel ('CALCULADORA',ventana) # crea el objeto etiqueta con la cadena indicada
		etiqueta.move(7,227) # mueve la etiqueta a las coordenadas en pixels del interior de la ventana
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR') # crea el objeto boton -con un icono , texto en el boton-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		botonLIMPIAR = PyQt5.QtWidgets.QPushButton ('LIMPIAR') # crea el objeto boton -texto en el boton-
		botonLIMPIAR.setToolTip ('ESTE ES EL BOTON PARA <b>LIMPIAR</b> RESULTADOS') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonATRAS = PyQt5.QtWidgets.QPushButton ('RETROCEDER') # crea el objeto boton -texto en el boton-
		botonATRAS.setToolTip ('ESTE ES EL BOTON PARA <b>RETROCEDER</b> UNA POSICION') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton7 = PyQt5.QtWidgets.QPushButton ('7') # crea el objeto boton -texto en el boton-
		boton7.setToolTip ('ESTE ES EL BOTON NUMERO <b>7</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton8 = PyQt5.QtWidgets.QPushButton ('8') # crea el objeto boton -texto en el boton-
		boton8.setToolTip ('ESTE ES EL BOTON NUMERO <b>8</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton9 = PyQt5.QtWidgets.QPushButton ('9') # crea el objeto boton -texto en el boton-
		boton9.setToolTip ('ESTE ES EL BOTON NUMERO <b>9</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonDIVISION = PyQt5.QtWidgets.QPushButton ('/') # crea el objeto boton -texto en el boton-
		botonDIVISION.setToolTip ('ESTE ES EL BOTON PARA <b>DIVISION</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton4 = PyQt5.QtWidgets.QPushButton ('4') # crea el objeto boton -texto en el boton-
		boton4.setToolTip ('ESTE ES EL BOTON NUMERO <b>4</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton5 = PyQt5.QtWidgets.QPushButton ('5') # crea el objeto boton -texto en el boton-
		boton5.setToolTip ('ESTE ES EL BOTON NUMERO <b>5</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton6 = PyQt5.QtWidgets.QPushButton ('6') # crea el objeto boton -texto en el boton-
		boton6.setToolTip ('ESTE ES EL BOTON NUMERO <b>6</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonMULTIPLICACION = PyQt5.QtWidgets.QPushButton ('*') # crea el objeto boton -texto en el boton-
		botonMULTIPLICACION.setToolTip ('ESTE ES EL BOTON PARA <b>MULTIPLICACION</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton1 = PyQt5.QtWidgets.QPushButton ('1') # crea el objeto boton -texto en el boton-
		boton1.setToolTip ('ESTE ES EL BOTON NUMERO <b>1</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton2 = PyQt5.QtWidgets.QPushButton ('2') # crea el objeto boton -texto en el boton-
		boton2.setToolTip ('ESTE ES EL BOTON NUMERO <b>2</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton3 = PyQt5.QtWidgets.QPushButton ('3') # crea el objeto boton -texto en el boton-
		boton3.setToolTip ('ESTE ES EL BOTON NUMERO <b>3</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonRESTA = PyQt5.QtWidgets.QPushButton ('-') # crea el objeto boton -texto en el boton-
		botonRESTA.setToolTip ('ESTE ES EL BOTON PARA <b>RESTAR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		boton0 = PyQt5.QtWidgets.QPushButton ('0') # crea el objeto boton -texto en el boton-
		boton0.setToolTip ('ESTE ES EL BOTON NUMERO <b>0</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonPUNTO = PyQt5.QtWidgets.QPushButton ('.') # crea el objeto boton -texto en el boton-
		botonPUNTO.setToolTip ('ESTE ES EL BOTON PARA <b>PUNTO DECIMAL</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonIGUAL = PyQt5.QtWidgets.QPushButton ('=') # crea el objeto boton -texto en el boton-
		botonIGUAL.setToolTip ('ESTE ES EL BOTON PARA <b>RESULTADO</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSUMA = PyQt5.QtWidgets.QPushButton ('+') # crea el objeto boton -texto en el boton-
		botonSUMA.setToolTip ('ESTE ES EL BOTON PARA <b>SUMAR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		rejillaBotones = PyQt5.QtWidgets.QGridLayout () # crea el objeto cuadricula para botones
		ventana.setLayout (rejillaBotones) # crea la cuadricula
		listaNOMBRES_BOTONES = [botonLIMPIAR,botonATRAS,False,botonSALIR,boton7,boton8,boton9,botonDIVISION,boton4,boton5,boton6,botonMULTIPLICACION,boton1,boton2,boton3,botonRESTA,boton0,botonPUNTO,botonIGUAL,botonSUMA] # lista de botones
		listaPOSICION_BOTONES = [(linea,columna) for linea in range (5) for columna in range (4)] # generador por compresion posicion botones en la cuadricula
		for posicionBoton,nombreBoton in zip (listaPOSICION_BOTONES,listaNOMBRES_BOTONES) : # iterador , bucle for in , pasa las posiciones a posicionBoton y los botones a nombreBoton -zip devuelve una tupla con los valores de ambas listas en tuplas de dos elementos 
			if nombreBoton == False : # condicion , si se cumple
				continue # vuelve al siguiente valor del iterador
			rejillaBotones.addWidget (nombreBoton,*posicionBoton) # añade el boton indicado en la posicion de la rejilla 
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = ventana.frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaCUADRICULA_BOTONES') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaCUADRICULA_editortEXTO (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana 
		etiqueta = PyQt5.QtWidgets.QLabel ('CAMPOS TEXTO',ventana) # crea el objeto etiqueta con la cadena indicada
		etiqueta.move(7,227) # mueve la etiqueta a las coordenadas en pixels del interior de la ventana
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR') # crea el objeto boton -con un icono , texto en el boton-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		etiquetaTitulo = PyQt5.QtWidgets.QLabel ('TITULO') # crea el objeto etiqueta con la cadena indicada
		etiquetaAutor = PyQt5.QtWidgets.QLabel ('AUTOR') # crea el objeto etiqueta con la cadena indicada
		etiquetaReseña = PyQt5.QtWidgets.QLabel ('RESEÑA') # crea el objeto etiqueta con la cadena indicada
		textoTitulo = PyQt5.QtWidgets.QLineEdit () # crea un campo de texto -linea de texto-
		textoTitulo.setToolTip ('PONER <b>TITULO</b> AQUI') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la linea de campo
		textoAutor = PyQt5.QtWidgets.QLineEdit () # crea un campo de texto -linea de texto-
		textoAutor.setToolTip ('PONER <b>AUTOR</b> AQUI') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la linea de campo
		textoReseña = PyQt5.QtWidgets.QTextEdit () # crea un bloque de texto -editor texto-
		textoReseña.setToolTip ('PONER <b>RESEÑA</b> AQUI') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el editor de texto
		rejilla = PyQt5.QtWidgets.QGridLayout () # crea el objeto cuadricula 
		rejilla.addWidget (etiquetaTitulo,1,0) # añade la etiqueta indicada en la posicion de la rejilla
		rejilla.addWidget (textoTitulo,1,1) # añade la linea de campo indicada en la posicion de la rejilla
		rejilla.addWidget (etiquetaAutor,2,0) # añade la etiqueta indicada en la posicion de la rejilla
		rejilla.addWidget (textoAutor,2,1) # añade la linea de campo indicada en la posicion de la rejilla
		rejilla.addWidget (etiquetaReseña,3,0) # añade la etiqueta indicada en la posicion de la rejilla
		rejilla.addWidget (textoReseña,3,1,4,1) # añade el editor de texto indicado en la posicion de la rejilla
		rejilla.addWidget (botonSALIR,5,0,5,1) # añade el boton indicado en la posicion de la rejilla
		ventana.setLayout (rejilla) # crea la cuadricula
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto-
		formaVentana = ventana.frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaCUADRICULA_editortEXTO') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
	
	def ventanaLCD (self) : # definicion del metodo
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana 
		etiqueta = PyQt5.QtWidgets.QLabel ('PANTALLA LCD',ventana) # crea el objeto etiqueta con la cadena indicada
		etiqueta.move(7,231) # mueve la etiqueta a las coordenadas en pixels del interior de la ventana
		lcd = PyQt5.QtWidgets.QLCDNumber (ventana) # crea el display numerico en formato lcd 
		lcd.setToolTip ('PANTALLA TIPO  <b>LCD</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la pantalla lcd 
		barraDeslizante = PyQt5.QtWidgets.QSlider (PyQt5.QtCore.Qt.Horizontal,ventana) # crea la barra deslizante horizontal -PyQt5.QtCore.Qt.Horizontal-
		barraDeslizante.setToolTip ('DESLIZAR <b>BOTON</b> PARA CAMBIAR VALOR PANTALLA LCD') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la barra deslizante
		barraDeslizante.valueChanged.connect (lcd.display) # cambia el valor de la pantalla lcd al mover la barra deslizante
		botonSALIR = PyQt5.QtWidgets.QPushButton (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png'),'CERRAR') # crea el objeto boton -con un icono , texto en el boton-
		botonSALIR.setToolTip ('ESTE ES EL BOTON PARA <b>SALIR</b>') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por el boton
		botonSALIR.clicked.connect (PyQt5.QtCore.QCoreApplication.instance ().quit) # llama y ejecuta el metodo indicado del modulo QtCore al hacer click sobre el boton -cierra la ventana ; quit-
		ventanaVirtual = PyQt5.QtWidgets.QVBoxLayout () # crea la ventana virtual 
		ventanaVirtual.addWidget (lcd) # añade el objeto creador a la ventana virtual -pantalla lcd-
		ventanaVirtual.addWidget (barraDeslizante) # añade el objeto creador a la ventana virtual -barra deslizante-
		ventanaVirtual.addWidget (botonSALIR) # añade el objeto creador a la ventana virtual -boton salir-
		ventana.setLayout (ventanaVirtual) # crea la ventana virtual con sus componentes añadidos
		ventana.resize (400,250) # tamaño de la ventana al crearse en pixels -ancho,alto- 
		formaVentana = ventana.frameGeometry () # especifica la forma de la ventana -rectangulo-
		puntoCentralVentana = PyQt5.QtWidgets.QDesktopWidget ().availableGeometry ().center () # devuelve el punto cental en relacion a la resolucion de la pantalla
		formaVentana.moveCenter (puntoCentralVentana) # prepara la ventana rectangular al punto central de la pantalla , coincidiendo el punto central de la ventana con el de la pantalla
		ventana.move (formaVentana.topLeft ()) # mueve el punto superior izquierdo de la ventana al punto superior izquierdo de formaVentana , centrando la ventana con el centro de la pantalla
		ventana.setWindowTitle ('ventanaLCD') # titulo de la ventana en la parte superior 
		ventana.setWindowIcon (PyQt5.QtGui.QIcon ('./Escritorio/ICONO.png')) # establece el icono de la aplicacion -recibe el fichero de icono de la ruta indicada por el modulo QtGui-
		ventana.setToolTip ('esto es un texto informativo <b><i>setToolTip</i></b> que sale al poner el puntero sobre la ventana vacia') # crea el mensaje de texto enriquecido con el formato RTF que sera presentado al pasar el cursor por la ventana vacia
		ventana.show () # genera la ventana con las especificaciones indicadas
		sys.exit (aplicacion.exec_()) # sale del script python -ejecuta la aplicacion del objeto en bucle-
		
	def VENTANA_MENSAJE (self) : # definicion del metodo 
		aplicacion = PyQt5.QtWidgets.QApplication (sys.argv) # crea el objeto aplicacion
		ventana = PyQt5.QtWidgets.QWidget () # crea el objeto constructor de ventana
		ventana.setGeometry (300,300,300,220) # los dos primeros valores mueve la ventana a las coordenadas en pixels de la pantalla (move (300,300)) y los dos segundos valores el tamaño de la ventana al crearse en pixels -ancho,alto- (resize (300,220))
		ventana.setWindowTitle ('VENTANA_MENSAJE') # titulo de la ventana en la parte superior
		respuestaEVENTO_CIERRE = PyQt5.QtWidgets.QMessageBox.question (ventana,'caja mensaje','QUIERE SALIR ?',PyQt5.QtWidgets.QMessageBox.Yes | PyQt5.QtWidgets.QMessageBox.No,PyQt5.QtWidgets.QMessageBox.No) # crea la caja de mensajes con el titulo de la primera cadena y el mensaje en la ventana de la segunda cadena , la combinacion de botones y el boton por defecto marcado , devuelve el valor del boton marcado
		if respuestaEVENTO_CIERRE == PyQt5.QtWidgets.QMessageBox.Yes : # condicion , si el valor -evento- devuelto es igual al indicado
			ventana.close () # acepta el evento y cierra la ventana
		else : # en caso que el valor -evento- no sea el indicado
			ventana.close () # acepta el evento y cierra la ventana 
			
print ('instanciar y crear objeto de la clase InterfazGraficaUsuario ; GUI = InterfazGraficaUsuario () \n')

GUI = InterfazGraficaUsuario () # instancia y crea el objeto de la clase

print ('ejecutar ventana basica ; GUI.ventanaBASICA () \n')

GUI.ventanaBASICA () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana vacia con el titulo

print ('ejecutar ventana basica con icono ; GUI.ventanaBASICAconICONO () \n')

GUI.ventanaBASICAconICONO () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana vacia con el titulo y un icono a la izquierda

print ('ejecutar ventana basica con icono y texto informativo ; GUI.ventanaBASICA_ICONO_textoInformativo () \n')

GUI.ventanaBASICA_ICONO_textoInformativo () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana vacia con el titulo y un icono a la izquierda y un texto informativo al pasar el puntero

print ('ejecutar ventana con boton  de salir con icono y texto informativo ; GUI.ventanaBOTON () \n')

GUI.ventanaBOTON () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un boton de salida y texto informativo

print ('ejecutar ventana con boton  de salir con icono y texto informativo centrada en pantalla ; GUI.ventanaBOTON_CENTRADA () \n')

GUI.ventanaBOTON_CENTRADA () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un boton de salida y texto informativo centrada en pantalla 

print ('ejecutar ventana centrada en pantalla con boton y barra de estado  ; GUI.ventanaCENTRADA_barraESTADO () \n')

GUI.ventanaCENTRADA_barraESTADO () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un boton y barra de estado centrada en pantalla 

print ('ejecutar ventana centrada en pantalla con boton , barra de estado y barra menu  ; GUI.ventanaBarraESTADO_barraMENU () \n')

GUI.ventanaBarraESTADO_barraMENU () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un boton , barra de estado y barra menu centrada en pantalla

print ('ejecutar ventana centrada en pantalla con boton , barra de estado , barra menu , barra iconos y editor de texto  ; GUI.ventanaBarraESTADO_MENU_barraICONOS_EDITORtexto () \n')

GUI.ventanaBarraESTADO_MENU_barraICONOS_EDITORtexto () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un boton , barra de estado , barra menu , barra iconos y editor texto centrada en pantalla

print ('ejecutar ventana centrada en pantalla con boton , barra de estado , barra menu , barra iconos , editor de texto y etiquetas  ; GUI.ventanaETIQUETA () \n')

GUI.ventanaETIQUETA () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un boton , barra de estado , barra menu , barra iconos , editor texto y etiqueta centrada en pantalla

print ('ejecutar ventana centrada en pantalla con botones y etiquetas  ; GUI.ventanaETIQUETA_BOTONES () \n')

GUI.ventanaETIQUETA_BOTONES () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con un botones y etiquetas centrada en pantalla

print ('ejecutar ventana centrada en pantalla con botones en cuadricula  ; GUI.ventanaCUADRICULA_BOTONES () \n')


GUI.ventanaCUADRICULA_BOTONES () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con una cuadricula de botones centrada en pantalla

print ('ejecutar ventana centrada en pantalla con etiquetas y campos de texto en cuadricula  ; GUI.ventanaCUADRICULA_editortEXTO () \n')

GUI.ventanaCUADRICULA_editortEXTO () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con una cuadricula de etiquetas y campos de texto  centrada en pantalla

print ('ejecutar ventana centrada en pantalla con pantalla lcd , boton deslizante y boton salir  ; GUI.ventanaLCD () \n')

GUI.ventanaLCD () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana con una pantalla lcd , boton deslizante y boton salir centrada en pantalla

print ('ejecutar ventana : crea una ventana de mensaje standard con dos botones  de salida  ; GUI.VENTANA_MENSAJE () \n')

GUI.VENTANA_MENSAJE () # ejecuta el metodo del objeto -ejecuta el codigo del lenguaje QT5 , PyQt5- , crea una ventana de mensaje standard con dos botones  de salida 





