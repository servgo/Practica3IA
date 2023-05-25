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
    valores = columna.value_counts()
    num = len(columna)
    entr = 0
    for count in valores:
        p = count / num
        entr -= p * math.log2(p)
    return entr

def ganancia(column, target_column):
    unique_values = column.unique()
    total_entropy = entropia(target_column)
    weighted_entropy = 0
    for value in unique_values:
        subset = target_column[column == value]
        subset_entropy = entropia(subset)
        weighted_entropy += (len(subset) / len(column)) * subset_entropy
    gain = total_entropy - weighted_entropy
    return gain

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
