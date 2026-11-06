# Curso Estadística

El Análisis Factorial (tanto Exploratorio como Confirmatorio) no opera directamente sobre las respuestas en bruto de los sujetos, sino sobre una **matriz de asociación** ($\mathbf{S}$ de covarianzas o $\mathbf{R}$ de correlaciones). El objetivo final del AF es descomponer esa matriz y reproducirla mediante un número reducido de variables latentes (factores). Si la estructura de asociación basal no se comprende a fondo a nivel algebraico y geométrico, el AF se convierte en una caja negra.

---

### Plan de Aprendizaje: De la Asociación Lineal al Modelo Factorial

1. **Módulo 1: Variabilidad Univariada y Bivariada (Covarianza)**
* Centroide y dispersión: Desvíos respecto a la media.
* Covarianza muestral ($s_{xy}$): Mecanismo algebraico, productos cruzados e interpretación geométrica (cuadrantes de dispersión).
* Limitación escalar: Por qué la covarianza no permite comparar fuerzas de asociación directamente.


2. **Módulo 2: Estandarización y Asociación Relativa (Correlación de Pearson)**
* Puntuaciones típicas ($z$).
* Coeficiente de correlación de Pearson ($r$): Derivación como covarianza de variables estandarizadas y como coseno del ángulo entre vectores en el espacio de sujetos ($\cos \theta$).
* Descomposición de la varianza: Coeficiente de determinación ($r^2$).


3. **Módulo 3: Álgebra Matricial de la Asociación**
* Construcción de la matriz de datos centrada ($\mathbf{X}_c$) y estandarizada ($\mathbf{Z}$).
* Derivación compacta: $\mathbf{S} = \frac{1}{n-1}\mathbf{X}_c^T\mathbf{X}_c$ y $\mathbf{R} = \frac{1}{n-1}\mathbf{Z}^T\mathbf{Z}$.
* Propiedades clave para el AF: Simetría, diagonal principal y condición de matriz definida positiva (determinante $\vert{}R\vert{} > 0$).


4. **Módulo 4: El Puente Hacia AFE y AFC**
* Supuestos de factorizabilidad: Determinante, esfericidad de Bartlett y medida KMO.
* La ecuación fundamental del AF en términos matriciales: $\boldsymbol{\Sigma} = \boldsymbol{\Lambda}\boldsymbol{\Phi}\boldsymbol{\Lambda}^T + \boldsymbol{\Theta}$.
* ¿Por qué y cuándo factorizar $\mathbf{R}$ (escalas estandarizadas o ítems heterogéneos) frente a $\mathbf{S}$ (unidades homogéneas y AFC estructural)?



---

## Módulo 1: La Covarianza como Base del Co-movimiento

Comencemos por el bloque fundamental.

### 1. Definición Formal y Fórmulas

Sean dos variables observadas $X$ e $Y$ medidas en una muestra de tamaño $n$.

* **Medias muestrales:**

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, \quad \bar{Y} = \frac{1}{n}\sum_{i=1}^n Y_i$$


* **Varianza muestral de $X$** (dispersión interna):

$$s_x^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})(X_i - \bar{X})$$


* **Covarianza muestral entre $X$ e $Y$** (variación conjunta):

$$s_{xy} = \operatorname{Cov}(X,Y) = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})$$



Forma computacional equivalente (reducción de errores por redondeo):


$$s_{xy} = \frac{1}{n-1} \left( \sum_{i=1}^n X_i Y_i - \frac{\sum X_i \sum Y_i}{n} \right)$$

### 2. Anatomía Geométrica de los Productos Cruzados

Al centrar los datos en $(\bar{X}, \bar{Y})$, el plano cartesiano se divide en cuatro cuadrantes respecto al centroide:

| Caso | Desvío $(X_i - \bar{X})$ | Desvío $(Y_i - \bar{Y})$ | Signo del Producto Cruzado | Interpretación |
| --- | --- | --- | --- | --- |
| **Cuadrante I** | $+$ | $+$ | **$+$** | Sujeto por encima de la media en ambos ítems |
| **Cuadrante II** | $-$ | $+$ | **$-$** | Sujeto bajo la media en $X$, sobre la media en $Y$ |
| **Cuadrante III** | $-$ | $-$ | **$+$** | Sujeto por debajo de la media en ambos ítems |
| **Cuadrante IV** | $+$ | $-$ | **$-$** | Sujeto sobre la media en $X$, bajo la media en $Y$ |

La suma de estos productos cruzados $\sum (X_i - \bar{X})(Y_i - \bar{Y})$ representa el balance neto: si predominan los puntos en los cuadrantes I y III, la suma es marcadamente positiva; si predominan en II y IV, es negativa. Al dividir por $n-1$, obtenemos el promedio muestral de variación conjunta insesgado.

### 3. Ejemplo Numérico Paso a Paso

Supongamos $n = 5$ respuestas a dos ítems tipo Likert de 5 puntos:

* $X$: *Autoeficacia percibida*
* $Y$: *Uso de herramientas analíticas*

| Sujeto ($i$) | $X_i$ | $Y_i$ | $(X_i - \bar{X})$ | $(Y_i - \bar{Y})$ | $(X_i - \bar{X})^2$ | $(Y_i - \bar{Y})^2$ | $(X_i - \bar{X})(Y_i - \bar{Y})$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1 | $-1.0$ | $-1.8$ | $1.00$ | $3.24$ | $+1.80$ |
| 2 | 3 | 2 | $0.0$ | $-0.8$ | $0.00$ | $0.64$ | $0.00$ |
| 3 | 2 | 3 | $-1.0$ | $+0.2$ | $1.00$ | $0.04$ | $-0.20$ |
| 4 | 4 | 4 | $+1.0$ | $+1.2$ | $1.00$ | $1.44$ | $+1.20$ |
| 5 | 4 | 4 | $+1.0$ | $+1.2$ | $1.00$ | $1.44$ | $+1.20$ |
| **$\sum$** | **15** | **14** | **$0.0$** | **$0.0$** | **$4.00$** | **$6.80$** | **$+4.00$** |

* Medias: $\bar{X} = 15/5 = 3.0$, $\bar{Y} = 14/5 = 2.8$
* Varianzas muestrales ($n-1 = 4$):

$$s_x^2 = \frac{4.00}{4} = 1.00 \implies s_x = 1.00$$


$$s_y^2 = \frac{6.80}{4} = 1.70 \implies s_y \approx 1.3038$$


* Covarianza muestral:

$$s_{xy} = \frac{+4.00}{4} = 1.00$$



### 4. Interpretación y Limitación Escalar

