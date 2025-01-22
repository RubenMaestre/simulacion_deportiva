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

    # Seleccionar tipo de partidos
    tipo_partidos = st.radio("Selecciona el tipo de partidos", ["Toda la temporada", "Partidos de local", "Partidos de visitante"])

    # Obtener el archivo correspondiente al nombre de temporada seleccionado
    temporada_seleccionada = [archivo for archivo, label in temporadas_mapeo.items() if label == temporada_label][0]
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada_seleccionada}.xlsx")

    # Cargar datos de la temporada seleccionada
    df = pd.read_excel(archivo_seleccionado)

    # Filtrar los partidos del equipo seleccionado
    if tipo_partidos == "Toda la temporada":
        df_equipo = df[
            (df["home_team_name"] == equipo) | (df["away_team_name"] == equipo)
        ].copy()
    elif tipo_partidos == "Partidos de local":
        df_equipo = df[df["home_team_name"] == equipo].copy()
    elif tipo_partidos == "Partidos de visitante":
        df_equipo = df[df["away_team_name"] == equipo].copy()

    # Recalcular victoria
    def calcular_victoria(row):
        if row["home_team_name"] == equipo:
            return 1 if row["home_team_goal_count"] > row["away_team_goal_count"] else 0
        elif row["away_team_name"] == equipo:
            return 1 if row["away_team_goal_count"] > row["home_team_goal_count"] else 0
        return 0

    df_equipo["victoria"] = df_equipo.apply(calcular_victoria, axis=1)

    # Calcular ganancias por partido
    def calcular_ganancia(row):
        if row["victoria"] == 1:
            if row["home_team_name"] == equipo:
                return cantidad * row["odds_ft_home_team_win"]
            elif row["away_team_name"] == equipo:
                return cantidad * row["odds_ft_away_team_win"]
        return -cantidad  # Si pierde, pierde la cantidad apostada

    df_equipo["Ganancia"] = df_equipo.apply(calcular_ganancia, axis=1)

    # Formatear columna victoria como "Acierto" (Fallo o Ganado)
    df_equipo["Acierto"] = df_equipo["victoria"].apply(lambda x: "Ganado" if x == 1 else "Fallo")

    # Crear un DataFrame con las columnas solicitadas
    df_mostrado = df_equipo.rename(columns={
        "home_team_name": "Equipo local",
        "home_team_goal_count": "Goles local",
        "away_team_goal_count": "Goles visitantes",
        "away_team_name": "Equipo visitante"
    })[["Equipo local", "Goles local", "Goles visitantes", "Equipo visitante", "Acierto", "Ganancia"]]

    # Formatear Ganancia solo para mostrar en la tabla
    df_mostrado["Ganancia"] = df_mostrado["Ganancia"].apply(lambda x: f"{x:.2f}".replace(",", "."))

    # Calcular total gastado
    total_gastado = cantidad * len(df_equipo)

    # Calcular total de ganancias
    ganancia_total = df_equipo["Ganancia"].sum()

    # Calcular balance final
    balance_final = ganancia_total - total_gastado

    # Mostrar resultados
    st.markdown(f"### Resultados de la simulación para el {equipo} en la {temporada_label} ({tipo_partidos})")
    st.dataframe(df_mostrado)
    st.markdown(f"### Total gastado: **{total_gastado:.2f} €**")
    st.markdown(f"### Total ganancias: **{ganancia_total:.2f} €**")
    st.markdown(f"### Balance final: **{balance_final:.2f} €**")
