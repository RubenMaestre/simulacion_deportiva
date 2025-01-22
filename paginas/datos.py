import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

def display():
    st.title("Datos: FC Barcelona y Real Madrid")
    st.markdown("""
        Este análisis incluye los datos desde la temporada 2012/2013 hasta la actualidad.
        Aquí puedes seleccionar un equipo y una temporada para visualizar el rendimiento en términos de victorias, empates y derrotas.
    """)

    # Ruta relativa a la carpeta "data"
    ruta_datos = "data"  # Ruta relativa
    
    # Cargar los nombres de los archivos disponibles
    temporadas_archivos = [archivo.replace(".xlsx", "") for archivo in os.listdir(ruta_datos) if archivo.endswith(".xlsx")]
    
    # Crear un mapeo para renombrar las temporadas
    temporadas_mapeo = {archivo: f"Temporada {archivo[-2:]}/{archivo[:4][-2:]}" for archivo in temporadas_archivos}

    # Ordenar temporadas de forma descendente por año
    temporadas_ordenadas = sorted(temporadas_mapeo.keys(), reverse=True)
    temporadas_labels = [temporadas_mapeo[archivo] for archivo in temporadas_ordenadas]

    # Seleccionar equipo
    equipo = st.selectbox("Selecciona un equipo", ["FC Barcelona", "Real Madrid"])

    # Seleccionar temporada con nombres ajustados
    temporada_label = st.selectbox("Selecciona una temporada", temporadas_labels)
    
    # Obtener el archivo correspondiente al nombre de temporada seleccionado
    temporada_seleccionada = [archivo for archivo, label in temporadas_mapeo.items() if label == temporada_label][0]
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada_seleccionada}.xlsx")

    # Cargar datos de la temporada seleccionada
    df = pd.read_excel(archivo_seleccionado)

    # Filtrar los partidos del equipo seleccionado
    df_equipo = df[
        (df["home_team_name"] == equipo) | (df["away_team_name"] == equipo)
    ].copy()

    # Añadir columna de resultado
    def calcular_resultado(row):
        if row["home_team_name"] == equipo and row["home_team_goal_count"] > row["away_team_goal_count"]:
            return "Victoria"
        elif row["away_team_name"] == equipo and row["away_team_goal_count"] > row["home_team_goal_count"]:
            return "Victoria"
        elif row["home_team_goal_count"] == row["away_team_goal_count"]:
            return "Empate"
        else:
            return "Derrota"

    df_equipo["Resultado"] = df_equipo.apply(calcular_resultado, axis=1)

    # Contar victorias, empates y derrotas con un orden predefinido
    categorias = ["Victoria", "Empate", "Derrota"]
    conteo_resultados = df_equipo["Resultado"].value_counts()
    conteo_resultados = conteo_resultados.reindex(categorias, fill_value=0)  # Ordena y rellena valores faltantes con 0

    # Crear el gráfico
    fig, ax = plt.subplots()
    barras = conteo_resultados.plot(kind="bar", ax=ax, color=["green", "orange", "red"])
    ax.set_title(f"Resultados del {equipo} en la {temporada_label}")
    ax.set_xlabel("Resultado")
    ax.set_ylabel("Número de partidos")
    ax.set_xticks(range(len(conteo_resultados.index)))
    ax.set_xticklabels(conteo_resultados.index, rotation=0)

    # Añadir el número encima de cada barra
    for barra in ax.patches:
        ax.annotate(
            f"{barra.get_height():.0f}",  # El número
            (barra.get_x() + barra.get_width() / 2, barra.get_height()),  # Posición
            ha="center", va="bottom", fontsize=10, color="black"
        )

    # Mostrar el gráfico
    st.pyplot(fig)
