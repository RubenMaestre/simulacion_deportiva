# Importamos las funciones necesarias para configurar la página y crear la barra lateral
from modules.config_page import set_global_page_config  # Configuración global para toda la página
from modules.create_sidebar import create_sidebar  # Genera la barra lateral y maneja la navegación
import streamlit as st  # Biblioteca principal para la creación de la aplicación web

# Configuración global de la página
# Esta función establece parámetros como el título, el ícono y el diseño general de la aplicación.
# Es el primer paso para definir cómo se verá y sentirá tu proyecto.
set_global_page_config()

# Crear la barra lateral
# Con esta función generamos una barra lateral interactiva que permite navegar entre las diferentes secciones de la aplicación.
# Además, redirige automáticamente al contenido correspondiente según la selección del usuario.
create_sidebar()
