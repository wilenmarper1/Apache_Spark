# batch_covid.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Crear sesión Spark
spark = SparkSession.builder.appName("BatchCovidAnalysis").getOrCreate()

# Cargar dataset
df = spark.read.csv("country_wise_latest.csv", header=True, inferSchema=True)

print("Estructura del archivo:")
df.printSchema()

print("Primeras filas del dataset:")
df.show(10, truncate=False)

# Limpieza básica: eliminar duplicados y nulos en columnas clave
df_clean = df.dropDuplicates(["Country/Region"]).dropna(subset=["Confirmed", "Deaths"])

print("Datos limpiados correctamente")

# Análisis 1: Top 10 países con más casos confirmados
top_confirmed = df_clean.orderBy(col("Confirmed").desc()).select("Country/Region", "Confirmed")
print("Top 10 países con más casos confirmados:")
top_confirmed.show(10, truncate=False)

# Análisis 2: Mortalidad por región OMS
region_deaths = df_clean.groupBy("WHO Region").sum("Deaths").orderBy(col("sum(Deaths)").desc())
print("Muertes totales por región OMS:")
region_deaths.show(truncate=False)

# Análisis 3: Tasa de recuperación promedio por región
region_recovery = df_clean.groupBy("WHO Region").avg("Recovered / 100 Cases")
print("Promedio de recuperación (%):")
region_recovery.show(truncate=False)

# Guardar resultados procesados
top_confirmed.write.mode("overwrite").csv("resultados_covid/top_confirmed")
region_deaths.write.mode("overwrite").csv("resultados_covid/region_deaths")
region_recovery.write.mode("overwrite").csv("resultados_covid/region_recovery")

print("Resultados guardados en carpeta 'resultados_covid/'")
print("Procesamiento batch finalizado correctamente.")
