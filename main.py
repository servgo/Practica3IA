import pandas as pd
import math

data = {
    'Seta': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'PesaMucho': [0, 0, 1, 1, 0, 0, 0, 1],
    'EsMaloliente': [0, 0, 1, 0, 1, 0, 0, 1],
    'EsConManchas': [0, 1, 0, 0, 1, 1, 0, 0],
    'EsSuave': [0, 0, 1, 1, 0, 1, 1, 0],
    'EsVenenosa': [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

def entropia(columna):
    valores = columna.value_counts() #Cuantas repeticiones hay de los valores unicos
    num = len(columna)
    entr = 0
    for i in valores:
        p = i / num
        entr -= p * math.log2(p)
    return entr

def ganancia(columna, columnaReferencia): #Calcular la ganancia de cada columna en relacion a EsVenenosa
    valoresUnicos = columna.unique() #Definir los valores unicos que hay
    entropiaGlobal = entropia(columnaReferencia)
    entropiaColumna = 0
    for i in valoresUnicos: #Repetir con cada valor unico
        subconjVal = columnaReferencia[columna == i]
        entrSubconj = entropia(subconjVal)
        entropiaColumna += (len(subconjVal) / len(columna)) * entrSubconj
    g = entropiaGlobal - entropiaColumna
    return g

entropiaVenenosa = entropia(df['EsVenenosa'])
gananciaPesaMucho = ganancia(df['PesaMucho'], df['EsVenenosa'])
gananciaEsMaloliente = ganancia(df['EsMaloliente'], df['EsVenenosa'])
gananciaManchas = ganancia(df['EsConManchas'], df['EsVenenosa'])
gananciaSuave = ganancia(df['EsSuave'], df['EsVenenosa'])
print("Datos iniciales:")
print(df)


##Raiz
print("Primero vamos a elegir la raíz del árbol")
print("\tEntropía de EsVenenosa:", entropiaVenenosa)
print("\tGanancia de PesaMucho:", gananciaPesaMucho)
print("\tGanancia de EsMaloliente:", gananciaEsMaloliente)
print("\tGanancia de EsConManchas:", gananciaManchas)
print("\tGanancia de EsSuave:", gananciaSuave)
print("\tPor tanto la raíz del árbol será EsSuave")
print("Ahora hay 2 opciones, que sea suave o no, por lo que habrá que estudiar las dos posibilidades")

g = df.groupby(df.EsSuave) #Separamos por la columna EsSuave ya que es nuestra raiz
noSuave = g.get_group(0)
siSuave = g.get_group(1)
print("Datos agrupados por EsSuave:")
print(noSuave)
print(siSuave)
entropiaDfNoSuave = entropia(noSuave['EsVenenosa'])
entropiaDfSuave = entropia(siSuave['EsVenenosa'])


##NoSuave
print("Empezamos por noSuave y calculamos su entropia")
print("\tLa entropia de esVenenosa sabiendo que no es suave es:", entropiaDfNoSuave)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaPesaMuchoNS = ganancia(noSuave['PesaMucho'], noSuave['EsVenenosa'])
gananciaEsMalolienteNS = ganancia(noSuave['EsMaloliente'], noSuave['EsVenenosa'])
gananciaManchasNS = ganancia(noSuave['EsConManchas'], noSuave['EsVenenosa'])
print("\tGanancia de PesaMucho sabiendo que no es suave:", gananciaPesaMuchoNS)
print("\tGanancia de EsMaloliente sabiendo que no es suave:", gananciaEsMalolienteNS)
print("\tGanancia de EsConManchas sabiendo que no es suave:", gananciaManchasNS)
print("\tLa mayor ganancia es EsMaloliente asi que ese será el siguiente nodo de esta rama")


##EsSuave
print("Ahora realizamos el mismo procedimiento con siSuave")
print("\tLa entropia de esVenenosa sabiendo que si es suave es:", entropiaDfSuave)
print("\tAhora calculamos las ganancias del resto de columnas")
gananciaPesaMuchoSS = ganancia(siSuave['PesaMucho'], siSuave['EsVenenosa'])
gananciaEsMalolienteSS = ganancia(siSuave['EsMaloliente'], siSuave['EsVenenosa'])
gananciaManchasSS = ganancia(siSuave['EsConManchas'], siSuave['EsVenenosa'])
print("\tGanancia de PesaMucho sabiendo que si es suave:", gananciaPesaMuchoSS)
print("\tGanancia de EsMaloliente sabiendo que si es suave:", gananciaEsMalolienteSS)
print("\tGanancia de EsConManchas sabiendo que si es suave:", gananciaManchasSS)
print("\tLa mayor ganancia es EsMaloliente asi que ese será el siguiente nodo de esta rama")


##Arbol
print("Una vez realizados estos cálculos, podemos saber si una seta es venenosa o no,")
print("ya que con los datos proporcionados, las ramas creadas no generan discrepancia de si puede o no ser venenosa")
print("Por tanto, recogemos los datos y hemos generado un árbol para que sea más visual")
print("El árbol es la imagen arbolID3.png")


