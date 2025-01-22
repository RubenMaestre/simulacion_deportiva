import streamlit as st  # Biblioteca principal para crear la aplicación web
from streamlit_option_menu import option_menu  # Librería para diseñar un menú de navegación visual y funcional
from paginas import inicio, datos, simulacion, doblo_apuesta  # Importamos las páginas de la aplicación

# Función para crear la barra lateral
def create_sidebar():
    # Añadir un encabezado personalizado en la barra lateral
    # Este bloque utiliza HTML y Markdown para mostrar el nombre del creador del proyecto con un diseño centrado y elegante.
    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'Rubén Maestre'
        f'</div>',
        unsafe_allow_html=True  # Permite incluir HTML en el Markdown
    )

    # Crear el menú de navegación en la barra lateral
    # Este menú permite al usuario moverse fácilmente entre las diferentes secciones de la aplicación: Inicio, Datos y Simulación.
    with st.sidebar:  # El menú se define dentro de la barra lateral
        selected = option_menu(
            "Menú",  # Título del menú
            ["Inicio", "Datos", "Simulación", "Doblo Apuesta"],  # Opciones disponibles en el menú
            icons=["house", "database", "calculator", "arrow-up-right-circle"],  # Íconos asociados a cada opción
            menu_icon="cast",  # Ícono general del menú
            default_index=0,  # Opción seleccionada por defecto al iniciar la aplicación
            orientation="vertical"  # Configura el menú en formato vertical para un diseño más intuitivo
        )

    # Redirigir a la función correspondiente según la selección del menú
    # Cada página tiene su propia lógica y visualización, que se activa al seleccionar la opción correspondiente.
    if selected == "Inicio":
        inicio.display()  # Muestra la página de Inicio
    elif selected == "Datos":
        datos.display()  # Muestra la página de Datos
    elif selected == "Simulación":
        simulacion.display()  # Muestra la página de Simulación
    elif selected == "Doblo Apuesta":
        doblo_apuesta.display()  # Muestra la página de Doblo Apuesta
