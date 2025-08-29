import streamlit as st
import pandas as pd
import random
from pathlib import Path
import functions

# --- Import du fichier csv ---
if "file_path" not in st.session_state:
    st.session_state.file_path = Path("tables.csv") # Création d'un objet Path avec le chemin du fichier contenant les tables

# --- Initialisation ---
if st.session_state.file_path.is_file():
    st.session_state.df = pd.read_csv(st.session_state.file_path, sep=";")
else:
    if "df" not in st.session_state:
        st.session_state.df = functions.generate_dataframe()

if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "message" not in st.session_state:
    st.session_state.message = ""
if "user_answer" not in st.session_state:
    st.session_state.user_answer = 0
if "question_replied" not in st.session_state:
    st.session_state.question_replied = False

# --- Interface Streamlit ---
st.title("🎯 Entraîne-toi aux tables de multiplication (1 à 10)")

if st.session_state.current_question is None:
    functions.new_question()

row = st.session_state.current_question

st.subheader(f"Combien fait {int(row['a'])} × {int(row['b'])} ?")

user_answer = st.number_input("Ta réponse :", min_value=0, step=1, key="user_answer")

if st.button("Valider"):
    if st.session_state.question_replied == False and user_answer != 0:
        functions.check_answer(user_answer)
    elif user_answer == 0:
        st.session_state.message = "Veuillez répondre à la question avant de valider !"
    else:
        st.session_state.message = "Question déjà traitée, cliquez sur Question suivante !"

st.write(st.session_state.message)

if st.button("Question suivante"):
    if st.session_state.question_replied == True:
        functions.new_question()
        st.session_state.message = ""
        st.rerun()
    else:
        st.session_state.message = "Vous devez répondre à la question !"

#st.write(st.session_state.question_replied)
#st.write(st.session_state.user_answer)
#st.write(st.session_state.df.at[idx,"score"] * st.session_state.df.at[idx,"time_factor"])

# --- Stats ---
with st.expander("📊 Voir mes stats"):
    st.dataframe(st.session_state.df)
