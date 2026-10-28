import streamlit as st
st.title("IA PYRAMIDE KORHOGO")
q = st.text_area("ton exercice")
if st.button("corriger"):
  st.write("correction de :")
  st.write(q)
