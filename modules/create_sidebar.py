import streamlit as st

def create_sidebar():
    # Crear un menú básico en el sidebar
    menu = st.sidebar.radio(
        "Menú",
        ["Inicio", "Datos", "EDA", "Modelo", "Sobre el proyecto", "Sobre nosotros"]
    )

    # Redirigir según la selección
    if menu == "Inicio":
        st.write("Página de inicio")
    elif menu == "Datos":
        st.write("Página de datos")
    elif menu == "EDA":
        st.write("Análisis Exploratorio de Datos (EDA)")
    elif menu == "Modelo":
        st.write("Página del modelo")
    elif menu == "Sobre el proyecto":
        st.write("Información sobre el proyecto")
    elif menu == "Sobre nosotros":
        st.write("Información sobre nosotros")

