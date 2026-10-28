import streamlit as st
st.title("IA PYRAMIDE KORHOGO")
mat=st.selectbox("Matiere",["maths","français","anglais"])
exo = st.text_area("Ton exercice :")
if st.button("corriger"):
  if exo == "":
    st.warning("Ecris d'abord !")
  else:
    st.success("Ok pour "+mat)
