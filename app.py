# LEARN #
### ALGORITMO DE APRENDIZAJE INSTANTÁNEO ###

# El presente algoritmo trata de extraer o destilar una regla de una serie de datos numéricos que permitan predecir el resultado futuro. #

# Se compone de varias fases #
# Entrada de datos #
# fijación de objetivo #
# predicción de resulado #
# medición del error #
# corrección del error (pesos) #
# predicción en base a regla destilada #

# En la práctica esto es una NEURONA LINEAL que aprende a sumar dos números.
# La regla real es  obj = 1*ra + 1*rb , así que la meta del entrenamiento es
# que los pesos w1 y w2 se acerquen solos a 1.0 sin que se lo digamos nosotros.

import random


# --- ESTADO INICIAL Y PARÁMETROS ---

error = 0            # Diferencia entre lo correcto y lo predicho (conserva el signo).

w1: float = 0.0      # Peso de la 1ª entrada. Empieza "sin saber nada".
w2: float = 0.0      # Peso de la 2ª entrada. Debe converger hacia 1.0.

sesgo = 0            # Término independiente. Para la suma pura no hace falta (queda 0).

interaccion = 40     # Nº de ejemplos distintos que verá el modelo (vueltas del for).


# --- BUCLE DE ENTRENAMIENTO ---
# Cada vuelta del 'for' es un EJEMPLO nuevo: un par de números y su suma real.
for i in range(interaccion):

    # FASE 1 · Entrada de datos: dos números al azar entre 0 y 9.
    ra = random.randint(0,9)
    rb = random.randint(0,9)

    # FASE 2 · Fijación del objetivo: la suma verdadera, la "respuesta correcta".
    obj = ra + rb

    # Corregimos los pesos sobre ESTE ejemplo hasta que el modelo lo acierte.
    while True:

            # FASE 3 · Predicción: el intento del modelo con los pesos actuales.
            pre = w1*ra + w2*rb

            # FASE 4 · Medición del error: cuánto y hacia dónde se equivoca.
            #   error > 0  -> se quedó corto (habrá que subir pesos)
            #   error < 0  -> se pasó        (habrá que bajar pesos)
            error = obj - pre

            # ¿Acierta? Comparamos por REDONDEO, no por igualdad exacta: 'pre' es
            # un float (p. ej. 7.9999998) y casi nunca sería == a un entero.
            if (round(pre) == round(obj)):

                print(f" Interacción: {i} ¡ACIERTO! Objetivo: {obj} predicción: {pre}  error: {error} valor1: {ra} valor2: {rb} peso1: {w1} peso2: {w2} \n")

                break  # Ejemplo resuelto: salimos y pasamos al siguiente par.

            else:

                print(f" Interacción: {i} ¡ERROR! Objetivo: {obj} predicción: {pre}  error: {error} valor1: {ra} valor2: {rb} peso1: {w1} peso2: {w2} \n")

                # FASE 5 · Corrección de pesos (descenso de gradiente):
                #   nuevo_peso = peso + tasa * error * entrada
                # - El signo del error fija la dirección (subir/bajar) por sí solo.
                # - Multiplicar por la entrada corrige más el peso más influyente.
                # - 0.005 es la TASA DE APRENDIZAJE: paso pequeño para no "explotar".
                w1 += 0.005*error*ra
                w2 += 0.005*error*rb

# Al terminar, w1 y w2 quedan cerca de 1.0: el modelo ha "destilado" la regla de sumar.