* **Interpretación:** $s_{xy} = +1.00$ indica una tendencia de co-variación lineal positiva: cuando una observación supera la media en $X$, tiende a superar la media en $Y$.
* **El problema de escala:** La covarianza se expresa en unidades combinadas: $\text{unidades}(X) \times \text{unidades}(Y)$. Si multiplicamos los valores de $X$ por 10 (por ejemplo, cambiando una escala de 5 puntos a un rango de 10 a 50 puntos), la nueva covarianza se multiplicaría por 10: $s_{x_{nuevo}, y} = 10.00$, a pesar de que la intensidad y forma de la relación entre los sujetos no cambió en lo absoluto.

Esta dependencia de la escala métrica es la que obliga a introducir la **estandarización**, dando paso a la correlación de Pearson y a la matriz $\mathbf{R}$.

&nbsp;

&nbsp;

---
# Módulo 2: Estandarización y Asociación Relativa (Correlación de Pearson)

En el Módulo 1 se constató que la covarianza muestral $s_{xy}$ refleja fielmente la dirección del co-movimiento entre dos variables, pero su magnitud numérica está condicionada por las unidades de medida originales de los ítems. Para construir una métrica de asociación invariante ante transformaciones lineales de escala, es necesario estandarizar las observaciones.

---

## 1. Puntuaciones Típicas ($z$) y sus Propiedades Matemáticas

Dada una variable cuantitativa $X$ con media muestral $\bar{X}$ y desviación estándar muestral $s_x > 0$, la puntuación tipificada o estandarizada para el sujeto $i$ se define como:

$$z_{xi} = \frac{X_i - \bar{X}}{s_x}$$

### Propiedad A: Media Nula ($\bar{z}_x = 0$)
$$\sum_{i=1}^n z_{xi} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{s_x}\right) = \frac{1}{s_x}\sum_{i=1}^n (X_i - \bar{X}) = \frac{0}{s_x} = 0 \implies \bar{z}_x = 0$$

### Propiedad B: Varianza y Desviación Estándar Unitarias ($s_{z_x}^2 = 1$, $s_{z_x} = 1$)
$$s_{z_x}^2 = \frac{1}{n-1}\sum_{i=1}^n (z_{xi} - \bar{z}_x)^2 = \frac{1}{n-1}\sum_{i=1}^n z_{xi}^2$$

Sustituyendo la definición de $z_{xi}$:

$$s_{z_x}^2 = \frac{1}{n-1}\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{s_x}\right)^2 = \frac{1}{s_x^2} \left[ \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 \right] = \frac{s_x^2}{s_x^2} = 1$$

Al tipificar, eliminamos el efecto de la unidad métrica y fijamos la escala de dispersión en desviaciones estándar respecto a la media.

---

## 2. Derivación Formal del Coeficiente de Correlación de Pearson ($r_{xy}$)

El coeficiente de correlación producto-momento de Pearson se define rigurosamente como la **covarianza entre las variables tipificadas** $Z_x$ y $Z_y$:

$$r_{xy} = \operatorname{Cov}(Z_x, Z_y) = \frac{1}{n-1}\sum_{i=1}^n (z_{xi} - \bar{z}_x)(z_{yi} - \bar{z}_y)$$

Dado que $\bar{z}_x = 0$ y $\bar{z}_y = 0$:

$$r_{xy} = \frac{1}{n-1}\sum_{i=1}^n z_{xi} z_{yi}$$

Sustituyendo las definiciones originales de $z_{xi}$ y $z_{yi}$:

$$r_{xy} = \frac{1}{n-1}\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{s_x}\right)\left(\frac{Y_i - \bar{Y}}{s_y}\right) = \frac{\frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{s_x s_y}$$

Reemplazando el numerador por la covarianza muestral $s_{xy}$:

$$r_{xy} = \frac{s_{xy}}{s_x s_y}$$

### Consecuencias Algebraicas:
1. **Invarianza de Escala:** Si aplicamos transformaciones lineales estrictamente crecientes $X^* = aX + b$ (con $a > 0$) e $Y^* = cY + d$ (con $c > 0$), se demuestra que:
   $$r_{x^*y^*} = r_{xy}$$
2. **Límites Teóricos:** Por la desigualdad de Cauchy-Schwarz, se garantiza que:
   $$-1 \le r_{xy} \le +1$$

---

## 3. Ejemplo Numérico Paso a Paso ($n = 5$)

Continuando con la muestra observada en el Módulo 1:
* $\bar{X} = 3.00$, $\quad s_x^2 = 1.00 \implies s_x = 1.00$
* $\bar{Y} = 2.80$, $\quad s_y^2 = 1.70 \implies s_y = \sqrt{1.70} \approx 1.30384$
* $s_{xy} = 1.00$

### A. Vía Directa (Sintética)
$$r_{xy} = \frac{s_{xy}}{s_x s_y} = \frac{1.00}{(1.00)(1.30384)} = \frac{1.00}{1.30384} \approx 0.76696 \approx 0.767$$

### B. Vía Tabular Explícita (Puntuaciones $z$)

| Sujeto ($i$) | $(X_i - \bar{X})$ | $(Y_i - \bar{Y})$ | $z_{xi} = \frac{X_i - 3.0}{1.00}$ | $z_{yi} = \frac{Y_i - 2.8}{1.30384}$ | Producto $z_{xi} z_{yi}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | $-1.0$ | $-1.8$ | $-1.00000$ | $-1.38054$ | $+1.38054$ |
| 2 | $0.0$ | $-0.8$ | $0.00000$ | $-0.61357$ | $0.00000$ |
| 3 | $-1.0$ | $+0.2$ | $-1.00000$ | $+0.15339$ | $-0.15339$ |
| 4 | $+1.0$ | $+1.2$ | $+1.00000$ | $+0.92036$ | $+0.92036$ |
| 5 | $+1.0$ | $+1.2$ | $+1.00000$ | $+0.92036$ | $+0.92036$ |
| **$\sum$** | **$0.0$** | **$0.0$** | **$0.00000$** | **$0.00000$** | **$+3.06787$** |

Aplicando el divisor de grados de libertad ($n - 1 = 4$):

$$r_{xy} = \frac{\sum_{i=1}^5 z_{xi} z_{yi}}{4} = \frac{3.06787}{4} \approx 0.76697 \approx 0.767$$

---

## 4. Interpretación Geométrica: Vectores en el Espacio de Sujetos ($\mathbb{R}^n$)

En la perspectiva multivariada que sustenta al Análisis Factorial, se invierte la lógica cartesiana tradicional: en lugar de ubicar $n$ puntos dentro de un espacio de variables, **cada variable se modela como un único vector dentro de un espacio vectorial de $n$ dimensiones ($\mathbb{R}^n$)**, donde cada eje ortogonal corresponde a un sujeto observado.

Definamos los vectores centrados de las dos variables:

$$\mathbf{x}_c = \begin{pmatrix} X_1 - \bar{X} \\ X_2 - \bar{X} \\ \vdots \\ X_n - \bar{X} \end{pmatrix} = \begin{pmatrix} -1.0 \\ 0.0 \\ -1.0 \\ 1.0 \\ 1.0 \end{pmatrix}, \quad \mathbf{y}_c = \begin{pmatrix} Y_1 - \bar{Y} \\ Y_2 - \bar{Y} \\ \vdots \\ Y_n - \bar{Y} \end{pmatrix} = \begin{pmatrix} -1.8 \\ -0.8 \\ 0.2 \\ 1.2 \\ 1.2 \end{pmatrix}$$

### A. Producto Escalar (Punto)
El producto interior euclidiano usual entre $\mathbf{x}_c$ e $\mathbf{y}_c$ es:
$$\mathbf{x}_c \cdot \mathbf{y}_c = \mathbf{x}_c^T \mathbf{y}_c = \sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})$$

