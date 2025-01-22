# app.py
from modules.config_page import set_global_page_config
import streamlit as st
from modules.create_sidebar import create_sidebar

# Configuración global de la página
set_global_page_config()

# Barra lateral y menú
create_sidebar()

