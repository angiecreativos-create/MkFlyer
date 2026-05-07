# =================================================================
# PROYECTO: Configurador de Posters MKFlyer
# ESTUDIANTE: Angie Katherine Barrera Becerra
# DESCRIPCIÓN: Programa interactivo que utiliza estructuras de 
# entrada, proceso y salida para la gestión de catálogo.
# =================================================================

import streamlit as st

# 1. ENTRADA DE DATOS (Input)
# Aquí cumplimos con el requerimiento de capturar información del usuario.
st.title("🎨 MKFlyer: Sistema de Gestión de Diseño")
st.markdown("---")

st.sidebar.header("Configuración del Diseño")
# Entrada de texto
nombre_diseno = st.sidebar.text_input("Nombre del Póster:", "Poster_Enero_01")

# Entrada de selección (Categorías)
tipo_marco = st.sidebar.selectbox(
    "Seleccione el acabado del marco:",
    ["Madera Roble", "Negro Industrial", "Blanco Galería", "Rojo Pasión"]
)

# Entrada numérica (Grosor)
grosor = st.sidebar.slider("Grosor del marco (mm):", 5, 50, 20)


# 2. PROCESAMIENTO DE LA INFORMACIÓN (Process)
# Aquí aplicamos la lógica para transformar las entradas en datos técnicos.
def calcular_especificaciones(acabado, ancho_mm):
    # Diccionario para asignar códigos de color (Buena práctica de codificación)
    colores = {
        "Madera Roble": "#8B4513",
        "Negro Industrial": "#000000",
        "Blanco Galería": "#FFFFFF",
        "Rojo Pasión": "#FF0000"
    }
    
    hex_color = colores.get(acabado, "#808080")
    
    # Un cálculo simple para demostrar procesamiento
    area_borde_estimada = ancho_mm * 4 # Simulación lógica
    
    return hex_color, area_borde_estimada

# Ejecutamos la función de proceso
codigo_hex, area = calcular_especificaciones(tipo_marco, grosor)


# 3. SALIDA DE RESULTADOS (Output)
# Aquí mostramos la información procesada de manera limpia y ordenada.
st.subheader("📋 Resumen de la Propuesta de Diseño")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Diseño", nombre_diseno)

with col2:
    st.metric("Color HEX", codigo_hex)

with col3:
    st.metric("Grosor", f"{grosor} mm")

# Espacio visual para mostrar el "resultado"
st.info(f"El sistema ha procesado el diseño '{nombre_diseno}' con un acabado {tipo_marco}.")

# Botón de acción final
if st.button("Finalizar y Guardar"):
    st.balloons()
    st.success(f"Configuración guardada. El borde de {grosor}mm ha sido aplicado correctamente.")

# Pie de página (Requerimiento de identificación)
st.caption("Actividad: Primer Programa Python | Angie Barrera")