Obsérvese que:
$$\mathbf{x}_c^T \mathbf{y}_c = (n-1) s_{xy}$$

### B. Norma (Longitud) de los Vectores Centrados
La longitud euclidiana $\|\mathbf{v}\| = \sqrt{\mathbf{v}^T\mathbf{v}}$ de un vector centrado está unida a la desviación estándar:
$$\|\mathbf{x}_c\| = \sqrt{\sum_{i=1}^n (X_i - \bar{X})^2} = \sqrt{(n-1) s_x^2} = s_x \sqrt{n-1}$$
$$\|\mathbf{y}_c\| = \sqrt{\sum_{i=1}^n (Y_i - \bar{Y})^2} = \sqrt{(n-1) s_y^2} = s_y \sqrt{n-1}$$

Para nuestros datos:
* $\|\mathbf{x}_c\| = \sqrt{4.00} = 2.00$
* $\|\mathbf{y}_c\| = \sqrt{6.80} \approx 2.60768$

### C. El Teorema del Coseno del Ángulo ($\cos \theta$)
De acuerdo con la geometría euclidiana, el producto interior satisface:
$$\mathbf{x}_c^T \mathbf{y}_c = \|\mathbf{x}_c\| \|\mathbf{y}_c\| \cos \theta$$

Despejando $\cos \theta$:
$$\cos \theta = \frac{\mathbf{x}_c^T \mathbf{y}_c}{\|\mathbf{x}_c\| \|\mathbf{y}_c\|} = \frac{\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{\left(s_x \sqrt{n-1}\right)\left(s_y \sqrt{n-1}\right)} = \frac{\frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})}{s_x s_y}$$

Identificando los términos con las definiciones previas:

$$\cos \theta = \frac{s_{xy}}{s_x s_y} = r_{xy}$$

> **Conclusión Geométrica Fundamental:**  
> El coeficiente de correlación de Pearson entre dos variables es exactamente igual al **coseno del ángulo $\theta$** formado por sus respectivos vectores centrados en el espacio muestral $\mathbb{R}^n$.

Para nuestro caso numérico:
$$\cos \theta = 0.7670 \implies \theta = \arccos(0.7670) \approx 0.6967 \text{ rad} \approx 39.92^\circ$$

---

## 5. Coeficiente de Determinación ($r^2$) y Conexión con el AFE/AFC

### A. Descomposición de la Varianza ($r^2$)
El cuadrado del coeficiente de correlación, $r^2$, define la proporción de varianza de una variable que puede ser reproducida linealmente a partir de la otra:

$$r^2 = (0.76696)^2 \approx 0.5882 \implies 58.82\%$$

El $58.82\%$ de la variabilidad entre las respuestas de los sujetos en el ítem $X$ e ítem $Y$ es **varianza compartida (común)**, mientras que el $41.18\%$ restante representa **varianza no compartida** (especificidad del ítem más error de medición).

### B. El Puente Hacia el Corazón del Análisis Factorial

| Configuración Geométrica | Ángulo $\theta$ | $r_{xy} = \cos \theta$ | $r^2$ | Interpretación para AFE / AFC |
| :--- | :---: | :---: | :---: | :--- |
| **Colineales coincidentes** | $0^\circ$ | $+1.0$ | $1.00$ | Redundancia lineal total. Provoca singularidad en la matriz ($|R| = 0$). |
| **Haz angular cerrado** | $\theta < 45^\circ$ | $> 0.70$ | $> 0.50$ | Las variables apuntan en la misma dirección latente; compartirán cargas elevadas en el mismo factor común. |
| **Ortogonalidad** | $90^\circ$ | $0.0$ | $0.00$ | Independencia lineal. No existe varianza común compartida; no pueden agruparse bajo un factor único. |
| **Oposición** | $180^\circ$ | $-1.0$ | $1.00$ | Ítem inverso. El factor capturará la dimensión con cargas de signos opuestos. |

En el Análisis Factorial:
1. El **AFE** busca encontrar un conjunto de $m$ ejes ortogonales u oblicuos (factores latentes, con $m \ll p$) tales que los vectores de las variables observadas queden explicados por su proyección sobre esos nuevos ejes.
2. La suma de las proyecciones al cuadrado sobre los factores retenidos constituirá la **comunalidad** ($h^2_j$), que no es más que la extensión multivariada del $r^2$ bivariado que acabamos de derivar.

---

&nbsp;

&nbsp;

---

# Módulo 3: Álgebra Matricial de la Asociación

En los módulos precedentes se analizó la asociación bivariada mediante productos cruzados y cosenos de ángulos en $\mathbb{R}^n$. Cuando el objetivo es modelar simultáneamente $p$ variables observadas (ítems de un instrumento psicométrico o biométrico), la formulación escalar resulta ineficiente. El Análisis Factorial (AFE y AFC) se fundamenta enteramente en el **álgebra matricial** de las matrices de covarianzas ($\mathbf{S}$) y correlaciones ($\mathbf{R}$).

---

## 1. Construcción de Matrices de Datos: $\mathbf{X}$, $\mathbf{X}_c$ y $\mathbf{Z}$

Consideremos una muestra de $n$ individuos evaluados en $p$ variables observadas.

### A. Matriz de Datos Crudos ($\mathbf{X}$)
Es una matriz rectangular de orden $n \times p$:

$$
\mathbf{X} = \begin{pmatrix} 
X_{11} & X_{12} & \cdots & X_{1p} \\
X_{21} & X_{22} & \cdots & X_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
X_{n1} & X_{n2} & \cdots & X_{np}
\end{pmatrix}
$$

* Las **filas** ($i = 1, \dots, n$) representan a los sujetos muestreados.
* Las **columnas** ($j = 1, \dots, p$) representan los vectores de cada variable o ítem.

El vector de medias muestrales $\bar{\mathbf{x}}$ (de orden $p \times 1$) es:

$$
\bar{\mathbf{x}} = \frac{1}{n} \mathbf{X}^T \mathbf{1}_n = \begin{pmatrix} \bar{X}_1 \\ \bar{X}_2 \\ \vdots \\ \bar{X}_p \end{pmatrix}
$$

