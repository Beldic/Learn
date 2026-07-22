# 🧠 LEARN — Algoritmo de Aprendizaje Instantáneo

Un programa mínimo en Python que **aprende a sumar dos números él solo**, sin que
nadie le diga que la regla es "sumar". Es la versión más pequeña posible de una red
neuronal: **una sola neurona lineal** entrenada con **descenso de gradiente**.

---

## 🎯 ¿Qué hace?

Sumar dos números es una relación lineal:

```
resultado = w1 · a + w2 · b
```

Si el programa "aprende a sumar", debe **descubrir por sí mismo** que los pesos
correctos son `w1 = 1` y `w2 = 1`. No se lo decimos: lo encuentra a base de
**equivocarse y corregirse** muchas veces.

Al arrancar, los pesos valen `0.0`, así que el modelo es un ignorante y falla.
Con cada fallo ajusta los pesos un poquito, y poco a poco se acercan a `1.0`.
Cuando lo consigue, puede sumar pares de números que **nunca había visto**.

---

## ⚙️ Cómo funciona: el ciclo de aprendizaje

El corazón del programa es un ciclo de 5 fases que se repite una y otra vez:

| Fase | Qué hace | En el código |
|------|----------|--------------|
| **1. Entrada de datos** | Genera dos números al azar (0–9) | `ra`, `rb` |
| **2. Fijación del objetivo** | Calcula la suma verdadera | `obj = ra + rb` |
| **3. Predicción** | El modelo intenta adivinar con sus pesos | `pre = w1*ra + w2*rb` |
| **4. Medición del error** | Compara lo predicho con lo correcto | `error = obj - pre` |
| **5. Corrección de pesos** | Ajusta los pesos para fallar menos | `w1 += tasa*error*ra` |

### La regla de corrección (lo más importante)

```
nuevo_peso = peso + tasa · error · entrada
```

Esta fórmula es toda la "magia", y hace tres cosas a la vez, sin un solo `if`:

- **Dirección** → el `error` ya es positivo si el modelo se quedó corto y negativo
  si se pasó. Sumarlo corrige en el sentido correcto automáticamente.
- **Magnitud** → error grande = corrección grande; error casi cero = corrección
  casi nula. El modelo *frena suavemente* al acercarse a la respuesta.
- **Reparto justo** → multiplicar por la entrada hace que el peso más influyente
  se corrija más.

---

## 🔑 Dos conceptos clave

### La tasa de aprendizaje (`0.005`)
Es el tamaño del "paso" con el que se corrigen los pesos.

- **Demasiado grande** → el modelo se pasa una y otra vez y los pesos **explotan**
  hacia el infinito. (Con `0.1` este programa no converge.)
- **Demasiado pequeña** → aprende, pero muy despacio.

### Comparar por redondeo, no por igualdad exacta
La predicción es un número decimal (p. ej. `7.9999998`), así que **casi nunca**
será *exactamente* igual a un entero. Por eso el acierto se decide con:

```python
if round(pre) == round(obj):
```

Esto da un margen de tolerancia (±0.5) que:
- ✅ evita bucles infinitos esperando una igualdad imposible,
- ⚠️ pero hace que los pesos se queden en "suficientemente bueno"
  (~`0.9` / ~`1.1`) en vez de `1.0` exacto. Es el clásico intercambio
  **tolerancia ↔ precisión**.

---

## ▶️ Cómo ejecutarlo

```bash
python3 app.py
```

Verás una traza por pantalla. Al principio abundan los `¡ERROR!`; a medida que
aprende, empiezan a aparecer `¡ACIERTO!` a la primera:

```
 Interacción: 0 ¡ERROR!   Objetivo: 8  predicción: 0.0    ...  peso1: 0.0   peso2: 0.0
 ...
 Interacción: 0 ¡ACIERTO! Objetivo: 8  predicción: 7.56   ...  peso1: 0.37  peso2: 1.13
 ...
 Interacción: 39 ¡ACIERTO! Objetivo: 5 predicción: 5.23   ...  peso1: 0.91  peso2: 1.09
```

Cuando el modelo acierta ejemplos nuevos **sin corregir nada**, es la prueba de
que ha **generalizado la regla** en lugar de memorizar casos concretos.

---

## 🎓 Usar el modelo entrenado: preguntas frecuentes

Tres preguntas clave que tocan la diferencia entre *aprender* y *saber*.

### 1. ¿Cómo usamos el algoritmo ya entrenado?

Una vez entrenado, **todo el "conocimiento" del programa cabe en dos números:
`w1` y `w2`**. Nada más. Por eso entrenar y usar son **dos momentos distintos**:

- **Entrenar** (el bucle con predicción + error + corrección) es caro y lento, y
  solo se hace **una vez**.
- **Usar** es coger esos pesos ya ajustados y hacer **solo la predicción**, para
  números nuevos, **sin bucle, sin error, sin corrección**:

  ```
  resultado = w1 * a + w2 * b
  ```

A ese momento se le llama **inferencia**: el modelo ya no aprende, solo *aplica*
lo aprendido. Fíjate en la asimetría: entrenar requiere miles de vueltas; usar es
**una sola multiplicación y una suma**. Instantáneo.

### 2. ¿Por qué se le llama "modelo"?

Porque un **modelo** es una **representación simplificada de la realidad**. Igual
que una maqueta de un edificio no es el edificio, pero captura su forma esencial.

El programa **no guarda** ninguna tabla de sumas ni memoriza ejemplos: captura la
*esencia* de la operación en unos pocos parámetros. **Los pesos SON el modelo.**

