import streamlit as st
import pandas as pd
import functions

# Writing of a title
st.title("Chargement d'un fichier")

# Interface for selecting and load a csv file
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

# Display of the selected file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=";")
    st.write("Aperçu du fichier :")
    st.dataframe(df)

