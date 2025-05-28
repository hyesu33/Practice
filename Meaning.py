import streamlit as st
import pandas as pd
import random

# Load vocabulary list from CSV
@st.cache_data
def load_vocab():
    url = "https://raw.githubusercontent.com/KY7437/G01Final/main/wordlist.csv"
    df = pd.read_csv(url)
    vocab_dict = dict(zip(df["word"], df["meaning"])) 
    return vocab_dict

vocab = load_vocab()

# Initialize session state
if "quiz_items" not in st.session_state:
    st.session_state.quiz_items = random.sample(list(vocab.items()), 5)
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.user_input = ""

st.title("📖 Vocabulary Meaning Quiz")

# Display current question
if st.session_state.current_q < len(st.session_state.quiz_items):
    word, correct_meaning = st.session_state.quiz_items[st.session_state.current_q]

    st.subheader(f"Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_items)}")
    st.write(f"**Word:** {word}")

    user_input = st.text_input("Enter the Korean meaning:", key=f"input_{st.session_state.current_q}")

    if st.button("Submit", key=f"submit_{st.session_state.current_q}") and not st.session_state.show_result:
        st.session_state.user_input = user_input.strip().lower()
        st.session_state.show_result = True

    if st.session_state.show_result:
        if st.session_state.user_input == correct_meaning.strip().lower():
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer was **{correct_meaning}**.")

        if st.button("Next"):
            st.session_state.current_q += 1
            st.session_state.show_result = False
            st.rerun()

# Final score
else:
    st.subheader("🎉 Quiz Finished!")
    st.write(f"Your total score is: **{st.session_state.score} / {len(st.session_state.quiz_items)}**")

    if st.button("Play Again"):
        st.session_state.quiz_items = random.sample(list(vocab.items()), 5)
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.show_result = False
        st.session_state.user_input = ""
        st.rerun()
