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
entropiaPesaMucho = ganancia(df['PesaMucho'], df['EsVenenosa'])
entropiaEsMaloliente = ganancia(df['EsMaloliente'], df['EsVenenosa'])
entropiaManchas = ganancia(df['EsConManchas'], df['EsVenenosa'])
entropiaSuave = ganancia(df['EsSuave'], df['EsVenenosa'])

print("Entropía de EsVenenosa:", entropiaVenenosa)
print("Ganancia de PesaMucho:", entropiaPesaMucho)
print("Ganancia de EsMaloliente:", entropiaEsMaloliente)
print("Ganancia de EsConManchas:", entropiaManchas)
print("Ganancia de EsSuave:", entropiaSuave)
