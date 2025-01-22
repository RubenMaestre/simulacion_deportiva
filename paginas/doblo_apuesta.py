import streamlit as st
import pandas as pd
import os

def display():
    # Título y descripción de la página
    st.title("Simulación: Doblo la apuesta tras pérdida")
    st.markdown("""
        Descubre si una estrategia de doblar la apuesta tras cada pérdida podría ser rentable a largo plazo
        para el **FC Barcelona** o el **Real Madrid**. Esta simulación utiliza datos históricos y las cuotas promedio
        de las casas de apuestas.
    """)

    # Ruta de datos
    ruta_datos = "data"

    # Listar los archivos disponibles
    temporadas_archivos = [archivo.replace(".xlsx", "") for archivo in os.listdir(ruta_datos) if archivo.endswith(".xlsx")]
    temporadas_mapeo = {
        archivo: f"Temporada {archivo[:4][-2:]}/{archivo[-2:]}"
        for archivo in temporadas_archivos
    }
    temporadas_ordenadas = sorted(temporadas_mapeo.keys(), reverse=True)
    temporadas_labels = [temporadas_mapeo[archivo] for archivo in temporadas_ordenadas]

    # Selección del equipo y temporada
    equipo = st.selectbox("Selecciona un equipo", ["FC Barcelona", "Real Madrid"])
    temporada_label = st.selectbox("Selecciona una temporada", temporadas_labels)

    # Introducir cantidad fija inicial
    cantidad_inicial = st.number_input("Cantidad inicial a apostar (€):", min_value=1.0, value=10.0, step=5.0)

    # Tipo de partidos
    tipo_partidos = st.radio("Selecciona el tipo de partidos", ["Toda la temporada", "Partidos de local", "Partidos de visitante"])

    # Cargar el archivo seleccionado
    temporada_seleccionada = [archivo for archivo, label in temporadas_mapeo.items() if label == temporada_label][0]
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada_seleccionada}.xlsx")
    df = pd.read_excel(archivo_seleccionado)

    # Filtrar según el equipo y el tipo de partidos
    if tipo_partidos == "Toda la temporada":
        df_equipo = df[
            (df["home_team_name"] == equipo) | (df["away_team_name"] == equipo)
        ].copy()
    elif tipo_partidos == "Partidos de local":
        df_equipo = df[df["home_team_name"] == equipo].copy()
    elif tipo_partidos == "Partidos de visitante":
        df_equipo = df[df["away_team_name"] == equipo].copy()

    # Calcular victoria
    def calcular_victoria(row):
        if row["home_team_name"] == equipo:
            return 1 if row["home_team_goal_count"] > row["away_team_goal_count"] else 0
        elif row["away_team_name"] == equipo:
            return 1 if row["away_team_goal_count"] > row["home_team_goal_count"] else 0
        return 0

    df_equipo["victoria"] = df_equipo.apply(calcular_victoria, axis=1)

    # Simulación de la estrategia de doblar la apuesta
    apuesta_actual = cantidad_inicial
    ganancias = []
    total_gastado = 0.0

    for _, row in df_equipo.iterrows():
        if row["victoria"] == 1:  # Ganado
            if row["home_team_name"] == equipo:
                ganancia = (apuesta_actual * row["odds_ft_home_team_win"])
            else:
                ganancia = (apuesta_actual * row["odds_ft_away_team_win"])
            apuesta_actual = cantidad_inicial  # Reinicia la apuesta tras ganar
        else:  # Perdido
            ganancia = -apuesta_actual
            apuesta_actual *= 2  # Duplicar apuesta tras pérdida

        total_gastado += apuesta_actual / 2  # Gasto en la jornada actual
        ganancias.append(ganancia)

    # Agregar las ganancias al DataFrame
    df_equipo["Ganancia"] = ganancias

    # Crear tabla mostrada
    df_mostrado = df_equipo.rename(columns={
        "home_team_name": "Equipo local",
        "home_team_goal_count": "Goles local",
        "away_team_goal_count": "Goles visitantes",
        "away_team_name": "Equipo visitante"
    })[["Equipo local", "Goles local", "Goles visitantes", "Equipo visitante", "Ganancia"]]

    # Formatear Ganancia
    df_mostrado["Ganancia"] = df_mostrado["Ganancia"].apply(lambda x: f"{x:.2f}".replace(",", "."))

    # Calcular balance final
    ganancia_total = sum(ganancias)
    balance_final = ganancia_total - total_gastado  # Corrección: Resta del gasto total

    # Mostrar resultados
    st.markdown(f"### Resultados de la simulación para el {equipo} en la {temporada_label} ({tipo_partidos})")
    st.dataframe(df_mostrado)
    st.markdown(f"### Total gastado: **{total_gastado:.2f} €**")
    st.markdown(f"### Total ganancias: **{ganancia_total:.2f} €**")
    st.markdown(f"### Balance final: **{balance_final:.2f} €**")
