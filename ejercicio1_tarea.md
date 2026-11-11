### Ejercicio: Consistencia Interna y Alfa de Cronbach Matricial

Diseñamos una escala de evaluación de **Autoeficacia Tecnológica** compuesta por $p = 4$ ítems medidos en escala Likert de 1 a 5 puntos, aplicada a una muestra de $n = 8$ docentes.

---

### 1. Datos de Entrada para Python

Copia y pega directamente esta matriz $\mathbf{X}$ ($8 \times 4$):

```python
import numpy as np

# Matriz de datos X: n = 8 individuos (filas), p = 4 ítems (columnas)
X = np.array([
    [4, 4, 3, 4],
    [5, 4, 4, 5],
    [3, 3, 2, 3],
    [2, 2, 2, 1],
    [4, 5, 4, 4],
    [3, 2, 3, 3],
    [5, 5, 5, 4],
    [2, 3, 1, 2]
], dtype=float)

```

---

### 2. Fundamentación y Fórmulas Matriciales

La fórmula clásica psicométrica del Alfa de Cronbach es:

$$\alpha = \frac{p}{p - 1} \left( 1 - \frac{\sum_{j=1}^p s_j^2}{s_{total}^2} \right)$$

En álgebra matricial, todas estas cantidades se derivan de forma compacta a partir de la **matriz de varianzas-covarianzas muestral $\mathbf{S}$**:

1. **Centrado de la matriz $\mathbf{X}$:**

$$\bar{\mathbf{x}} = \frac{1}{n} \mathbf{X}^T \mathbf{1}_n, \quad \mathbf{X}_c = \mathbf{X} - \mathbf{1}_n \bar{\mathbf{x}}^T$$





2. **Matriz de covarianzas muestral $\mathbf{S}$ ($p \times p$):**

$$\mathbf{S} = \frac{1}{n - 1} \mathbf{X}_c^T \mathbf{X}_c$$





3. **Suma de las varianzas de los ítems individuales:**
Corresponde exactamente a la **traza** de $\mathbf{S}$ (suma de su diagonal principal):

$$\sum_{j=1}^p s_j^2 = \operatorname{tr}(\mathbf{S}) = \sum_{j=1}^p s_{jj}$$


4. **Varianza de la puntuación total del test ($s_{total}^2$):**
Si la puntuación total de cada sujeto es la suma de sus ítems $Y_i = \sum_{j=1}^p X_{ij}$, la varianza del total es la suma de todos los elementos de la matriz $\mathbf{S}$ (varianzas más covarianzas). Matricialmente se calcula mediante la forma cuadrática con el vector de unos $\mathbf{1}_p$:

$$s_{total}^2 = \mathbf{1}_p^T \mathbf{S} \, \mathbf{1}_p$$


5. **Formulación matricial del Alfa de Cronbach:**

$$\alpha = \frac{p}{p - 1} \left( 1 - \frac{\operatorname{tr}(\mathbf{S})}{\mathbf{1}_p^T \mathbf{S} \, \mathbf{1}_p} \right)$$



---

### 3. Resolución Numérica Paso a Paso

#### Paso 1: Vector de medias muestrales ($\bar{\mathbf{x}}$)

Con $n = 8$:

* Suma por columnas: $\mathbf{X}^T \mathbf{1}_8 = [28, \; 28, \; 24, \; 26]^T$
* Medias:

$$\bar{\mathbf{x}} = \frac{1}{8} \begin{pmatrix} 28 \\ 28 \\ 24 \\ 26 \end{pmatrix} = \begin{pmatrix} 3.50 \\ 3.50 \\ 3.00 \\ 3.25 \end{pmatrix}$$



#### Paso 2: Matriz centrada $\mathbf{X}_c = \mathbf{X} - \mathbf{1}_8 \bar{\mathbf{x}}^T$ ($8 \times 4$)



Restando el vector de medias a cada fila:

