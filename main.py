import app.setPage as setPage
import streamlit as st
from app.Juegos.juego1 import deployJuego1
from app.Juegos.juego2 import deployJuego2
from app.mainPage import mainPage
if "j1" not in st.session_state:
    st.session_state.j1 = False
if "j2" not in st.session_state:
    st.session_state.j2 = False


   

print(setPage.page)
match setPage.page:
    case "main":
        mainPage()
        
    case "juego1":
        deployJuego1()
    case "juego2":
        deployJuego2()
    
