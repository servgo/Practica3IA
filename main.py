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
    entropia = 0
    for count in valores:
        p = count / num
        entropia -= p * math.log2(p)
    return entropia

entropiaVenenosa = entropia(df['EsVenenosa'])
entropiaPesaMucho = entropia(df['PesaMucho'])
entropiaEsMaloliente = entropia(df['EsMaloliente'])
entropiaManchas = entropia(df['EsConManchas'])
entropiaSuave = entropia(df['EsSuave'])
print("Entropía de EsVenenosa:", entropiaVenenosa)
print("Entropía de PesaMucho:", entropiaPesaMucho)
print("Entropía de EsMaloliente:", entropiaEsMaloliente)
print("Entropía de EsConManchas:", entropiaManchas)
print("Entropía de EsSuave:", entropiaSuave)
gananciaPesa = entropiaVenenosa - entropiaPesaMucho
gananciaMaloliente = entropiaVenenosa - entropiaEsMaloliente
gananciaManchas = entropiaVenenosa - entropiaManchas
gananciaSuave = entropiaVenenosa - entropiaSuave
print("Ganancia de PesaMucho:", gananciaPesa)
print("Ganancaia de EsMaloliente:", gananciaMaloliente)
print("Ganancia de EsConManchas:", gananciaManchas)
print("Ganancia de EsSuave:", gananciaSuave)