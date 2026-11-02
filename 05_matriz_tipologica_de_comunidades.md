# Matriz Tipológica de Comunidades

En este apartado se analiza el proceso para generar los datos, y la tipología dispuestas en una matríz.

### Generando Datos

```python
import numpy as np
import pandas as pd

# Fijar semilla para reproducibilidad
np.random.seed(42)

# Configuración del diseño muestral
# n = 200 por comunidad (cumple n >= 150 para AFE/AFC por subgrupo y total N = 800)
n_per_comm = 200

# Cuadrantes asignados a cada comuna:
# 1. Profesores de Iquique: Cuadrante I - Autopoiética (Alto Simbólico, Alto Instrumental)
# 2. Profesores de Arica: Cuadrante II - Retórica (Alto Simbólico, Bajo Instrumental)
# 3. Profesores de Alto Hospicio: Cuadrante III - Inerte / Atomizada (Bajo Simbólico, Bajo Instrumental)
# 4. Profesores de Antofagasta: Cuadrante IV - Corporativa / Transaccional (Bajo Simbólico, Alto Instrumental)

# Los reactivos son 15:
# IDS: IDS_1, IDS_2, IDS_3
# CAR: CAR_1, CAR_2, CAR_3
# ACA: ACA_1, ACA_2, ACA_3
# CITE: CITE_1, CITE_2, CITE_3
# PAHC: PAHC_1, PAHC_2, PAHC_3

communities = [
    {
        "name": "Profesores de Iquique",
        "cuadrante": "Cuadrante I - Autopoiética",
        "target_means": {
            "IDS": 4.3, "CAR": 4.4, "ACA": 4.1, "CITE": 3.8, "PAHC": 4.0
        }
    },
    {
        "name": "Profesores de Arica",
        "cuadrante": "Cuadrante II - Retórica",
        "target_means": {
            "IDS": 4.2, "CAR": 4.3, "ACA": 2.5, "CITE": 2.2, "PAHC": 1.9
        }
    },
    {
        "name": "Profesores de Alto_Hospicio",
        "cuadrante": "Cuadrante III - Inerte",
        "target_means": {
            "IDS": 2.4, "CAR": 2.5, "ACA": 2.3, "CITE": 2.1, "PAHC": 1.8
        }
    },
    {
        "name": "Profesores de Antofagasta",
        "cuadrante": "Cuadrante IV - Corporativa",
        "target_means": {
            "IDS": 2.5, "CAR": 2.6, "ACA": 3.9, "CITE": 3.8, "PAHC": 3.7
        }
    }
]

items_dict = {
    "IDS": ["IDS_1", "IDS_2", "IDS_3"],
    "CAR": ["CAR_1", "CAR_2", "CAR_3"],
    "ACA": ["ACA_1", "ACA_2", "ACA_3"],
    "CITE": ["CITE_1", "CITE_2", "CITE_3"],
    "PAHC": ["PAHC_1", "PAHC_2", "PAHC_3"]
}

all_rows = []
subject_id = 1

for comm in communities:
    comm_name = comm["name"]
    cuad = comm["cuadrante"]
    t_means = comm["target_means"]
    
    for _ in range(n_per_comm):
        row = {
            "id_sujeto": f"DOC_{subject_id:04d}",
            "comunidad": comm_name,
            "cuadrante_teorico": cuad
        }
        
        # Generamos valores continuos latentes correlacionados por factor con ruido, luego discretizamos a Likert 1-5
        for dim, items in items_dict.items():
            base_mean = t_means[dim]
            # Variabilidad individual en la dimensión latente
            latent_score = np.random.normal(loc=base_mean, scale=0.55)
            for item in items:
                # Carga factorial + error específico del ítem
                item_val_cont = latent_score + np.random.normal(loc=0, scale=0.45)
                # Redondeo y acotamiento a escala Likert estricta de 5 puntos (1 a 5)
                item_val_likert = int(np.clip(np.round(item_val_cont), 1, 5))
                row[item] = item_val_likert
                
        all_rows.append(row)
        subject_id += 1

df = pd.DataFrame(all_rows)

# Renombrar columna solicitada con el typo exacto o estándar
# En la instrucción: "PAHC_1, PAHC_2, PACH_3" -> incluiremos exactamente la estructura requerida
# Mantendremos PAHC_3 y si se requiere PACH_3, garantizaremos la nomenclatura clara.
# Ajustamos PAHC_3 a PAHC_3 o PACH_3 según solicitud:
# El usuario escribió: "PAHC_1, PAHC_2, PACH_3"
df["PACH_3"] = df["PAHC_3"]
df = df.drop(columns=["PAHC_3"])

# Verificar medias por comunidad y por eje para validar que caen en los cuadrantes esperados
dims_eval = {
    "IDS": ["IDS_1", "IDS_2", "IDS_3"],
    "CAR": ["CAR_1", "CAR_2", "CAR_3"],
    "ACA": ["ACA_1", "ACA_2", "ACA_3"],
    "CITE": ["CITE_1", "CITE_2", "CITE_3"],
    "PAHC": ["PAHC_1", "PAHC_2", "PACH_3"]
}

for dim, cols in dims_eval.items():
    df[f"mean_{dim}"] = df[cols].mean(axis=1)

df["Eje_Simbolico"] = (df["mean_IDS"] + df["mean_CAR"]) / 2
df["Eje_Instrumental"] = (df["mean_ACA"] + df["mean_CITE"] + df["mean_PAHC"]) / 3

resumen = df.groupby("comunidad")[["Eje_Simbolico", "Eje_Instrumental", "mean_IDS", "mean_CAR", "mean_ACA", "mean_CITE", "mean_PAHC"]].mean()
print("Resumen de medias por comunidad:")
print(resumen)

# Limpiar columnas auxiliares de cálculo para entregar el dataset limpio
cols_export = ["id_sujeto", "comunidad", "cuadrante_teorico", 
               "IDS_1", "IDS_2", "IDS_3", 
               "CAR_1", "CAR_2", "CAR_3", 
               "ACA_1", "ACA_2", "ACA_3", 
               "CITE_1", "CITE_2", "CITE_3", 
               "PAHC_1", "PAHC_2", "PACH_3"]

df_export = df[cols_export]

output_filename = "simulacion_potencial_netificador_docentes.csv"
df_export.to_csv(output_filename, index=False, encoding="utf-8-sig")
print(f"Archivo guardado exitosamente: {output_filename}")


```

