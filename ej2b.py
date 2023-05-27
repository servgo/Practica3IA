import pandas as pd
import math

data = {
    'X1': [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'X2': [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    'X3': [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    'X4': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    'X5': [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    'X6': [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    'T': [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)


def entropia(columna):
    valores = columna.value_counts()  # Cuantas repeticiones hay de los valores unicos
    num = len(columna)
    entr = 0
    for i in valores:
        p = i / num
        entr -= p * math.log2(p)
    return entr


def ganancia(columna, columnaReferencia):  # Calcular la ganancia de cada columna en relacion a la solución
    valoresUnicos = columna.unique()  # Definir los valores unicos que hay
    entropiaGlobal = entropia(columnaReferencia)
    entropiaColumna = 0
    for i in valoresUnicos:  # Repetir con cada valor unico
        subconjVal = columnaReferencia[columna == i]
        entrSubconj = entropia(subconjVal)
        entropiaColumna += (len(subconjVal) / len(columna)) * entrSubconj
    g = entropiaGlobal - entropiaColumna
    return g


entropiaT = entropia(df['T'])
gananciaX1 = ganancia(df['X1'], df['T'])
gananciaX2 = ganancia(df['X2'], df['T'])
gananciaX3 = ganancia(df['X3'], df['T'])
gananciaX4 = ganancia(df['X4'], df['T'])
gananciaX5 = ganancia(df['X5'], df['T'])
gananciaX6 = ganancia(df['X6'], df['T'])

print("Datos iniciales:")
print(df)

##Raiz
print("Primero vamos a elegir la raíz del árbol")
print("\tEntropía de T:", entropiaT)
print("\tGanancia de X1:", gananciaX1)
print("\tGanancia de X2:", gananciaX2)
print("\tGanancia de X3:", gananciaX3)
print("\tGanancia de X4:", gananciaX4)
print("\tGanancia de X5:", gananciaX5)
print("\tGanancia de X6:", gananciaX6)

print("\tPor tanto la raíz del árbol será X1")
print("Ahora hay 2 opciones, que sea 0 o 1, por lo que habrá que estudiar las dos posibilidades")

g = df.groupby(df.X1)  # Separamos por la columna X1 ya que es nuestra raiz
X1_0 = g.get_group(0)
X1_1 = g.get_group(1)
print("Datos agrupados por X1:")
print(X1_0)
print(X1_1)
entropiaDfX1_0 = entropia(X1_0['T'])
entropiaDfX1_1 = entropia(X1_1['T'])

##X1_0
print("Empezamos por X1_0 y calculamos su entropia")
print("\tLa entropia de T sabiendo que X es 0 es:", entropiaDfX1_0)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaX2_X1_0 = ganancia(X1_0['X2'], X1_0['T'])
gananciaX3_X1_0 = ganancia(X1_0['X3'], X1_0['T'])
gananciaX4_X1_0 = ganancia(X1_0['X4'], X1_0['T'])
gananciaX5_X1_0 = ganancia(X1_0['X5'], X1_0['T'])
gananciaX6_X1_0 = ganancia(X1_0['X6'], X1_0['T'])

print("\tGanancia de X2 sabiendo que X1 es 0:", gananciaX2_X1_0)
print("\tGanancia de X3 sabiendo que X1 es 0:", gananciaX3_X1_0)
print("\tGanancia de X4 sabiendo que X1 es 0:", gananciaX4_X1_0)
print("\tGanancia de X5 sabiendo que X1 es 0:", gananciaX5_X1_0)
print("\tGanancia de X6 sabiendo que X1 es 0:", gananciaX6_X1_0)

print("\tLa mayor ganancia es X3 y X5 asi que X3 será el siguiente nodo de esta rama")

##X1_1
print("Empezamos por X1_1 y calculamos su entropia")
print("\tLa entropia de T sabiendo que X es 1 es:", entropiaDfX1_1)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaX2_X1_1 = ganancia(X1_1['X2'], X1_1['T'])
gananciaX3_X1_1 = ganancia(X1_1['X3'], X1_1['T'])
gananciaX4_X1_1 = ganancia(X1_1['X4'], X1_1['T'])
gananciaX5_X1_1 = ganancia(X1_1['X5'], X1_1['T'])
gananciaX6_X1_1 = ganancia(X1_1['X6'], X1_1['T'])

print("\tGanancia de X2 sabiendo que X1 es 1:", gananciaX2_X1_1)
print("\tGanancia de X3 sabiendo que X1 es 1:", gananciaX3_X1_1)
print("\tGanancia de X4 sabiendo que X1 es 1:", gananciaX4_X1_1)
print("\tGanancia de X5 sabiendo que X1 es 1:", gananciaX5_X1_1)
print("\tGanancia de X6 sabiendo que X1 es 1:", gananciaX6_X1_1)

print("\tLa mayor ganancia es X3 asi que ese será el siguiente nodo de esta rama")

# X3_X1_0
g2 = X1_0.groupby(X1_0.X3)
X3_0_X1_0 = g2.get_group(0)
X3_1_X1_0 = g2.get_group(1)
print(X3_0_X1_0)
print(X3_1_X1_0)
entropiaDfX3_0_X1_0 = entropia(X3_0_X1_0['T'])
entropiaDfX3_1_X1_0 = entropia(X3_1_X1_0['T'])

# X3_0_X1_0
print(
    "En el caso de que X1 sea 0 y X3 sea 0, según los datos proporcionados T siempre es 0 por lo que se puede cerrar esta rama")

##X3_1_X1_0
print("Seguimos por X3_1_X1_0 y calculamos su entropia")
print("\tLa entropia de T sabiendo que X1 es 0 y X3 es igual a 1 es::", entropiaDfX3_1_X1_0)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaX2_X3_1_X1_0 = ganancia(X3_1_X1_0['X2'], X3_1_X1_0['T'])
gananciaX4_X3_1_X1_0 = ganancia(X3_1_X1_0['X4'], X3_1_X1_0['T'])
gananciaX5_X3_1_X1_0 = ganancia(X3_1_X1_0['X5'], X3_1_X1_0['T'])
gananciaX6_X3_1_X1_0 = ganancia(X3_1_X1_0['X6'], X3_1_X1_0['T'])

print("\tGanancia de X2 sabiendo que X1 es 0 y X3 es igual a 1 es:", gananciaX2_X3_1_X1_0)
print("\tGanancia de X4 sabiendo que X1 es 0 y X3 es igual a 1 es:", gananciaX4_X3_1_X1_0)
print("\tGanancia de X5 sabiendo que X1 es 0 y X3 es igual a 1 es:", gananciaX5_X3_1_X1_0)
print("\tGanancia de X6 sabiendo que X1 es 0 y X3 es igual a 1 es:", gananciaX6_X3_1_X1_0)
print("\tLa mayor ganancia es X4 y X5, elegimos X4 para seguir")

print("Ahora repetimos el proceso por la rama de X1 = 1, evaluando X3")

# X3_0_X1_0
g3 = X1_1.groupby(X1_1.X3)
X3_0_X1_1 = g3.get_group(0)
X3_1_X1_1 = g3.get_group(1)
print(X3_0_X1_1)
print(X3_1_X1_1)
entropiaDfX3_0_X1_1 = entropia(X3_0_X1_1['T'])
entropiaDfX3_1_X1_1 = entropia(X3_1_X1_1['T'])
print("Empezamos por X3_0_X1_1 y calculamos su entropia")
print("\tLa entropia de T sabiendo que X1 es 1 y X3 es igual a 0 es:", entropiaDfX3_0_X1_1)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaX2_X3_0_X1_1 = ganancia(X3_0_X1_1['X2'], X3_0_X1_1['T'])
gananciaX4_X3_0_X1_1 = ganancia(X3_0_X1_1['X4'], X3_0_X1_1['T'])
gananciaX5_X3_0_X1_1 = ganancia(X3_0_X1_1['X5'], X3_0_X1_1['T'])
gananciaX6_X3_0_X1_1 = ganancia(X3_0_X1_1['X6'], X3_0_X1_1['T'])

print("\tGanancia de X2 sabiendo que X1 es 1 y X3 es igual a 0 es:", gananciaX2_X3_0_X1_1)
print("\tGanancia de X4 sabiendo que X1 es 1 y X3 es igual a 0 es:", gananciaX4_X3_0_X1_1)
print("\tGanancia de X5 sabiendo que X1 es 1 y X3 es igual a 0 es:", gananciaX5_X3_0_X1_1)
print("\tGanancia de X6 sabiendo que X1 es 1 y X3 es igual a 0 es:", gananciaX6_X3_0_X1_1)
print("\tLa mayor ganancia es X6 por lo que esa será la siguiente rama del árbol")
print("\tViendo X6 en el contexto de X1 = 1 y X3 = 0, con los datos proporcionados,")
print("\tPodemos asegurar que si X6 es 0 T será 0 y si X6 es 1 T será 1")
print("Ahora seguimos evaluando por la unica rama que nos queda abierta, si X1 = 0, X3 = 1")
print("y evaluamos X4")

# X4_X3_1_X1_0
g4 = X3_1_X1_0.groupby(X3_1_X1_0.X4)
X4_0_X3_1_X1_0 = g4.get_group(0)
X4_1_X3_1_X1_0 = g4.get_group(1)
print(X4_0_X3_1_X1_0)
print(X4_1_X3_1_X1_0)

# X4_0_X3_1_X1_0
print("\tViendo los datos, si X1 = 0, X3 = 1, si X4 = 0 siempre T es 0, por lo que no hace falta evaluar esa rama")
print("\tPor tanto, evaluaremos solo el caso de que X4 sea 1")

# X4_1_X3_1_X1_0
entropiaDfX4_1X3_1_X1_0 = entropia(X4_1_X3_1_X1_0['T'])
print("\tLa entropia de T sabiendo que X1 es 0 y X3 es igual a 1 y que X4 es 1 es:", entropiaDfX4_1X3_1_X1_0)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaX2_X4_1_X3_1_X1_0 = ganancia(X4_1_X3_1_X1_0['X2'], X4_1_X3_1_X1_0['T'])
gananciaX5_X4_1_X3_1_X1_0 = ganancia(X4_1_X3_1_X1_0['X5'], X4_1_X3_1_X1_0['T'])
gananciaX6_X4_1_X3_1_X1_0 = ganancia(X4_1_X3_1_X1_0['X6'], X4_1_X3_1_X1_0['T'])

print("\tGanancia de X2 sabiendo que X1 es 0 y X3 es igual a 1 y X4 es 1 es:", gananciaX2_X4_1_X3_1_X1_0)
print("\tGanancia de X5 sabiendo que X1 es 0 y X3 es igual a 1 y X4 es 1 es:", gananciaX5_X4_1_X3_1_X1_0)
print("\tGanancia de X6 sabiendo que X1 es 0 y X3 es igual a 1 y X4 es 1 es:", gananciaX6_X4_1_X3_1_X1_0)
print("\tLa ganancia mayor es X6, por lo que elegimos esa rama")
print("\tViendo los datos, si X6 en este contexto es 1 T es 1 y viceversa")
print("Por tanto, ya tendríamos el árbol completo")

##Arbol
print("Por tanto, recogemos los datos y hemos generado un árbol para que sea más visual")
print("El árbol es la imagen arbolID3_2b.png")
