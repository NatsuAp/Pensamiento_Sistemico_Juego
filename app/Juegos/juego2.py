import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
import app.setPage as setPage
def deployJuego2():
    if "ls" not in st.session_state:
        st.session_state.ls = False
    st.header("Juego - Polaridad", divider= True)
    st.subheader("Instrucciones")
    st.write("""Lea el ciclo e identifique si se trata de una bipolaridad positiva o negativa """)
    loadScratch()
    if st.button("Terminar"):
        st.session_state.j2 = True
        st.session_state.page = "main"
        st.rerun()
def loadScratch():
    html_path = Path("utils/Scratch/NEXUS SWAP.html")
    if html_path.exists():
        components.html(html_path.read_text(encoding="utf-8"), height=700, scrolling=True)
    else:
        st.error("Hubo un error al cargar el juego")