import numpy as np

# Datos de entrada y salida objetivo
x = np.array([
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 1, 1, 1, 0]
])


objetivo = np.array([1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0])

# Inicialización de pesos y umbral
np.random.seed()
pesos = [0.1] * 6
umbral = 0.5

# Parámetros de aprendizaje
tasa_aprendizaje = 0.1
epocas = 5

# Entrenamiento del perceptrón
for epoca in range(epocas):
    print("Época:", epoca+1)
    print("Pesos:", pesos)
    for i in range(x.shape[0]):
        # Cálculo de la salida del perceptrón multiplicando las matrices
        net = np.dot(x[i], pesos)
        # Si la preducción es mayor o igual que el umbral lo establecemos a 1
        y_pred = 1 if net >= umbral else 0

        # Actualización de pesos y umbral comprobando si coincide con lo esperado
        if y_pred != objetivo[i]:
            pesos += tasa_aprendizaje * (objetivo[i] - y_pred) * x[i]
            umbral += tasa_aprendizaje * (objetivo[i] - y_pred)

        print("Salida:", y_pred)

    print("--------------------")

print("Pesos finales:", pesos)
print("Umbral final:", umbral)
print("Como podemos apreciar, a partir de la época 3 el perceptrón ya ha aprendido y nos da la salida esperada")


