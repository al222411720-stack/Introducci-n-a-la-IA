from datetime import datetime, timedelta
import random
import tkinter as tk
from tkinter import messagebox, ttk

# ------------------------------------------------------------
# HISTORIAL EN MEMORIA Y ESTADÍSTICAS
# ------------------------------------------------------------
historial_pacientes = []

# ------------------------------------------------------------
# VENTANA EMERGENTE TIPO APLICACIÓN
# ------------------------------------------------------------


def mostrar_reporte_medico_app(
    titulo_ventana, titulo_header, datos_paciente, signos_vitales, diagnostico_data, stats_data
):
    top = tk.Toplevel()
    top.title(titulo_ventana)
    top.geometry("520x680")
    top.resizable(False, False)
    top.configure(bg="#f8fafc")

    top.transient(top.master)
    top.grab_set()

    # Header
    header_frame = tk.Frame(top, bg="#065f46", height=65)
    header_frame.pack(fill="x", side="top")

    lbl_header = tk.Label(
        header_frame,
        text=titulo_header,
        font=("Segoe UI", 13, "bold"),
        fg="#ffffff",
        bg="#065f46",
    )
    lbl_header.pack(pady=18)

    body = tk.Frame(top, bg="#f8fafc", padx=20, pady=10)
    body.pack(fill="both", expand=True)

    # Tarjeta 1: Paciente
    card1 = tk.LabelFrame(
        body,
        text="  Datos del Paciente  ",
        font=("Segoe UI", 9, "bold"),
        fg="#065f46",
        bg="#ffffff",
        bd=1,
        relief="solid",
        padx=12,
        pady=6,
    )
    card1.pack(fill="x", pady=4)

    for k, v in datos_paciente.items():
        row = tk.Frame(card1, bg="#ffffff")
        row.pack(fill="x", pady=1)
        tk.Label(
            row,
            text=f"{k}:",
            font=("Segoe UI", 9, "bold"),
            fg="#64748b",
            bg="#ffffff",
            width=16,
            anchor="w",
        ).pack(side="left")
        tk.Label(
            row,
            text=v,
            font=("Segoe UI", 9),
            fg="#0f172a",
            bg="#ffffff",
            anchor="w",
        ).pack(side="left", fill="x", expand=True)

    # Tarjeta 2: Signos Vitales
    card2 = tk.LabelFrame(
        body,
        text="  Registro de Signos Vitales  ",
        font=("Segoe UI", 9, "bold"),
        fg="#065f46",
        bg="#ffffff",
        bd=1,
        relief="solid",
        padx=12,
        pady=6,
    )
    card2.pack(fill="x", pady=4)

    for k, v in signos_vitales.items():
        row = tk.Frame(card2, bg="#ffffff")
        row.pack(fill="x", pady=1)
        tk.Label(
            row,
            text=f"{k}:",
            font=("Segoe UI", 9, "bold"),
            fg="#64748b",
            bg="#ffffff",
            width=20,
            anchor="w",
        ).pack(side="left")
        tk.Label(
            row,
            text=str(v),
            font=("Segoe UI", 9),
            fg="#0f172a",
            bg="#ffffff",
            anchor="w",
            wraplength=260,
            justify="left",
        ).pack(side="left", fill="x", expand=True)

    # Tarjeta 3: Diagnóstico
    card3 = tk.LabelFrame(
        body,
        text="  Diagnóstico y Cita  ",
        font=("Segoe UI", 9, "bold"),
        fg="#065f46",
        bg="#ffffff",
        bd=1,
        relief="solid",
        padx=12,
        pady=6,
    )
    card3.pack(fill="x", pady=4)

    prioridad = diagnostico_data.get("Prioridad", "NORMAL")
    color_prio = {
        "ALTA": "#dc2626",
        "MEDIA": "#d97706",
        "NORMAL": "#16a34a",
    }.get(prioridad, "#475569")

    for k, v in diagnostico_data.items():
        row = tk.Frame(card3, bg="#ffffff")
        row.pack(fill="x", pady=1)
        tk.Label(
            row,
            text=f"{k}:",
            font=("Segoe UI", 9, "bold"),
            fg="#64748b",
            bg="#ffffff",
            width=20,
            anchor="w",
        ).pack(side="left")

        fg_val = color_prio if k == "Prioridad" else "#0f172a"
        font_val = (
            ("Segoe UI", 9, "bold") if k == "Prioridad" else ("Segoe UI", 9)
        )

        tk.Label(
            row,
            text=v,
            font=font_val,
            fg=fg_val,
            bg="#ffffff",
            anchor="w",
            wraplength=260,
            justify="left",
        ).pack(side="left", fill="x", expand=True)

    # Tarjeta 4: Métricas
    card4 = tk.LabelFrame(
        body,
        text="  Métricas de Sesión  ",
        font=("Segoe UI", 9, "bold"),
        fg="#065f46",
        bg="#ffffff",
        bd=1,
        relief="solid",
        padx=12,
        pady=6,
    )
    card4.pack(fill="x", pady=4)

    for k, v in stats_data.items():
        row = tk.Frame(card4, bg="#ffffff")
        row.pack(fill="x", pady=1)
        tk.Label(
            row,
            text=f"{k}:",
            font=("Segoe UI", 9, "bold"),
            fg="#64748b",
            bg="#ffffff",
            width=24,
            anchor="w",
        ).pack(side="left")
        tk.Label(
            row,
            text=str(v),
            font=("Segoe UI", 9),
            fg="#0f172a",
            bg="#ffffff",
            anchor="w",
        ).pack(side="left", fill="x", expand=True)

    # Botón de cierre
    btn_cerrar = tk.Button(
        body,
        text="Aceptar y Cerrar",
        command=top.destroy,
        bg="#059669",
        fg="white",
        activebackground="#047857",
        activeforeground="white",
        font=("Segoe UI", 9, "bold"),
        bd=0,
        pady=8,
        cursor="hand2",
    )
    btn_cerrar.pack(fill="x", pady=(8, 0))


