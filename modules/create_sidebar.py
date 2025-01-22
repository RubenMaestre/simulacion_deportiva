# modules/create_sidebar.py
import streamlit as st
from paginas import inicio, datos  # Asegúrate de importar datos.py

def create_sidebar():
    # Crear el menú lateral
    menu = st.sidebar.radio(
        "Menú",
        ["Inicio", "Datos", "EDA", "Modelo", "Sobre el proyecto", "Sobre nosotros"]
    )

    # Redirigir según la selección
    if menu == "Inicio":
        inicio.display()
    elif menu == "Datos":
        datos.display()  # Llama a la función display() de datos.py
    elif menu == "EDA":
        st.write("Análisis Exploratorio de Datos (EDA)")
    elif menu == "Modelo":
        st.write("Página del modelo")
    elif menu == "Sobre el proyecto":
        st.write("Información sobre el proyecto")
    elif menu == "Sobre nosotros":
        st.write("Información sobre nosotros")
