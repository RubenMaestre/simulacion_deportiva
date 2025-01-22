import streamlit as st
import pandas as pd
import os

def display():
    st.title("Simulación de Apuestas")
    st.markdown("""
        En esta sección puedes simular las ganancias o pérdidas al apostar una cantidad fija semanal al FC Barcelona o al Real Madrid,
        basándonos en datos históricos y las cuotas disponibles.
    """)

    # Ruta relativa a la carpeta "data"
    ruta_datos = "data"
    
    # Cargar los nombres de los archivos disponibles
    temporadas_archivos = [archivo.replace(".xlsx", "") for archivo in os.listdir(ruta_datos) if archivo.endswith(".xlsx")]
    
    # Crear un mapeo para renombrar las temporadas
    temporadas_mapeo = {
        archivo: f"Temporada {archivo[:4][-2:]}/{archivo[-2:]}"
        for archivo in temporadas_archivos
    }

    # Ordenar temporadas de forma descendente por año
    temporadas_ordenadas = sorted(temporadas_mapeo.keys(), reverse=True)
    temporadas_labels = [temporadas_mapeo[archivo] for archivo in temporadas_ordenadas]

    # Seleccionar equipo
    equipo = st.selectbox("Selecciona un equipo", ["FC Barcelona", "Real Madrid"])

    # Seleccionar temporada con nombres ajustados
    temporada_label = st.selectbox("Selecciona una temporada", temporadas_labels)

    # Introducir cantidad a apostar semanalmente
    cantidad = st.number_input("Cantidad a apostar semanalmente (€):", min_value=0.0, value=10.0, step=5.0)

    # Obtener el archivo correspondiente al nombre de temporada seleccionado
    temporada_seleccionada = [archivo for archivo, label in temporadas_mapeo.items() if label == temporada_label][0]
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada_seleccionada}.xlsx")

    # Cargar datos de la temporada seleccionada
    df = pd.read_excel(archivo_seleccionado)

    # Filtrar los partidos del equipo seleccionado
    df_equipo = df[
        (df["home_team_name"] == equipo) | (df["away_team_name"] == equipo)
    ].copy()

    # Calcular ganancias por partido
    def calcular_ganancia(row):
        if row["home_team_name"] == equipo and row["victoria"] == 1:
            return cantidad * row["odds_ft_home_team_win"]
        elif row["away_team_name"] == equipo and row["victoria"] == 1:
            return cantidad * row["odds_ft_away_team_win"]
        else:
            return -cantidad  # Si pierde, pierde la cantidad apostada

    df_equipo["Ganancia"] = df_equipo.apply(calcular_ganancia, axis=1)

    # Calcular total de ganancias
    ganancia_total = df_equipo["Ganancia"].sum()

    # Mostrar resultados
    st.markdown(f"### Resultados de la simulación para el {equipo} en la {temporada_label}")
    st.dataframe(df_equipo[["home_team_name", "away_team_name", "victoria", "Ganancia"]])
    st.markdown(f"### Ganancia/Pérdida total: **{ganancia_total:.2f} €**")

