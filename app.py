{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # =================================================================\
# PROYECTO: Configurador de Posters MKFlyer\
# ESTUDIANTE: Angie Katherine Barrera Becerra\
# DESCRIPCI\'d3N: Programa interactivo que utiliza estructuras de \
# entrada, proceso y salida para la gesti\'f3n de cat\'e1logo.\
# =================================================================\
\
import streamlit as st\
\
# 1. ENTRADA DE DATOS (Input)\
# Aqu\'ed cumplimos con el requerimiento de capturar informaci\'f3n del usuario.\
st.title("\uc0\u55356 \u57256  MKFlyer: Sistema de Gesti\'f3n de Dise\'f1o")\
st.markdown("---")\
\
st.sidebar.header("Configuraci\'f3n del Dise\'f1o")\
# Entrada de texto\
nombre_diseno = st.sidebar.text_input("Nombre del P\'f3ster:", "Poster_Enero_01")\
\
# Entrada de selecci\'f3n (Categor\'edas)\
tipo_marco = st.sidebar.selectbox(\
    "Seleccione el acabado del marco:",\
    ["Madera Roble", "Negro Industrial", "Blanco Galer\'eda", "Rojo Pasi\'f3n"]\
)\
\
# Entrada num\'e9rica (Grosor)\
grosor = st.sidebar.slider("Grosor del marco (mm):", 5, 50, 20)\
\
\
# 2. PROCESAMIENTO DE LA INFORMACI\'d3N (Process)\
# Aqu\'ed aplicamos la l\'f3gica para transformar las entradas en datos t\'e9cnicos.\
def calcular_especificaciones(acabado, ancho_mm):\
    # Diccionario para asignar c\'f3digos de color (Buena pr\'e1ctica de codificaci\'f3n)\
    colores = \{\
        "Madera Roble": "#8B4513",\
        "Negro Industrial": "#000000",\
        "Blanco Galer\'eda": "#FFFFFF",\
        "Rojo Pasi\'f3n": "#FF0000"\
    \}\
    \
    hex_color = colores.get(acabado, "#808080")\
    \
    # Un c\'e1lculo simple para demostrar procesamiento\
    area_borde_estimada = ancho_mm * 4 # Simulaci\'f3n l\'f3gica\
    \
    return hex_color, area_borde_estimada\
\
# Ejecutamos la funci\'f3n de proceso\
codigo_hex, area = calcular_especificaciones(tipo_marco, grosor)\
\
\
# 3. SALIDA DE RESULTADOS (Output)\
# Aqu\'ed mostramos la informaci\'f3n procesada de manera limpia y ordenada.\
st.subheader("\uc0\u55357 \u56523  Resumen de la Propuesta de Dise\'f1o")\
\
col1, col2, col3 = st.columns(3)\
\
with col1:\
    st.metric("Dise\'f1o", nombre_diseno)\
\
with col2:\
    st.metric("Color HEX", codigo_hex)\
\
with col3:\
    st.metric("Grosor", f"\{grosor\} mm")\
\
# Espacio visual para mostrar el "resultado"\
st.info(f"El sistema ha procesado el dise\'f1o '\{nombre_diseno\}' con un acabado \{tipo_marco\}.")\
\
# Bot\'f3n de acci\'f3n final\
if st.button("Finalizar y Guardar"):\
    st.balloons()\
    st.success(f"Configuraci\'f3n guardada. El borde de \{grosor\}mm ha sido aplicado correctamente.")\
\
# Pie de p\'e1gina (Requerimiento de identificaci\'f3n)\
st.caption("Actividad: Primer Programa Python | Angie Barrera")}