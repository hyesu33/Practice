import streamlit as st
import pandas as pd
import random

# Load word list
@st.cache_data
def load_data():
    df = pd.read_csv("wordlist.csv")
    df["word"] = df["word"].str.lower()
    df["meaning"] = df["meaning"].str.strip()
    return df

df = load_data()
words = df["word"].tolist()
meanings = df["meaning"].tolist()

# Team setup
st.title("🎯 Group Vocabulary Bingo Game")

teams = st.text_input("Enter team names separated by commas (e.g., Team A, Team B):")
if teams:
    team_list = [t.strip() for t in teams.split(",")]
    if "scores" not in st.session_state:
        st.session_state.scores = {team: 0 for team in team_list}

# Create bingo board
bingo_words = random.sample(list(zip(words, meanings)), 9)
selected_words = [w[0] for w in bingo_words]
selected_meanings = dict(bingo_words)

# Show board
st.markdown("### 🧩 Bingo Board")
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        with cols[j]:
            st.button(selected_words[index].capitalize(), key=f"bingo_{index}")

# New quiz word
if "quiz_word" not in st.session_state:
    st.session_state.quiz_word = random.choice(selected_words)
    st.session_state.correct_word = st.session_state.quiz_word
    st.session_state.quiz_meaning = selected_meanings[st.session_state.quiz_word]

st.markdown("### 📘 What word matches this meaning?")
st.info(f"**{st.session_state.quiz_meaning}**")

# Answer input
if teams:
    chosen_team = st.selectbox("Which team is answering?", team_list)
    guess = st.text_input("Enter your team's answer (word):").strip().lower()

    if st.button("Submit Answer"):
        if guess == st.session_state.correct_word:
            st.success(f"✅ Correct! '{guess}' is right.")
            st.session_state.scores[chosen_team] += 1
        else:
            st.error(f"❌ Incorrect. The correct word was '{st.session_state.correct_word}'.")
        
        # New quiz word
        st.session_state.quiz_word = random.choice(selected_words)
        st.session_state.correct_word = st.session_state.quiz_word
        st.session_state.quiz_meaning = selected_meanings[st.session_state.quiz_word]

# Scoreboard
if teams:
    st.markdown("### 🏆 Scoreboard")
    for team, score in st.session_state.scores.items():
        st.write(f"**{team}**: {score} point(s)")
