import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def show_loading_screen(root, callback):
    # Configurar ventana
    root.geometry("800x600")
    # Mostrar pantalla de carga
    loading_label = tk.Label(root, text="AVAL-IA", font=("Arial", 62, "bold"))
    loading_label.pack(expand=True)
    loading_sub = tk.Label(root, text="Cargando...")
    loading_sub.pack()
    # Después de 2 segundos, limpiar y pasar a la siguiente pantalla
    root.after(2000, lambda: [loading_label.destroy(), loading_sub.destroy(), callback()])

def show_student_details(root):
    # Ventana emergente para detalles del alumno
    details = tk.Toplevel(root)
    details.title("Detalles de Ana Pérez")
    details.geometry("400x600")

    # Info textual
    tk.Label(details, text="Detalles de Marcos Eijo - 2º BAC B", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(details, text="Calificaciones:\n- Examen 1 (40%) - 7.5\n- Trabajo (30%) - 8.0\nNota final: 7.7").pack()
    tk.Label(details, text="Anotaciones:\n- 22/04: 'Buena participación'").pack(pady=5)
    tk.Label(details, text="Entregas:\n- Trabajo (30/04): Pendiente").pack(pady=5)
    tk.Label(details, text="Análisis IA:\n- 'Marcos mantiene un 7.7, podría subir a 8.'").pack(pady=5)

    # Gráfica de proyección (simulada)
    fig = Figure(figsize=(4, 2), dpi=100)
    plot = fig.add_subplot(1, 1, 1)

    # Simulamos progreso: notas de la 1ª eval, 2ª, y proyección futura
    evaluaciones = ["Eval 1", "Eval 2", "Proy. Eval 3"]
    notas = [7.3, 7.7, 8.0]

    plot.plot(evaluaciones, notas, marker='o', color='blue')
    plot.set_title("Proyección de nota estimada")
    plot.set_ylim(0, 10)
    plot.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=details)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    # Botón cerrar
    tk.Button(details, text="Cerrar", command=details.destroy).pack(pady=10)


def show_demo_screen(root):
    # Configurar ventana principal
    root.geometry("800x600")
    
        # Menú superior (más bonito con fondo y letras grandes)
    menu_bar = tk.Frame(root, bg="#2196F3", pady=10)  # Fondo verde
    menu_bar.pack(side=tk.TOP, fill=tk.X)

    # Etiquetas del menú superior con letras más grandes
    menu_label = tk.Label(menu_bar, text="Clases | Calificaciones | Calendario | IA", font=("Arial", 16, "bold"), fg="white", bg="#2196F3")
    menu_label.pack(side=tk.TOP, padx=20, pady=5)

    
    # Título de la clase
    tk.Label(root, text="2º BAC B", font=("Arial", 12)).pack(side=tk.TOP, pady=5)
    
    # Frame principal para dividir izquierda y derecha
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    # Izquierda: Lista de alumnos
    left_frame = tk.Frame(main_frame)
    left_frame.pack(side=tk.LEFT, padx=10)
    tk.Label(left_frame, text="Alumnos", font=("Arial", 10, "bold")).pack()
    ana_label = tk.Label(left_frame, text="Marcos Eijo", fg="blue", cursor="hand2")
    ana_label.pack(anchor="w")
    tk.Label(left_frame, text="Antonio Campos").pack(anchor="w")
    tk.Label(left_frame, text="María López").pack(anchor="w")
    tk.Label(left_frame, text="Alba García").pack(anchor="w")
    tk.Label(left_frame, text="Marta Diz").pack(anchor="w")
    tk.Label(left_frame, text="Óscar Rey").pack(anchor="w")
    tk.Label(left_frame, text="Fina Paulos").pack(anchor="w")
    tk.Label(left_frame, text="Bertín Deza").pack(anchor="w")
    tk.Label(left_frame, text="Pablo Arias").pack(anchor="w")
    ana_label.bind("<Button-1>", lambda e: show_student_details(root))
    
        # Derecha: Calendario semanal
    right_frame = tk.Frame(main_frame)
    right_frame.pack(side=tk.RIGHT, padx=10)
    tk.Label(right_frame, text="< Semana 16 >", font=("Arial", 10, "bold")).pack(pady=5)

    days_frame = tk.Frame(right_frame)
    days_frame.pack()

    # Días y horas
    dias = ["", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas = [
        "8:45", "9:35", "10:45", "11:35", "12:45", "13:35",
        "---",
        "15:40", "16:30",
        "---"
    ]

    # Cabecera con días
    for j, dia in enumerate(dias):
        label = tk.Label(days_frame, text=dia, width=12, font=("Arial", 9, "bold"), borderwidth=1, relief="solid")
        label.grid(row=0, column=j)

    # Horas + celdas vacías
    for i, hora in enumerate(horas):
        # Columna de horas
        label = tk.Label(days_frame, text=hora, width=10, font=("Arial", 9), borderwidth=1, relief="solid")
        label.grid(row=i+1, column=0)

        # Celdas por día
        for j in range(1, 6):  # Lunes a Viernes
            celda = tk.Label(days_frame, text="", width=12, height=2, borderwidth=1, relief="solid", bg="#ffffff")
            celda.grid(row=i+1, column=j)
 # Modificar la celda para el Jueves a las 11:35
    # El índice para Jueves (columna 5) y las 11:35 (fila 4)
    examen_label = tk.Label(days_frame, text="Examen Ud 4", width=12, height=2, borderwidth=1, relief="solid", bg="red", fg="white")
    examen_label.grid(row=4, column=5)

