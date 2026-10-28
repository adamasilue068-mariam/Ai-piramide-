import streamlit as st
st.title("IA PYRAMIDE KORHOGO")
m = st.selectbox("matieres",["maths","francais","histoire","physique-chimie"])
t = st.text_area("exercice")
p = st.fille_uploader("photo", type=["jpg","png","jpeg"])
if p: st.image(p)
if st.button("corriger"): st.success(f"correction {m} bien recu !")
