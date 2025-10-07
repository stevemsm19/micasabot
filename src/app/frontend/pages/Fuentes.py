import streamlit as st
from app.frontend.utils.constants import SOURCES

st.set_page_config(page_title="Fuentes")
st.title("📚 Fuentes")

html_sources = """
<div style="
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    padding: 10px;
">
"""
for name, url in SOURCES.items():
    html_sources += f"""
        <div style="
            flex: 1 1 200px;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        ">
            <a href="{url}" target="_blank" style="color: #0d1b2a; text-decoration: none;">
                {name}
            </a>
        </div>
    """
html_sources += "</div>"

st.html(html_sources)
