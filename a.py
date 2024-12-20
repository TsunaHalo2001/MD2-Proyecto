#Metodo generar al que se le ingresa una cadena y si contiene un valor no terminal, se reemplaza por una produccion de la gramatica
def generar(cadena, S, P):
	# Si la cadena es vac?a, se retorna una lista con la cadena vac?a
	if not cadena:
		return S == ''
	# Si la cadena contiene un valor no terminal
	# Se inicializa una lista vac?a
	cadenas = []
	# Se recorren las producciones con estructura [[A, B, C], [D, E]]
	# Donde A, D son los no terminales y B, C, E son las producciones
	for i in range(len(P)):
		# Se obtiene el no terminal
		no_terminal = P[i][0]
		# Se obtienen las producciones
		producciones = P[i][1:]
		# Si el no terminal est? en la cadena
		if no_terminal in cadena:
			# Se recorren las producciones
			for produccion in producciones:
				# Se reemplaza el no terminal por la producci?n
				nueva_cadena = cadena.replace(no_terminal, produccion, 1)
				# Se agrega la nueva cadena a la lista
				cadenas.append(nueva_cadena)

	return cadenas

#Metodo para generar caenas de la gramatica hasta un numero de iteraciones
#Se le ingresa las iteraciones, los simbolos no terminales, los simbolos terminales, el simbolo inicial y las producciones
#Se retorna la lista por ejemplo:
#n = 1
#['aSb', 'ab']
#n = 2
#['aaSbb', 'aabb', 'ab']
def generar_vocabulario(V, T, S, P, n):
	# Se ingresa el simbolo inicial a la lista
	cadenas = [S]

	# Se recorren las iteraciones
	for i in range(n):
		# Se recorren las cadenas en el arreglo a retornar
		for cadena in cadenas:
			for i in range(len(P)):
				if P[i][0] in cadena:
					cadenas.remove(cadena)
			cadenas_generadas = generar(cadena, S, P)
		# Se actualiza la lista de cadenas
		cadenas += cadenas_generadas

	return cadenas
	
# Ejemplo de uso
V = {'S', 'a', 'b'}
T = {'a', 'b'}
S = 'S'
P = [['S', 'aSb', 'ab']]

cadena = "aabb"
cadenas = generar_vocabulario(V, T, S, P, 4)
print(cadenas)

