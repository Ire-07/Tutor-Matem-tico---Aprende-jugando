import tkinter as tk
from tkinter import messagebox

def mostrar_modulo(root):
    ventana = tk.Toplevel(root)
    ventana.title("Criterios de Divisibilidad - Tutor Matemático")
    ventana.geometry("750x580")
    ventana.configure(bg="#e3f2fd")

    # Frame principal con canvas y scrollbar
    frame_principal = tk.Frame(ventana, bg="#e3f2fd")
    frame_principal.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_principal, bg="#e3f2fd", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#e3f2fd")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Título
    tk.Label(
        scrollable_frame,
        text="🧮 CRITERIOS DE DIVISIBILIDAD",
        font=("Comic Sans MS", 20, "bold"),
        fg="#0d47a1",
        bg="#e3f2fd"
    ).pack(pady=10)

    # Teoría
    teoria = (
        "📘 *¿Qué son los criterios de divisibilidad?*\n\n"
        "Son reglas que nos permiten saber si un número es divisible por otro,\n"
        "sin necesidad de hacer la división.\n\n"
        "📗 *Criterio del 2:* Un número es divisible por 2 si termina en cifra par (0, 2, 4, 6, 8).\n"
        "➡ Ejemplo: 124 es divisible por 2 porque termina en 4.\n\n"
        "📙 *Criterio del 3:* Un número es divisible por 3 si la suma de sus cifras es múltiplo de 3.\n"
        "➡ Ejemplo: 123 → 1+2+3 = 6 (múltiplo de 3) ✅\n\n"
        "📕 *Criterio del 5:* Un número es divisible por 5 si termina en 0 o 5.\n"
        "➡ Ejemplo: 85 → termina en 5 ✅\n\n"
        "📒 *Criterio del 9:* Un número es divisible por 9 si la suma de sus cifras es múltiplo de 9.\n"
        "➡ Ejemplo: 729 → 7+2+9 = 18 (múltiplo de 9) ✅"
    )

    tk.Label(
        scrollable_frame,
        text=teoria,
        font=("Arial", 12),
        justify="left",
        bg="#e3f2fd",
        fg="#333",
        wraplength=700
    ).pack(padx=20, pady=10)

    # Separador
    tk.Label(scrollable_frame, text="──────────────────────────────", bg="#e3f2fd", fg="#999").pack(pady=5)

    # Función para generar ejercicios dinámicamente
    ejercicios = [
        ("🎯 Ejercicio 1: ¿Cuál de estos números es divisible por 2?", ["153", "248", "575"], "248",
         "✅ Muy bien, 248 es divisible por 2 porque termina en 8.", "❌ No es correcto, repasá el criterio del 2."),
        ("🎯 Ejercicio 2: ¿Cuál de estos números es divisible por 3?", ["247", "333", "520"], "333",
         "✅ 3+3+3 = 9, múltiplo de 3. ¡Excelente!", "❌ Recordá: sumá las cifras y revisá si es múltiplo de 3."),
        ("🎯 Ejercicio 3: ¿Cuál de estos números es divisible por 5?", ["112", "145", "338"], "145",
         "✅ Termina en 5, por lo tanto es divisible por 5.", "❌ Fijate en la última cifra, debe ser 0 o 5."),
    ]

    for texto, opciones, correcta, mensaje_ok, mensaje_error in ejercicios:
        tk.Label(
            scrollable_frame,
            text=texto,
            font=("Arial", 13, "bold"),
            bg="#e3f2fd"
        ).pack(pady=15)

        def generar_verificador(correcta, mensaje_ok, mensaje_error):
            return lambda respuesta: messagebox.showinfo("¡Correcto!", mensaje_ok) if respuesta == correcta else messagebox.showwarning("Incorrecto", mensaje_error)

        for opcion in opciones:
            tk.Button(
                scrollable_frame,
                text=opcion,
                width=10,
                bg="#bbdefb",
                font=("Arial", 12, "bold"),
                command=generar_verificador(correcta, mensaje_ok, mensaje_error)
            ).pack(pady=5)

    # Botón volver al menú
    tk.Button(
        scrollable_frame,
        text="Volver al menú principal",
        command=ventana.destroy,
        bg="#42a5f5",
        font=("Arial", 12, "bold")
    ).pack(pady=25)
