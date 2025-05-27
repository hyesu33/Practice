import streamlit as st
import pandas as pd
import random

# Load vocabulary from CSV
@st.cache_data
def load_vocab():
    df = pd.read_csv("https://raw.githubusercontent.com/KY7437/G01Final/refs/heads/main/wordlist.csv") 
    vocab_dict = dict(zip(df["word"], df["meaning"]))
    return vocab_dict

vocab = load_vocab()

# Pick a random word from full list
if "answer_word" not in st.session_state:
    st.session_state.answer_word, st.session_state.meaning = random.choice(list(vocab.items()))
    st.session_state.attempts = 0
    st.session_state.max_attempts = 6
    st.session_state.finished = False

st.title("🔤 Vocabulary Guessing Game")
st.write("Guess the word based on its Korean meaning.")
st.write(f"📘 Meaning: **{st.session_state.meaning}**")
st.write(f"🔡 Number of letters: **{len(st.session_state.answer_word)}**")
st.write(f"🎯 You have {st.session_state.max_attempts - st.session_state.attempts} attempts remaining.")

# Input
if not st.session_state.finished:
    user_guess = st.text_input("Your guess:").strip().lower()

    if st.button("Submit"):
        if user_guess == "":
            st.warning("Please enter a word.")
        else:
            st.session_state.attempts += 1

            if user_guess == st.session_state.answer_word.lower():
                st.success(f"✅ Correct! The word was **{st.session_state.answer_word}**.")
                st.session_state.finished = True
            else:
                if st.session_state.attempts >= st.session_state.max_attempts:
                    st.error(f"❌ Out of attempts! The word was **{st.session_state.answer_word}**.")
                    st.session_state.finished = True
                else:
                    st.warning("Incorrect. Try again.")

# Restart
if st.session_state.finished:
    if st.button("Play Again"):
        st.session_state.answer_word, st.session_state.meaning = random.choice(list(vocab.items()))
        st.session_state.attempts = 0
        st.session_state.finished = False
if st.button("Try Again"):
    st.experimental_rerun()
