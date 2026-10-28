import streamlit as st
st.title("IA PYRAMIDE KORHOGO")
exo = st.text_area("Ton exercice :")
if st.button("corriger"):
  try:
    st.success(f"{exo} = {eval(exo)}")
  except:
    st.success(f"Reçu : {exo}")
