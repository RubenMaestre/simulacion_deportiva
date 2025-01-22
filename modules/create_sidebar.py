# modules/create_sidebar.py
import streamlit as st
from streamlit_option_menu import option_menu
from paginas import inicio

def create_sidebar():
    # Texto personalizado en el sidebar
    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Simulación de Inversión en Apuestas de Fútbol<br>'
        f'Un proyecto de Rubén Maestre'
        f'</div>',
        unsafe_allow_html=True
    )

    # Menú lateral
    with st.sidebar:
        selected = option_menu(
            "Menú",
            ["Inicio"],
            icons=["house"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical"
        )

    # Redirigir según selección
    if selected == "Inicio":
        inicio.display()
