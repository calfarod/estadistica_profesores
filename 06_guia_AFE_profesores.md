# Guía Metodológica y Aplicada: Análisis Factorial Exploratorio (AFE) en Jamovi
## Validación Psicométrica del Constructo "Potencial Netificador"

---

## 1. Fundamentos Teóricos y Modelo Matemático del AFE

El **Análisis Factorial Exploratorio (AFE)** es una técnica estadística multivariada de interdependencia cuyo propósito es identificar la estructura latente que subyace a un conjunto de variables observables (ítems o reactivos), reduciendo la dimensionalidad sin imponer restricciones restrictivas a priori.

### 1.1 Modelo Matemático Fundamental
El modelo asume que cada variable observada estandarizada $X_i$ ($i = 1, \dots, p$) es una combinación lineal de $m$ factores comunes latentes $F_j$ ($j = 1, \dots, m$, donde $m < p$) más un factor único o error específico $e_i$:

$$X_i = \lambda_{i1} F_1 + \lambda_{i2} F_2 + \dots + \lambda_{im} F_m + e_i$$

Donde:
* $X_i$: Variable observada $i$ estandarizada ($\mu = 0, \sigma^2 = 1$).
* $\lambda_{ij}$: Carga factorial (*factor loading*) del ítem $i$ en el factor latente $j$. Representa la correlación (o coeficiente de regresión estandarizado) entre el ítem y el factor.
* $F_j$: Factor común latente no observable.
* $e_i$: Error de medición y especificidad única del ítem ($Var(e_i) = u_i^2$, denominada *unicidad* o *uniqueness*).

### 1.2 Descomposición de la Varianza: Comunalidad vs. Unicidad
Dado que las variables están estandarizadas, la varianza total de cada variable ($Var(X_i) = 1$) se descompone en:

$$Var(X_i) = h_i^2 + u_i^2 = 1$$

* **Comunalidad ($h_i^2$):** Proporción de la varianza del ítem explicada por el conjunto de los factores comunes retenidos:
  $$h_i^2 = \sum_{j=1}^{m} \lambda_{ij}^2 \quad \text{(en caso ortogonal)}$$
  *Criterio práctico:* Se esperan valores de $h_i^2 \ge 0.40$ (idealmente $\ge 0.50$). Un $h_i^2 < 0.30$ indica que el ítem comparte poca varianza con el modelo y es candidato a eliminación.
* **Unicidad ($u_i^2$):** Varianza residual no capturada por los factores comunes ($u_i^2 = 1 - h_i^2$).

---

## 2. Supuestos Previos y Pruebas de Adecuación Muestral

Antes de extraer factores, se debe verificar rigurosamente si la matriz de correlaciones de los datos empíricos ($R$) es factorizable.

### 2.1 Tamaño Muestral ($N$)
* **Criterio metodológico:** Ratio mínima de $10:1$ sujetos por ítem observable.
* **Aplicación al caso:** Con $p = 15$ reactivos (`IDS_1` a `PACH_3`), el umbral mínimo es $N = 150$. Con la muestra generada de $N = 800$ (o submuestras comunitarias de $n = 200$), se cumple con holgura ($N/p = 53.3:1$), garantizando estimaciones de cargas estables y errores estándar reducidos.

### 2.2 Medida de Adecuación Muestral Kaiser-Meyer-Olkin (KMO)
El índice KMO compara la magnitud de los coeficientes de correlación observados ($r_{ij}$) frente a la magnitud de los coeficientes de correlación parcial ($a_{ij}$):

$$KMO = \frac{\sum_{i \neq j} \sum r_{ij}^2}{\sum_{i \neq j} \sum r_{ij}^2 + \sum_{i \neq j} \sum a_{ij}^2}$$

Donde $a_{ij}$ es la correlación parcial entre los ítems $i$ y $j$ controlando el efecto de todos los demás reactivos.

* **Interpretación:**
  * Si los ítems comparten factores latentes, las correlaciones parciales $a_{ij}$ tenderán a cero, y el KMO se aproximará a $1.0$.
  * **Punto de corte adoptado:** $KMO \ge 0.80$ (Meritorio / Excelente).
  * Jamovi también reporta el **KMO individual (MSA - Measure of Sampling Adequacy)** por ítem en la diagonal anti-imagen. Cualquier ítem con $MSA_i < 0.60$ debe ser revisado o descartado.

