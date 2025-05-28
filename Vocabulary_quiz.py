import streamlit as st
import pandas as pd
import random

# Load your word list CSV
@st.cache_data
def load_vocab():
    url = "https://raw.githubusercontent.com/KY7437/G01Final/main/wordlist.csv"
    df = pd.read_csv(url)
    vocab_dict = dict(zip(df["Word"], df["Meaning"]))
    return vocab_dict

vocab = load_vocab()

# Initialize session state
if "quiz_items" not in st.session_state:
    st.session_state.quiz_items = random.sample(list(vocab.items()), 5)
    st.session_state.current_q = 0
    st.session_state.score = 0

st.title("📚 Vocabulary Quiz")

# Display current question
if st.session_state.current_q < len(st.session_state.quiz_items):
    answer_word, meaning = st.session_state.quiz_items[st.session_state.current_q]

    st.subheader(f"Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_items)}")
    st.write(f"**Meaning:** {meaning}")

    user_input = st.text_input("Enter the English word:", key=st.session_state.current_q)

    if st.button("Submit", key=f"submit_{st.session_state.current_q}"):
        if user_input.strip().lower() == answer_word.lower():
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer was **{answer_word}**.")
        st.session_state.current_q += 1
        st.rerun()

# Display final score
else:
    st.subheader("🎉 Quiz Finished!")
    st.write(f"Your total score is: **{st.session_state.score} / 5**")

    if st.button("Play Again"):
        st.session_state.quiz_items = random.sample(list(vocab.items()), 5)
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()