$$\mathbf{X}_c = \begin{pmatrix} +0.50 & +0.50 &  0.00 & +0.75 \\ +1.50 & +0.50 & +1.00 & +1.75 \\ -0.50 & -0.50 & -1.00 & -0.25 \\ -1.50 & -1.50 & -1.00 & -2.25 \\ +0.50 & +1.50 & +1.00 & +0.75 \\ -0.50 & -1.50 &  0.00 & -0.25 \\ +1.50 & +1.50 & +2.00 & +0.75 \\ -1.50 & -0.50 & -2.00 & -1.25 \end{pmatrix}$$

#### Paso 3: Matriz de Varianzas y Covarianzas $\mathbf{S} = \frac{1}{7} \mathbf{X}_c^T \mathbf{X}_c$

Calculamos la suma de productos cruzados $\mathbf{X}_c^T \mathbf{X}_c$:

$$\mathbf{X}_c^T \mathbf{X}_c = \begin{pmatrix} 10.00 &  8.00 &  8.00 &  9.50 \\ 8.00 & 10.00 &  7.00 &  8.50 \\ 8.00 &  7.00 & 10.00 &  7.50 \\ 9.50 &  8.50 &  7.50 & 11.50 \end{pmatrix}$$

Dividiendo por $n - 1 = 7$:

$$\mathbf{S} = \begin{pmatrix} 1.4286 & 1.1429 & 1.1429 & 1.3571 \\ 1.1429 & 1.4286 & 1.0000 & 1.2143 \\ 1.1429 & 1.0000 & 1.4286 & 1.0714 \\ 1.3571 & 1.2143 & 1.0714 & 1.6429 \end{pmatrix}$$

#### Paso 4: Traza de $\mathbf{S}$ (Suma de varianzas individuales)

Tomamos la diagonal principal de $\mathbf{S}$:


$$\operatorname{tr}(\mathbf{S}) = 1.4286 + 1.4286 + 1.4286 + 1.6429 = 5.9286$$


*(Valor fraccionario exacto: $\frac{10 + 10 + 10 + 11.5}{7} = \frac{41.5}{7} \approx 5.92857$)*

#### Paso 5: Varianza de la puntuación total ($\mathbf{1}_p^T \mathbf{S} \, \mathbf{1}_p$)

Vector columna de unos para $p = 4$: $\mathbf{1}_4 = [1, 1, 1, 1]^T$.
Multiplicamos primero $\mathbf{S} \mathbf{1}_4$ (suma de cada fila de $\mathbf{S}$):


$$\mathbf{S} \mathbf{1}_4 = \begin{pmatrix} 1.4286 + 1.1429 + 1.1429 + 1.3571 \\ 1.1429 + 1.4286 + 1.0000 + 1.2143 \\ 1.1429 + 1.0000 + 1.4286 + 1.0714 \\ 1.3571 + 1.2143 + 1.0714 + 1.6429 \end{pmatrix} = \begin{pmatrix} 5.0714 \\ 4.7857 \\ 4.6429 \\ 5.2857 \end{pmatrix}$$

Ahora premultiplicamos por $\mathbf{1}_4^T$ (sumamos los elementos resultantes):


$$\mathbf{1}_4^T \mathbf{S} \, \mathbf{1}_4 = 5.0714 + 4.7857 + 4.6429 + 5.2857 = 19.7857$$


*(Valor fraccionario exacto: $\frac{138.5}{7} \approx 19.78571$)*

#### Paso 6: Cálculo del Coeficiente Alfa de Cronbach ($\alpha$)

Sustituimos $p = 4$, $\operatorname{tr}(\mathbf{S}) = 5.9286$ y $s_{total}^2 = 19.7857$:

$$\alpha = \frac{4}{4 - 1} \left( 1 - \frac{5.9286}{19.7857} \right)$$

$$\alpha = \frac{4}{3} \left( 1 - 0.29964 \right)$$

$$\alpha = \frac{4}{3} \times 0.70036 \approx 0.9338$$

**Interpretación psicométrica:** Un coeficiente de $\alpha \approx 0.934$ indica una consistencia interna excelente; los 4 ítems covarían intensamente entre sí y evalúan de manera armónica el mismo constructo.

---

Se pide:

- Preparar su computadora.

- Realizar los cálculos en Python, utilice fórmulas matriciales.

---

❤️ Thankyou Lord!