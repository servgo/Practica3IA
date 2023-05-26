import numpy as np

# Datos de entrada y salida objetivo
x = np.array([
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0]
])


objetivo = np.array([1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0])

# Inicialización de pesos y umbral
pesos = [0.1] * 6
umbral = 0.1

# Parámetros de aprendizaje
tasa_aprendizaje = 0.1
epocas = 10

# Entrenamiento del perceptrón
for epoca in range(epocas):
    print("Época:", epoca+1)
    print("Pesos:", pesos)
    for i in range(x.shape[0]):
        # Cálculo de la salida del perceptron multiplicando las matrices
        net = np.dot(x[i], pesos) + umbral
        # Si la predicción es mayor que 0 dará 1 y en caso contrario 0
        if net > 0:
            y_pred = 1
        else:
            y_pred = 0

        # Actualización de pesos y umbral comprobando si coincide con lo esperado
        # Suma a todas las posiciones dejando igual las que estan a 0 (sumandole una multiplicacion por 0)
        if y_pred != objetivo[i]:
            pesos += tasa_aprendizaje * (objetivo[i] - y_pred) * x[i]
            umbral += tasa_aprendizaje * (objetivo[i] - y_pred)

        print("Salida:", y_pred)

    print("--------------------")

print("Pesos finales:", pesos)
print("Umbral final:", umbral)
print("Como podemos apreciar, a partir de la época 6 el perceptrón ya ha aprendido y nos da la salida esperada")