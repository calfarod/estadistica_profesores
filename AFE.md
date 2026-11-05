# Plan Pedagógico de Análisis Factorial Exploratorio (AFE)

El Análisis Factorial Exploratorio busca condensar una matriz de datos observados en un número reducido de variables latentes (factores) que expliquen la correlación entre los reactivos.

---

## 1. Cronograma Modular del Plan

| Módulo | Nombre del Módulo | Objetivo Conceptual | Tablas Matemáticas Involucradas |
| --- | --- | --- | --- |
| **M1** | **Estandarización y Asociación** | Transformar mediciones arbitrarias a una escala común y cuantificar su covarianza. | Tabla de Datos Crudos ($X$), Tabla Estandarizada ($Z$), Matriz de Correlaciones ($R$). |
| **M2** | **Adecuación Muestral** | Verificar si los datos tienen correlación suficiente para justificar un factor. | Matriz Anti-imagen ($A$), Coeficientes MSA individual y KMO global. |
| **M3** | **Extracción de Factores** | Descomponer la varianza compartida mediante autovalores y autovectores. | Matriz Reducida ($R - U$), Tabla de Autovalores/Varianza, Matriz de Cargas no Rotadas ($\Lambda$). |
| **M4** | **Rotación Factorial** | Reorientar los ejes para lograr estructura simple (interpretación unívoca). | Matriz de Patrón ($P$), Matriz de Estructura ($S$), Matriz de Correlación Factorial ($\Phi$). |
| **M5** | **Puntuaciones Factoriales** | Calcular el valor individual de cada sujeto en cada dimensión latente. | Matriz de Ponderaciones ($W$), Tabla de Puntuaciones Factoriales ($F$). |

---

## 2. Desarrollo Detallado a través de las Tablas de Cálculo Manual

Para entender la mecánica interna del AFE, utilizaremos un microejemplo didáctico con **$N = 6$ profesores** y **$p = 4$ variables** medidas en escala Likert (1 a 5):

* $X_1, X_2$: Reactivos de Identidad/Valores (Dimensión Simbólica).
* $X_3, X_4$: Reactivos de Recursos/Acción (Dimensión Instrumental).

---

### Módulo 1: De los Datos Crudos a la Matriz de Correlaciones

#### Tabla 1: Datos Crudos ($X$)

La matriz inicial de observaciones directas de dimensión $N \times p$ ($6 \times 4$):

| Sujeto | $X_1$ (Identidad) | $X_2$ (Valores) | $X_3$ (Recursos) | $X_4$ (Acción) |
| --- | --- | --- | --- | --- |
| **1** | 5 | 4 | 2 | 1 |
| **2** | 4 | 5 | 1 | 2 |
| **3** | 5 | 5 | 2 | 2 |
| **4** | 2 | 1 | 4 | 5 |
| **5** | 1 | 2 | 5 | 4 |
| **6** | 2 | 2 | 5 | 5 |
| **Media ($\bar{X}$)** | **3.17** | **3.17** | **3.17** | **3.17** |
| **Desv. Est. ($s$)** | **1.72** | **1.72** | **1.72** | **1.72** |

#### Tabla 2: Datos Estandarizados ($Z$)

Para eliminar sesgos de escala o dispersión, cada celda se transforma a puntaje $z$:


$$z_{ij} = \frac{x_{ij} - \bar{X}_j}{s_j}$$

| Sujeto | $z_{X_1}$ | $z_{X_2}$ | $z_{X_3}$ | $z_{X_4}$ |
| --- | --- | --- | --- | --- |
| **1** | $+1.064$ | $+0.484$ | $-0.677$ | $-1.258$ |
| **2** | $+0.484$ | $+1.064$ | $-1.258$ | $-0.677$ |
| **3** | $+1.064$ | $+1.064$ | $-0.677$ | $-0.677$ |
| **4** | $-0.677$ | $-1.258$ | $+0.484$ | $+1.064$ |
| **5** | $-1.258$ | $-0.677$ | $+1.064$ | $+0.484$ |
| **6** | $-0.677$ | $-0.677$ | $+1.064$ | $+1.064$ |

#### Tabla 3: Matriz de Correlaciones de Pearson ($R$)

Se calcula multiplicando matricialmente: $R = \frac{1}{N-1} Z^T Z$. Es una matriz simétrica de tamaño $p \times p$ ($4 \times 4$):

|  | $X_1$ | $X_2$ | $X_3$ | $X_4$ |
| --- | --- | --- | --- | --- |
| **$X_1$** | **1.000** | $0.865$ | $-0.888$ | $-0.888$ |
| **$X_2$** | $0.865$ | **1.000** | $-0.888$ | $-0.888$ |
| **$X_3$** | $-0.888$ | $-0.888$ | **1.000** | $0.865$ |
| **$X_4$** | $-0.888$ | $-0.888$ | $0.865$ | **1.000** |

