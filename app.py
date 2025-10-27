import tkinter as tk
from tkinter import messagebox
from modulos import fracciones, multiplos_mcd, divisibilidad, paralelogramos, proporcionalidad
import tkinter as tk
from PIL import Image, ImageTk 

# ==============================
# Ventana principal del software educativo
# ==============================
class TutorMatematicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tutor Matemático - Aprendé Jugando en ControlMax")
        self.root.geometry("700x500")
        self.root.configure(bg="#eaf6ff")
        try:
          # Cargar logo y redimensionar
           logo_img = Image.open(r"C:\Users\Irene\OneDrive\Desktop\Proyectos\Matematicas\recursos\logo.png")
           logo_img = logo_img.resize((40, 40), Image.Resampling.LANCZOS)
           logo_tk = ImageTk.PhotoImage(logo_img)

           # Asegurar que la ventana tenga dimensiones antes de colocar el logo
           self.root.update()
    
            # Crear label y ubicar en esquina superior derecha
           logo_label = tk.Label(self.root, image=logo_tk, bg="#eaf6ff")
           logo_label.place(x=self.root.winfo_width()-50, y=10)  # 10 px desde arriba, 50 px desde derecha
           self.logo_ref = logo_tk  # Mantener referencia
        except Exception as e:
          print("No se pudo cargar el logo:", e)


        # Título principal
        titulo = tk.Label(
            root,
            text="📘 Tutor Matemático\nAprendé jugando en ControlMax",
            font=("Comic Sans MS", 20, "bold"),
            fg="#004c91",
            bg="#eaf6ff",
            justify="center"
        )
        titulo.pack(pady=30)

        # Botones del menú principal
        botones = [
            ("Fracciones", fracciones.mostrar_modulo),
            ("Múltiplos y MCD/MCM", multiplos_mcd.mostrar_modulo),
            ("Criterios de Divisibilidad", divisibilidad.mostrar_modulo),
            ("Paralelogramos y Geometría", paralelogramos.mostrar_modulo),
            ("Proporcionalidad Directa", proporcionalidad.mostrar_modulo)
        ]

        for texto, funcion in botones:
            tk.Button(
                root,
                text=texto,
                command=lambda f=funcion: f(root),
                width=30,
                height=2,
                bg="#9fd8df",
                fg="black",
                font=("Arial", 12, "bold"),
                relief="raised",
                cursor="hand2"
            ).pack(pady=10)

        # Botón para salir
        tk.Button(
            root,
            text="Salir",
            command=self.salir,
            width=20,
            height=1,
            bg="#ff9a8b",
            fg="black",
            font=("Arial", 12, "bold")
        ).pack(pady=30)

    def salir(self):
        if messagebox.askyesno("Salir", "¿Seguro que querés cerrar el Tutor Matemático?"):
            self.root.quit()

# ==============================
# EJECUCIÓN PRINCIPAL
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = TutorMatematicoApp(root)
    root.mainloop()
