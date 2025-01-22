import streamlit as st

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
# Agrega más opciones según sea necesario

