import streamlit as st
import pandas as pd
import os

def display():
    # Título principal y descripción de la página
    st.title("Simulación basada en cuotas menores")
    st.markdown("""
    Filtra los partidos del **FC Barcelona** o el **Real Madrid** para cuotas específicas y simula
    si apostar semanalmente por ellos habría sido una estrategia rentable.
    """)

    # Ruta relativa donde se encuentran los archivos con los datos históricos
    ruta_datos = "data"

    # Listamos los archivos Excel disponibles en la carpeta "data"
    temporadas_archivos = [archivo.replace(".xlsx", "") for archivo in os.listdir(ruta_datos) if archivo.endswith(".xlsx")]

    # Creamos un diccionario que mapea los nombres de archivo a un formato más amigable para el usuario
    temporadas_mapeo = {
        archivo: f"Temporada {archivo[:4][-2:]}/{archivo[-2:]}"
        for archivo in temporadas_archivos
    }

    # Ordenamos las temporadas en orden descendente
    temporadas_ordenadas = sorted(temporadas_mapeo.keys(), reverse=True)
    temporadas_labels = [temporadas_mapeo[archivo] for archivo in temporadas_ordenadas]

    # Selección del equipo para el que se hará la simulación
    equipo = st.selectbox("Selecciona un equipo", ["FC Barcelona", "Real Madrid"])

    # Selección de la temporada
    temporada_label = st.selectbox("Selecciona una temporada", temporadas_labels)

    # Input para definir la cantidad fija que se apostará cada semana
    cantidad = st.number_input("Cantidad a apostar semanalmente (€):", min_value=0.0, value=10.0, step=5.0)

    # Selección del tipo de partidos (local, visitante o todos)
    tipo_partidos = st.radio("Selecciona el tipo de partidos", ["Toda la temporada", "Partidos de local", "Partidos de visitante"])

    # Filtro para las cuotas
    cuota_limite = st.selectbox(
        "Selecciona el límite de la cuota",
        [1.20, 1.30, 1.40, 1.50, 1.60, 1.80],
        format_func=lambda x: f"Cuota ≤ {x}"
    )

    # Obtenemos el archivo correspondiente según la temporada seleccionada
    temporada_seleccionada = [archivo for archivo, label in temporadas_mapeo.items() if label == temporada_label][0]
    archivo_seleccionado = os.path.join(ruta_datos, f"{temporada_seleccionada}.xlsx")

    # Cargamos los datos de la temporada seleccionada
    df = pd.read_excel(archivo_seleccionado)

    # Filtramos los partidos según el equipo seleccionado y el tipo de partidos
    if tipo_partidos == "Toda la temporada":
        df_equipo = df[
            (df["home_team_name"] == equipo) | (df["away_team_name"] == equipo)
        ].copy()
    elif tipo_partidos == "Partidos de local":
        df_equipo = df[df["home_team_name"] == equipo].copy()
    elif tipo_partidos == "Partidos de visitante":
        df_equipo = df[df["away_team_name"] == equipo].copy()

    # Filtramos los partidos según la cuota
    df_equipo = df_equipo[
        ((df_equipo["home_team_name"] == equipo) & (df_equipo["odds_ft_home_team_win"] <= cuota_limite)) |
        ((df_equipo["away_team_name"] == equipo) & (df_equipo["odds_ft_away_team_win"] <= cuota_limite))
    ]

    # Función que determina si el equipo ganó el partido
    def calcular_victoria(row):
        if row["home_team_name"] == equipo:
            return 1 if row["home_team_goal_count"] > row["away_team_goal_count"] else 0
        elif row["away_team_name"] == equipo:
            return 1 if row["away_team_goal_count"] > row["home_team_goal_count"] else 0
        return 0

    df_equipo["victoria"] = df_equipo.apply(calcular_victoria, axis=1)

    # Función que calcula la ganancia por partido, dependiendo del resultado
    def calcular_ganancia(row):
        if row["victoria"] == 1:
            if row["home_team_name"] == equipo:
                return cantidad * row["odds_ft_home_team_win"]
            elif row["away_team_name"] == equipo:
                return cantidad * row["odds_ft_away_team_win"]
        return -cantidad  # Si pierde, se resta la cantidad apostada

    df_equipo["Ganancia"] = df_equipo.apply(calcular_ganancia, axis=1)

    # Creamos una columna adicional para indicar si la apuesta fue acertada o no
    df_equipo["Acierto"] = df_equipo["victoria"].apply(lambda x: "Ganado" if x == 1 else "Fallo")

    # Renombramos y seleccionamos las columnas clave para mostrarlas en la tabla de resultados
    df_mostrado = df_equipo.rename(columns={
        "home_team_name": "Equipo local",
        "home_team_goal_count": "Goles local",
        "away_team_goal_count": "Goles visitantes",
        "away_team_name": "Equipo visitante"
    })[["Equipo local", "Goles local", "Goles visitantes", "Equipo visitante", "Acierto", "Ganancia"]]

    # Formateamos las ganancias para mostrar dos decimales en la tabla
    df_mostrado["Ganancia"] = df_mostrado["Ganancia"].apply(lambda x: f"{x:.2f}".replace(",", "."))

    # Calculamos el total gastado, multiplicando la cantidad apostada por el número de partidos
    total_gastado = cantidad * len(df_equipo)

    # Calculamos el total de ganancias acumuladas
    ganancia_total = df_equipo["Ganancia"].sum()

    # Calculamos el balance final restando el total gastado a las ganancias
    balance_final = ganancia_total - total_gastado

    # Mostramos los resultados de la simulación en la interfaz
    st.markdown(f"### Resultados de la simulación para el {equipo} en la {temporada_label} ({tipo_partidos}) con cuota ≤ {cuota_limite}")
    st.dataframe(df_mostrado)
    st.markdown(f"### Total gastado: **{total_gastado:.2f} €**")
    st.markdown(f"### Total ganancias: **{ganancia_total:.2f} €**")
    st.markdown(f"### Balance final: **{balance_final:.2f} €**")