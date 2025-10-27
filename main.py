import streamlit as st
from PIL import Image

st.title("Tutor Matemático - Aprende Jungando en ControlMax")

# Mostrar imagen
img = Image.open("recursos\logo.png")
st.image(img, width=150)

# Interacción con el usuario
num = st.number_input("Ingresa un número", min_value=1, max_value=100)
st.write(f"El número que ingresaste es {num}")