donde $\mathbf{1}_n$ es un vector columna de unos de dimensión $n \times 1$.

---

### B. Matriz de Datos Centrados ($\mathbf{X}_c$)
Resta a cada columna su media correspondiente:

$$
\mathbf{X}_c = \mathbf{X} - \mathbf{1}_n \bar{\mathbf{x}}^T = \begin{pmatrix} 
(X_{11} - \bar{X}_1) & (X_{12} - \bar{X}_2) & \cdots & (X_{1p} - \bar{X}_p) \\
(X_{21} - \bar{X}_1) & (X_{22} - \bar{X}_2) & \cdots & (X_{2p} - \bar{X}_p) \\
\vdots & \vdots & \ddots & \vdots \\
(X_{n1} - \bar{X}_1) & (X_{n2} - \bar{X}_2) & \cdots & (X_{np} - \bar{X}_p)
\end{pmatrix}
$$

Matricialmente, esto se calcula mediante la **matriz de centrado** $\mathbf{H}_n = \mathbf{I}_n - \frac{1}{n}\mathbf{1}_n\mathbf{1}_n^T$ (simétrica e idempotente, $\mathbf{H}_n = \mathbf{H}_n^T = \mathbf{H}_n^2$):

$$
\mathbf{X}_c = \mathbf{H}_n \mathbf{X}
$$

---

### C. Matriz de Datos Tipificados ($\mathbf{Z}$)
Para normalizar la dispersión, definimos la matriz diagonal de desviaciones estándar muestrales $\mathbf{D}_s$ (de orden $p \times p$):

$$
\mathbf{D}_s = \operatorname{diag}(s_1, s_2, \dots, s_p) = \begin{pmatrix} 
s_1 & 0 & \cdots & 0 \\
0 & s_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & s_p
\end{pmatrix}
$$

Su inversa, $\mathbf{D}_s^{-1}$, contiene los recíprocos de las desviaciones estándar en la diagonal principal:

$$
\mathbf{D}_s^{-1} = \operatorname{diag}\left(\frac{1}{s_1}, \frac{1}{s_2}, \dots, \frac{1}{s_p}\right)
$$

La matriz de puntuaciones estandarizadas $\mathbf{Z}$ (de orden $n \times p$) resulta de multiplicar por la derecha:

$$
\mathbf{Z} = \mathbf{X}_c \mathbf{D}_s^{-1} = \begin{pmatrix} 
z_{11} & z_{12} & \cdots & z_{1p} \\
z_{21} & z_{22} & \cdots & z_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
z_{n1} & z_{n2} & \cdots & z_{np}
\end{pmatrix}
$$

---

## 2. Derivación Compacta de las Matrices de Asociación: $\mathbf{S}$ y $\mathbf{R}$

### A. La Matriz de Varianzas-Covarianzas ($\mathbf{S}$)
La matriz $\mathbf{S}$ condensa todas las varianzas y covarianzas entre los $p$ ítems en un arreglo cuadrado de dimensión $p \times p$:

$$
\mathbf{S} = \frac{1}{n-1}\mathbf{X}_c^T \mathbf{X}_c
$$

Al ejecutar el producto matricial fila por columna entre $\mathbf{X}_c^T$ (dimensión $p \times n$) y $\mathbf{X}_c$ (dimensión $n \times p$):

$$
\mathbf{S} = \begin{pmatrix} 
s_1^2 & s_{12} & \cdots & s_{1p} \\
s_{21} & s_2^2 & \cdots & s_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
s_{p1} & s_{p2} & \cdots & s_p^2
\end{pmatrix}
$$

* **Elementos diagonales ($j = k$):** Son los productos interiores del vector centrado de una variable consigo mismo divididos por $n-1$:
  $$s_j^2 = \frac{1}{n-1} \mathbf{x}_{c,j}^T \mathbf{x}_{c,j}$$
* **Elementos fuera de la diagonal ($j \ne k$):** Son los productos interiores cruzados entre dos variables divididos por $n-1$:
  $$s_{jk} = \frac{1}{n-1} \mathbf{x}_{c,j}^T \mathbf{x}_{c,k}$$

---

### B. La Matriz de Correlaciones de Pearson ($\mathbf{R}$)
Calculando la covarianza de la matriz tipificada $\mathbf{Z}$:

$$
\mathbf{R} = \frac{1}{n-1}\mathbf{Z}^T \mathbf{Z}
$$

Sustituyendo $\mathbf{Z} = \mathbf{X}_c \mathbf{D}_s^{-1}$:

$$
\mathbf{R} = \frac{1}{n-1}\left(\mathbf{X}_c \mathbf{D}_s^{-1}\right)^T \left(\mathbf{X}_c \mathbf{D}_s^{-1}\right) = \mathbf{D}_s^{-1} \left(\frac{1}{n-1}\mathbf{X}_c^T \mathbf{X}_c\right) \mathbf{D}_s^{-1}
$$

Identificando $\mathbf{S}$ en el núcleo de la expresión:

$$
\mathbf{R} = \mathbf{D}_s^{-1} \mathbf{S} \mathbf{D}_s^{-1}
$$

Desarrollando esta multiplicación:

$$
\mathbf{R} = \begin{pmatrix} 
1 & r_{12} & \cdots & r_{1p} \\
r_{21} & 1 & \cdots & r_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
r_{p1} & r_{p2} & \cdots & 1
\end{pmatrix}
$$

A la inversa, si se dispone de la matriz de correlaciones $\mathbf{R}$ y las desviaciones típicas, se reconstruye $\mathbf{S}$ como:

$$
\mathbf{S} = \mathbf{D}_s \mathbf{R} \mathbf{D}_s
$$

---

## 3. Ejemplo Numérico Completo: $p = 3$ Variables, $n = 5$ Sujetos

Ampliemos la muestra de los módulos anteriores añadiendo un tercer ítem:
* $X_1$: Autoeficacia percibida
* $X_2$: Uso de herramientas analíticas
* $X_3$: Satisfacción con el análisis de datos

### A. Matriz de Datos Crudos ($\mathbf{X}$)

$$
\mathbf{X} = \begin{pmatrix} 
2 & 1 & 3 \\
3 & 2 & 3 \\
2 & 3 & 2 \\
4 & 4 & 5 \\
4 & 4 & 4
\end{pmatrix}
$$

* Medias muestrales:
  $$\bar{X}_1 = \frac{15}{5} = 3.0, \quad \bar{X}_2 = \frac{14}{5} = 2.8, \quad \bar{X}_3 = \frac{17}{5} = 3.4$$

---

### B. Matriz Centrada ($\mathbf{X}_c$)

