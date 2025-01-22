# Importamos la librería Streamlit para crear aplicaciones web interactivas y visualizaciones.
import streamlit as st

# Definimos una función principal para mostrar el contenido de la aplicación.
def display():
    # Título principal, utilizando Markdown con estilo HTML para personalizar el diseño.
    st.markdown(
        "<h1 style='text-align: center;'>Simulación de inversión en apuestas de fútbol</h1>",
        unsafe_allow_html=True  # Permite la interpretación de HTML dentro del Markdown.
    )
    
    # Subtítulo que introduce la pregunta clave del proyecto.
    st.markdown(
        "<h2 style='text-align: center;'>¿Te has preguntado alguna vez si realmente es rentable apostar toda una temporada al Barcelona o al Madrid?</h2>",
        unsafe_allow_html=True
    )
    # Espaciado adicional para mejorar la estética visual.
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Sección de introducción personal, dividida en columnas para un diseño equilibrado.
    col1, col2, col3 = st.columns([5, 0.5, 2])  # Ajustamos el ancho relativo de las columnas.

    with col1:  # Primera columna: contiene el texto de introducción.
        st.markdown("""
            <div style='text-align: justify;'>
                <h3>Introducción</h3>
                <p>
                    Siempre me había preguntado si comenzabas desde la jornada 1 apostando una cantidad fija cada semana
                    al <strong>FC Barcelona</strong> o al <strong>Real Madrid</strong>, ¿A final de temporada ganarías dinero o lo perderías?
                </p>
                <p>
                    Me he planteado si esto podría ser una inversión interesante... Igual que comprar acciones de una compañía tiene sus riesgos 
                    pero puede generar beneficios, ¿Apostar por un equipo de fútbol durante toda una temporada, partido a partido, 
                    puede ser una apuesta rentable?
                </p>
                <p>
                    Con esa duda en mente, me puse manos a la obra. Primero, recogí los datos de partidos desde la temporada 2012/2013 hasta la actual. 
                    Organizé la información en una gran base de datos y me dediqué a limpiarla para quedarme solo con lo que realmente necesitaba. 
                    Entre esos datos, también incluí la media de las cuotas de las casas de apuestas.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:  # Columna del medio: la dejamos vacía para crear un espacio de separación para mantener la página más limpia.
        st.write("")

    with col3:  # Columna derecha: añadimos la imagen del logo.
        st.image("sources/logo.png", width=240)  # Ajustamos el tamaño de la imagen.

    # Más espaciado para mantener un diseño limpio y ordenado.
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Sección explicativa del proyecto, dividida en columnas para destacar diferentes aspectos.
    col4, col5, col6 = st.columns([5, 0.8, 5])  # Columnas equilibradas con un separador estrecho.

    with col4:  # Primera columna de esta sección: metodología.
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

    with col5:  # Separador visual.
        st.write("")

    with col6:  # Segunda columna: descripción de las páginas del proyecto.
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

    # Espaciado final para claridad.
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Reflexión final sobre el proyecto y futuras ideas...
    st.markdown("""
        <div style='text-align: justify;'>
            <h4>Próximos pasos</h4>
            <p>
                Este proyecto es una combinación de análisis de datos y simulaciones financieras aplicadas al mundo de las apuestas deportivas.
                Si te interesa descubrir si apostar al <strong>FC Barcelona</strong> o al <strong>Real Madrid</strong> es una estrategia ganadora,
                te invito a explorar cada una de las páginas y probar diferentes escenarios.
            </p>
            <p>
                Pero no acaba aquí. Igual que tenía curiosidad por el Barcelona y el Madrid, también me ronda la idea de que en la Segunda División 
                del fútbol español todas las semanas hay un alto número de empates. Las cuotas en estos casos suelen ser mayores, lo que plantea una 
                pregunta interesante: ¿Se podría ganar dinero apostando todas las semanas a que hay empates en los partidos de Segunda División? 
                Pues bien, esto lo veremos en la siguiente entrega...
            </p>
        </div>

    """, unsafe_allow_html=True)
