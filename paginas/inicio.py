import streamlit as st

def display():
    # Título
    st.markdown(
        "<h1 style='text-align: center;'>Simulación de Inversión en Apuestas de Fútbol</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción personal
    col1, col2, col3 = st.columns([5, 0.5, 2])

    with col1:
        st.markdown("""
            <div style='text-align: justify;'>
                <h3>Introducción</h3>
                <p>
                    Siempre me había preguntado si comenzabas desde la jornada 1 apostando una cantidad fija cada semana
                    al <strong>FC Barcelona</strong> o al <strong>Real Madrid</strong>, ¿a final de temporada ganarías dinero o lo perderías?
                </p>
                <p>
                    Con esa duda en mente, me puse manos a la obra. Primero, recogí los datos de partidos desde la temporada
                    2012/2013 hasta la actual. Organizé la información en una gran base de datos y me dediqué a limpiarla para
                    quedarme solo con lo que realmente necesitaba. Entre esos datos, también incluí la media de las cuotas de
                    las casas de apuestas.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.write("")

    with col3:
        st.write("")

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Explicación del proyecto
    col4, col5, col6 = st.columns([5, 0.8, 5])

    with col4:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4>Metodología</h4>
                <p>
                    He creado diferentes documentos por temporada, separando los partidos de cada año. Tampoco me he complicado
                    mucho ajustando las cuotas, porque suelen ser bastante similares en todas las casas de apuestas, especialmente
                    cuando estos equipos se enfrentan a rivales inferiores.
                </p>
                <p>
                    La idea principal fue analizar los resultados de apostar una cantidad fija cada semana y ver si, al final de la temporada,
                    las ganancias superaban a las pérdidas.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col5:
        st.write("")

    with col6:
        st.markdown("""
            <div style='text-align: justify;'>
                <h4>Las páginas del proyecto</h4>
                <p>
                    He dividido este proyecto en dos páginas principales:
                </p>
                <ul>
                    <li>
                        <strong>Página de datos</strong>: En esta sección puedes ver el número de victorias, empates y derrotas del <strong>FC Barcelona</strong>
                        y del <strong>Real Madrid</strong> para cada temporada.
                    </li>
                    <li>
                        <strong>Página de simulación</strong>: Aquí puedes introducir una cantidad fija para apostar semanalmente y descubrir si ganarías
                        dinero o no al final de la temporada. Además, puedes filtrar para que solo se consideren los partidos de local,
                        de visitante, o todos los partidos de la temporada.
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Cierre
    st.markdown("""
        <div style='text-align: justify;'>
            <h4>Conclusión</h4>
            <p>
                Este proyecto es una combinación de análisis de datos y simulaciones financieras aplicadas al mundo de las apuestas deportivas.
                Si te interesa descubrir si apostar al <strong>FC Barcelona</strong> o al <strong>Real Madrid</strong> es una estrategia ganadora,
                te invito a explorar cada una de las páginas y probar diferentes escenarios.
            </p>
        </div>
    """, unsafe_allow_html=True)
