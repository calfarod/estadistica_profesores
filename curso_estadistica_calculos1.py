import numpy as np

# 1. Definición de la matriz de datos X (n = 5 sujetos, p = 3 variables)
X = np.array([
    [2, 1, 3],
    [3, 2, 3],
    [2, 3, 2],
    [4, 4, 5],
    [4, 4, 4]
], dtype=float)

# Visualización ordenada de los resultados
print("1 --- MATRIZ ORIGINAL X (5x3) ---")
print(X)

# Dimensiones: n filas (sujetos), p columnas (variables)
n, p = X.shape

# 2. Definición del vector columna de unos 1_n de dimensión (n x 1)
unos_n = np.ones((n, 1))

print("\n2 --- VECTOR COLUMNA DE UNOS 1_n (5x1) ---")
print(unos_n)

# 3. Trasponer la matriz X -> X^T tiene dimensión (p x n)
X_transpuesta = X.T

print("\n3 --- MATRIZ TRASPUESTA X^T (3x5) ---")
print(X_transpuesta)

# 4. Multiplicación de matrices: (X^T @ 1_n) genera la suma de cada columna (p x 1)
suma_columnas = X_transpuesta @ unos_n

print("\n4 --- PRODUCTO X^T @ 1_n (sumas_columnas) ---")
print(suma_columnas)

# 5. Multiplicación por el escalar (1/n) para obtener el vector de medias
x_barra = (1.0 / n) * suma_columnas

print("\n5 --- VECTOR DE MEDIAS: x_barra = (1/n) * X^T @ 1_n ---")
print(x_barra)

# 6. Determinación de la Matriz de Datos Centrados X_c
X_c = X - unos_n @ x_barra.T

print("\n6 --- MATRIZ DE DATOS CENTRADOS X_c = X - unos_n @ x_barra.T ---")
print(X_c)

# 7. Matriz de Varianzas y Covarianzas S
escalar = 1 / (n-1)
S = escalar * X_c.T @ X_c

print("\n7 --- MATRIZ DE VARIANZAS Y COVARIANZAS S")
print(S)

# 8. Varianzas (Es la diagonal de la matriz S)
varianzas = np.diag(S)

print("\n8 --- Varianzas (varianzas) ---")
print(varianzas)

# 9. Desviaciones Estándar 
desv_std = np.sqrt(varianzas)
D_s = np.diag(desv_std)

print("\n9 --- Desviaciones Estándar D_s ---")
print(np.round(D_s, decimals= 5))

# 10. Inverso de Matriz Desviaciones Estándar
D_s_inv = np.linalg.inv(D_s)

print("\n10 --- Matriz de Desviaciones Estándar Invertida ---")
print(np.round(D_s_inv, decimals= 4))

# 11. Matriz de Correlaciones de Pearson
R = D_s_inv @ S @ D_s_inv

print("\n11 --- MATRIZ DE CORRELACIONES DE PEARSON (R) ---")
print(np.round(R, decimals= 4))