import tkinter as tk
from tkinter import messagebox

def mostrar_modulo(root):
    ventana = tk.Toplevel(root)
    ventana.title("Múltiplos y MCD/MCM - Tutor Matemático")
    ventana.geometry("750x550")
    ventana.configure(bg="#f1f8e9")

    # Frame con canvas y scrollbar
    frame_principal = tk.Frame(ventana, bg="#f1f8e9")
    frame_principal.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_principal, bg="#f1f8e9", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f1f8e9")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Contenido dentro del scrollable_frame
    titulo = tk.Label(
        scrollable_frame,
        text="🔢 MÚLTIPLOS Y M.C.D / M.C.M",
        font=("Comic Sans MS", 20, "bold"),
        fg="#2e7d32",
        bg="#f1f8e9"
    )
    titulo.pack(pady=10)

    teoria = (
        "📘 *Múltiplos y divisores*\n\n"
        "➡ Un múltiplo de un número se obtiene al multiplicarlo por 1, 2, 3, etc.\n"
        "   Ejemplo: los múltiplos de 3 son 3, 6, 9, 12, 15...\n\n"
        "➡ Un divisor es un número que puede dividir a otro sin dejar resto.\n"
        "   Ejemplo: los divisores de 12 son 1, 2, 3, 4, 6 y 12.\n\n"
        "📗 *M.C.D. (Máximo Común Divisor)*\n"
        "Es el número más grande que divide a dos o más números.\n"
        "Ejemplo: MCD(12, 18) = 6.\n\n"
        "📙 *M.C.M. (Mínimo Común Múltiplo)*\n"
        "Es el número más pequeño que es múltiplo común de dos o más números.\n"
        "Ejemplo: MCM(4, 6) = 12."
    )

    tk.Label(
        scrollable_frame,
        text=teoria,
        font=("Arial", 12),
        justify="left",
        bg="#f1f8e9",
        fg="#333",
        wraplength=700
    ).pack(padx=20, pady=10)

    # Separador
    tk.Label(scrollable_frame, text="──────────────────────────────", bg="#f1f8e9", fg="#999").pack(pady=5)

    # Ejercicio 1
    tk.Label(
        scrollable_frame,
        text="🎯 Ejercicio: ¿Cuál es el M.C.D de 12 y 18?",
        font=("Arial", 13, "bold"),
        bg="#f1f8e9"
    ).pack(pady=15)
    opciones = ["3", "6", "9"]
    respuesta_correcta = "6"

    def verificar(respuesta):
        if respuesta == respuesta_correcta:
            messagebox.showinfo("¡Correcto!", "✅ Muy bien, el M.C.D de 12 y 18 es 6.")
        else:
            messagebox.showwarning("Incorrecto", "❌ No es correcto, intentá nuevamente.")

    for opcion in opciones:
        tk.Button(
            scrollable_frame,
            text=opcion,
            width=10,
            height=1,
            bg="#c5e1a5",
            font=("Arial", 12, "bold"),
            command=lambda o=opcion: verificar(o)
        ).pack(pady=5)

    # Ejercicio 2
    tk.Label(
        scrollable_frame,
        text="\n🎯 Ejercicio 2: ¿Cuál es el M.C.M de 4 y 6?",
        font=("Arial", 13, "bold"),
        bg="#f1f8e9"
    ).pack(pady=15)
    opciones2 = ["8", "10", "12"]
    respuesta_correcta2 = "12"

    def verificar2(respuesta):
        if respuesta == respuesta_correcta2:
            messagebox.showinfo("¡Correcto!", "✅ Excelente, el M.C.M de 4 y 6 es 12.")
        else:
            messagebox.showwarning("Incorrecto", "❌ No es correcto, intentá nuevamente.")

    for opcion in opciones2:
        tk.Button(
            scrollable_frame,
            text=opcion,
            width=10,
            height=1,
            bg="#aed581",
            font=("Arial", 12, "bold"),
            command=lambda o=opcion: verificar2(o)
        ).pack(pady=5)

    # Botón volver al menú
    tk.Button(
        scrollable_frame,
        text="Volver al menú principal",
        command=ventana.destroy,
        bg="#9fd8df",
        font=("Arial", 12, "bold")
    ).pack(pady=25)

