import numpy as np

# Matriz de datos
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

n, p = X.shape

# Vectores de unos
unos_n = np.ones((n, 1))
unos_p = np.ones((p, 1))

# 1. Vector de medias y matriz centrada X_c
x_barra = (1.0 / n) * (X.T @ unos_n)

print(f"1 --- Matriz de Medias --- \n", x_barra, "\n")

# 2. Matriz Centrada
X_c = X - unos_n @ x_barra.T
print(f"2 --- Matriz Centrada --- \n", X_c, "\n")

# 3. Matriz de covarianzas S
S = np.round((1.0 / (n - 1)) * (X_c.T @ X_c), decimals= 4)

print(f"3 --- Matriz de Covarianzas S --- \n", S, "\n")

# 4. Componentes matriciales del Alfa de Cronbach
traza_S = np.trace(S)                     # Suma de varianzas individuales
traza_S = np.round(traza_S, decimals= 4)

print(f"4 --- Trazas S --- \n", traza_S, "\n")

# 5. Varianza de la puntuación total
var_total = unos_p.T @ S @ unos_p

print(f"🍅 5 --- Varianza de la Puntuación Total --- \n", var_total, "\n")

# 6. Coeficiente Alfa
alfa = (p / (p - 1.0)) * (1.0 - (traza_S / var_total))

print(f"6 --- Coeficiente Alfa de Cronbach --- \n", alfa, "\n"*2)

def interpretar_alfa_cronbach(alfa: float) -> dict:
    """
    Evalúa e interpreta el coeficiente Alfa de Cronbach según el baremo clásico
    psicométrico de George & Mallery y Nunnally.
    """
    if alfa < 0:
        calificacion = "Inadmisible / Error Estructural"
        descripcion = (
            "Alfa negativo. Indica covarianzas netas negativas entre ítems. "
            "Revisar urgentemente ítems redactados en sentido inverso que no hayan sido recodificados."
        )
    elif alfa >= 0.95:
        calificacion = "Excelente (Precaución por Redundancia)"
        descripcion = (
            "Consistencia interna extremadamente alta. Adecuado para decisiones críticas e individuales, "
            "pero puede señalar redundancia o contenido repetitivo entre reactivos."
        )
    elif alfa >= 0.90:
        calificacion = "Excelente"
        descripcion = (
            "Consistencia interna muy alta. Estructura adecuada para diagnósticos individuales "
            "o instrumentos estandarizados de alta precisión."
        )
    elif alfa >= 0.80:
        calificacion = "Buena"
        descripcion = "Nivel óptimo y recomendado para la mayoría de investigaciones aplicadas."
    elif alfa >= 0.70:
        calificacion = "Aceptable"
        descripcion = "Umbral estándar mínimo aceptado en ciencias sociales y de la conducta."
    elif alfa >= 0.60:
        calificacion = "Cuestionable"
        descripcion = (
            "Solo admisible en fases exploratorias tempranas o en escalas de muy pocos ítems (p <= 3)."
        )
    elif alfa >= 0.50:
        calificacion = "Pobre"
        descripcion = (
            "Consistencia baja. Requiere revisar o eliminar ítems que presentan correlaciones bajas con el total."
        )
    else:
        calificacion = "Inaceptable"
        descripcion = "Nivel de error de medición inaceptable. Los ítems no miden un constructo común."

    return {
        "alfa": round(alfa, 4),
        "calificacion": calificacion,
        "descripcion": descripcion
    }


# --- Ejemplo de integración con el cálculo matricial ---
if __name__ == "__main__":
    # Supongamos el resultado obtenido en el ejercicio anterior
    alfa_calculado = alfa.item()    #.item() convierte el resultado matricial a número flotante

    resultado = interpretar_alfa_cronbach(alfa_calculado)

    print("=" * 120)
    print(f"Alfa de Cronbach: {resultado['alfa']}")
    print(f"Calificación:     {resultado['calificacion']}")
    print(f"Interpretación:   {resultado['descripcion']}")
    print("=" * 120, "\n"*3)