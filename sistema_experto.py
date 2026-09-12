from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SistemaExpertoSaludBIGDTA") \
    .getOrCreate()

print("\n==========================================")
print("     SISTEMA EXPERTO DE DIAGNÓSTICO")
print("==========================================")

fiebre = input("¿Tiene fiebre? (s/n): ").lower()
tos = input("¿Tiene tos? (s/n): ").lower()
dolor = input("¿Tiene dolor de garganta? (s/n): ").lower()

if fiebre == "s" and tos == "s":
    diagnostico = "Posible infección respiratoria"
elif tos == "s" and dolor == "s":
    diagnostico = "Posible irritación respiratoria"
elif fiebre == "s":
    diagnostico = "Se recomienda valoración profesional"
else:
    diagnostico = "No se identificó un patrón"

datos = [(fiebre, tos, dolor, diagnostico)]
columnas = ["Fiebre", "Tos", "Dolor_Garganta", "Diagnostico_Final"]

df_salud = spark.createDataFrame(datos, schema=columnas)

print("\n==========================================")
print("     RESULTADO EN APACHE SPARK")
print("==========================================")
df_salud.show(truncate=False)

spark.stop()