### 2.3 Test de Esfericidad de Bartlett
Contrasta la hipótesis nula ($H_0$) de que la matriz de correlación poblacional es una matriz de identidad ($R = I$), lo que indicaría que las variables son ortogonales e independientes entre sí:

$$H_0: R = I \quad \text{vs.} \quad H_1: R \neq I$$

El estadístico de prueba aproximado sigue una distribución $\chi^2$:

$$\chi^2 = - \left( N - 1 - \frac{2p + 5}{6} \right) \cdot \ln |R|$$

Con grados de libertad:
$$gl = \frac{p(p - 1)}{2}$$

* **Criterio:** Rechazar $H_0$ con un valor $p < 0.001$. Confirma correlaciones no nulas y habilita la factorización.

---

## 3. Métodos de Extracción y Métodos de Rotación

### 3.1 Método de Extracción: Ejes Principales vs. Máxima Verosimilitud
* **Factorización de Ejes Principales (Principal Axis Factoring - PAF):**
  * *Mecanismo:* Sustituye los unos de la diagonal principal de la matriz $R$ por estimaciones iniciales de las comunalidades (comúnmente el $R^2$ de la regresión múltiple de cada ítem sobre los demás). Itera hasta que las comunalidades convergen.
  * *Ventaja:* No asume distribución normal multivariada estricta; es robusto frente a distribuciones ordinales Likert con asimetría moderada.
* **Máxima Verosimilitud (Maximum Likelihood - ML):**
  * *Mecanismo:* Maximiza la función de verosimilitud de la matriz de covarianzas muestral.
  * *Ventaja:* Ofrece bondad de ajuste estadística formal ($\chi^2$). Requiere normalidad multivariada.

> **Configuración recomendada para Jamovi:** Seleccionar **Principal Axis Factoring** (PAF) o **Minimum Residuals** (MinRes) como método de estimación primaria.

### 3.2 Rotación Factorial: Rotación Oblicua (Promax / Direct Oblimin)
La solución inicial extrae factores que maximizan la varianza explicada global, pero las cargas no suelen presentar significado teórico interpretable. La rotación busca la **estructura simple de Thurstone**:
1. Cada factor debe tener cargas elevadas en pocos reactivos.
2. Cada reactivo debe saturar fuertemente en un único factor.

* **¿Por qué rotación oblicua (Promax u Oblimin) y no ortogonal (Varimax)?**
  * La rotación ortogonal fuerza a que los factores tengan correlación cero entre sí ($r = 0$).
  * En ciencias sociales y organizacionales, las dimensiones de un mismo constructo (como *Cohesión Axiológica* y *Agencia Colectiva*) covarían naturalmente ($r \neq 0$).
  * La rotación oblicua permite estimar libremente la matriz de correlación entre factores ($\Phi$). Si la correlación real resultara ser nula, la solución matemática convergería automáticamente a un esquema cuasi-ortogonal.
* **Lectura de Matrices en Rotación Oblicua:**
  * **Matriz de Patrón (*Pattern Matrix*):** Coeficientes de regresión estandarizados directos de cada factor sobre el ítem, controlando los demás factores. **Es la matriz principal para interpretar y definir la pertenencia del ítem.**
  * **Matriz de Estructura (*Structure Matrix*):** Correlaciones bivariadas simples entre ítems y factores (incluye varianza compartida debida a la correlación entre factores).
  * **Matriz de Correlación Interfactorial:** Grado de asociación entre los factores identificados.

---

## 4. Criterios de Retención de Factores

Jamovi permite seleccionar cuántos factores extraer. La decisión debe basarse en la triangulación de tres criterios:

1. **Criterio de Kaiser (Autovalores $\lambda > 1$):**
   * Retiene factores cuya varianza explicada supere la varianza de un solo ítem estandarizado ($\lambda_j > 1.0$).
   * *Limitación:* Tiende a sobreestimar el número de factores en muestras grandes o con muchos ítems.
