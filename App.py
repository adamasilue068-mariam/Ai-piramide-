import streamlit as St 
st.title("IA PYRAMIDE KORHOGO")
st.write("l'intelligence de korhogo")
m=st.selectbox("matière",["Maths", français, anglais])
e=st.text_area("Ton exercice :")
if e=="":
  st.warnting("Ecris d'abord !")
else:
  st.success("correction Ok pour"+m)
  st.write("méthode: 1-comprendre 2-formule 3- vérifier")
  st.balloons()
