import numpy as np

# Datos de entrada y salida objetivo
X = np.array([
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

X

t = np.array([1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0])

# Inicialización de pesos y umbral
np.random.seed()
weights = np.random.rand(X.shape[1])
threshold = np.random.rand()

# Parámetros de aprendizaje
learning_rate = 0.1
epochs = 10

# Entrenamiento del perceptrón
for epoch in range(epochs):
    print("Época:", epoch+1)
    print("Pesos:", weights)
    for i in range(X.shape[0]):
        # Cálculo de la salida del perceptrón multiplicando las matrices
        net = np.dot(X[i], weights)
        # Si la preducción es mayor o igual que el umbral lo establecemos a 1
        y_pred = 1 if net >= threshold else 0

        # Actualización de pesos y umbral comprobando si coincide con lo esperado
        if y_pred != t[i]:
            weights += learning_rate * (t[i] - y_pred) * X[i]
            threshold += learning_rate * (t[i] - y_pred)

        print("Salida:", y_pred)

    print("--------------------")

print("Pesos finales:", weights)
print("Umbral final:", threshold)