$$
\mathbf{X}_c = \begin{pmatrix} 
2 - 3.0 & 1 - 2.8 & 3 - 3.4 \\
3 - 3.0 & 2 - 2.8 & 3 - 3.4 \\
2 - 3.0 & 3 - 2.8 & 2 - 3.4 \\
4 - 3.0 & 4 - 2.8 & 5 - 3.4 \\
4 - 3.0 & 4 - 2.8 & 4 - 3.4
\end{pmatrix} = \begin{pmatrix} 
-1.0 & -1.8 & -0.4 \\
 0.0 & -0.8 & -0.4 \\
-1.0 & +0.2 & -1.4 \\
+1.0 & +1.2 & +1.6 \\
+1.0 & +1.2 & +0.6
\end{pmatrix}
$$

---

### C. Cálculo de $\mathbf{S} = \frac{1}{4} \mathbf{X}_c^T \mathbf{X}_c$

Calculamos la matriz de productos cruzados $\mathbf{X}_c^T \mathbf{X}_c$:

$$
\mathbf{X}_c^T \mathbf{X}_c = \begin{pmatrix} 
-1.0 & 0.0 & -1.0 & 1.0 & 1.0 \\
-1.8 & -0.8 & 0.2 & 1.2 & 1.2 \\
-0.4 & -0.4 & -1.4 & 1.6 & 0.6
\end{pmatrix}
\begin{pmatrix} 
-1.0 & -1.8 & -0.4 \\
 0.0 & -0.8 & -0.4 \\
-1.0 & +0.2 & -1.4 \\
+1.0 & +1.2 & +1.6 \\
+1.0 & +1.2 & +0.6
\end{pmatrix}
$$

* **Elementos diagonales ($\sum x_{ci}^2$):**
  * Columna 1: $(-1)^2 + 0^2 + (-1)^2 + 1^2 + 1^2 = 4.00$
  * Columna 2: $(-1.8)^2 + (-0.8)^2 + 0.2^2 + 1.2^2 + 1.2^2 = 6.80$
  * Columna 3: $(-0.4)^2 + (-0.4)^2 + (-1.4)^2 + 1.6^2 + 0.6^2 = 0.16 + 0.16 + 1.96 + 2.56 + 0.36 = 5.20$

* **Elementos cruzados ($\sum x_{ci} x_{ki}$):**
  * $(1, 2)$: $(-1)(-1.8) + (0)(-0.8) + (-1)(0.2) + (1)(1.2) + (1)(1.2) = 1.80 - 0.20 + 1.20 + 1.20 = 4.00$
  * $(1, 3)$: $(-1)(-0.4) + (0)(-0.4) + (-1)(-1.4) + (1)(1.6) + (1)(0.6) = 0.40 + 1.40 + 1.60 + 0.60 = 4.00$
  * $(2, 3)$: $(-1.8)(-0.4) + (-0.8)(-0.4) + (0.2)(-1.4) + (1.2)(1.6) + (1.2)(0.6) = 0.72 + 0.32 - 0.28 + 1.92 + 0.72 = 3.40$

Dividiendo entre $n - 1 = 4$:

$$
\mathbf{S} = \frac{1}{4} \begin{pmatrix} 
4.00 & 4.00 & 4.00 \\
4.00 & 6.80 & 3.40 \\
4.00 & 3.40 & 5.20
\end{pmatrix} = \begin{pmatrix} 
1.00 & 1.00 & 1.00 \\
1.00 & 1.70 & 0.85 \\
1.00 & 0.85 & 1.30
\end{pmatrix}
$$

---

### D. Construcción de la Matriz de Correlaciones ($\mathbf{R}$)

Las desviaciones estándar muestrales son:
* $s_1 = \sqrt{1.00} = 1.00$
* $s_2 = \sqrt{1.70} \approx 1.30384$
* $s_3 = \sqrt{1.30} \approx 1.14018$

Matriz diagonal de desvíos $\mathbf{D}_s^{-1}$:

$$
\mathbf{D}_s^{-1} = \begin{pmatrix} 
1.00 & 0 & 0 \\
0 & \frac{1}{1.30384} & 0 \\
0 & 0 & \frac{1}{1.14018}
\end{pmatrix} \approx \begin{pmatrix} 
1.0000 & 0 & 0 \\
0 & 0.7670 & 0 \\
0 & 0 & 0.8771
\end{pmatrix}
$$

Calculando $r_{jk} = \frac{s_{jk}}{s_j s_k}$:
* $r_{12} = \frac{1.00}{(1.00)(1.30384)} \approx 0.7670$
* $r_{13} = \frac{1.00}{(1.00)(1.14018)} \approx 0.8771$
* $r_{23} = \frac{0.85}{(1.30384)(1.14018)} = \frac{0.85}{1.48661} \approx 0.5718$

La matriz $\mathbf{R}$ resultante es:

$$
\mathbf{R} = \begin{pmatrix} 
1.0000 & 0.7670 & 0.8771 \\
0.7670 & 1.0000 & 0.5718 \\
0.8771 & 0.5718 & 1.0000
\end{pmatrix}
$$

---

## 4. Propiedades Matemáticas Clave para el Análisis Factorial

Las matrices de asociación no son tablas numéricas arbitrarias; cumplen propiedades algebraicas indispensables sobre las cuales descansan los algoritmos de descomposición espectral:

### 1. Simetría Estricta
Tanto $\mathbf{S}$ como $\mathbf{R}$ son simétricas respecto a la diagonal principal:

$$
\mathbf{S} = \mathbf{S}^T \quad \text{y} \quad \mathbf{R} = \mathbf{R}^T
$$

* Para todo par de variables, $s_{jk} = s_{kj}$ y $r_{jk} = r_{kj}$.
* El número de elementos informativos únicos no redundantes (el triángulo inferior o superior más la diagonal) es:
  $$p^* = \frac{p(p + 1)}{2}$$
  En nuestro ejemplo con $p = 3$: $\frac{3(4)}{2} = 6$ elementos únicos. Este valor $p^*$ impone el **límite superior de parámetros identificables en AFC**.

---

### 2. Traza Matricial ($\operatorname{tr}$) y Varianza Total
La traza es la suma de los elementos de la diagonal principal:

* Para la matriz de covarianzas:
  $$\operatorname{tr}(\mathbf{S}) = \sum_{j=1}^p s_j^2 = \text{Varianza Total Observada}$$
  En el ejemplo: $\operatorname{tr}(\mathbf{S}) = 1.00 + 1.70 + 1.30 = 4.00$.

* Para la matriz de correlaciones:
  $$\operatorname{tr}(\mathbf{R}) = \sum_{j=1}^p 1 = p$$
  En el ejemplo: $\operatorname{tr}(\mathbf{R}) = 1 + 1 + 1 = 3.00$.

> **Relevancia Factorial:**  
> En AFE y ACP, la suma de los autovalores ($\lambda_j$) de la matriz es idéntica a su traza ($\sum \lambda_j = \operatorname{tr}$). Por eso, al factorizar $\mathbf{R}$, la varianza total a explicar es exactamente igual al número de ítems $p$.

