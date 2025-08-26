import streamlit as st
import app.setPage as setPage

def mainPage():
    st.title("Conexiones Sistémicas")
    st.write("""### Este proyecto consiste de dos juegos relacionados a los temas dados en la materia de Pensamiento sistémico""")
    st.write("---")
    st.write("""#### 1. Causalidad o Correlación   """)
    
    if st.session_state.j1 == False:
    
        if st.button("Iniciar", key="k1"):
            setPage.page = "juego1"
            st.rerun()
    else:
        st.button("Iniciar", disabled= True)
        st.write("""Ya terminaste este juego""")
    st.write("---")
    st.write("""##### 2. Polaridad""")
    if st.session_state.j2 == False:
        if st.button("Iniciar", key="k2"):
            setPage.page = "juego2"
    else:
        st.button("Iniciar", key="k3" ,disabled= True)
        st.write("""Ya terminaste este juego""")        
    st.write("---")