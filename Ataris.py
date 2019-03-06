########################################################################
#						      Librerías							       #
########################################################################

from lxml import etree
from os import system	#	Esta librería la importo para usar el comando clear
#							y mantener de este modo una salida por pantalla limpia

########################################################################
#						      Funciones							       #
########################################################################

def BuscadorDeJuegos(juego): 	#	Recibe una cadena, y busca esa cadena entre todos
								#	los títulos del fichero
	ListaCompleta = EliminarRepetidos(guia.xpath('//game/description/text()'))
	Saga = []
	for Cartucho in ListaCompleta:
		if LimpiarCadena(Cartucho).find(juego)!=-1:
			Saga.append(Cartucho)
	return Saga		#	Devuelve una lista de juegos cuyo titulo contiene la cadena

def wikiJuego(juego):	#	Recibe un título e imprime por pantalla cierta informacion
						#	del mismo.
	clear(0)
	Consola=guia.xpath('//game[description="%s"]/../header/listname/text()'%juego)
	Genero=guia.xpath('//game[description="%s"]/genre/text()'%juego)
	EdadRecomendada=guia.xpath('//game[description="%s"]/rating/text()'%juego)
	Descripcion=guia.xpath('//game[description="%s"]/story/text()'%juego)
	print('''		Consola:  %s
		Titulo:   %s
		Genero:   %s
		Edad Recomendada: %s
		'''%(Consola[0],juego,Genero[0],EdadRecomendada[0]))
	try:
		print("		Descripcion:	",Descripcion[0])	#	Si tiene una descripción lo imprime,
	except:												#	pero si no la tiene, imprime "???" 
		print("		Descripcion:	???")
	Pausa()

def LimpiarCadena(Cadena):	#	Esta función elimina algunos caracteres de una cadena. La uso sobre todo
							#	dentro de la función BuscadorDeJuegos(juego)
	CadenaLimpia=Cadena.upper().replace(".","").replace(" ","").replace("-","")
	return CadenaLimpia

def JuegosSobreLaMedia(Compañia,Media):		#Recibe una compañía y la calificación media de sus juegos.

	JuegosValorados=guia.xpath('//game[manufacturer="%s"][score>"%s"]/description/text()'%(Compañia,Media))
	return JuegosValorados		#	Devuelve una lista de los juegos por encima de su media

def CalificacionMedia(Compañia):	#	Recibe una compañía y calcula una media con todas las calificaciones
									#	que recibieron sus juegos.
	calificaciones=guia.xpath('//game[manufacturer="%s"]/score/text()'%Compañia)
	Total=0
	for num in calificaciones:
		Total=Total+float(num)
	try: 
		Media=round((Total)/len(calificaciones),2)
	except:
		if Compañia in EliminarRepetidos(guia.xpath('//game/manufacturer/text()')):
			Media=("	  Esta compañia no tiene juegos calificados")	
		else:
			Media=("	  Esa compañía no existe.")
	return Media	#	Devuelve la mencionada media.

def MenuCompañias():	#	Imprime por pantalla todas las compañías. Al mismo tiempo mete todos los nombres
						#	en un fichero para dar la opción de paginar dicha lista con less.
	ListaCompañias=EliminarRepetidos(guia.xpath('//game/manufacturer/text()'))

	for Compañia in ListaCompañias:
		print("		",Compañia)
		system('echo "		  {}" >> ListaCompañias &2> /dev/null'.format(Compañia))
	print()
	Decision=input("\n		  ¿Deseas paginarlo con less?		").upper()

	Afirmacion=['SI','YES','S','Y']		#	Conjunto de afirmaciones válidas para paginar.

	if Decision in Afirmacion:
		system('less ListaCompañias')	#	Si confirma por teclado, pagina la lista y justo después
	system('rm ListaCompañias')			#	borra el fichero.
	return ListaCompañias	#	Devuelve la lista de las compañías.

def clear(Espaciado):	#	Pequeña funcion que simula un clear, además recibe un entero para centrar
						#	el texto que lo sigue a continuación.
	system('clear')
	print("\n"*Espaciado)

def Pausa():

	input('\n		  "Pusa enter" para volver al menú...')

def JuegosPorAño(año):	#	Recibe un año concreto y devuelve una lista de los juegos lanzados dicho año

	listajuegos = guia.xpath('//game[year="%s"]/description/text()'%año)

	return listajuegos

def EliminarRepetidos(lista):	#	Recibe una lista y elimina los elementos repetidos.

	ListaSinRepetir = []
	for A in lista:
		if A not in ListaSinRepetir:
			ListaSinRepetir.append(A)
	return sorted(ListaSinRepetir)	#	Devuelve una lista de elementos únicos ordenada.

def JuegosPorEdad(Categoria):	#	Recibe un valor de edad recomendada y cuenta el número de juegos
								#	que está dentro de esa calificación.
	Total=guia.xpath('count(//game[rating="%s"])'%Categoria)
	
	return int(Total)	

def Generos(Compañia,Año):		#	Recibe una compañía y un año y devuelve una lista de los géneros
								#	de los juegos que lanzó durante ese año.
	ListaGeneros=EliminarRepetidos(guia.xpath('//game[manufacturer="%s"][year="%s"]/genre/text()'%(Compañia,Año)))

	return ListaGeneros

def AñosActividad(Compañia):	#	Muestra los años en los que la empresa lanzó juegos.

	Actividad=sorted(EliminarRepetidos(guia.xpath('//game[manufacturer="%s"]/year/text()'%Compañia)))
	if len(Actividad)>1:
		print("\n		",Compañia,"estuvo activa los siguientes años:")
		for año in Actividad:
			print("		   ",año)
	else:
		print("\n		",Compañia,"solo estuvo activa en",Actividad[0])
	return Actividad		#	Devuelve una lista de dicho(s) año(s)