---

### Módulo 2: Verificación de Supuestos Matemáticos

#### Tabla 4: Matriz de Correlaciones Parciales / Anti-Imagen ($Q$)

Calcula la correlación entre cada par de variables aislando el efecto de todas las demás. Si hay factores comunes fuertes, las correlaciones parciales deben ser cercanas a cero.

$$r_{ij \cdot \text{resto}} = -\frac{a_{ij}}{\sqrt{a_{ii} a_{jj}}} \quad \text{donde } A = R^{-1}$$

* **KMO Global:**

$$KMO = \frac{\sum \sum_{i \ne j} r_{ij}^2}{\sum \sum_{i \ne j} r_{ij}^2 + \sum \sum_{i \ne j} q_{ij}^2}$$


* Si $\sum q_{ij}^2 \approx 0 \implies KMO \to 1.0$ (Muestreo adecuado).


* **Prueba de Bartlett:**

$$\chi^2 = -\left( N - 1 - \frac{2p + 5}{6} \right) \ln \vert{}R\vert{}$$



Verifica si el determinante $\vert{}R\vert{} < 1.0$, descartando que la matriz sea una identidad ($I$) sin correlaciones.

---

### Módulo 3: Extracción de Factores (Eje Principal / Descomposición)

El AFE descompone la matriz $R$ en dos fuentes de varianza:


$$R \approx \Lambda \Lambda^T + \Psi$$


Donde $\Lambda$ son las cargas factoriales comunes y $\Psi$ es la diagonal de unicidad ($u^2$).

#### Tabla 5: Matriz de Correlaciones Reducida ($R_r$)

A diferencia del Análisis de Componentes Principales (PCA) que coloca $1.0$ en la diagonal, el Análisis de Ejes Principales (PAF) sustituye los unos de la diagonal por estimaciones de **Comunalidad Inicial** ($h_0^2 = R^2_{\text{múltiple}}$):

|  | $X_1$ | $X_2$ | $X_3$ | $X_4$ |
| --- | --- | --- | --- | --- |
| **$X_1$** | **$h_1^2$** | $r_{12}$ | $r_{13}$ | $r_{14}$ |
| **$X_2$** | $r_{21}$ | **$h_2^2$** | $r_{23}$ | $r_{24}$ |
| **$X_3$** | $r_{31}$ | $r_{32}$ | **$h_3^2$** | $r_{34}$ |
| **$X_4$** | $r_{41}$ | $r_{42}$ | $r_{43}$ | **$h_4^2$** |

#### Tabla 6: Resumen de Autovalores y Varianza Explicada

Se calculan los autovalores resolviendo la ecuación característica $\vert{}R - \lambda I\vert{} = 0$:

| Factor ($k$) | Autovalor ($\lambda_k$) | % Varianza Individual | % Varianza Acumulada | Decisión de Retención |
| --- | --- | --- | --- | --- |
| **1** | **3.640** | $91.0\%$ | $91.0\%$ | Retener ($\lambda > 1.0$) |
| **2** | **0.180** | $4.5\%$ | $95.5\%$ | Descartar / Retener si teoría bifurca |
| **3** | $0.090$ | $2.3\%$ | $97.8\%$ | Descartar |
| **4** | $0.090$ | $2.2\%$ | $100.0\%$ | Descartar |

#### Tabla 7: Matriz de Cargas Factoriales no Rotadas ($\Lambda$)

Se obtiene multiplicando cada autovector normalizado ($V_k$) por la raíz de su autovalor: $\lambda_{ik} = v_{ik} \sqrt{\lambda_k}$.

| Variable | Factor 1 | Factor 2 | Comunalidad ($h^2 = \sum \lambda^2$) | Unicidad ($u^2 = 1 - h^2$) |
| --- | --- | --- | --- | --- |
| **$X_1$** | $0.954$ | $0.134$ | $0.928$ | $0.072$ |
| **$X_2$** | $0.954$ | $-0.134$ | $0.928$ | $0.072$ |
| **$X_3$** | $-0.954$ | $0.222$ | $0.959$ | $0.041$ |
| **$X_4$** | $-0.954$ | $-0.222$ | $0.959$ | $0.041$ |

*Nota:* Como se observa, el Factor 1 sin rotar mezcla todas las variables. Es necesario rotar para separar los polos.

---

### Módulo 4: Rotación Oblicua (Oblimin / Promax)

