'''
ENUNCIADO

	Ejercicio 1

	Lista los titulos de los juegos desarrollados en los años 80

	Ejercicio 2

	Cuenta el número de juegos recomendados para mayores de 17 años o adultos

	Ejercicio 3

	Filtra los juegos desarrollados por Atari Ink

	Ejercicio 4

	Pide una compañia por teclado, si existe muestra los años en los que desarrolló videojuegos y si no existe muestra un error.

	Ejercicio 5

	Pide una cadena por teclado. Si hay un juego con ese nombre muestra todos los que tenga la saga (los títulos, edad recomendada e historia si tiene)
'''

from lxml import etree

def JuegosPorAño()

guia = etree.parse('Ataris.xml')

while True:

	print('''\n\n	Elige una de las siguientes opciones:

					1. Muestra los juegos desarrollados en un año concreto
					0. Salir
		''')

	opcion=(int(input("\n		Opción:  ")))

	try:

		if opcion==1:

			año=int(input())

	except:
		print("\n		",opcion,"no es un entero del menú.")