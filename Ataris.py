'''
ENUNCIADO

	Ejercicio 1

	Pide un año por teclado y muestra todos los juegos desarrollados en dicho año

	Ejercicio 2

	Muestra las edades recomendadas y pide una en concreto. A continuación cuenta el número de juegos
	con dicha edad recomendada.

	Ejercicio 3

	Pide una compañia por teclado tras imprimir una lista de estas. Imprime solo los juegos que tuvieron
	una calificación por encima de su media. 

	Ejercicio 4

	Muestra una lista de todas las compañias por pantalla. Pide una y enseña los años en los que estuvo
	activa. A continuación pide uno de esos años e imprime los géneros en los que se enfocó dicho año.

	Ejercicio 5

	
	Pide una cadena por teclado. Si hay un juego con ese nombre muestra todos los que tenga que ver
	en una lista. A continuación muestra un menú con dichos juegos donde si selecciona alguno muestre
	un menú con todos los títulos y que te permita seleccionar cada uno e imprimir:
		-Consola
		-Título
		-Género
		-Edad Recomendada
		-Descripcion
	Hasta que pulses la última opción
'''

########################################################################
#						      Librerías							       #
########################################################################

from lxml import etree
from os import system


########################################################################
#						      Funciones							       #
########################################################################

def BuscadorDeJuegos(juego):

	ListaCompleta = EliminarRepetidos(guia.xpath('//game/description/text()'))
	Saga = []

	for Cartucho in ListaCompleta:

		if LimpiarCadena(Cartucho).find(juego)!=-1:
			Saga.append(Cartucho)
	return Saga

def wikiJuego(juego):

	clear(0)
	Consola=guia.xpath('//game[description="%s"]/../header/listname/text()'%juego)
	Genero=guia.xpath('//game[description="%s"]/genre/text()'%juego)
	EdadRecomendada=guia.xpath('//game[description="%s"]/rating/text()'%juego)
	Descripcion=guia.xpath('//game[description="%s"]/story/text()'%juego)
		
	#wiki={"Consola":Consola,"Titulo":juego,"Genero":Genero,"Edad Recomendada":EdadRecomendada,"Historia":Historia}
	#print(wiki)
	
	print('''		Consola:  %s
		Titulo:   %s
		Genero:   %s
		Edad Recomendada: %s
		'''%(Consola[0],juego,Genero[0],EdadRecomendada[0]))
	try:
		print("		Descripcion:	",Descripcion[0])
	except:
		print("		Descripcion:	???")
	Pausa()

def LimpiarCadena(Cadena):

	CadenaLimpia=Cadena.upper().replace(".","").replace(" ","").replace("-","")
	return CadenaLimpia

def JuegosSobreLaMedia(Compañia,Media):

	JuegosValorados=guia.xpath('//game[manufacturer="%s"][score>"%s"]/description/text()'%(Compañia,Media))

	return JuegosValorados

def CalificacionMedia(Compañia):

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
	return Media

def MenuCompañias():

	ListaCompañias=EliminarRepetidos(guia.xpath('//game/manufacturer/text()'))

	for Compañia in ListaCompañias:

		print("		",Compañia)
		system('echo "		  {}" >> ListaCompañias &2> /dev/null'.format(Compañia))

	print()
	Decision=input("\n		  ¿Deseas paginarlo con less?		").upper()

	Afirmacion=['SI','YES','S','Y']

	if Decision in Afirmacion:
		system('less ListaCompañias')
	system('rm ListaCompañias')

	return ListaCompañias

def clear(Espaciado):

	system('clear')
	print("\n"*Espaciado)

def Pausa():

	input('\n		  "Pusa enter" para volver al menú...')

def JuegosPorAño(año):

	listajuegos = guia.xpath('//game[year="%s"]/description/text()'%año)

	return listajuegos

def EliminarRepetidos(lista):

	ListaSinRepetir = []

	for A in lista:
		if A not in ListaSinRepetir:
			ListaSinRepetir.append(A)

	return sorted(ListaSinRepetir)

def JuegosPorEdad(Categoria):

	Total=guia.xpath('count(//game[rating="%s"])'%Categoria)
	
	return int(Total)	

