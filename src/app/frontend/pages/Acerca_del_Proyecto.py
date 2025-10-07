import streamlit as st

from app.frontend.utils.constants import SOURCES

st.set_page_config(page_title="Proyecto")
st.title("ℹ️ Información")

st.html(
    """
    <div style="background-color: #cce6f4; padding: 15px; border-left: 6px solid #133c55; border-radius: 5px;">
        Puedes hacer preguntas sobre <em>adquisición de vivienda en Colombia</em>, como:<br><br>
        • Conceptos clave (leasing habitacional, crédito hipotecario, etc.)<br>
        • Beneficios y subsidios disponibles<br>
        • Requisitos, tipos de vivienda, y más<br><br>
        También puedes subir <strong>tus propios documentos</strong> (PDF o TXT), y MiCasaBot te ayudará a responder preguntas basadas en su contenido.
    </div>
    """
)