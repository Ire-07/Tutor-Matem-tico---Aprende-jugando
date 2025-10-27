import streamlit as st
from PIL import Image
import os

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "recursos", "logo.png")
img = Image.open(img_path)
st.image(img, width=150)