---

### 3. Matriz Definida Positiva y el Determinante ($|\mathbf{R}|$)

Una matriz simétrica $\mathbf{A}$ de orden $p \times p$ es **definida positiva** si para cualquier vector no nulo $\mathbf{v} \ne \mathbf{0}$ se cumple:

$$
\mathbf{v}^T \mathbf{A} \mathbf{v} > 0
$$

Condiciones equivalentes fundamentales:
1. Todos los autovalores de la matriz son estrictamente positivos ($\lambda_j > 0$).
2. El determinante de la matriz es estrictamente positivo ($|\mathbf{A}| > 0$).
3. La matriz es invertible o no singular ($\mathbf{A}^{-1}$ existe).

---

### Cálculo del Determinante de Nuestra Matriz $\mathbf{R}$

Utilizando la expansión de Sarrus o cofactores para la matriz $3 \times 3$:

$$
|\mathbf{R}| = 1\big((1)(1) - (0.5718)^2\big) - 0.7670\big((0.7670)(1) - (0.8771)(0.5718)\big) + 0.8771\big((0.7670)(0.5718) - (0.8771)(1)\big)
$$

Desarrollando los términos intermedios:
1. $(1 - 0.32696) = 0.67304$
2. $-0.7670(0.7670 - 0.50153) = -0.7670(0.26547) \approx -0.20362$
3. $+0.8771(0.43857 - 0.87710) = +0.8771(-0.43853) \approx -0.38463$

Sumando algebraicamente:

$$
|\mathbf{R}| = 0.67304 - 0.20362 - 0.38463 = 0.08479 \approx 0.085
$$

---

## 5. El Significado del Determinante en la Factorizabilidad

El valor numérico de $|\mathbf{R}|$ describe el volumen ocupado por los vectores en el hiperespacio y actúa como un semáforo analítico para el Análisis Factorial:

```
|R| = 1.00                          0 < |R| < 1.00                     |R| = 0.00
------------------------------------------------------------------------------------>
Matriz Identidad (I)               Asociación Adecuada                Matriz Singular
- Variables ortogonales            - Los vectores comparten espacio   - Colinealidad exacta
- r_jk = 0 para todo j != k        - Factorizable                     - R no es invertible
- AFE / AFC NO es viable                                              - Falla el algoritmo
```

| Escenario | Magnitud de $|\mathbf{R}|$ | Geometría Vectorial | Consecuencia en AFE / AFC |
| :--- | :---: | :--- | :--- |
| **Ortogonalidad pura** | $|\mathbf{R}| = 1$ | Vectores perpendiculares entre sí a $90^\circ$. | $\mathbf{R} = \mathbf{I}$. No existe varianza común compartida; el análisis factorial carece de sentido. |
| **Espacio intermedio óptimo** | $0 < |\mathbf{R}| \ll 1$ | Los vectores forman haces angulares cerrados. | Estructura correlacional compartida. Factorizable. (Nuestro valor $|\mathbf{R}| \approx 0.085$ encaja aquí). |
| **Singularidad / Multicolinealidad** | $|\mathbf{R}| \le 0$ | Al menos un vector es combinación lineal exacta de los demás. | El hipervolumen colapsa a 0. La matriz no es invertible; los estimadores por Máxima Verosimilitud (ML) y MCO fallan (división por cero al calcular $\mathbf{R}^{-1}$ o $\mathbf{S}^{-1}$). |

En el siguiente módulo (Módulo 4), veremos cómo la prueba de esfericidad de Bartlett contrasta formalmente la hipótesis nula $H_0: |\mathbf{R}| = 1$ frente a $H_1: |\mathbf{R}| < 1$, y cómo este determinante es el corazón de los algoritmos de estimación factorial.

---

&nbsp;

&nbsp;

---
# Módulo 4: El Puente Hacia AFE y AFC

En los módulos anteriores sentamos los fundamentos analíticos: desde los productos cruzados y la covarianza (Módulo 1), pasando por la estandarización y la correlación como producto interior en $\mathbb{R}^n$ (Módulo 2), hasta la construcción y propiedades espectrales de las matrices $\mathbf{S}$ y $\mathbf{R}$ (Módulo 3). 

En este cuarto módulo cerramos el ciclo uniendo la matriz de asociación con los modelos de **Análisis Factorial Exploratorio (AFE)** y **Análisis Factorial Confirmatorio (AFC)**.

---

## 1. Diagnóstico de Factorizabilidad Previa

Antes de ajustar un modelo factorial, es indispensable comprobar si la matriz $\mathbf{R}$ contiene suficiente covarianza compartida para que la reducción dimensional tenga sentido estadístico.

### A. Prueba de Esfericidad de Bartlett

La prueba de Bartlett contrasta formalmente la hipótesis de que las variables observadas en la población son completamente independientes entre sí:

$$
H_0: \mathbf{P} = \mathbf{I}_p \quad (\text{todas las correlaciones poblacionales } \rho_{jk} = 0 \text{ para } j \ne k)
$$
$$
H_1: \mathbf{P} \ne \mathbf{I}_p
$$

Bajo la hipótesis nula, el determinante poblacional es exactamente la unidad ($|\mathbf{I}_p| = 1$). El estadístico de contraste se basa en la desviación del logaritmo natural del determinante muestral $|\mathbf{R}|$:

$$
\chi^2_{\text{Bartlett}} = -\left( n - 1 - \frac{2p + 5}{6} \right) \ln |\mathbf{R}|
$$

Con grados de libertad:

$$
gl = \frac{p(p - 1)}{2}
$$

* **Criterio de decisión:** Si el valor $p < 0.05$, se rechaza $H_0$. Esto confirma que la matriz no es una matriz identidad y que existen correlaciones no nulas factibles de resumir.
* **Cálculo con los datos del Módulo 3:**  
  Recordando que $n = 5$, $p = 3$, y $|\mathbf{R}| \approx 0.08479$:
  $$gl = \frac{3(2)}{2} = 3$$
  $$\chi^2 = -\left( 5 - 1 - \frac{6 + 5}{6} \right) \ln(0.08479) = -\left( 4 - \frac{11}{6} \right) (-2.4676) = -(2.1667)(-2.4676) \approx 5.346$$

### B. Medida de Adecuación Muestral KMO (Kaiser-Meyer-Olkin)

Mientras Bartlett evalúa la matriz global, el índice KMO compara la magnitud de las **correlaciones de orden cero** frente a las **correlaciones parciales**:

$$
\text{KMO} = \frac{\sum \sum_{j \ne k} r_{jk}^2}{\sum \sum_{j \ne k} r_{jk}^2 + \sum \sum_{j \ne k} a_{jk}^2}
$$

