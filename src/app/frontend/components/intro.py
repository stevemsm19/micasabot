import streamlit as st

def render_intro():
    st.set_page_config("Home", page_icon="🏠")
    st.title("MiCasa Bot 🏠")
    st.info(
        "Puedes hacer preguntas sobre **adquisición de vivienda en Colombia**, como:\n"
        "- Conceptos clave (leasing habitacional, crédito hipotecario, etc.)\n"
        "- Beneficios y subsidios disponibles\n"
        "- Requisitos, tipos de vivienda, y más\n\n"
        "También puedes subir **tus propios documentos** (PDF o TXT), y MiCasaBot te ayudará a responder preguntas basadas en su contenido."
    )
