'''
ENUNCIADO

	Ejercicio 1

	Lista los titulos de los juegos desarrollados en los años 80

	Ejercicio 2

	Cuenta el número de juegos recomendados para mayores de 17 años o adultos

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

def JuegosPorAño(año):

	listajuegos = guia.xpath('//game[year="%s"]/description/text()'%año)

	return listajuegos

guia = etree.parse('Ataris.xml')

while True:

	system('clear')
	print('''\n\n	Elige una de las siguientes opciones:

		1. Muestra los juegos desarrollados en un año concreto
		0. Salir
		''')

	opcion=(int(input("\n		Opción:  ")))

	try:

		if opcion==0:

			system('clear')
			break

		elif opcion==1:

			año=int(input("\n\n	Introduce un año concreto: "))
			print()

			for juego in JuegosPorAño(año):
				print("		",juego)

			input('\n		"Pusa enter" para volver al menú...')

		elif opcion==2:


			
#		elif opcion==2:


	except:

		print("\n		",opcion,"no es un entero del menú.")