Donde $a_{jk}$ representa la correlación parcial entre el ítem $j$ y el ítem $k$ controlando por todos los demás ítems de la escala. 
* Algebraicamente, los términos $a_{jk}$ provienen de los elementos fuera de la diagonal de la inversa de la matriz de correlaciones:
  $$\mathbf{A} = \mathbf{D}_r \mathbf{R}^{-1} \mathbf{D}_r \quad \text{donde } \mathbf{D}_r = (\operatorname{diag}(\mathbf{R}^{-1}))^{-1/2}$$
* **Interpretación:** Si los ítems comparten factores latentes comunes, la correlación parcial $a_{jk}$ (la correlación residual una vez purgado el efecto común) debería tender a cero. Por ende, la suma de $a_{jk}^2$ es pequeña y $\text{KMO} \to 1.0$.

| Rango KMO | Calidad de la Factorizabilidad |
| :--- | :--- |
| $\text{KMO} \ge 0.90$ | Sobresaliente |
| $0.80 \le \text{KMO} < 0.90$ | Notable / Bueno |
| $0.70 \le \text{KMO} < 0.80$ | Aceptable |
| $0.60 \le \text{KMO} < 0.70$ | Mediocre / Límite inferior |
| $\text{KMO} < 0.50$ | Inadmisible (no procede el AF) |

---

## 2. La Ecuación Fundamental del Análisis Factorial

El modelo del Análisis Factorial postula que cada una de las $p$ variables observadas estandarizadas ($Z_j$) puede descomponerse linealmente en $m$ factores comunes latentes ($\xi_1, \xi_2, \dots, \xi_m$, con $m \ll p$) más un factor único de error ($\delta_j$):

$$
Z_j = \lambda_{j1}\xi_1 + \lambda_{j2}\xi_2 + \dots + \lambda_{jm}\xi_m + \delta_j
$$

En notación matricial compacta:

$$
\mathbf{z} = \boldsymbol{\Lambda} \boldsymbol{\xi} + \boldsymbol{\delta}
$$

Donde:
* $\mathbf{z}$ es el vector $p \times 1$ de variables observadas centradas o estandarizadas.
* $\boldsymbol{\Lambda}$ es la **matriz de cargas factoriales** (*factor loadings*) de dimensión $p \times m$.
* $\boldsymbol{\xi}$ es el vector $m \times 1$ de factores comunes latentes (con media $\mathbf{0}$ y covarianza $\boldsymbol{\Phi}$).
* $\boldsymbol{\delta}$ es el vector $p \times 1$ de errores o factores únicos (con media $\mathbf{0}$ y covarianza $\boldsymbol{\Theta}$).

### Supuestos Clave del Modelo:
1. Factores comunes no correlacionan con los factores únicos: $\operatorname{Cov}(\boldsymbol{\xi}, \boldsymbol{\delta}) = \mathbf{0}$.
2. Los errores o factores únicos no correlacionan entre sí (independencia local): $\boldsymbol{\Theta} = \operatorname{diag}(u_1^2, u_2^2, \dots, u_p^2)$.

---

## 3. Derivación de la Matriz Implicada ($\boldsymbol{\Sigma}$)

El núcleo del AF consiste en reproducir la matriz observada ($\mathbf{S}$ o $\mathbf{R}$) a partir de los parámetros del modelo. La covarianza poblacional implicada $\boldsymbol{\Sigma}(\boldsymbol{\theta})$ se deriva calculando el valor esperado del producto exterior del vector de variables:

$$
\boldsymbol{\Sigma} = E[\mathbf{z}\mathbf{z}^T] = E\left[ (\boldsymbol{\Lambda}\boldsymbol{\xi} + \boldsymbol{\delta})(\boldsymbol{\Lambda}\boldsymbol{\xi} + \boldsymbol{\delta})^T \right]
$$

Aplicando transposición de productos $((AB)^T = B^T A^T)$ y distribuyendo:

$$
\boldsymbol{\Sigma} = E\left[ (\boldsymbol{\Lambda}\boldsymbol{\xi} + \boldsymbol{\delta})(\boldsymbol{\xi}^T\boldsymbol{\Lambda}^T + \boldsymbol{\delta}^T) \right]
$$
$$
\boldsymbol{\Sigma} = E\left[ \boldsymbol{\Lambda}\boldsymbol{\xi}\boldsymbol{\xi}^T\boldsymbol{\Lambda}^T + \boldsymbol{\Lambda}\boldsymbol{\xi}\boldsymbol{\delta}^T + \boldsymbol{\delta}\boldsymbol{\xi}^T\boldsymbol{\Lambda}^T + \boldsymbol{\delta}\boldsymbol{\delta}^T \right]
$$

Dado que el operador de esperanza matemática $E[\cdot]$ es lineal:

$$
\boldsymbol{\Sigma} = \boldsymbol{\Lambda} E[\boldsymbol{\xi}\boldsymbol{\xi}^T] \boldsymbol{\Lambda}^T + \boldsymbol{\Lambda} E[\boldsymbol{\xi}\boldsymbol{\delta}^T] + E[\boldsymbol{\delta}\boldsymbol{\xi}^T] \boldsymbol{\Lambda}^T + E[\boldsymbol{\delta}\boldsymbol{\delta}^T]
$$

Sustituyendo las matrices de covarianzas correspondientes:
* $E[\boldsymbol{\xi}\boldsymbol{\xi}^T] = \boldsymbol{\Phi}$ (matriz de covarianza/correlación entre factores latentes, orden $m \times m$).
* $E[\boldsymbol{\xi}\boldsymbol{\delta}^T] = \mathbf{0}$ y $E[\boldsymbol{\delta}\boldsymbol{\xi}^T] = \mathbf{0}$ (independencia entre factores y errores).
* $E[\boldsymbol{\delta}\boldsymbol{\delta}^T] = \boldsymbol{\Theta}$ (matriz diagonal de unicidades o varianzas de error, orden $p \times p$).

Llegamos a la **Ecuación Fundamental del Análisis Factorial**:

$$
\boldsymbol{\Sigma} = \boldsymbol{\Lambda} \boldsymbol{\Phi} \boldsymbol{\Lambda}^T + \boldsymbol{\Theta}
$$

### Caso Particular: Factores Ortogonales ($\boldsymbol{\Phi} = \mathbf{I}_m$)
Si se asume que los factores latentes no están correlacionados (como en rotaciones Varimax en AFE):

$$
\boldsymbol{\Sigma} = \boldsymbol{\Lambda} \boldsymbol{\Lambda}^T + \boldsymbol{\Theta}
$$

Desarrollando esta expresión elemento por elemento para un par de ítems $j$ y $k$:
* **Diagonal (Varianza del ítem $j$):**
  $$\sigma_{jj} = \sum_{a=1}^m \lambda_{ja}^2 + u_j^2 = h_j^2 + u_j^2$$
  *(Aquí se comprueba la descomposición del Módulo 2: Comunalidad + Unicidad = Varianza total).*