2. **Análisis Paralelo de Horn (*Parallel Analysis*):**
   * Es el estándar empírico de mayor rigor psicométrico.
   * *Procedimiento:* Simula múltiples matrices de datos aleatorios no correlacionados con el mismo número de sujetos y variables. Retiene únicamente aquellos factores empíricos cuyos autovalores superen el percentil 95 de los autovalores generados por azar.
3. **Poder Predictivo Teórico (5 Dimensiones):**
   * En este modelo, el objetivo confirmatorio previo es evaluar si los 15 reactivos convergen en 5 factores correspondientes a: `IDS`, `CAR`, `ACA`, `CITE` y `PAHC`.

---

## 5. Procedimiento Paso a Paso en Jamovi

### Paso 1: Carga y Preparación de Datos
1. Abre **Jamovi** y haz clic en el menú superior izquierdo $\rightarrow$ `Open` $\rightarrow$ `Browse`.
2. Carga el archivo `simulacion_potencial_netificador_docentes.csv`.
3. Ve a la pestaña **Data**. Verifica que las 15 variables de interés (`IDS_1` a `PACH_3`) tengan asignado el tipo de medida **Continuous** o **Ordinal** con ícono de regla/barras.

### Paso 2: Configuración del Módulo AFE
1. En la barra de herramientas superior, haz clic en **Analyses** $\rightarrow$ **Factor** $\rightarrow$ **Exploratory Factor Analysis**.
2. En el panel izquierdo, selecciona los 15 reactivos (`IDS_1`, `IDS_2`, `IDS_3`, `CAR_1`, `CAR_2`, `CAR_3`, `ACA_1`, `ACA_2`, `ACA_3`, `CITE_1`, `CITE_2`, `CITE_3`, `PAHC_1`, `PAHC_2`, `PACH_3`) y desplázalos a la casilla **Variables**.

### Paso 3: Selección de Parámetros de Extracción y Rotación
1. **Extraction:**
   * Selecciona `Principal axis` (o `Minimum residuals`).
2. **Rotation:**
   * Selecciona `Oblimin` (o `Promax`).
3. **Number of Factors:**
   * Marca primero `Parallel analysis` (para evaluar si el criterio analítico sugiere 5 factores de manera espontánea).
   * Para contrastar de forma fija la teoría de 5 factores, marca `Based on eigenvalue` o fija `Manual` en `5`.

### Paso 4: Activación de Pruebas y Opciones de Visualización
1. Despliega la sección **Assumption Checks**:
   * Marca `KMO measure of sampling adequacy`.
   * Marca `Bartlett's test of sphericity`.
2. Despliega la sección **Factor Loadings**:
   * Marca `Sort loadings by size` (ordena visualmente los ítems por magnitud de carga para facilitar la lectura).
   * En `Hide loadings below`, escribe `0.30` (oculta cargas marginales y resalta las cargas principales y cruzadas).
3. Despliega **Additional Output**:
   * Marca `Factor correlations` (para ver la correlación entre las dimensiones latentes).
   * Marca `Initial eigenvalues` y `Scree plot` (gráfico de sedimentación).

---

## 6. Guía de Lectura e Interpretación de Salidas (Outputs)

### 6.1 Tabla: "Assumption Checks"
```text
Assumption Checks
─────────────────────────────────────────────────────────────
                            Stat     df     p
─────────────────────────────────────────────────────────────
  Bartlett's Test of Sphericity    XXXX.XX   105    < .001
  KMO Measure of Sampling Adequacy   0.88
─────────────────────────────────────────────────────────────
```
* **Lectura:**
  * **Bartlett ($p < 0.001$):** Se descarta que las variables no tengan relación entre sí. Matriz adecuada.
  * **KMO Global ($\ge 0.80$):** Indica que las correlaciones parciales son pequeñas; las respuestas están determinadas por variables latentes compartidas.

### 6.2 Gráfico de Sedimentación (Scree Plot) y Análisis Paralelo
* El gráfico muestra una curva descendente de autovalores.
* **Línea continua (Datos empíricos) vs. Línea discontinua (Simulación de azar):**
* El número de factores a retener corresponde a los puntos empíricos que se sitúan **estrictamente por encima** de la línea de datos aleatorios generada por el análisis paralelo.

