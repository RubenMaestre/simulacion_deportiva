import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Función principal para mostrar los datos del rendimiento del FC Barcelona y Real Madrid
def display():
    # Título de la página con un enfoque claro en los datos de rendimiento
    st.title("Datos: FC Barcelona y Real Madrid")
    st.markdown("""
        En esta sección tienes acceso a los datos históricos de los dos equipos más destacados de La Liga: el **FC Barcelona** y el **Real Madrid**. 
        Este análisis incluye los resultados desde la temporada **2012/2013** hasta la temporada **2023/2024**, y te permite visualizar sus números 
        en términos de **victorias**, **empates** y **derrotas** en cada temporada seleccionada gráficamente.
    """)

    # Definimos la ruta donde se encuentran los datos de las temporadas
    ruta_datos = "data"  # Ruta relativa al directorio de datos
    
    # Listamos todos los archivos Excel disponibles y eliminamos la extensión para facilitar su manejo
    temporadas_archivos = [archivo.replace(".xlsx", "") for archivo in os.listdir(ruta_datos) if archivo.endswith(".xlsx")]
    
    # Creamos un mapeo que convierte los nombres de los archivos en etiquetas de temporada más entendibles
    temporadas_mapeo = {
        archivo: f"Temporada {archivo[:4][-2:]}/{archivo[-2:]}"  # Formato "23/24"
        for archivo in temporadas_archivos
    }

    # Ordenamos las temporadas de más reciente a más antigua y generamos etiquetas para mostrar al usuario
    temporadas_ordenadas = sorted(temporadas_mapeo.keys(), reverse=True)
    temporadas_labels = [temporadas_mapeo[archivo] for archivo in temporadas_ordenadas]

    # Menú desplegable para que el usuario elija el equipo
    equipo = st.selectbox("Selecciona un equipo", ["FC Barcelona", "Real Madrid"])

    # Menú desplegable para que el usuario elija la temporada
    temporada_label = st.selectbox("Selecciona una temporada", temporadas_labels)
    
    # Identificamos el archivo correspondiente a la temporada seleccionada
    temporada_seleccionada = [archivo for archivo, label in temporadas_mapeo.items() if label == temporada_label][0]
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada_seleccionada}.xlsx")

    # Cargamos los datos de la temporada seleccionada
    df = pd.read_excel(archivo_seleccionado)

    # Filtramos solo los partidos en los que participa el equipo seleccionado
    df_equipo = df[
        (df["home_team_name"] == equipo) | (df["away_team_name"] == equipo)
    ].copy()

    # Calculamos el resultado de cada partido desde la perspectiva del equipo seleccionado
    def calcular_resultado(row):
        if row["home_team_name"] == equipo and row["home_team_goal_count"] > row["away_team_goal_count"]:
            return "Victoria"  # Ganó como local
        elif row["away_team_name"] == equipo and row["away_team_goal_count"] > row["home_team_goal_count"]:
            return "Victoria"  # Ganó como visitante
        elif row["home_team_goal_count"] == row["away_team_goal_count"]:
            return "Empate"  # Empató
        else:
            return "Derrota"  # Perdió

    # Añadimos una columna "Resultado" al DataFrame con la información calculada
    df_equipo["Resultado"] = df_equipo.apply(calcular_resultado, axis=1)

    # Contamos cuántos partidos terminaron en victoria, empate o derrota
    categorias = ["Victoria", "Empate", "Derrota"]  # Orden específico de las categorías
    conteo_resultados = df_equipo["Resultado"].value_counts()
    conteo_resultados = conteo_resultados.reindex(categorias, fill_value=0)  # Rellenamos con 0 las categorías faltantes

    # Creamos un gráfico de barras para visualizar los resultados
    fig, ax = plt.subplots()
    barras = conteo_resultados.plot(kind="bar", ax=ax, color=["green", "orange", "red"])  # Colores según el resultado
    ax.set_title(f"Resultados del {equipo} en la {temporada_label}")  # Título del gráfico
    ax.set_xlabel("Resultado")  # Etiqueta del eje X
    ax.set_ylabel("Número de partidos")  # Etiqueta del eje Y
    ax.set_xticks(range(len(conteo_resultados.index)))  # Posición de las etiquetas en el eje X
    ax.set_xticklabels(conteo_resultados.index, rotation=0)  # Mantenemos las etiquetas horizontales

    # Añadimos los valores numéricos sobre cada barra para mayor claridad
    for barra in ax.patches:
        ax.annotate(
            f"{barra.get_height():.0f}",  # Valor numérico
            (barra.get_x() + barra.get_width() / 2, barra.get_height()),  # Posición
            ha="center", va="bottom", fontsize=10, color="black"
        )

    # Mostramos el gráfico en la interfaz
    st.pyplot(fig)
