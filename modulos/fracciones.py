import tkinter as tk
from tkinter import messagebox

def mostrar_modulo(root):
    ventana = tk.Toplevel(root)
    ventana.title("Fracciones - Tutor Matemático")
    ventana.geometry("750x550")
    ventana.configure(bg="#fef6e4")

    # Frame principal con canvas y scrollbar
    frame_principal = tk.Frame(ventana, bg="#fef6e4")
    frame_principal.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_principal, bg="#fef6e4", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#fef6e4")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Título
    tk.Label(
        scrollable_frame,
        text="🍰 FRACCIONES",
        font=("Comic Sans MS", 20, "bold"),
        fg="#ff6f61",
        bg="#fef6e4"
    ).pack(pady=10)

    # Teoría
    teoria = (
        "Una fracción representa una parte de un todo.\n\n"
        "➡ El número de arriba se llama *numerador* y muestra cuántas partes tomamos.\n"
        "➡ El número de abajo se llama *denominador* y muestra en cuántas partes se divide el todo.\n\n"
        "Ejemplo: 1/2 significa una mitad, o una parte de dos iguales.\n\n"
        "🔹 Fracciones equivalentes: Son fracciones diferentes que representan la misma cantidad.\n"
        "Imaginá dos pizzas del mismo tamaño:\n"
        "🍕 Pizza A: la cortás en 2 partes y comés 1 → 1/2\n"
        "🍕 Pizza B: la cortás en 4 partes y comés 2 → 2/4\n"
        "Aunque los números son distintos, comiste la misma cantidad de pizza 😋\n"
        "Por eso 1/2 y 2/4 son fracciones equivalentes. Representan la misma cantidad, aunque tengan distintos números.\n"
        "Ejemplo: 1/2 = 2/4 = 3/6\n\n"
        "🔹 Fracción simple o irreducible: Una fracción simple es la versión más pequeña posible de una fracción equivalente.\n"
        "👉 Es la que ya no se puede simplificar más.\n"
        "Ejemplo: 4/8 → 4÷4 / 8÷4 = 1/2"
    )

    tk.Label(
        scrollable_frame,
        text=teoria,
        font=("Arial", 12),
        justify="left",
        bg="#fef6e4",
        fg="#333",
        wraplength=700
    ).pack(padx=10, pady=10)

    # Separador
    tk.Label(
        scrollable_frame,
        text="──────────────────────────────",
        bg="#fef6e4",
        fg="#999"
    ).pack(pady=5)

    # Ejercicio interactivo
    tk.Label(
        scrollable_frame,
        text="🎯 Ejercicio: ¿Cuál de estas fracciones es equivalente a 1/2?",
        font=("Arial", 13, "bold"),
        bg="#fef6e4"
    ).pack(pady=15)

    opciones = ["2/3", "2/4", "3/8"]
    respuesta_correcta = "2/4"

    def verificar(respuesta):
        if respuesta == respuesta_correcta:
            messagebox.showinfo("¡Correcto!", "✅ ¡Muy bien! 1/2 y 2/4 representan la misma cantidad.")
        else:
            messagebox.showwarning("Incorrecto", "❌ No es correcto, intentá nuevamente.")

    for opcion in opciones:
        tk.Button(
            scrollable_frame,
            text=opcion,
            width=10,
            height=1,
            bg="#dbe7f0",
            font=("Arial", 12, "bold"),
            command=lambda o=opcion: verificar(o)
        ).pack(pady=5)

    # Botón volver al menú
    tk.Button(
        scrollable_frame,
        text="Volver al menú principal",
        command=ventana.destroy,
        bg="#9fd8df",
        font=("Arial", 12, "bold")
    ).pack(pady=20)