def Generos(Compañia,Año):

	ListaGeneros=EliminarRepetidos(guia.xpath('//game[manufacturer="%s"][year="%s"]/genre/text()'%(Compañia,Año)))

	return ListaGeneros

def AñosActividad(Compañia):

	Actividad=sorted(EliminarRepetidos(guia.xpath('//game[manufacturer="%s"]/year/text()'%Compañia)))
	if len(Actividad)>1:
		print("\n		",Compañia,"estuvo activa desde",Actividad[0],"hasta",Actividad[len(Actividad)-1])
	else:
		print("\n		",Compañia,"solo estuvo activa en",Actividad[0])

	return Actividad

########################################################################
#						   Código Principal							   #
########################################################################
	
guia = etree.parse('Ataris.xml')

while True:

	clear(0)
	print('''\n\n	Elige una de las siguientes opciones:

	1. Muestra los juegos desarrollados en un año concreto
	2. Contador de juegos por "Edad recomendada"
	3. Imprime por pantalla los juegos que superaron la media de su compañía
	4. Muestra en que género se enfocó una compañía un año concreto
	5. Listar una saga por el titulo de uno de los juegos
	0. Salir
		''')
	
	try:

		opcion=(int(input("\n		Opción:  ")))

	except:

		print('\n		Debes introducir una opción válida')		
		Pausa()
	else:

		if opcion==0:

			clear(0)
			break

		elif opcion==1:

			año=int(input("\n\n	Introduce un año concreto: "))
			print()

			if len(JuegosPorAño(año))==0:
				print("		No se lanzaron juegos ese año.")

			for juego in JuegosPorAño(año):
				print("		",juego)

			Pausa()

		elif opcion==2:
			
			clear(6)
			EdadesRecomendadas=EliminarRepetidos(guia.xpath('//rating/text()'))

			print("		    Selecciona una opcion:\n")
			Indice=1
			for Categoria in EdadesRecomendadas:

				print("		    ",Indice,".",Categoria)
				Indice=Indice+1
			
			print("		    ",Indice,". Volver")
			seleccion=int(input("\n			  Opción: "))

			if seleccion<6:
				clear(10)
				print("		     [",EdadesRecomendadas[seleccion-1],"] -",JuegosPorEdad(EdadesRecomendadas[seleccion-1]))
				Pausa()

		elif opcion==3:

			clear(6)
			Lista=MenuCompañias()
			Compañia=input("		    Compañia:	")
			
			if Compañia in Lista:

				Media=CalificacionMedia(Compañia)
				Top=JuegosSobreLaMedia(Compañia,Media)
				for juego in Top:
					print("		    ",juego)
			else:

				print("		    ",Compañia,"no existe.")

			Pausa()

		elif opcion==4:

			clear(6)
			Lista=MenuCompañias()
			Compañia=input("		    Compañia:	")

			if Compañia in Lista:
				Activos=AñosActividad(Compañia)
				if len(Activos)>1:
					Año=int(input("		    Dime un año:	"))
					if Año<100:
						Año=Año+1900
				else:
					Año=Activos[0]
			ListaGeneros=Generos(Compañia,Año)
			print()
			for Genero in ListaGeneros:
				print("		",Genero)
			Pausa()

		elif opcion==5:
			clear(9)
			juego=LimpiarCadena(input('''			    Buscador de juegos
		  	    > '''))
			Saga=BuscadorDeJuegos(juego)
			if len(Saga)>1:

				while True:
					clear(9-len(Saga)//3)
					Indice=1
					for Cartucho in Saga:
						print("	          ",Indice,".",Cartucho)
						Indice=Indice+1
					print("	           0 . Salir")
					try:		
						Seleccion=int(input("\n	           Seleccion:	"))	
						if Seleccion==0:
							break
						elif Seleccion-1<len(Saga):
							wikiJuego(Saga[Seleccion-1])
						else:
							print("			    Debes introducir una opcion del menú.")
							Pausa()
					except:
						print("			    Debes introducir una opcion del menú.")
						Pausa()
			else:
				print("	   No se han encontrado juegos con la palabra:",juego)
				Pausa()


'''

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