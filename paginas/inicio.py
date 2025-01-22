# paginas/inicio.py
import streamlit as st

def display():
    # Cabecera del proyecto
    st.image('sources/logo.png', use_container_width=True)  # Cambiado el parámetro
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Título
    st.markdown(
        "<h1 style='text-align: center;'>Simulación de Inversión en Apuestas de Fútbol</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Contenido inicial
    col1, col2, col3 = st.columns([5, 0.5, 2])

    with col1:
        st.markdown("""
            <div style='text-align: justify;'>
                <h3>Introducción</h3>
                <p>Este proyecto tiene como objetivo desarrollar una simulación de inversión en apuestas deportivas basada en datos históricos de fútbol. Analizaremos patrones, evaluaremos cuotas y determinaremos estrategias para maximizar los retornos a largo plazo.</p>
                <p>La simulación abarca más de una década de datos de partidos de la Primera División Española, incluyendo equipos icónicos como el <strong>FC Barcelona</strong> y el <strong>Real Madrid</strong>.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.write("")

    with col3:
        st.image("sources/logo.png", use_container_width=True)  # Cambiado el parámetro

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns([5, 0.8, 5])

    with col4:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4>El Equipo</h4>
                Este proyecto ha sido desarrollado por <strong>Rubén Maestre</strong>, combinando conocimientos en ciencia de datos, IA y estrategias de marketing digital para abordar problemas prácticos del mundo de las apuestas deportivas.
            </div>
        """, unsafe_allow_html=True)

    with col5:
        st.write("")

    with col6:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4>Objetivo y Enfoque</h4>
                Este proyecto busca responder preguntas clave, como:
                <ul>
                    <li>¿Es posible construir una estrategia ganadora en apuestas deportivas a largo plazo?</li>
                    <li>¿Cómo afectan las cuotas y resultados históricos al rendimiento de una inversión?</li>
                </ul>
                Nuestra metodología combina análisis estadístico y simulaciones para evaluar el desempeño de diferentes estrategias de apuestas.
            </div>
        """, unsafe_allow_html=True)
