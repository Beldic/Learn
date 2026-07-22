# LEARN (versión POO) #
# Neurona lineal encapsulada en una clase.
#
# Es la misma idea que app.py, pero organizada con Programación Orientada a
# Objetos: el ESTADO (los pesos) y el COMPORTAMIENTO (entrenar / usar) viven
# juntos dentro de un objeto reutilizable.
#
#   - Algoritmo = el procedimiento de aprender (método entrenar).
#   - Modelo    = el resultado, los pesos ya ajustados (self.w1, self.w2).
#
# Se puede importar desde otros programas:  from learn import Learn

import random


class Learn:

    def __init__(self, w1, w2, sesgo, tasa):
        # El constructor define QUÉ ES la neurona al nacer.
        # Todo lo que va en 'self.' es su memoria: sobrevive entre métodos.
        self.w1 = w1        # Peso de la 1ª entrada (debe converger hacia 1.0).
        self.w2 = w2        # Peso de la 2ª entrada (debe converger hacia 1.0).
        self.sesgo = sesgo  # Término independiente (para la suma pura no se usa).
        self.tasa = tasa    # Tasa de aprendizaje: tamaño del paso de corrección.

    def entrenar(self, interaccion, minimo, maximo):
        # Ajusta los pesos a base de equivocarse y corregirse.
        # - interaccion: cuántos ejemplos distintos verá.
        # - minimo/maximo: rango de los números con los que practica.
        #   OJO: rangos grandes exigen una 'tasa' más pequeña (o explota).
        self.interaccion = interaccion
        self.min = minimo
        self.max = maximo

        error = 0  # Variable transitoria (no forma parte de la memoria del objeto).

        # --- BUCLE DE ENTRENAMIENTO ---
        # Cada vuelta del 'for' es un ejemplo nuevo (un par y su suma real).
        for i in range(interaccion):

            # FASE 1 · Entrada de datos: dos números al azar dentro del rango.
            ra = random.randint(minimo, maximo)
            rb = random.randint(minimo, maximo)

            # FASE 2 · Objetivo: la suma verdadera, la "respuesta correcta".
            obj = ra + rb

            # Corregimos sobre ESTE ejemplo hasta acertarlo.
            while True:

                # FASE 3 · Predicción con los pesos actuales del objeto.
                pre = self.w1*ra + self.w2*rb

                # FASE 4 · Error: cuánto y hacia dónde se equivoca (lleva el signo).
                error = obj - pre

                # ¿Acierta? Por REDONDEO, no por igualdad exacta (pre es un float).
                if (round(pre) == round(obj)):

                    print(f" Interacción: {i} ¡ACIERTO! Objetivo: {obj} predicción: {pre}  error: {error} valor1: {ra} valor2: {rb} peso1: {self.w1} peso2: {self.w2} \n")

                    break  # Ejemplo resuelto: pasamos al siguiente par.

                else:

                    print(f" Interacción: {i} ¡ERROR! Objetivo: {obj} predicción: {pre}  error: {error} valor1: {ra} valor2: {rb} peso1: {self.w1} peso2: {self.w2} \n")

                    # FASE 5 · Corrección de pesos (descenso de gradiente):
                    #   nuevo_peso = peso + tasa * error * entrada
                    # Modificamos self.w1/self.w2 para que el aprendizaje PERSISTA.
                    self.w1 += self.tasa*error*ra
                    self.w2 += self.tasa*error*rb

    def usar(self, a, b):
        # INFERENCIA: aplica la regla ya aprendida a dos números nuevos.
        # Sin bucle, sin error, sin corrección: una multiplicación y una suma.
        # Recibe a/b por parámetro (reutilizable) y devuelve el resultado.
        res = self.w1*a + self.w2*b
        return round(res)
