# app.py
import streamlit as st
from app.Juegos.juego1 import deployJuego1
from app.Juegos.juego2 import deployJuego2
from app.mainPage import mainPage

# ---- estado por sesión ----
st.session_state.setdefault("page", "main")
st.session_state.setdefault("j1", False)
st.session_state.setdefault("j2", False)

page = st.session_state.page

# ---- router ----
if page == "main":
    mainPage()
elif page == "juego1":
    deployJuego1()
elif page == "juego2":
    deployJuego2()