La rotación gira los ejes mediante una matriz de transformación $T$, permitiendo correlación entre factores ($\Phi \ne I$). Da lugar a tres tablas clave:

#### Tabla 8: Matriz de Patrón ($P$) — *Pattern Matrix*

Contiene las cargas directas aisladas (coeficientes de regresión estandarizados $\beta$):

| Variable | Factor 1 (Simbólico) | Factor 2 (Instrumental) | Comunalidad ($h^2$) | Unicidad ($u^2$) |
| --- | --- | --- | --- | --- |
| **$X_1$ (Identidad)** | **0.94** | $< 0.10$ | $0.93$ | $0.07$ |
| **$X_2$ (Valores)** | **0.91** | $< 0.10$ | $0.93$ | $0.07$ |
| **$X_3$ (Recursos)** | $< 0.10$ | **0.96** | $0.96$ | $0.04$ |
| **$X_4$ (Acción)** | $< 0.10$ | **0.95** | $0.96$ | $0.04$ |

#### Tabla 9: Matriz de Estructura ($S$) — *Structure Matrix*

Contiene la correlación simple entre variables y factores: $S = P \cdot \Phi$.

| Variable | Factor 1 | Factor 2 |
| --- | --- | --- |
| **$X_1$** | $0.94$ | $r_{F1,F2} \cdot 0.94$ |
| **$X_2$** | $0.91$ | $r_{F1,F2} \cdot 0.91$ |
| **$X_3$** | $r_{F1,F2} \cdot 0.96$ | $0.96$ |
| **$X_4$** | $r_{F1,F2} \cdot 0.95$ | $0.95$ |

#### Tabla 10: Matriz de Correlación entre Factores ($\Phi$)

Muestra el ángulo de apertura entre los factores oblicuos:

|  | Factor 1 | Factor 2 |
| --- | --- | --- |
| **Factor 1** | **1.000** | $r_{F1, F2}$ |
| **Factor 2** | $r_{F1, F2}$ | **1.000** |

---

### Módulo 5: Estimación de Puntuaciones Factoriales

Para saber qué valor tiene cada docente en cada dimensión, se calculan las puntuaciones factoriales utilizando el **Método de Regresión** de Thomson o el **Método de Bartlett**:


$$W = R^{-1} S$$

$$F = Z \cdot W$$

#### Tabla 11: Matriz de Ponderaciones de Puntuación Factorial ($W$)

Contiene los pesos que multiplican a cada respuesta estandarizada:

| Variable | Ponderador $W_{F1}$ | Ponderador $W_{F2}$ |
| --- | --- | --- |
| **$X_1$** | $w_{11}$ | $w_{12}$ |
| **$X_2$** | $w_{21}$ | $w_{22}$ |
| **$X_3$** | $w_{31}$ | $w_{32}$ |
| **$X_4$** | $w_{41}$ | $w_{42}$ |

#### Tabla 12: Puntuaciones Factoriales Finales por Sujeto ($F$)

La tabla que finalmente se exporta a Jamovi como `Puntuación del Factor 1` y `Puntuación del Factor 2`:

| Sujeto | Comunidad | Puntuación Factor 1 ($F_1$) | Puntuación Factor 2 ($F_2$) | Cuadrante Asignado |
| --- | --- | --- | --- | --- |
| **1** | Profesores de Iquique | $+1.12$ | $+0.98$ | Cuadrante I (Autopoiética) |
| **2** | Profesores de Arica | $+0.85$ | $-1.15$ | Cuadrante II (Retórica) |
| **3** | Profesores de Iquique | $+1.25$ | $+1.10$ | Cuadrante I (Autopoiética) |
| **4** | Profesores de Antofagasta | $-1.02$ | $+0.89$ | Cuadrante IV (Corporativa) |
| **5** | Profesores de Alto Hospicio | $-1.30$ | $-0.95$ | Cuadrante III (Inerte) |
| **6** | Profesores de Antofagasta | $-0.90$ | $+1.05$ | Cuadrante IV (Corporativa) |

---

## 3. Hoja de Ruta de Aprendizaje

1. **Ejercitar el paso de Tabla 1 a Tabla 3:** Realizar a mano la estandarización $Z$ y el producto $Z^T Z$ para un par de variables.
2. **Entender la ecuación fundamental:** Deducir por qué la Comunalidad $h^2$ más la Unicidad $u^2$ siempre suma $1.0$.
3. **Contrastar la Matriz de Patrón frente a la de Estructura:** Notar que en rotaciones ortogonales (Varimax) ambas matrices son idénticas, y solo se separan cuando la rotación es oblicua (Oblimin/Promax).

---