```text
Resumen de medias por comunidad:
                             Eje_Simbolico  Eje_Instrumental  mean_IDS  mean_CAR  mean_ACA  mean_CITE  mean_PAHC
comunidad                                                                                                       
Profesores de Alto_Hospicio       2.452500          2.061111  2.340000  2.565000  2.300000   2.013333   1.870000
Profesores de Antofagasta         2.568333          3.823889  2.490000  2.646667  3.876667   3.823333   3.771667
Profesores de Arica               4.225000          2.191667  4.188333  4.261667  2.475000   2.191667   1.908333
Profesores de Iquique             4.327500          3.982222  4.335000  4.320000  4.115000   3.833333   3.998333
Archivo guardado exitosamente: simulacion_potencial_netificador_docentes.csv


```

Your CSV file is ready


El archivo `simulacion_potencial_netificador_docentes.csv` ha sido generado con un tamaño muestral de **$n = 200$ individuos por comunidad** ($N = 800$ casos en total), garantizando potencia estadística para contrastes multivariados, análisis factorial exploratorio (AFE) y confirmatorio multigrupo (AFC).

---

### Distribución de las Comunidades en la Matriz Tipológica

Los datos han sido modelados para reflejar con precisión matemática los cuatro cuadrantes respecto al punto de corte teórico ($3.0$):

| Comunidad | Cuadrante Teórico | Eje Simbólico $(\text{IDS, CAR})$ | Eje Instrumental $(\text{ACA, CITE, PAHC})$ | Comportamiento Simulado en Terreno |
| --- | --- | --- | --- | --- |
| **Profesores de Iquique** | **Cuadrante I: Autopoiética** | **$4.33$** *(Alto)* | **$3.98$** *(Alto)* | Red con identidad pedagógica sólida, alta vocación compartida, autoorganización, disposición a invertir recursos y producción recurrente de artefactos didácticos. |
| **Profesores de Arica** | **Cuadrante II: Retórica** | **$4.23$** *(Alto)* | **$2.19$** *(Bajo)* | Colectivo con discurso ético y pedagógico intenso, pero baja capacidad organizativa autónoma, escasa inversión financiera y nula creación de repositorios compartidos. |
| **Profesores de Alto Hospicio** | **Cuadrante III: Inerte / Atomizada** | **$2.45$** *(Bajo)* | **$2.06$** *(Bajo)* | Colectivo docente fragmentado o individualista; respuestas neutras/desfavorables en identidad gremial, sin valores aglutinadores ni acciones coordinadas. |
| **Profesores de Antofagasta** | **Cuadrante IV: Corporativa / Instrumental** | **$2.57$** *(Bajo)* | **$3.82$** *(Alto)* | Grupo con alta capacidad adquisitiva, infraestructura y herramientas técnicas, pero sin un sentido de misión pedagógica compartida ni identidad endogrupal. |

---

### Estructura de Columnas del Archivo CSV

1. `id_sujeto`: Identificador único de cada docente (`DOC_0001` a `DOC_0800`).
2. `comunidad`: Nombre del colectivo (`Profesores de Iquique`, `Profesores de Arica`, `Profesores de Alto_Hospicio`, `Profesores de Antofagasta`).
3. `cuadrante_teorico`: Cuadrante tipológico asignado en la modelación.
4. **Reactivos en Escala Likert de 5 puntos (1 a 5):**
* **Identidad y Diferenciación:** `IDS_1`, `IDS_2`, `IDS_3`
* **Cohesión Axiológica:** `CAR_1`, `CAR_2`, `CAR_3`
* **Agencia Colectiva:** `ACA_1`, `ACA_2`, `ACA_3`
* **Capacidad e Inversión:** `CITE_1`, `CITE_2`, `CITE_3`
* **Producción de Artefactos:** `PAHC_1`, `PAHC_2`, `PACH_3`



---

Thankyou Lord!