Vocabulario que conviene fijar:
- **Algoritmo** = el *procedimiento* de aprendizaje (predecir → medir → corregir).
- **Modelo** = el *resultado* de ese procedimiento (los pesos ya ajustados).

El algoritmo es la *fábrica*; el modelo es el *producto* que sale de ella.

### 3. ¿Qué peculiaridades tiene?

- **El conocimiento es minúsculo.** Todo lo aprendido son 2 números. Puedes tirar
  los datos de entrenamiento y quedarte solo con `w1` y `w2`: el modelo sigue
  sabiendo sumar. (Los modelos grandes hacen lo mismo, pero con miles de millones
  de pesos.)
- **No es exacto, es aproximado.** Quedó en `w1≈0.9`, `w2≈1.1`, no en `1.0`
  clavado. No "sabe" sumar de verdad: tiene una *aproximación* lo bastante buena en
  su rango.
- **Generaliza… pero solo en su dominio.** Aprendió con números del 0 al 9 y
  acierta pares nuevos de ese rango. Pero **extrapola mal fuera**: con `w1=0.9`,
  `w2=1.1`, pedirle `1000 + 0` da `900` (¡debería ser `1000`!). Un modelo solo es
  fiable **dentro del rango en que fue entrenado**.
- **Es determinista al usarlo.** Fijados los pesos, la misma entrada da siempre la
  misma salida. La aleatoriedad estaba solo en el *entrenamiento*.
- **No recuerda los ejemplos, solo la regla.** No queda rastro de los 40 pares que
  vio: los "destiló" en la regla y los olvidó.

| | Entrenar (algoritmo) | Usar (modelo) |
|---|---|---|
| Qué hace | ajusta pesos con sus errores | aplica `w1·a + w2·b` |
| Coste | miles de vueltas | 1 operación |
| Cuándo | una vez | siempre que quieras |
| Necesita el error | sí | no |

---

## 🧱 Versión POO: la clase `Learn` (`POO/learn.py`)

La misma neurona, pero reorganizada con **Programación Orientada a Objetos**. En
vez de variables sueltas y globales, ahora el **estado** (los pesos) y el
**comportamiento** (entrenar / usar) viven juntos dentro de un objeto reutilizable
que se puede **importar desde otros programas**.

### La clase de un vistazo

| Miembro | Rol | Qué hace |
|---------|-----|----------|
| `__init__(w1, w2, sesgo, tasa)` | **constructor** | Define la neurona: inicializa los pesos y la tasa de aprendizaje en `self.` (su memoria). |
| `entrenar(interaccion, minimo, maximo)` | **algoritmo** | Genera ejemplos en el rango dado y ajusta `self.w1` / `self.w2` con sus errores. El aprendizaje **persiste** en el objeto. |
| `usar(a, b)` | **inferencia** | Aplica la regla ya aprendida: `return self.w1*a + self.w2*b`. Sin bucle, sin error. |

### Idea clave: el conocimiento vive en `self.`

Todo lo que la neurona necesita *recordar* (los pesos) se guarda con `self.`, para
que sobreviva cuando `entrenar` termina. Lo transitorio (un ejemplo de práctica,
los números que sumas al usarla) son variables locales normales. Esa separación es
lo que permite **entrenar una vez y usar la neurona muchas veces**.

### Cómo usarla desde otro programa

```python
from learn import Learn

# 1) Crear la neurona:  w1, w2, sesgo, tasa
n = Learn(0.0, 0.0, 0.0, 0.005)

# 2) Entrenarla (una vez):  nº de ejemplos, mínimo, máximo
n.entrenar(60, 0, 9)

# 3) Usarla tantas veces como quieras, con números nuevos:
print(n.usar(7, 2))   # ≈ 9
print(n.usar(3, 5))   # ≈ 8
```

> ⚠️ **La tasa depende del rango.** Con `tasa=0.005` y rango `0–9` converge bien,
> pero con un rango grande (p. ej. `0–1000`) esa misma tasa hace que los pesos
> **exploten**: entradas grandes → gradiente grande → paso demasiado grande. La
> solución profesional es **normalizar las entradas** a un rango pequeño. (Por eso
> casi todos los modelos de ML normalizan sus datos.)

---

## 📁 Estructura del proyecto

```
Learn/
├── app.py            # Versión inicial (script): el algoritmo paso a paso, comentado
├── README.md         # Este documento
├── POO/
│   └── learn.py      # Versión POO: la clase Learn (constructor, entrenar, usar)
└── learn_env/        # Entorno virtual de Python
```

---

## 🚧 Próximos pasos

- [x] **Predecir con la regla destilada**: usar los pesos ya aprendidos para sumar
  un par nuevo *sin* volver a entrenar. → hecho en `usar(a, b)`.
- [x] **Convertirlo en módulo reutilizable**: la clase `Learn` (`POO/learn.py`) ya
  se importa desde otros programas con `entrenar()` y `usar()`.
- [ ] **Normalizar las entradas** para que la neurona funcione con cualquier rango
  sin ajustar la tasa a mano.
- [ ] **Interconectar varias neuronas** (una red). Requiere dos piezas nuevas:
  una **función de activación no lineal** (apilar neuronas lineales sin ella
  colapsa a una sola) y **retropropagación** para repartir el error entre capas.

---

*Proyecto de aprendizaje: construido paso a paso para entender, desde cero, cómo
una máquina "aprende" a partir de sus propios errores.*