########################################################################
#						   Código Principal							   #
########################################################################
	
guia = etree.parse('Ataris.xml')

while True:													############################
															#			Menú           #
	clear(0)												############################
	print('''\n\n	Elige una de las siguientes opciones:				

	1. Muestra los juegos desarrollados en un año concreto
	2. Contador de juegos por "Edad recomendada"
	3. Imprime por pantalla los juegos que superaron la media de su compañía
	4. Muestra en que género se enfocó una compañía un año concreto
	5. Listar una saga por el titulo de uno de los juegos
	0. Salir
		''')
	
	try:		#	Uso un try por si el usuario introduce un valor nulo o un caracter no entero. 

		opcion=int(input("\n		Opción:  "))

	except:		#	Error:

		print('\n		Debes introducir una opción válida')		
		Pausa()
	else:		#	Si introduce un entero ejecuta una de las siguientes opciones.

		if opcion==0:		#############
							#	Salir   #
			clear(0)		#############
			break

		elif opcion==1:

			año=int(input("\n\n	Introduce un año concreto: "))	#######################################
			if año<100:		  #	   Si introduce un año como		#	Muestra los juegos desarrollados  #
				año=año+1900  #    el 89, le suma 1900			#	en un año concreto				  #
			print()												#######################################						
			if len(JuegosPorAño(año))==0:
				print("		No se lanzaron juegos ese año.")
			for juego in JuegosPorAño(año):
				print("		",juego)

			Pausa()

		elif opcion==2:											#################################################
																#	Contador de juegos por "Edad recomendada"   #
			clear(6)											#################################################
			EdadesRecomendadas=EliminarRepetidos(guia.xpath('//rating/text()'))

			print("		    Selecciona una opcion:\n")
			Indice=1
			for Categoria in EdadesRecomendadas:				#	Muestra un menú indexado con las
				print("		    ",Indice,".",Categoria)			#	edades recomendadas
				Indice=Indice+1
			
			print("		    ",Indice,". Volver")
			seleccion=int(input("\n			  Opción: "))
			if seleccion<6:
				clear(10)
				print("		     [",EdadesRecomendadas[seleccion-1],"] -",JuegosPorEdad(EdadesRecomendadas[seleccion-1]))
				Pausa()									#	Usa la función del contador de EdadesRecomendadas
														#	a partir de la seleccion hecha.
		elif opcion==3:

			clear(6)										############################################
			Lista=MenuCompañias()							#	Imprime por pantalla los juegos que    #
			Compañia=input("		    Compañia:	")		#	superaron la media de su compañía      #
															############################################
			if Compañia in Lista:							
			#	Si la compañía introducida está en la lista:
				Media=CalificacionMedia(Compañia)
				Top=JuegosSobreLaMedia(Compañia,Media)
				for juego in Top:	#	Imprime la lista de juegos top
					print("		    ",juego)
			else:
			#	Si no, da un error
				print("		    ",Compañia,"no existe.")
			Pausa()

		elif opcion==4:
																	########################################
			clear(6)												#	Muestra en que género se enfocó    #
			Lista=MenuCompañias()									#	una compañía un año concreto	   #
			Compañia=input("		    Compañia:	")				#####################################.###
																	
			if Compañia in Lista:					#	Si la compañía introducida está en la lista:
				Activos=AñosActividad(Compañia)		#	Muestra una lista de sus años activos
				if len(Activos)>1:					#	Pide un año
					Año=int(input("		    Dime un año:	"))
					if Año<100:
						Año=Año+1900
				else:
					Año=Activos[0]
			ListaGeneros=Generos(Compañia,Año)
			print()
			for Genero in ListaGeneros:				#	E imprime una lista de los géneros
				print("		",Genero)				#	de los juegos lanzados dicho año
			Pausa()

		elif opcion==5:							##########################################################
			clear(9)							#	Listar una saga por el titulo de uno de los juegos   #
												##########################################################
			juego=LimpiarCadena(input('''			    Buscador de juegos
		  	    > '''))
			Saga=BuscadorDeJuegos(juego)
			if len(Saga)>1:						#	Si encuentra uno o varios juegos, muestra un menú con estos
				while True:
					clear(9-len(Saga)//3)
					Indice=1
					for Cartucho in Saga:
						print("	          ",Indice,".",Cartucho)
						Indice=Indice+1											############
					print("	           0 . Salir")								#	Menú   #
					try:														############
						Seleccion=int(input("\n	           Seleccion:	"))	
						if Seleccion==0:		#	Si introduce un 0, sale del menú
							break
						elif Seleccion-1<len(Saga):
							wikiJuego(Saga[Seleccion-1])
						else:
							print("			    Debes introducir una opcion del menú.")
							Pausa()
					except:
						print("			    Debes introducir una opcion del menú.")
						Pausa()
			else:								#	Si no encuentra nada muestra el error.
				print("	   No se han encontrado juegos con la palabra:",juego)
				Pausa()




'''
		Prototipo Opicion 5 Menú
			Lista=EliminarRepetidos(guia.xpath('//game[manufacturer="Atari, Inc."][score>"3.4"]/description/text()'))
			ListaMayus=[]
			for juego in Lista:
				ListaMayus.append(LimpiarCadena(juego))


			juego=input(''		    Buscador de juegos
			  	    > '')

			Igualador=0
			for Cartucho in ListaMayus:

				if Cartucho.find(LimpiarCadena(juego))!=-1:
					print(Lista[Igualador])

				Igualador=Igualador+1
'''