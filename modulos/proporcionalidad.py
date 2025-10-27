import tkinter as tk
from tkinter import messagebox

def mostrar_modulo(root):
    ventana = tk.Toplevel(root)
    ventana.title("Proporcionalidad Directa e Inversa - Tutor Matemático")
    ventana.geometry("780x600")
    ventana.configure(bg="#fff3e0")

    # Frame principal con canvas y scrollbar
    frame_principal = tk.Frame(ventana, bg="#fff3e0")
    frame_principal.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame_principal, bg="#fff3e0", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#fff3e0")

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
        text="⚖️ PROPORCIONALIDAD DIRECTA E INVERSA",
        font=("Comic Sans MS", 20, "bold"),
        fg="#e65100",
        bg="#fff3e0"
    ).pack(pady=10)

    # Teoría
    teoria = (
        "📘 *¿Qué es la proporcionalidad?*\n"
        "Dos magnitudes son proporcionales cuando al cambiar una, la otra cambia de forma predecible.\n\n"
        "📗 *Proporcionalidad directa:*\n"
        "Cuando una magnitud aumenta, la otra también lo hace en la misma razón.\n"
        "Ejemplo: si duplico la cantidad de cuadernos, también duplico el costo.\n"
        "→ y = kx (constante de proporcionalidad).\n\n"
        "📙 *Proporcionalidad inversa:*\n"
        "Cuando una magnitud aumenta, la otra disminuye en la misma proporción.\n"
        "Ejemplo: si duplico la cantidad de obreros, el tiempo de trabajo se reduce a la mitad.\n"
        "→ y = k/x.\n\n"
        "📏 *Regla de tres:*\n"
        "Permite calcular un valor desconocido en una proporción:\n"
        "a/b = c/x → x = (b * c) / a"
    )

    tk.Label(
        scrollable_frame,
        text=teoria,
        font=("Arial", 12),
        justify="left",
        bg="#fff3e0",
        fg="#4e342e",
        wraplength=740
    ).pack(padx=20, pady=10)

    # Ejercicio 1
    tk.Label(
        scrollable_frame,
        text="\n🎯 Ejercicio 1: Si 4 manzanas cuestan $8, ¿cuánto costarán 10 manzanas?",
        font=("Arial", 13, "bold"),
        bg="#fff3e0"
    ).pack(pady=10)

    respuesta_correcta = 20
    entrada = tk.Entry(scrollable_frame, font=("Arial", 12), width=8)
    entrada.pack()

    def verificar():
        try:
            valor = float(entrada.get())
            if valor == respuesta_correcta:
                messagebox.showinfo("¡Correcto!", "✅ 4:8 = 10:x → x = 20. Es proporcionalidad directa.")
            else:
                messagebox.showwarning("Incorrecto", "❌ Revisá la regla de tres: (8×10)/4 = 20.")
        except:
            messagebox.showerror("Error", "Ingresa un número válido.")

    tk.Button(
        scrollable_frame,
        text="Verificar respuesta",
        bg="#ffcc80",
        font=("Arial", 12, "bold"),
        command=verificar
    ).pack(pady=5)

    # Ejercicio 2
    tk.Label(
        scrollable_frame,
        text="\n🎯 Ejercicio 2: Si 6 obreros hacen una obra en 12 días, ¿cuántos días tardan 12 obreros?",
        font=("Arial", 13, "bold"),
        bg="#fff3e0"
    ).pack(pady=10)

    entrada2 = tk.Entry(scrollable_frame, font=("Arial", 12), width=8)
    entrada2.pack()

    def verificar2():
        try:
            valor = float(entrada2.get())
            if valor == 6:
                messagebox.showinfo("¡Correcto!", "✅ Es proporcionalidad inversa: (6×12)=12×x → x=6.")
            else:
                messagebox.showwarning("Incorrecto", "❌ Revisá: más obreros → menos días (inversa).")
        except:
            messagebox.showerror("Error", "Ingresa un número válido.")

    tk.Button(
        scrollable_frame,
        text="Verificar respuesta",
        bg="#ffb74d",
        font=("Arial", 12, "bold"),
        command=verificar2
    ).pack(pady=5)

    # Botón volver al menú
    tk.Button(
        scrollable_frame,
        text="Volver al menú principal",
        command=ventana.destroy,
        bg="#66bb6a",
        font=("Arial", 12, "bold")
    ).pack(pady=20)