# ------------------------------------------------------------
# LÓGICA DE DIAGNÓSTICO MÉDICO
# ------------------------------------------------------------


def evaluar_paciente():
    nombre = entry_nombre.get().strip()
    direccion = entry_direccion.get().strip()

    if not nombre or not direccion:
        messagebox.showwarning(
            "Campos Incompletos",
            "Por favor, ingrese el nombre y la dirección del paciente.",
        )
        return

    try:
        q_fc = float(entry_fc.get().strip())
        r_spo2 = float(entry_spo2.get().strip())
        s_peso = float(entry_peso.get().strip())
        t_talla = float(entry_talla.get().strip())
        pa_sys = float(entry_pa_sys.get().strip())
        pa_dia = float(entry_pa_dia.get().strip())
    except ValueError:
        messagebox.showerror(
            "Error en Signos Vitales",
            "Asegúrese de colocar valores numéricos válidos en todos los signos vitales.",
        )
        return

    fiebre = combo_fiebre.get() == "Sí"
    tos = combo_tos.get() == "Sí"
    dolor = combo_dolor.get() == "Sí"

    alertas_vitales = []
    if q_fc < 60 or q_fc > 100:
        alertas_vitales.append(f"Frecuencia cardíaca fuera de rango ({q_fc} bpm)")
    if r_spo2 < 90:
        alertas_vitales.append(f"Hipoxia / Oxigenación baja ({r_spo2}%)")
    if pa_sys >= 140 or pa_dia >= 90:
        alertas_vitales.append(
            f"Presión Arterial Alta ({int(pa_sys)}/{int(pa_dia)} mmHg)"
        )
    elif pa_sys < 90 or pa_dia < 60:
        alertas_vitales.append(
            f"Presión Arterial Baja ({int(pa_sys)}/{int(pa_dia)} mmHg)"
        )

    imc = s_peso / (t_talla**2) if t_talla > 0 else 0

    if r_spo2 < 90 or pa_sys >= 160 or (fiebre and tos and dolor):
        diagnostico = "Cuadro agudo / Alteración de signos vitales crítica"
        prioridad = "ALTA"
        especialidad = "Urgencias / Neumología"
    elif (fiebre and tos) or (tos and dolor) or (q_fc > 100 or pa_sys >= 140):
        diagnostico = "Infección respiratoria o alteración hemodinámica moderada"
        prioridad = "MEDIA"
        especialidad = "Medicina Interna"
    elif fiebre or tos or dolor or len(alertas_vitales) > 0:
        diagnostico = "Sintomatología leve / Alteración menor de signos vitales"
        prioridad = "NORMAL"
        especialidad = "Medicina General"
    else:
        diagnostico = "Sin hallazgos de patología evidente"
        prioridad = "NORMAL"
        especialidad = "Medicina Preventiva"

    fecha_actual = datetime.now()

    if prioridad in ["ALTA", "MEDIA"]:
        horas_espera = random.randint(1, 6)
        fecha_cita = fecha_actual + timedelta(hours=horas_espera)
        str_cita = f"HOY {fecha_cita.strftime('%d/%m/%Y')} a las {fecha_cita.strftime('%H:%M')} hrs"
    else:
        dias_despues = random.randint(2, 7)
        hora_aleatoria = random.randint(8, 16)
        fecha_cita = (fecha_actual + timedelta(dias=dias_despues)).replace(
            hour=hora_aleatoria, minute=0
        )
        str_cita = f"{fecha_cita.strftime('%d/%m/%Y')} a las {fecha_cita.strftime('%H:%M')} hrs"

    historial_pacientes.append({"nombre": nombre, "prioridad": prioridad})
    conteo_usuario = sum(
        1 for p in historial_pacientes if p["nombre"].lower() == nombre.lower()
    )
    es_primer_reporte = "SÍ" if conteo_usuario == 1 else "NO"

    detalles_vitales = (
        ", ".join(alertas_vitales)
        if alertas_vitales
        else "Signos dentro de parámetros normales"
    )

    datos_paciente = {
        "Nombre": nombre,
        "Dirección": direccion,
        "Fecha Registro": fecha_actual.strftime("%d/%m/%Y %H:%M"),
    }

    signos_vitales = {
        "Frecuencia Cardíaca": f"{q_fc} bpm",
        "Oxigenación SpO2": f"{r_spo2} %",
        "Peso / Talla": f"{s_peso} kg / {t_talla} m (IMC: {imc:.1f})",
        "Presión Arterial": f"{int(pa_sys)}/{int(pa_dia)} mmHg",
        "Evaluación Vitales": detalles_vitales,
    }

    diagnostico_data = {
        "Diagnóstico": diagnostico,
        "Especialidad Remitida": especialidad,
        "Prioridad": prioridad,
        "Cita Asignada": str_cita,
    }

    stats_data = {
        "¿Primer reporte del paciente?": es_primer_reporte,
        "Historial del paciente": f"{conteo_usuario} atenciones",
        "Total registros en sesión": len(historial_pacientes),
    }

    mostrar_reporte_medico_app(
        "Centro Médico - Evaluación Clínica",
        "🏥 REPORTE CLÍNICO DEL PACIENTE",
        datos_paciente,
        signos_vitales,
        diagnostico_data,
        stats_data,
    )


