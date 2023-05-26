import numpy as np

# Definir el laberinto
laberinto = np.array([
    ['S', '0', '0', '0'],
    ['0', 'X', '0', '0'],
    ['0', 'X', '0', '0'],
    ['0', '0', '0', 'E']
])

# Definir las acciones posibles
acciones = ['arriba', 'abajo', 'izquierda', 'derecha']

# Definir los parámetros de Q-learning
tasa_aprendizaje = 0.1
factor_descuento = 0.9
tasa_exploracion = 0.1
num_episodios = 1000

# Obtener las dimensiones del laberinto
num_filas, num_columnas = laberinto.shape

# Crear la matriz Q inicializada con ceros
Q = np.zeros((num_filas, num_columnas, len(acciones)))


# Función auxiliar para obtener las acciones posibles en un estado dado
def obtener_acciones_posibles(estado):
    fila, columna = estado
    acciones_posibles = []
    if fila > 0 and laberinto[fila - 1, columna] != 'X':
        acciones_posibles.append('arriba')
    if fila < num_filas - 1 and laberinto[fila + 1, columna] != 'X':
        acciones_posibles.append('abajo')
    if columna > 0 and laberinto[fila, columna - 1] != 'X':
        acciones_posibles.append('izquierda')
    if columna < num_columnas - 1 and laberinto[fila, columna + 1] != 'X':
        acciones_posibles.append('derecha')
    return acciones_posibles


# Función auxiliar para seleccionar una acción en base a la función Q y la política de exploración
def seleccionar_accion(estado):
    if np.random.rand() < tasa_exploracion:
        # Acción aleatoria para la exploración
        return np.random.choice(acciones)
    else:
        # Acción basada en la función Q
        fila, columna = estado
        return acciones[np.argmax(Q[fila, columna])]


# Bucle principal de entrenamiento
for episodio in range(num_episodios):
    # Reiniciar el estado del agente al inicio del laberinto
    estado = (0, 0)
    terminado = False

    while not terminado:
        # Seleccionar una acción
        accion = seleccionar_accion(estado)

        # Tomar la acción y obtener el nuevo estado y la recompensa
        if accion == 'arriba':
            nuevo_estado = (estado[0] - 1, estado[1])
        elif accion == 'abajo':
            nuevo_estado = (estado[0] + 1, estado[1])
        elif accion == 'izquierda':
            nuevo_estado = (estado[0], estado[1] - 1)
        elif accion == 'derecha':
            nuevo_estado = (estado[0], estado[1] + 1)

        # Verificar si el nuevo estado está dentro de los límites del laberinto
        if nuevo_estado[0] < 0 or nuevo_estado[0] >= num_filas or nuevo_estado[1] < 0 or nuevo_estado[1] >= num_columnas:
            continue

        # Obtener la recompensa en el nuevo estado
        if laberinto[nuevo_estado] == 'E':
            recompensa = 10  # Recompensa por llegar a la casilla de salida
            terminado = True
        elif laberinto[nuevo_estado] == 'X':
            recompensa = -10  # Recompensa por caer en un agujero
            terminado = True
        else:
            recompensa = 0  # No hay recompensa en el resto de las casillas

        # Actualizar la función Q utilizando la fórmula de Q-learning
        q_actual = Q[estado + (acciones.index(accion),)]
        max_q_futuro = np.max(Q[nuevo_estado])
        q_nueva = (1 - tasa_aprendizaje) * q_actual + tasa_aprendizaje * (recompensa + factor_descuento * max_q_futuro)
        Q[estado + (acciones.index(accion),)] = q_nueva

        # Actualizar el estado actual
        estado = nuevo_estado

# Imprimir la matriz Q resultante con las acciones correspondientes
for i in range(len(acciones)):
    print("Matriz Q para la acción", acciones[i] + ":")
    print(Q[:, :, i])
    print()

# Obtener el camino óptimo desde el inicio a la salida
estado = (0, 0)
camino_optimo = [estado]
terminado = False

while not terminado:
    fila, columna = estado
    indice_accion = np.argmax(Q[fila, columna])
    accion = acciones[indice_accion]

    if accion == 'arriba':
        estado = (fila - 1, columna)
    elif accion == 'abajo':
        estado = (fila + 1, columna)
    elif accion == 'izquierda':
        estado = (fila, columna - 1)
    elif accion == 'derecha':
        estado = (fila, columna + 1)

    camino_optimo.append(estado)

    if laberinto[estado] == 'E':
        terminado = True

# Imprimir el camino óptimo
print("Camino óptimo:")
for estado in camino_optimo:
    print(estado)
