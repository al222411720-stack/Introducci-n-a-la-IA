import tkinter as tk
from tkinter import messagebox
from pyspark.sql import SparkSession

root = tk.Tk()
root.withdraw()

fiebre = messagebox.askyesno("Sistema Experto", "¿Tiene fiebre?")
tos = messagebox.askyesno("Sistema Experto", "¿Tiene tos?")
dolor = messagebox.askyesno("Sistema Experto", "¿Tiene dolor de garganta?")

if fiebre and tos:
    diagnostico = "Posible infección respiratoria"
elif tos and dolor:
    diagnostico = "Posible irritación respiratoria"
elif fiebre:
    diagnostico = "Se recomienda valoración profesional"
else:
    diagnostico = "No se identificó un patrón"

spark = SparkSession.builder.appName("SistemaExpertoGUI").getOrCreate()

datos = [("Sí" if fiebre else "No", "Sí" if tos else "No", "Sí" if dolor else "No", diagnostico)]
columnas = ["Fiebre", "Tos", "Dolor_Garganta", "Diagnostico_Final"]

df_salud = spark.createDataFrame(datos, schema=columnas)

print("\n==========================================")
print("     RESULTADO EN APACHE SPARK")
print("==========================================")
df_salud.show(truncate=False)

messagebox.showinfo("Resultado del Sistema Experto", f"Diagnóstico final:\n{diagnostico}")

spark.stop()