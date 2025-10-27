import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def mostrar_modulo(root):
    ventana = tk.Toplevel(root)
    ventana.title("Paralelogramos y su Construcción - Tutor Matemático")
    ventana.geometry("780x600")
    ventana.configure(bg="#e8f5e9")

    # Frame principal con scroll
    frame_principal = tk.Frame(ventana, bg="#e8f5e9")
    frame_principal.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_principal, bg="#e8f5e9", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#e8f5e9")

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
        text="📐 PARALELOGRAMOS Y SU CONSTRUCCIÓN",
        font=("Comic Sans MS", 20, "bold"),
        fg="#1b5e20",
        bg="#e8f5e9"
    ).pack(pady=10)

    # Teoría
    teoria = (
        "📘 *Definición:*\n"
        "Un paralelogramo es un cuadrilátero que tiene sus lados opuestos paralelos.\n"
        "Los lados opuestos son iguales y sus ángulos opuestos también.\n\n"
        "📗 *Tipos de paralelogramos:*\n"
        "• **Rombo** → todos los lados son iguales y sus diagonales se cruzan en ángulo recto.\n"
        "• **Rectángulo** → tiene ángulos rectos (90°) y lados opuestos iguales.\n"
        "• **Romboide** → lados opuestos iguales, pero sin ángulos rectos.\n"
        "• **Cuadrado** → tiene todos los lados iguales y ángulos rectos.\n\n"
        "📏 *Propiedades principales:*\n"
        "✔ Los lados opuestos son paralelos e iguales.\n"
        "✔ Las diagonales se cortan por la mitad.\n"
        "✔ Los ángulos opuestos son iguales.\n"
        "✔ La suma de los ángulos interiores es 360°."
    )

    tk.Label(
        scrollable_frame,
        text=teoria,
        font=("Arial", 12),
        justify="left",
        bg="#e8f5e9",
        fg="#2e7d32",
        wraplength=740
    ).pack(padx=20, pady=10)

    # Imagen ilustrativa
    ruta_imagen = r"C:\Users\Irene\OneDrive\Desktop\Proyectos\Matematicas\recursos\paralelogramos.png"
    if os.path.exists(ruta_imagen):
        img = Image.open(ruta_imagen)
        img = img.resize((300, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        label_img = tk.Label(scrollable_frame, image=img_tk, bg="#e8f5e9")
        label_img.image = img_tk  # <-- Mantener referencia
        label_img.pack(pady=5)
    else:
        tk.Label(
            scrollable_frame,
            text="🖼 (Agrega una imagen llamada 'paralelogramo.png' en la carpeta recursos)",
            bg="#e8f5e9",
            fg="#388e3c"
        ).pack(pady=5)

    # Ejercicio interactivo
    tk.Label(
        scrollable_frame,
        text="\n🎯 Ejercicio: ¿Cuál de los siguientes es un paralelogramo?",
        font=("Arial", 13, "bold"),
        bg="#e8f5e9"
    ).pack(pady=15)

    opciones = ["Triángulo", "Rombo", "Trapecio"]
    respuesta_correcta = "Rombo"

    def verificar(opcion):
        if opcion == respuesta_correcta:
            messagebox.showinfo("¡Correcto!", "✅ El rombo es un paralelogramo con todos sus lados iguales.")
        else:
            messagebox.showwarning("Incorrecto", "❌ Ese no cumple la condición de tener lados opuestos paralelos.")

    for op in opciones:
        tk.Button(
            scrollable_frame,
            text=op,
            width=12,
            bg="#a5d6a7",
            font=("Arial", 12, "bold"),
            command=lambda o=op: verificar(o)
        ).pack(pady=5)

    # Botón volver al menú
    tk.Button(
        scrollable_frame,
        text="Volver al menú principal",
        command=ventana.destroy,
        bg="#66bb6a",
        font=("Arial", 12, "bold")
    ).pack(pady=20)

