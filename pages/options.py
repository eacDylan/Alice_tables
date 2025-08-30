import streamlit as st
import pandas as pd
import functions

st.title("Options sur le DataFrame")

# --- The user can reset the dataframe ---
if st.button("Réinitialiser le DataFrame"):
    st.session_state.df = functions.generate_dataframe()
    st.session_state.df.to_csv(st.session_state.file_path, index=False, sep=";")
    st.success("Le DataFrame a été réinitialisé ✅")

# --- The user can upload the dataframe from a CSV file ---
uploaded_file = st.file_uploader("Charger un fichier CSV", type="csv")

if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file, sep=";")
    st.session_state.df.to_csv(st.session_state.file_path, index=False, sep=";")
    st.success("Nouveau DataFrame chargé !")

# --- The user can download the dataframe to a CSV file ---
# dataframe => CSV conversion
csv = st.session_state.df.to_csv(index=False, sep=";")

file_name = st.text_input(
    label="Nom du fichier à exporter :",
      value="Tables_Alice",
      key="file_name"
)

st.download_button(
    label="📥 Télécharger les données (CSV)",
    data=csv,
    file_name=file_name,
    mime="text/csv"
)

# Afficher le DataFrame actuel
st.write("DataFrame actuel :")
if "df" in st.session_state:
    st.dataframe(st.session_state.df)
