#Issac Gonzalez 4 de Abril de 2022
#Primera versión completada
import random
import numpy as np

#Definir aleatoriedad de posibles casos
def nuevaSolucionAleatoria():
	tablero=[]
	while (len(tablero)<8):
		propuesta=random.randint(0, 7)
		if (propuesta not in tablero):
			tablero.append(propuesta)
	#print(tablero)
	print('-------')
	return tablero

#Generación de la iteración de vecinos o soluciones
def solvec(vec, tabu):
	sol = []
	for i in range (0,8):
		for j in range (i+1,8):
			repeticion = 0
			st=[]
			st.extend(vec[:i]) 
			st.append(vec[j])
			st.extend(vec[i+1:j]) 
			st.append(vec[i])
			st.extend(vec[j+1:])
			for elemento in tabu:
				if st == elemento['vec']:
					repeticion = 1
			if (repeticion==0):
				na = ataques(st)
				tabusol = {'vec':st, 'ataque':na}
				sol.append(tabusol) #Solo agrega a sol la solucion tabu
	return sol

#Mapeo de posiciones en el tablero
#Las posiciones del arreglo son las columnas
#Los valores dentro del arreglo son las filas
def matriz(vec):
	m = np.zeros((8,8)) #Crear tablero de 0's
	c=0
	for i in vec:#Para cada columna
		m[i][c]=1
		c+=1
	#print(m)
	return m

#Debemos de evaluar cuantos ataques diagonales tiene cada reina
def ataques (vec):
	n = 0 #Num total de ataques
	m = matriz(vec)#convertir el vector en matriz
	print(m)
	c = 0 #columna
	for i in vec: #Recorrer cada elemento de cada vector
		nr = 0 #Numero de reinas
		#Fila, columna, matriz
		nr+= ADSI(i,c,m) 
		nr+= ADII(i,c,m) 
		nr+= ADSD(i,c,m)
		nr+= ADID(i,c,m)
		n+=nr
		c+=1
	return n

def ADSI(i,c,m): #Ataque superior izquierda
	while(c!=0)&(i!=0):
		c-=1
		i-=1
		if m[i][c]==1:
			return 1
	return 0

def ADII(i,c,m): #Inferior izquierda
	while(c!=0) & (i!=7):
		c-=1
		i+=1
		if m[i][c]==1:
			return 1
	return 0

def ADSD(i,c,m): #Superior Derecha
	while(c!=7) & (i!=0):
		c+=1
		i-=1
		if m[i][c]==1:
			return 1
	return 0

def ADID(i,c,m): #Inferior derecha
	while(c!=7) & (i!=7):
		c+=1
		i+=1
		if m[i][c]==1:
			return 1
	return 0

def ms(vec, solsec):#Mejor solucion
	ms = solsec
	for i in vec:
		if i['ataque']<ms['ataque']:
			ms=i
	return ms

#Main----------
sol = nuevaSolucionAleatoria() #Generacion de una solucion aleatoria
nasolsec = ataques(sol) #Obtener el (N)umero de (A)taques de la (SOL)ucion (SE)le(C)cionada
b = 0 #0 es que no se ha encontrado la solucion o existe un mejor vecino (TERMINO DE PROGRAMA)
tabu = []
solsec={'vec':sol,'ataque':nasolsec} #Diccionario vecino, numero de ataques
c=1 #Contador de num de solución
while b == 0:
	vec = solvec(solsec['vec'], tabu) #Vecino = solucion vecina (solucion seleccionada[Diccionario vecino de solucion aleatoria])
	msv = ms(vec,solsec) #Mejor solucion vecina
	print('------------')
	if(solsec['ataque']>msv['ataque']):
		solsec = msv#Solucion seleccionada
		print(c) 
		c+=1
		print(solsec['ataque'])
	else:
		b = 1
print(solsec['vec'])
print(solsec['ataque'])
print(matriz(solsec['vec']))