### 6.3 Tabla: "Factor Loadings" (Matriz de Patrón Rotada)
Esta es la salida central del análisis. Presenta las cargas factoriales estandarizadas ($\lambda$):

```text
Factor Loadings
─────────────────────────────────────────────────────────────────────────────
             Factor 1    Factor 2    Factor 3    Factor 4    Factor 5    Uniqueness
─────────────────────────────────────────────────────────────────────────────
  IDS_1        0.84                                                        0.28
  IDS_2        0.79                                                        0.35
  IDS_3        0.75                                                        0.41
  CAR_1                    0.86                                            0.24
  CAR_2                    0.81                                            0.31
  CAR_3                    0.77                                            0.38
  ACA_1                                0.80                                0.33
  ACA_2                                0.76                                0.39
  ACA_3                                0.72                                0.44
  CITE_1                                           0.85                    0.26
  CITE_2                                           0.82                    0.30
  CITE_3                                           0.74                    0.42
  PAHC_1                                                       0.88        0.21
  PAHC_2                                                       0.83        0.29
  PACH_3                                                       0.79        0.34
─────────────────────────────────────────────────────────────────────────────
Nota: Cargas factoriales menores a 0.30 están ocultas. Rotación Oblimin.
```

#### Reglas de Decisión Psicométrica:
1. **Saturación Principal Satisfactoria:**
   * Cada reactivo debe presentar una carga primaria $\lambda_{ij} \ge 0.50$ (en muestras grandes, cargas $\ge 0.40$ son aceptables, pero $\ge 0.70$ denota excelente representatividad del constructo).
2. **Cargas Cruzadas (*Cross-loadings*):**
   * Un ítem presenta carga cruzada si satura en un factor secundario con $\lambda \ge 0.30$.
   * Si la diferencia entre la carga primaria y la secundaria es inferior a $0.20$, el ítem es ambiguo y debe reformularse o removerse.
3. **Unicidad (*Uniqueness*):**
   * Refleja la varianza no explicada ($u_i^2$). Si $u_i^2 > 0.60$ (comunalidad $h_i^2 < 0.40$), el ítem aporta escaso valor al factor.

### 6.4 Tabla: "Factor Correlations"
Muestra la correlación de Pearson entre los 5 factores latentes ($F_1$ a $F_5$).
* Coeficientes moderados ($0.20 \le r \le 0.60$) respaldan la teoría de que son componentes complementarios de un meta-constructo superior (**Netificación**), justificando el posterior Análisis Factorial Confirmatorio (AFC) de segundo orden.
* Correlaciones extremadamente altas ($r > 0.85$) indicarían redundancia factorial (colinealidad de constructos), sugiriendo que dos factores deberían fusionarse.

---

## 7. Protocolo de Diagnóstico por Comunidad (Segmentación de Terreno)

Una vez dominado el procedimiento general, Jamovi permite evaluar cómo se comporta la estructura factorial en cada una de las 4 comunidades docentes simuladas:

1. Ve a la pestaña **Data** $\rightarrow$ botón **Filters**.
2. Escribe una regla lógica para aislar una comunidad, por ejemplo:
   $$\text{comunidad} == \text{"Profesores de Iquique"}$$
3. Revisa la salida del AFE para esa submuestra:
   * **Iquique (Autopoiética):** Promedios altos en todos los factores, comunalidades consistentes y estructura de 5 dimensiones bien demarcada.
   * **Arica (Retórica):** Las dimensiones `IDS` y `CAR` mostrarán medias altas ($> 4.0$), mientras que los ítems de `CITE` y `PAHC` reportarán medias deprimidas ($< 2.5$).
   * **Alto Hospicio (Inerte):** Puntuaciones medias sistemáticamente bajas en todos los reactivos.
   * **Antofagasta (Corporativa):** Medias elevadas en `ACA`, `CITE` y `PAHC`, con medias bajas o indiferentes en `IDS` y `CAR`.

Este contraste confirmará si los reactivos discriminan adecuadamente entre grupos con distinto grado de maduración comunitaria.