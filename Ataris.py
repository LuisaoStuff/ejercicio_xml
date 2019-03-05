'''
ENUNCIADO

	Ejercicio 1

	Pide un año por teclado y muestra todos los juegos desarrollados en dicho año

	Ejercicio 2

	Muestra las edades recomendadas y pide una en concreto. A continuación cuenta el número de juegos
	con dicha edad recomendada.

	Ejercicio 3

	Pide una compañia por teclado, si existe pide un año y muestra los géneros sin repetir que lanzó
	dicho año. Si no existe muestra un error


	Ejercicio 4

	Pide una compañia por teclado, si existe muestra los años en los que desarrolló videojuegos y si 
	no existe muestra un error.

	Ejercicio 5

	
	Pide una cadena por teclado. Si hay un juego con ese nombre muestra todos los que tenga la saga
	en una lista. A continuación muestra un menú con dichos juegos donde si selecciona alguno muestre:
		-Título
		-Género
		-Edad Recomendada
		-Historia
'''

from lxml import etree
from os import system

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

	return ListaSinRepetir

def JuegosPorEdad(Categoria):

	Total=guia.xpath('count(//game[rating="%s"])'%Categoria)
	
	return int(Total)	


guia = etree.parse('Ataris.xml')

while True:

	clear(0)
	print('''\n\n	Elige una de las siguientes opciones:

		1. Muestra los juegos desarrollados en un año concreto
		2. Contador de juegos por "Edad recomendada"
		3. Géneros lanzados por cada compañia
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
			Contador=1
			for Categoria in EdadesRecomendadas:

				print("		    ",Contador,".",Categoria)
				Contador=Contador+1
			
			print("		    ",Contador,". Volver")
			seleccion=int(input("\n			  Opción: "))

			if seleccion<6:
				clear(10)
				print("		     [",EdadesRecomendadas[seleccion-1],"] -",JuegosPorEdad(EdadesRecomendadas[seleccion-1]))
				Pausa()

		elif opcion==3:

			clear(6)
			MenuCompañias()