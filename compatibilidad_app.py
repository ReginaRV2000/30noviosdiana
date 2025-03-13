import streamlit as st
import pandas as pd
from streamlit_extras.let_it_rain import rain

# Cargar los datos del CSV
compatibilidad = pd.read_csv("compatibilidad_diana2.csv")

# Configurar la página
st.set_page_config(page_title="Los 30 novios de Diana", page_icon="❤️", layout="centered")

# Título con letras grandes y rojas entre dos corazones
st.markdown(
    "<h1 style='text-align: center; color: red;'>❤️ ❤️ Los 30 Novios  de Diana ❤️ ❤️</h1>",
    unsafe_allow_html=True
)

# Mostrar texto debajo del título
st.markdown(
    "<h3 style='text-align: center; font-weight: bold;'>¿Qué galán será el mejor para Diana?</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<h6 style='text-align: center;'>Hecho por Regina, Diana, Gisele, y Giovanni</h6>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 16px;'> Instrucciones: Selecciona el checkbox del galán que mejor te parezca como pareja de Diana. ¡Haz tu elección y ve qué tan compatible es con ella!</p>",
    unsafe_allow_html=True
)

# Función para lanzar lluvia de emojis basada en Compatibilidad_num
def emoji_rain(compatibilidad_num):
    if compatibilidad_num >= 95:
        rain(emoji="👰", font_size=54, falling_speed=10, animation_length="infinite")
    elif 90 <= compatibilidad_num < 95:
        rain(emoji="💗", font_size=54, falling_speed=10, animation_length="infinite")
    elif 86 <= compatibilidad_num < 90:
        rain(emoji="💋", font_size=54, falling_speed=10, animation_length="infinite")
    elif 81 <= compatibilidad_num < 86:
        rain(emoji="🫤", font_size=54, falling_speed=10, animation_length="infinite")
    elif 71 <= compatibilidad_num < 81:
        rain(emoji="👎", font_size=54, falling_speed=10, animation_length="infinite")
    else:
        rain(emoji="😵", font_size=54, falling_speed=10, animation_length="infinite")

# Función para mostrar la frase según la compatibilidad
def compatibilidad_frase(compatibilidad_num):
    if compatibilidad_num >= 95:
        return "**_SUENAN LAS CAMPANAS, es hora de casarse.... (si crees en el matrimonio)_** Escucha el sonido de su amor aquí:"
    elif 90 <= compatibilidad_num < 95:
        return "**_La pareja casi perfecta, 😎_** Escucha el sonido de su amor aquí:"
    elif 86 <= compatibilidad_num < 90:
        return "**_¡Se ven bien juntos!_** Escucha el sonido de su amor aquí:"
    elif 81 <= compatibilidad_num < 86:
        return "**_Pues... si no hay otra opción..._** Escucha el sonido de su amor aquí:"
    elif 71 <= compatibilidad_num < 81:
        return "**_no creemos que sea buena idea..._** Escucha el sonido de su amor aquí:"
    else:
        return "**_mejor otra opción..._**"

# Función para reproducir sonido
def play_sound(compatibilidad_num):
    if compatibilidad_num >= 95:
        return "church.mp3"
    elif 90 <= compatibilidad_num < 95:
        return "applause.mp3"
    elif 86 <= compatibilidad_num < 90:
        return "aww.mp3"
    elif 81 <= compatibilidad_num < 86:
        return "cricket.mp3"
    elif 71 <= compatibilidad_num < 81:
        return "boo.mp3"
    else:
        return "fail.mp3"

# Iterar sobre cada actor y mostrar el checkbox con la imagen al lado
for index, row in compatibilidad.iterrows():
    # Mostrar checkbox y foto del actor al lado
    col1, col2 = st.columns([1, 5])  # Define dos columnas: una más pequeña para la imagen y una más grande para el checkbox
    
    with col1:
        st.image(row['Imagen'], width=50)  # Mostrar la imagen del actor (con tamaño pequeño)
    
    with col2:
        # Crear el checkbox al lado de la imagen
        checked = st.checkbox(f"{row['Nombre']}", key=row['Nombre'])
    
    # Si el checkbox está marcado, mostrar la compatibilidad y reproducir el audio
    if checked:
        compatibilidad_num = row['Compatibilidad_num']  # Extraer el número de compatibilidad
        
        # Mostrar la compatibilidad de Diana con el actor
        st.write(f"Compatibilidad de Diana con {row['Nombre']}: {row['Compatibilidad']} ❤️✨  {compatibilidad_frase(compatibilidad_num)}")

        # Llamar la función para el emoji de lluvia
        emoji_rain(compatibilidad_num)

        # Reproducir el sonido correspondiente
        st.audio(play_sound(compatibilidad_num), format="audio/mp3")

#streamlit run /Users/regina/Documents/Next/WebScrapping/Proyecto Final Web/ compatibilidad_app.py