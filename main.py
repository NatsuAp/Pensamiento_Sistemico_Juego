import streamlit as st
import json
import numpy as np

def load_Preguntas1():
    with open("utils/Pregunas-Causalidad-Correlacion.json", "r", encoding="utf-8") as f:
        st.session_state.preguntas1 = json.load(f)
    




def main():
    if "loaded" not in st.session_state:
        st.session_state.loaded = False
    if "preguntas1" not in st.session_state:
        st.session_state.preguntas1 = None
    if st.session_state.loaded == False:
        load_Preguntas1()
        st.session_state.loaded = True
    if "ans" not in st.session_state:
        st.session_state.ans = ""
    if "end" not in st.session_state:
        st.session_state.end = False
    if 'res' not in st.session_state:
        st.session_state.setdefault("res", [])   
  
    st.title("Pensamiento Sistemico")
    st.header("Juego - Causalidad o Correlacion", divider= True)
    if st.session_state.end == False:

        st.subheader("Instrucciones")
        st.write("""Identifique en cada caso si se trata de una causalidad o de una correlación. """)
        
        c = 1
        for p in st.session_state.preguntas1:
            
            res = f"res{c}"
            if res not in st.session_state:
                st.session_state[res] = None
            st.write(c)
            st.radio(p["problema"],[p["opcion_a"], p["opcion_b"]], index=None, key= res)
            

            c+=1
        if st.button("Terminar"):
            
            st.badge("Incorrecto", icon=":material/check:", color="green")
            st.session_state.end = True
            st.rerun()
    else:
            st.subheader("Respuestas:")
            i=1
            for p in st.session_state.preguntas1:
                res = f"res{i}"
                st.write(p["problema"])
                st.write("Tu respuesta:")
                st.write(st.session_state[res] )
                if st.session_state[res]== p["correcta"]:
                    st.badge("Correcto", icon=":material/check:", color="green")
                else:
                    st.badge("Incorrecto", icon="❌", color="red")
                    
                i+=1

                    




main()