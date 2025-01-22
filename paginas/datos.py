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

    # Ruta donde se encuentran los archivos Excel
    ruta_datos = r"C:\Users\34670\Desktop\python\base_datos_futbol\proyecto_inversion\data"
    
    # Cargar los nombres de los archivos disponibles
    temporadas = [archivo.replace(".xlsx", "") for archivo in os.listdir(ruta_datos) if archivo.endswith(".xlsx")]

    # Seleccionar equipo
    equipo = st.selectbox("Selecciona un equipo", ["FC Barcelona", "Real Madrid"])

    # Seleccionar temporada
    temporada = st.selectbox("Selecciona una temporada", temporadas)

    # Cargar datos de la temporada seleccionada
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada}.xlsx")
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

    # Contar victorias, empates y derrotas
    conteo_resultados = df_equipo["Resultado"].value_counts()

    # Crear el gráfico
    fig, ax = plt.subplots()
    conteo_resultados.plot(kind="bar", ax=ax, color=["green", "orange", "red"])
    ax.set_title(f"Resultados del {equipo} en la temporada {temporada}")
    ax.set_xlabel("Resultado")
    ax.set_ylabel("Número de partidos")
    ax.set_xticks(range(len(conteo_resultados.index)))
    ax.set_xticklabels(conteo_resultados.index, rotation=0)

    # Mostrar el gráfico
    st.pyplot(fig)
