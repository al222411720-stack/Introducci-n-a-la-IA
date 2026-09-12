from datetime import datetime
import random
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SistemaDiagnosticoEquiposBIGDTA") \
    .getOrCreate()

numero = random.randint(10000, 99999)
numero_reporte = f"REP-{numero}"
fecha_hora = datetime.now()
fecha = fecha_hora.strftime("%d/%m/%Y")
hora = fecha_hora.strftime("%H:%M")

print("\n==========================================")
print(" SISTEMA DE DIAGNÓSTICO DE EQUIPOS (SPARK)")
print("==========================================")

nombre = input("Nombre del usuario: ")
direccion = input("Dirección: ")

print("\nSeleccione el tipo de equipo:")
print("1. Computadora de escritorio\n2. Laptop\n3. All in One\n4. Servidor\n5. Otro")
tipo_opcion = input("Seleccione una opción: ")

tipos = {"1": "Computadora de escritorio", "2": "Laptop", "3": "All in One", "4": "Servidor"}
tipo_equipo = tipos.get(tipo_opcion, input("Especifique el tipo: ") if tipo_opcion == "5" else "No especificado")

print("\n==========================================")
print(" DIAGNÓSTICO")
print("==========================================")

electricidad = input("¿Tiene electricidad? (s/n): ").lower()
while electricidad not in ["s", "n"]:
    electricidad = input("Ingrese solamente s o n: ").lower()

if electricidad == "n":
    diagnostico = "Revisar alimentación eléctrica."
    recomendacion = "Verificar cable, contacto eléctrico, regulador o fuente."
    nivel = "ALTA"
else:
    enciende = input("¿El equipo enciende? (s/n): ").lower()
    while enciende not in ["s", "n"]:
        enciende = input("Ingrese solamente s o n: ").lower()

    if enciende == "n":
        diagnostico = "El equipo recibe electricidad pero no enciende."
        recomendacion = "Revisar fuente de poder, batería o tarjeta madre."
        nivel = "ALTA"
    else:
        imagen = input("¿Muestra imagen? (s/n): ").lower()
        while imagen not in ["s", "n"]:
            imagen = input("Ingrese solamente s o n: ").lower()

        if imagen == "n":
            diagnostico = "El equipo enciende pero no muestra imagen."
            recomendacion = "Revisar monitor, cable de video o memoria RAM."
            nivel = "MEDIA"
        else:
            sistema = input("¿Inicia el sistema operativo? (s/n): ").lower()
            while sistema not in ["s", "n"]:
                sistema = input("Ingrese solamente s o n: ").lower()

            if sistema == "n":
                diagnostico = "El equipo muestra imagen pero no inicia el SO."
                recomendacion = "Revisar disco, sistema operativo o RAM."
                nivel = "MEDIA"
            else:
                rendimiento = input("¿Funciona con lentitud? (s/n): ").lower()
                while rendimiento not in ["s", "n"]:
                    rendimiento = input("Ingrese solamente s o n: ").lower()

                if rendimiento == "s":
                    diagnostico = "El equipo funciona pero presenta bajo rendimiento."
                    recomendacion = "Revisar memoria RAM, almacenamiento o malware."
                    nivel = "BAJA"
                else:
                    diagnostico = "Funcionamiento básico correcto."
                    recomendacion = "No se detectaron problemas básicos."
                    nivel = "NORMAL"

datos = [(numero_reporte, fecha, hora, nombre, direccion, tipo_equipo, diagnostico, nivel, recomendacion)]
columnas = ["No_Reporte", "Fecha", "Hora", "Usuario", "Direccion", "Tipo_Equipo", "Diagnostico", "Nivel_Riesgo", "Recomendacion"]

df_reporte = spark.createDataFrame(datos, schema=columnas)

print("\n==========================================")
print("     REPORTE PROCESADO EN APACHE SPARK")
print("==========================================")
df_reporte.show(truncate=False)

spark.stop()