# ------------------------------------------------------------
# INTERFAZ GRÁFICA PRINCIPAL
# ------------------------------------------------------------
root = tk.Tk()
root.title("Sistema Experto de Diagnóstico Médico")
root.geometry("460x540")
root.resizable(False, False)

lbl_titulo = tk.Label(
    root, text="DIAGNÓSTICO Y EVALUACIÓN MÉDICA", font=("Segoe UI", 12, "bold")
)
lbl_titulo.pack(pady=8)

frame = tk.Frame(root)
frame.pack(padx=15, pady=5, fill="both", expand=True)

tk.Label(
    frame, text="Nombre del Paciente:", font=("Segoe UI", 9, "bold")
).grid(row=0, column=0, sticky="w", pady=3)
entry_nombre = tk.Entry(frame, width=22)
entry_nombre.grid(row=0, column=1, pady=3)

tk.Label(frame, text="Dirección:", font=("Segoe UI", 9, "bold")).grid(
    row=1, column=0, sticky="w", pady=3
)
entry_direccion = tk.Entry(frame, width=22)
entry_direccion.grid(row=1, column=1, pady=3)

tk.Label(
    frame,
    text="--- SIGNOS VITALES ---",
    font=("Segoe UI", 9, "bold"),
    fg="#0056b3",
).grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(frame, text="Frecuencia Cardíaca (Q - bpm):").grid(
    row=3, column=0, sticky="w", pady=2
)
entry_fc = tk.Entry(frame, width=10)
entry_fc.grid(row=3, column=1, sticky="w", pady=2)

