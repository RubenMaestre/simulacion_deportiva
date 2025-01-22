# modules/config_page.py
import streamlit as st

def set_global_page_config():
    st.set_page_config(
        page_title="Simulación de Inversión en Fútbol",
        page_icon="⚽",
        layout="wide"
    )
