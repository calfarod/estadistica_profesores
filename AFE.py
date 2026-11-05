import numpy as np
import pandas as pd

# Definir una mini matriz de datos simulada de 6 sujetos y 4 variables (2 de una dimensión simbólica, 2 de instrumental)
# Para ilustrar el cálculo manual paso a paso con números exactos y verificados
data = np.array([
    [5, 4, 2, 1],
    [4, 5, 1, 2],
    [5, 5, 2, 2],
    [2, 1, 4, 5],
    [1, 2, 5, 4],
    [2, 2, 5, 5]
])

print(data)

df_toy = pd.DataFrame(data, columns=['X1', 'X2', 'X3', 'X4'])
means = df_toy.mean()
stds = df_toy.std(ddof=1)
Z = (df_toy - means) / stds
R = df_toy.corr()

print("Medias:\n", means)
print("Desv Est:\n", stds)
print("Matriz Z:\n", Z.round(3))
print("Matriz R:\n", R.round(3))
print("\n", 32*"=")

# 3. Cálculo matricial de R: (1 / (N - 1)) * (Z.T @ Z)
N = len(df_toy)  # Número de observaciones (N = 6)
R_matricial = (1 / (N - 1)) * (Z.T @ Z)
print("Matriz R calculada matricialmente:")
print("", 32*"=")
print("R_matricial: \n", R_matricial.round(3))

# # Autovalores y autovectores de R
# eigenvalues, eigenvectors = np.linalg.eig(R)
# # Ordenar
# idx = eigenvalues.argsort()[::-1]
# eigenvalues = eigenvalues[idx]
# eigenvectors = eigenvectors[:, idx]

# print("Autovalores:", eigenvalues.round(3))
# print("Autovectores:\n", eigenvectors.round(3))

# # Cargas iniciales L = V * sqrt(Lambda)
# L = eigenvectors[:, :2] @ np.diag(np.sqrt(eigenvalues[:2]))
# print("Cargas iniciales (2 factores):\n", pd.DataFrame(L, index=['X1','X2','X3','X4'], columns=['F1','F2']).round(3))