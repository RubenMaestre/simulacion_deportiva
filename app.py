from modules.config_page import set_global_page_config
from modules.create_sidebar import create_sidebar
import streamlit as st

# Configuración global de la página
set_global_page_config()

# Crear la barra lateral y redirigir al contenido correspondiente
create_sidebar()


