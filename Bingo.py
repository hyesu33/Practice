import streamlit as st
import pandas as pd
import random

# Load and clean data
@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/hyesu33/Myapps/refs/heads/main/wordlist.csv")
    df["word"] = df["word"].str.lower().str.strip()
    df["meaning"] = df["meaning"].str.strip()
    return df

df = load_data()
all_words = df["word"].tolist()
meanings_dict = dict(zip(df["word"], df["meaning"]))

# Set up page
st.title("🎯 Group Vocabulary Bingo Game")

# Team setup
teams_input = st.text_input("Enter team names separated by commas (e.g., Red, Blue, Green):")
if teams_input:
    team_names = [team.strip() for team in teams_input.split(",")]

    if "scores" not in st.session_state:
        st.session_state.scores = {team: 0 for team in team_names}

    if "bingo_words" not in st.session_state:
        st.session_state.bingo_words = random.sample(all_words, 9)

    if "quiz_word" not in st.session_state:
        st.session_state.quiz_word = random.choice(st.session_state.bingo_words)

    current_word = st.session_state.quiz_word
    current_meaning = meanings_dict[current_word]

    # Show Bingo board (static words)
    st.markdown("### 🧩 Bingo Board Words")
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            with cols[j]:
                st.button(st.session_state.bingo_words[index].capitalize(), key=f"word_{index}")

    # Show quiz
    st.markdown("### ❓ Guess the Word!")
    st.info(f"👉 Meaning: **{current_meaning}**")
    selected_team = st.selectbox("Which team is answering?", team_names)
    guess = st.text_input("Enter your answer:").lower().strip()

    if st.button("Submit Answer"):
        if guess == current_word:
            st.success(f"✅ Correct! The answer was '{current_word.upper()}'.")
            st.session_state.scores[selected_team] += 1
        else:
            st.error(f"❌ Incorrect. The correct answer was '{current_word.upper()}'.")

        # Select next quiz word
        st.session_state.quiz_word = random.choice(st.session_state.bingo_words)

    # Show scoreboard
    st.markdown("### 🏆 Team Scores")
    for team, score in st.session_state.scores.items():
        st.write(f"**{team}**: {score} point(s)")
