import streamlit as st
from PIL import Image, ImageOps

# 1. ENTRADA
st.title("🎨 MKFlyer: Configurador Visual")

st.sidebar.header("Configuración")
archivo_subido = st.sidebar.file_opener = st.file_uploader("Sube tu póster (JPG/PNG)", type=["jpg", "png", "jpeg"])
color_nombre = st.sidebar.selectbox("Color del marco:", ["Negro", "Blanco", "Rojo", "Azul", "Madera"])
grosor = st.sidebar.slider("Grosor del marco:", 10, 100, 30)

# 2. PROCESO
# Mapeo de colores a valores RGB
colores_rgb = {
    "Negro": (10, 10, 10),
    "Blanco": (250, 250, 250),
    "Rojo": (200, 0, 0),
    "Azul": (0, 0, 150),
    "Madera": (139, 69, 19)
}

if archivo_subido is not None:
    # Abrir la imagen
    imagen = Image.open(archivo_subido)
    
    # Aplicar el marco (Proceso técnico)
    # Expand agrega un borde a la imagen original
    imagen_con_marco = ImageOps.expand(imagen, border=grosor, fill=colores_rgb[color_nombre])
    
    # 3. SALIDA
    st.subheader("Previsualización MKFlyer")
    st.image(imagen_con_marco, caption=f"Póster con marco {color_nombre}", use_column_width=True)
    
    # Botón para descargar el resultado
    st.success("¡Marco aplicado con éxito!")
else:
    st.warning("Por favor, sube una imagen en el menú de la izquierda para empezar.")

st.caption("Desarrollado por Angie Barrera | MKFlyer Live Preview")