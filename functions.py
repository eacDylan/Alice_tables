import streamlit as st
import pandas as pd


# --- Génération d'un DataFrame ---
def generate_dataframe():
    data = []
    for i in range(1, 11):
        for j in range(1, 11):
            data.append({
                "a": i,
                "b": j,
                "result": i * j,
                "score": 1,
                "time_factor": 1,
                "success": 0,
                "fail": 0
            })
    return pd.DataFrame(data)

# --- Sélection aléatoire d’une question ---
def new_question():
    weights = st.session_state.df["score"] * st.session_state.df["time_factor"]
    row = st.session_state.df.sample(
        n=1,
        weights=weights
        ).iloc[0]
    st.session_state.current_question = row
    st.session_state.question_replied = False
    st.session_state.pop("user_answer", None) # commande nécessaire pour remettre à zéro le champ réponse

# --- Vérification de la réponse ---
def check_answer(user_answer):
    row = st.session_state.current_question
    correct = row["result"]
    idx = st.session_state.df[
        (st.session_state.df["a"] == row["a"]) & (st.session_state.df["b"] == row["b"])
    ].index[0]

    if user_answer == correct:
        st.session_state.df.at[idx, "success"] += 1
        st.session_state.df.at[idx, "score"] = st.session_state.df.at[idx, "score"] / 2
        st.session_state.df["time_factor"] += 0.1
        st.session_state.df.at[idx, "time_factor"] = 0.1
        st.session_state.message = f"✅ Correct ! {int(row['a'])} × {int(row['b'])} = {int(correct)}"
    else:
        st.session_state.df.at[idx, "fail"] += 1
        st.session_state.df.at[idx, "score"] = st.session_state.df.at[idx, "score"] * 10
        #st.session_state.df["time_factor"] += 0.1
        st.session_state.message = f"❌ Faux ! {int(row['a'])} × {int(row['b'])} = {int(correct)}"
    
    st.session_state.question_replied = True
    st.session_state.df.to_csv(st.session_state.file_path, index=False, sep=";")