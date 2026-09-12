import random
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog
from pyspark.sql import SparkSession

# Crear ventana principal oculta para los cuadros de diálogo
root = tk.Tk()
root.withdraw()

# Formulario inicial
nombre = simpledialog.askstring("Diagnóstico", "Nombre del usuario:")
if not nombre:
    exit()

direccion = simpledialog.askstring("Diagnóstico", "Dirección:")

tipo_equipo = simpledialog.askstring(
    "Tipo de Equipo", 
    "Escriba el tipo de equipo:\n(Ej. Laptop, Escritorio, All in One, Servidor)"
)

# Cuestionario con botones Si / No
electricidad = messagebox.askyesno("Diagnóstico", "¿El equipo tiene electricidad?")

if not electricidad:
    diagnostico = "Revisar alimentación eléctrica."
    recomendacion = "Verificar cable, contacto eléctrico, regulador o fuente."
    nivel = "ALTA"
else:
    enciende = messagebox.askyesno("Diagnóstico", "¿El equipo enciende?")
    if not enciende:
        diagnostico = "El equipo recibe electricidad pero no enciende."
        recomendacion = "Revisar fuente de poder, batería o tarjeta madre."
        nivel = "ALTA"
    else:
        imagen = messagebox.askyesno("Diagnóstico", "¿Muestra imagen en pantalla?")
        if not imagen:
            diagnostico = "El equipo enciende pero no muestra imagen."
            recomendacion = "Revisar monitor, cable de video o memoria RAM."
            nivel = "MEDIA"
        else:
            sistema = messagebox.askyesno("Diagnóstico", "¿Inicia el sistema operativo?")
            if not sistema:
                diagnostico = "El equipo muestra imagen pero no inicia el SO."
                recomendacion = "Revisar disco, sistema operativo o RAM."
                nivel = "MEDIA"
            else:
                rendimiento = messagebox.askyesno("Diagnóstico", "¿Funciona con lentitud?")
                if rendimiento:
                    diagnostico = "El equipo funciona pero presenta bajo rendimiento."
                    recomendacion = "Revisar memoria RAM, almacenamiento o malware."
                    nivel = "BAJA"
                else:
                    diagnostico = "Funcionamiento básico correcto."
                    recomendacion = "No se detectaron problemas básicos."
                    nivel = "NORMAL"

# Generar reporte con PySpark
spark = SparkSession.builder.appName("DiagnosticoGUI").getOrCreate()

numero_reporte = f"REP-{random.randint(10000, 99999)}"
fecha = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M")

datos = [(numero_reporte, fecha, hora, nombre, direccion, tipo_equipo, diagnostico, nivel, recomendacion)]
columnas = ["No_Reporte", "Fecha", "Hora", "Usuario", "Direccion", "Tipo_Equipo", "Diagnostico", "Nivel_Riesgo", "Recomendacion"]

df_reporte = spark.createDataFrame(datos, schema=columnas)

print("\n==========================================")
print("     REPORTE PROCESADO EN APACHE SPARK")
print("==========================================")
df_reporte.show(truncate=False)

# Mostrar resultado final en ventana emergente
res_texto = f"Reporte: {numero_reporte}\nUsuario: {nombre}\nDiagnóstico: {diagnostico}\nNivel de Riesgo: {nivel}\nRecomendación: {recomendacion}"
messagebox.showinfo("Resultado del Diagnóstico", res_texto)

spark.stop()