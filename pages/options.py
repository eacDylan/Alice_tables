import streamlit as st
import pandas as pd
import functions

st.title("Options sur le DataFrame")

# Bouton pour réinitialiser
if st.button("Réinitialiser le DataFrame"):
    st.session_state.df = functions.generate_dataframe()
    st.session_state.df.to_csv(st.session_state.file_path, index=False, sep=";")
    st.success("Le DataFrame a été réinitialisé ✅")

# Upload d’un fichier CSV
uploaded_file = st.file_uploader("Charger un fichier CSV", type="csv")

if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file, sep=";")
    st.session_state.df.to_csv(st.session_state.file_path, index=False, sep=";")
    st.success("Nouveau DataFrame chargé !")

# Ajouter la possibilité d'exporter un dataframe au format csv

# Afficher le DataFrame actuel
st.write("DataFrame actuel :")
if "df" in st.session_state:
    st.dataframe(st.session_state.df)