# modules/config_page.py
import streamlit as st  # Importamos Streamlit, la herramienta principal para crear aplicaciones web interactivas

# Función para configurar los parámetros globales de la página
def set_global_page_config():
    # Configuración general de la aplicación
    # Aquí definimos elementos clave que afectan a toda la aplicación, como el título, el ícono y el diseño.
    st.set_page_config(
        page_title="¿Es rentable apostar por el Barcelona o el Madrid toda una temporada?",  # Título que aparecerá en la pestaña del navegador
        page_icon="⚽",  # Ícono que se mostrará junto al título, en este caso un balón de fútbol
        layout="wide"  # Diseño amplio que aprovecha todo el espacio disponible en pantalla
    )