tk.Label(frame, text="Oxigenación SpO2 (R - %):").grid(
    row=4, column=0, sticky="w", pady=2
)
entry_spo2 = tk.Entry(frame, width=10)
entry_spo2.grid(row=4, column=1, sticky="w", pady=2)

tk.Label(frame, text="Peso (S - kg):").grid(
    row=5, column=0, sticky="w", pady=2
)
entry_peso = tk.Entry(frame, width=10)
entry_peso.grid(row=5, column=1, sticky="w", pady=2)

tk.Label(frame, text="Talla (T - metros):").grid(
    row=6, column=0, sticky="w", pady=2
)
entry_talla = tk.Entry(frame, width=10)
entry_talla.grid(row=6, column=1, sticky="w", pady=2)

tk.Label(frame, text="Presión Arterial (PA - Sist/Diast):").grid(
    row=7, column=0, sticky="w", pady=2
)
frame_pa = tk.Frame(frame)
frame_pa.grid(row=7, column=1, sticky="w", pady=2)
entry_pa_sys = tk.Entry(frame_pa, width=4)
entry_pa_sys.pack(side="left")
tk.Label(frame_pa, text="/").pack(side="left")
entry_pa_dia = tk.Entry(frame_pa, width=4)
entry_pa_dia.pack(side="left")

tk.Label(
    frame,
    text="--- SÍNTOMAS ---",
    font=("Segoe UI", 9, "bold"),
    fg="#0056b3",
).grid(row=8, column=0, columnspan=2, pady=5)

tk.Label(frame, text="¿Tiene fiebre?").grid(row=9, column=0, sticky="w", pady=2)
combo_fiebre = ttk.Combobox(
    frame, values=["No", "Sí"], state="readonly", width=8
)
combo_fiebre.current(0)
combo_fiebre.grid(row=9, column=1, sticky="w", pady=2)

tk.Label(frame, text="¿Tiene tos?").grid(row=10, column=0, sticky="w", pady=2)
combo_tos = ttk.Combobox(frame, values=["No", "Sí"], state="readonly", width=8)
combo_tos.current(0)
combo_tos.grid(row=10, column=1, sticky="w", pady=2)

tk.Label(frame, text="¿Tiene dolor de garganta?").grid(
    row=11, column=0, sticky="w", pady=2
)
combo_dolor = ttk.Combobox(
    frame, values=["No", "Sí"], state="readonly", width=8
)
combo_dolor.current(0)
combo_dolor.grid(row=11, column=1, sticky="w", pady=2)

btn_evaluar = tk.Button(
    root,
    text="Evaluar Paciente y Asignar Cita",
    command=evaluar_paciente,
    bg="#28a745",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    cursor="hand2",
)
btn_evaluar.pack(pady=12)

root.mainloop()