* **Fuera de la diagonal (Covarianza o correlación entre ítem $j$ e ítem $k$):**
  $$\sigma_{jk} = \sum_{a=1}^m \lambda_{ja}\lambda_{ka}$$
  La correlación entre dos variables se reproduce enteramente mediante el producto de sus cargas en los factores compartidos.

---

## 4. Divergencia Estructural: ¿AFE o AFC?

Aunque ambos modelos comparten la misma ecuación matricial fundamental ($\boldsymbol{\Sigma} = \boldsymbol{\Lambda}\boldsymbol{\Phi}\boldsymbol{\Lambda}^T + \boldsymbol{\Theta}$), su concepción epistemológica y sus restricciones algebraicas son opuestas:

```
               MATRIZ OBSERVADA (S o R)
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
       [ AFE ]                           [ AFC ]
  - No impone ceros en Λ            - Fija restricciones estrictas
  - Todas las variables cargan        (λ = 0 en factores ajenos)
    en todos los factores           - Requiere hipótesis a priori
  - Indeterminación de rotación     - Grados de libertad > 0
    (Varimax, Oblimin, etc.)        - Prueba de ajuste global (χ², CFI, RMSEA)
```

| Criterio Comparativo | Análisis Factorial Exploratorio (AFE) | Análisis Factorial Confirmatorio (AFC) |
| :--- | :--- | :--- |
| **Punto de partida** | Ausencia de hipótesis definida sobre la estructura interna. | Hipótesis teórica sustantiva previa bien especificada. |
| **Estructura de $\boldsymbol{\Lambda}$** | Saturación completa: cada ítem tiene una carga estimada en cada factor (matriz completa). | Matriz restringida: la mayoría de los $\lambda_{jk}$ se fijan teóricamente en 0. |
| **Rotación de factores** | Obligatoria para interpretar (ortogonal u oblicua) debido a indeterminación matemática. | No se rota: los factores se identifican fijando una escala (marcador unitario o varianza latente en 1). |
| **Función de discrepancia** | Minimiza residuales para $m$ dimensiones libres. | Contraste de ajuste de sobre-identificación mediante funciones como ML (Máxima Verosimilitud):<br>$F_{\text{ML}} = \ln|\boldsymbol{\Sigma}| - \ln|\mathbf{S}| + \operatorname{tr}(\mathbf{S}\boldsymbol{\Sigma}^{-1}) - p$ |

---

## 5. Criterio de Selección: ¿Cuándo Factorizar $\mathbf{R}$ vs. $\mathbf{S}$?

| Matriz de Entrada | Escenario Metodológico Recomendado | Ventajas y Consecuencias |
| :---: | :--- | :--- |
| **Matriz $\mathbf{R}$**<br>*(Correlaciones)* | • Ítems medidos en escalas distintas (ej. edad en años junto a reactivos Likert de 1 a 5).<br>• Varianzas de los ítems muy dispares.<br>• Práctica estándar en la casi totalidad del **AFE**. | • Neutraliza el impacto de unidades de medida arbitrarias.<br>• Todos los ítems tienen la misma varianza basal ($s^2=1$).<br>• Pérdida de la información relativa a la dispersión original. |
| **Matriz $\mathbf{S}$**<br>*(Covarianzas)* | • Escalas con unidades de medida idénticas y homogéneas.<br>• Análisis de invariancia factorial multigrupo.<br>• Enfoque por defecto en **AFC y Modelos de Ecuaciones Estructurales (SEM)**. | • Preserva las verdaderas magnitudes de varianza del fenómeno.<br>• Permite comparar directamente parámetros métricos ($\lambda$) entre distintas poblaciones o momentos temporales. |

---

## 6. Síntesis Integradora del Trayecto

```
[MÓDULO 1] Covarianza (s_xy) ──> Base del co-movimiento
     │
[MÓDULO 2] Estandarización (z) y Pearson (r_xy = cos θ) ──> Ángulos e invariancia de escala
     │
[MÓDULO 3] Empaquetamiento Matricial (S y R) ──> Determinantes, simetría y espacio hiperdimensional
     │
[MÓDULO 4] Descomposición Factorial: Σ = Λ Φ Λ^T + Θ
     │
     ├──> AFE: Extracción y rotación de Λ en R
     └──> AFC: Contraste formal de hipótesis sobre S o R
```

Con este módulo completamos el mapa matemático completo: desde la desviación elemental de un individuo respecto a la media muestral, hasta la formulación matricial que permite reproducir y contrastar hipótesis estructurales en AFE y AFC.

---

&nbsp;

&nbsp;

---

# FORMULARIO

| **Estadístico** | **Fórmula** | 
| :--- | :--- |
| *Medias muestrales:* | $$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, \quad \bar{Y} = \frac{1}{n}\sum_{i=1}^n Y_i$$ | 
| *Varianza muestral de $X$* | $$s_x^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})(X_i - \bar{X})$$ | 
| *Covarianza muestral entre $X$ e $Y$* (variación conjunta) | $$s_{xy} = \operatorname{Cov}(X,Y) = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})$$ |
| Forma computacional equivalente (reducción de errores por redondeo) | $$s_{xy} = \frac{1}{n-1} \left( \sum_{i=1}^n X_i Y_i - \frac{\sum X_i \sum Y_i}{n} \right)$$ |
| *Puntuaciones Típicas ($z$) | $$z_{xi} = \frac{X_i - \bar{X}}{s_x}$$ // ($\bar{z}_x = 0$) //($s_{z_x}^2 = 1$, $s_{z_x} = 1$) | 
| *Coeficiente de Correlación de Pearson ($r_{xy}$)* | $$r_{xy} = \frac{s_{xy}}{s_x s_y}$$ | 
| *Producto Escalar (Punto)* | $$\mathbf{x}_c \cdot \mathbf{y}_c = \mathbf{x}_c^T \mathbf{y}_c = \sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y}) = (n-1) s_{xy}$$ | 
| *Norma (Longitud) de los Vectores Centrados* | $$\|\mathbf{x}_c\| = \sqrt{\sum_{i=1}^n (X_i - \bar{X})^2} = \sqrt{(n-1) s_x^2} = s_x \sqrt{n-1}$$ | 
| | $$\|\mathbf{y}_c\| = \sqrt{\sum_{i=1}^n (Y_i - \bar{Y})^2} = \sqrt{(n-1) s_y^2} = s_y \sqrt{n-1}$$ | 
| *El Teorema del Coseno del Ángulo ($\cos \theta$) | $$\mathbf{x}_c^T \mathbf{y}_c = \|\mathbf{x}_c\| \|\mathbf{y}_c\| \cos \theta$$ |
| | $$\cos \theta = \frac{s_{xy}}{s_x s_y} = r_{xy}$$ | 
| | |


&nbsp;

&nbsp;

---

Thankyou Lord!